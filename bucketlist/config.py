import os


class Config():
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TEST = False
    CSRF_ENABLED = True
    PORT = 5432
    HOST = "127.0.0.1"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None) + "/bucketlist"
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
    SECRET_KEY = os.getenv("SECRET_KEY")
    PAGINATION_PAGE_SIZE = 5
    PAGINATION_PAGE_ARGUMENT_NAME = 'page'


class Production(Config):
    DEBUG = False


class Staging(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", None) + "/testbucketlist"
    TESTING = True
