import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://myappuser:newpassword@localhost:5433/myapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
