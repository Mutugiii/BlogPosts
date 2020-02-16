from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_o_four(error):
    '''
    Function to handle wrong routes
    '''
    return render_template('404.html'),404
