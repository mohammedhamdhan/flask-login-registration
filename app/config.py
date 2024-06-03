import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgres://nuscartographers_database_user:idyVv6DH0O4eE102nGfz6TKTbP52MyF1@dpg-cpejs47109ks73fcdhhg-a/nuscartographers_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')  # Default value for development
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')  # Default to development if not set
