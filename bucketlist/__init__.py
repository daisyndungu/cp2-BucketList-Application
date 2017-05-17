from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from bucketlist.config import configurations

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configurations[config_name])
    configurations[config_name].init_app(app)
    db.init_app(app)
    from bucketlist.routes import api
    api.init_app(app)

    # CORS(app)
    return app
