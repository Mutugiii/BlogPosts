from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField, StringField
from wtforms.validators import Required

class UpdateUserProfile(FlaskForm):
    '''Form class to update User Information'''
    bio = TextAreaField('Bio', validators=[Required()])
    submit = SubmitField('Update Profile')

class BlogPostForm(FlaskForm):
    '''Form class for to create the blog post'''
    title = StringField('Bog Post Title', validators=[Required()])
    blogcontent = TextAreaField('Blog Content', validators=[Required()])
    submit = SubmitField('Post Blog Post')