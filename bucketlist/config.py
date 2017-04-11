import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'Bucketlist.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
TESTING = True
SERVER_NAME = '127.0.0.1:5000'
PAGINATION_PAGE_SIZE = 5
PAGINATION_PAGE_ARGUMENT_NAME = 'page'
# Disable CSRF protection in the testing configuration
WTF_CSRF_ENABLED = False
SECRET_KEY = os.getenv("SECRET_KEY", None)
