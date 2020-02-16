class Config:
    '''
    Config parent class that holds other general inheritable configurations
    '''
    API_URL='http://quotes.stormconsultancy.co.uk/random.json'

class DevConfig(Config):
    '''
    Class for dev configurations
    '''
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
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'Testing': TestConfig
}
