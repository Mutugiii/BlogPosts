from flask import render_template
from flask_mail import Message
from . import mail

def mailer(subject,template,to,**kwargs):
    '''
    Function to specify mail message
    '''
    sender_email = 'billmutuma@gmail.com'

    email = Message(subject, sender=sender_email,recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)