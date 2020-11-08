from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from main_app.models.account import Account
from werkzeug.security import check_password_hash
from main_app import login_manager
from flask_login import login_user, current_user

login_bp = Blueprint('login_bp', __name__)

@login_manager.user_loader
def load_user(account_id):
    return Account.query.get(int(account_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in, redirect back to app
    if current_user.is_authenticated:
        return redirect(url_for('login_success_bp.load_page'))

    form = LoginForm()

    if form.validate_on_submit():
        # Query database for username to see if it exists
        account = Account.query.filter_by(username=form.username.data).first()
        if account:
            # If the username exists, check if the password is correct, if so login, otherwise redirect back to same page
            # Need to add message to user if not correct.
            if check_password_hash(account.password, form.password.data):
                login_user(account, remember=form.remember.data)
                return redirect(url_for('login_success_bp.load_page'))
        #If username or password is invalid, flash and redirect
        flash('Invalid username or password provided')
        return redirect(url_for('login_bp.login'))

    return render_template('login_view.html', form=form)
