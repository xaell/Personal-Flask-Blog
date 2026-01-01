import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///dev.db")
    
class ProductionConfig(Config):
    DEBUG = False
    #Prod database not done yet, do later
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL")
