class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dataweb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
config = {
    'development': DevelopmentConfig,
}