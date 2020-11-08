from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from main_app.models.account import Account
from main_app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user

signup_bp = Blueprint('signup_bp', __name__)

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=32)])

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    # If the user is already logged in, redirect back to app
    if current_user.is_authenticated:
        return redirect(url_for('login_success_bp.load_page'))

    form = SignUpForm()

    if form.validate_on_submit():
        # Query database, if account already exists with that username. Redirect back to sign up.
        account = Account.query.filter_by(username=form.username.data).first()
        if account:
            flash('That username is taken')
            return redirect(url_for('signup_bp.signup'))

        # The username isn't taken. Hash the password, create an Account object, put it in db.
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_account = Account(username=form.username.data, password=hashed_password)
        db.session.add(new_account)
        db.session.commit()

        # Log the new user in, then redirect to success
        login_user(new_account)
        return redirect(url_for('login_success_bp.load_page'))

    return render_template('signup_view.html', form=form)
