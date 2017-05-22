import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from bucketlist.config import configurations

db = SQLAlchemy()


def create_app(config_name):
    if os.getenv('CIRCLECI'):
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URI")
        )
    else:
        app = Flask(__name__)
        app.config.from_object(configurations[config_name])
    configurations[config_name].init_app(app)
    db.init_app(app)
    from bucketlist.routes import api
    api.init_app(app)

    CORS(app)
    return app
