from flask import render_template, url_for, redirect, flash, request
from . import auth
from .forms import RegisterForm,LoginForm
from ..models import User
from flask_login import login_user,logout_user,login_required, current_user
from ..email import mail_message
from .. import db

@auth.route('/register', methods = ['GET','POST'])
def register():
    '''
    Function to register new users
    '''
    if current_user.is_authenticated:
        return redirect('main.index')
    reg_form = RegisterForm()
    if reg_form.validate_on_submit():
        user = User(email = reg_form.email.data, username = reg_form.username.data, password = reg_form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message('Welcome to Pitch','email/welcome',user.email,user=user)
        return redirect(url_for('auth.login'))
        flash('Thank you for signing up!')

    return render_template('auth/register.html', form = reg_form)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    Function to deal with user login 
    '''
    if current_user.is_authenticated:
        return redirect('main.index')
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or Password')

    return render_template('auth/login.html', form = login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')