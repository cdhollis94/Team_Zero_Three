from .__init__ import *

account_bp = Blueprint('account_bp', __name__)

# [CREATE FORMS] -----------------------------------------------------------------
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=32)])
# --------------------------------------------------------------------------------

# [DESIGNATE ROUTES] -------------------------------------------------------------
@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(int(account_id))

@account_bp.route('/')
@login_required
def load_page():
    return render_template('index_view.html', username=current_user.username)

@account_bp.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect back to app
    if current_user.is_authenticated:
        return redirect(url_for('account_bp.load_page'))

    form = LoginForm()

    if form.validate_on_submit():
        # Query database for username to see if it exists
        account = Account.query.filter_by(username=form.username.data).first()
        if account:
            # If the username exists, check if the password is correct, if so login, otherwise redirect back to same page
            # Need to add message to user if not correct.
            if check_password_hash(account.password, form.password.data):
                login_user(account, remember=form.remember.data)
                return redirect(url_for('account_bp.load_page'))
        #If username or password is invalid, flash and redirect
        flash('Invalid username or password provided')
        return redirect(url_for('account_bp.login'))

    return render_template('login_view.html', form=form)

@account_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('account_bp.login'))

@account_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # If the user is already logged in, redirect back to app
    if current_user.is_authenticated:
        return redirect(url_for('account_bp.load_page'))

    form = SignUpForm()

    if form.validate_on_submit():
        # Query database, if account already exists with that username. Redirect back to sign up.
        account = Account.query.filter_by(username=form.username.data).first()
        if account:
            flash('That username is taken')
            return redirect(url_for('account_bp.signup'))

        # The username isn't taken. Hash the password, create an Account object, put it in db.
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_account = Account(username=form.username.data, password=hashed_password)
        db.session.add(new_account)
        db.session.commit()

        # Log the new user in, then redirect to success
        login_user(new_account)
        return redirect(url_for('account_bp.load_page'))

    return render_template('signup_view.html', form=form)
# --------------------------------------------------------------------------------