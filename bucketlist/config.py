import os

import os
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5432
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", None) + "/buckectlist"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')
