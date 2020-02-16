class Config:
    '''
    Config parent class that holds other general inheritable configurations
    '''
    pass

class DevConfig(Config):
    '''
    Class for dev configurations
    '''
    pass

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
        DevConfig: 'development',
        ProdConfig: 'production',
        TestConfig: 'Testing'
}
