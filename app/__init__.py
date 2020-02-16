from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

# Initizializations
db = SQLAlchemy()

# Application Factory
def create_app(config_name):
    '''
    Function to startup the application
    '''
    app = Flask(__name__)

    # Creating Configurations
    app.config.from_object(config_options[config_name])

    # Initizlizing extensions
    db.init_app(app)

    # Registering Blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .requests import configure_request
    configure_request(app)

    return app

