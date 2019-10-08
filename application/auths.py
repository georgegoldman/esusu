from flask import Blueprint, render_template, redirect, url_for, flash, request, Markup
from application.web_forms import RegistrationForm, LoginForm, AdminForm, GroupForm, AdduserForm
from application.models import User, Group, Member
from application import db
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
def signup():

    form = RegistrationForm()

    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        username = form.username.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash('user already exist!')
            return render_template('signup.html', form=form)


        user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('view.login'))

    flash('check your email or passwords if they\'re correct !')
    return redirect(url_for('view.signup'))

@auth.route('/login', methods=['POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('view.account_home'))

        else:
            flash(Markup("Check your login details or account does not exit ! please <a href='/signup' class='alert-link'>signup</a>"))
            return redirect(url_for('view.login'))

@auth.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('view.home'))
