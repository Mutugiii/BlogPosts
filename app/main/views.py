from . import main
from flask import render_template, abort, redirect, url_for, request, flash
from ..requests import get_quote
from ..models import User, BlogPost, Comment
from .forms import UpdateUserProfile, BlogPostForm, CommentForm
from flask_login import login_required, current_user
from .. import photos,db
from datetime import datetime
from ..email import mailer

@main.route('/')
def index():
    '''Main index route'''
    quotes = get_quote()
    latest_blogs = BlogPost.query.order_by(db.desc(BlogPost.posted)).first()
    all_blogs = BlogPost.query.order_by(db.desc(BlogPost.posted)).all()
    user = BlogPost.query.filter_by(user_id = latest_blogs.user_id).first()
    return render_template('index.html', quotes = quotes, latest = latest_blogs, all = all_blogs, user = user)

@main.route('/profile/<uname>')
def profile(uname):
    '''Route to the User Profile'''
    user = User.query.filter_by(username = uname).first()
    posts = BlogPost.query.filter_by(user_id = user.id).all()

    if user is None:
        abort(404)
        
    return render_template('profile/profile.html', user = user, posts = posts)

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
        user.save_user()
    return redirect(url_for('.profile',uname = uname))

@main.route('/subscribe/<email>')
@login_required
def subscribe(email):
    '''Function to subscribe to mailing list'''
    user = User.query.filter_by(email = email).first()

    user.subscribed = True
    user.save_user()

    flash('Thank you for subscribing!')
    return redirect(url_for('.index'))

@main.route('/post/new/<uname>', methods = ['GET', 'POST'])
@login_required
def new_post(uname):
    '''Post a blog'''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    if user.role == 'user':
        flash('Only Writers can create posts')
        return redirect(url_for('main.index'))
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

            blog = BlogPost(title = form.title.data, content = form.blogcontent.data, post_pic_path = path, user_id = current_user.id)
            blog.save_post()

            users = User.query.all()
            for user in users:
                if user.subscribed == True:
                    blog = BlogPost.query.filter_by(user_id = user.id).first()
                    mailer('New Post Notification!!!', 'email/notification', user.email, user = user, blog = blog)

            return redirect(url_for('.index'))
    return render_template('post/post.html', form = form)

@main.route('/post/delete/<post_id>', methods = ['GET', 'POST'])
@login_required
def delete_post(post_id):
    '''Function to delete a post'''
    post = BlogPost.query.filter_by(id = post_id).first()
    user = User.query.filter_by(id = post.user_id).first()

    if user is None:
        abort(404)
    
    if user.role == 'user':
        flash('Only Writers can delete posts')
        return redirect(url_for('main.index'))
        abort(404)

    post.delete_post()
    flash('Post successfully deleted')
    return redirect(url_for('.index'))

@main.route('/post/update/<post_id>', methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    '''Function to update the Post'''
    post = BlogPost.query.filter_by(id = post_id).first()
    user = User.query.filter_by(id = post.user_id).first()

    if user is None:
        abort(404)
    
    if user.role == 'user':
        flash('Only Writers can Update posts')
        return redirect(url_for('main.view_post', post_id = post.id))
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

            post.title = form.title.data
            post.content = form.content.data
            post.post_pic_path = path
            post.user_id = current_user.id
            post.updated = datetime.utcnow
            post.save_post()

    return render_template('post/post.html', form = form)

@main.route('/post/comment/<post_id>', methods = ['GET', 'POST'])
@login_required
def post_comment(post_id):
    '''Function to post a comment on a post'''
    post = BlogPost.query.filter_by(id = post_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        if request.method == 'POST':
            comment_form = request.form
            form_content = comment_form.get('content')
            if not form_content:
                flash('Comment must be provided')
                return redirect(url_for('.view_post', post_id = post.id))
            comment = Comment(content = form.content.data, post_id = post_id)
            comment.save_comment()
            return redirect(url_for('.view_post', post_id = post_id))

    return render_template('post/comment.html', form = form, post = post)


@main.route('/post/comment/delete/<post_id>')
@login_required
def delete_comment(post_id):
    '''Function to delete a comment'''
    post = BlogPost.query.filter_by(id = post_id).first()
    comment = Comment.query.filter_by(post_id = post.id).first()
    user = User.query.filter_by(id = post.user_id).first()

    if user is None:
        abort(404)
    
    if user.role == 'user':
        flash('Only Writers can delete comments on posts')
        return redirect(url_for('main.index'))
        abort(404)

    comment.delete_comment()

    return redirect(url_for('.index'))

@main.route('/post/view/<post_id>')
def view_post(post_id):
    '''Function to view a specific post'''
    post = BlogPost.query.filter_by(id = post_id).first()
    comments = Comment.query.filter_by(post_id = post_id).all()
    user = BlogPost.query.filter_by(user_id = post.user_id).first()

    return render_template('post/specific_post.html', comments = comments, post = post, user = user)