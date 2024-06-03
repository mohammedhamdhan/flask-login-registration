import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1) if os.environ.get('DATABASE_URL') else 'sqlite:///site.db'    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')  # Default value for development
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')  # Default to development if not set
