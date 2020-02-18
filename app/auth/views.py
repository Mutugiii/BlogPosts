from flask import render_template, url_for, redirect, flash, request
from . import auth
from .forms import RegisterForm,LoginForm
from ..models import User
from flask_login import login_user,logout_user,login_required, current_user
from .. import db

@auth.route('/register', methods = ['GET','POST'])
def register():
    '''
    Function to register new users
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # Backend Validation
        if request.method == 'POST':
            reg_form = request.form
            name = reg_form.get('username')
            if not name:
                flash('Username must be entered')
                return redirect(url_for('auth.register'))
            passw = reg_form.get('password')
            if not passw:
                flash('Password must be entered')
                return redirect(url_for('auth.register'))
            pass_confirm = reg_form.get('password_confirmation')
            if not pass_confirm:
                flash('Password confirmation must be entered')
                return redirect(url_for('auth.register'))
            if len(passw) < 6:
                flash('Password Must be greater than 6 characters')
                return redirect(url_for('auth.register'))
            if pass_confirm != passw:
                flash('Passwords Must match')
                return redirect(url_for('auth.register'))

            user = User(email = form.email.data, username = form.username.data)
            user.set_password(form.password.data)
            user.save_user()
    
            return redirect(url_for('auth.login'))
            flash('Thank you for signing up!')

    return render_template('auth/register.html', form = form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    Function to deal with user login 
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        # Backend Validation
        if request.method == 'POST':
            login_form = request.form
            email = login_form.get('email')
            if not email:
                flash('Email Address must be entered')
                return redirect(url_for('auth.login'))
            passw = login_form.get('password')
            if not passw:
                flash('Password must be entered')
                return redirect(url_for('auth.login'))
            user = User.query.filter_by(email = form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember.data)
                return redirect(request.args.get('next') or url_for('main.index'))
            flash('Invalid username or Password')

    return render_template('auth/login.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')