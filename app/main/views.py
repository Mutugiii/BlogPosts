from . import main
from flask import render_template, abort, redirect, url_for, request, flash
from ..requests import get_quote
from ..models import User
from .forms import UpdateUserProfile
from flask_login import login_required, current_user
from .. import photos

@main.route('/')
def index():
    '''Main index route'''
    quotes = get_quote()
    return render_template('index.html', quotes = quotes)

@main.route('/profile/<uname>')
def profile(uname):
    '''Route to the User Profile'''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user)

@main.route('/profile/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    '''Function to update the user profile'''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateUserProfile()

    if form.validate_on_submit():
        if request.method == 'POST':
            update_form = request.form
            bio = update_form.get('bio')
            if not bio:
                flash('User Bio is required')
                return redirect(url_for('main.update_profile'))
            
            user.bio = form.bio.data
            user.save_user()
            return redirect(url_for('.profile', uname = user.username))

    return render_template('profile/update.html', form = form)

@main.route('/profile/<uname>/update/pic', methods = ['POST'])
@login_required
def update_picture(uname):
    '''
    Function for user to update profile picture
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user.save()
    return redirect(url_for('main.profile',uname = uname))