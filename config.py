class Config:
    '''
    Config parent class that holds other general inheritable configurations
    '''
    API_URL='http://quotes.stormconsultancy.co.uk/random.json'

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
