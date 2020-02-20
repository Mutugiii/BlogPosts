from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
    '''
    Class for the received quote from quotes storm api
    '''
    def __init__(self,id, author,quote,permalink):
        '''
        Initializing quote variable
        '''
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink

class User(UserMixin, db.Model):
    '''
    Class for user schema

    Args:
        db.Model: Connect to database and define as db table
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    subscribed = db.Column(db.Boolean, default = False, nullable = False)
    role = db.Column(db.String, nullable = False)
    blogs = db.relationship('BlogPost', backref='user', lazy = 'dynamic')
    password = db.Column(db.String(), nullable = False)

    def set_password(self, p):
        '''
        Function to set hashed password
        '''
        self.password = generate_password_hash(p)

    def verify_password(self, p):
        '''Function to verify password is correctly hashed'''
        return check_password_hash(self.password, p)

    def save_user(self):
        '''Function to save user to db'''
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'

class BlogPost(db.Model):
    '''Class for Blog in db(column)'''
    __tablename__ = 'blogposts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    content = db.Column(db.String(), nullable = True)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def save_post(self):
        '''Function to save post to db'''
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        '''Function to delete post from database'''
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'BlogPost {self.title}'

class Comment(db.Model):
    '''
    Model table to store, access and manipulate comments
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String())
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('blogposts.id'))

    def save_comment(self):
        '''Save Function'''
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        '''Function to delete comment from database'''
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.content}'