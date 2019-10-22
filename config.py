import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('zUSh0tePFrKuM5kor6ewSS4D8ebfIueB')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://isaac:5272@localhost/pitchlist'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}