from . import main
from flask import render_template
from ..requests import get_quote

@main.route('/')
def index():
    '''
    Main index route
    '''
    quotes = get_quote()
    return render_template('index.html', quotes = quotes)