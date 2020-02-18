from . import main
from flask import render_template

@main.route('/')
def index():
    '''
    Main index route
    '''
    return render_template('index.html')