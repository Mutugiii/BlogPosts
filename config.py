import os

class Config:
    '''
    Config parent class that holds other general inheritable configurations
    '''
    API_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Recaptcha Configurations
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_OPTIONS = {'theme':'clean'}

    # Flask Uploads destination
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # Mail Configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class DevConfig(Config):
    '''
    Class for dev configurations
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutugi:Mutugi@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class ProdConfig(Config):
    '''
    Class for production environment configurations
    '''
    pass

class TestConfig(Config):
    '''
    Class with configurations for test environment
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mutugu:Mutugi@localhost/blog_test'

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'Testing': TestConfig
}
