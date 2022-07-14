import os

class Config:
    # SQLALCHEMY_DATABASE_URI =  os.environ.get("DATABASE_URL", "sqlite:///temp/test.db")
    # SQLALCHEMY_DATABASE_URI =  "sqlite:///temp/test.db"
    # SQLALCHEMY_DATABASE_URI =  os.environ.get("DATABASE_URL", "mysql+pymysql://root:root@192.168.31.125:3306/twittor")
    SQLALCHEMY_DATABASE_URI =  os.environ.get("DATABASE_URL", "mysql+pymysql://root:root@localhost:3306/flask_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "flask_test_123"