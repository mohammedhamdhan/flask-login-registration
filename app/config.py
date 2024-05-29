import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://myappuser:newpassword@127.0.0.1/32/myapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
