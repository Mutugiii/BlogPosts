from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateUserProfile(FlaskForm):
    '''Form class to update User Information'''
    bio = TextAreaField('Bio', validators=[Required()])
    submit = SubmitField('Update Profile')