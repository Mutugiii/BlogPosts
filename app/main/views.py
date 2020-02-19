from . import main
from flask import render_template, abort, redirect, url_for, request, flash
from ..requests import get_quote
from ..models import User, BlogPost, Comment
from .forms import UpdateUserProfile, BlogPostForm
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
    '''Function for user to update profile picture'''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user.save()
    return redirect(url_for('main.profile',uname = uname))

@main.route('/post/new/<uname>', methods = ['GET', 'POST'])
@login_required
def new_post(uname):
    '''Post a blog'''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    if user.user_role == 'user':
        abort(404)

    form = BlogPostForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            blog_form = request.form
            blog_title = blog_form.get('title')
            if not blog_title:
                flash('Blog Post Title MUST be provided!')
                return redirect(url_for('.new_post', uname =user.username))
            blog_content = blog_form.get('blogcontent')
            if not blog_content:
                flash('Blog Post Content MUST be provided!')
                return redirect(url_for('.new_post', uname = user.username))
            if 'photo' in request.files:
                filename = photos.save(request.files['photo'])
                path = f'photos/{filename}'

            blog = BlogPost(title = form.title.data, content = form.content.data, post_pic_path = path)
            blog.save_post()

    return render_template('post/post.html', form = form)