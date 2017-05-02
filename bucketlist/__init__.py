from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from bucketlist.config import configurations

app = Flask(__name__)
app.config.from_object(configurations['development'])
db = SQLAlchemy(app)

api = Api(app)
CORS(app)
