from flask_jwt import jwt
from flask import Flask, request, make_response, jsonify
import datetime
import time
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from config import configurations

app = Flask(__name__)
app.config.from_object(configurations['development'])
db = SQLAlchemy(app)


class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class User(db.Model, AddUpdateDelete):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))

    def generate_auth_token(self, id):
        """
        Generates the Auth Token
        """
        try:
            payload = {
                'exp': (datetime.datetime.utcnow() +
                        datetime.timedelta(seconds=3600)),
                'iat': datetime.datetime.utcnow(),
                'sub': id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'),
                             algorithms=['HS256'])
        return {'response': payload['sub'], 'status': True}
    except jwt.ExpiredSignatureError:
        return {'response': 'Signature expired. Please log in again.',
                'status': False}
    except jwt.InvalidTokenError as e:
        return {'response': str(e), 'status': False}


def authorize_token(func):
    @wraps(func)
    def decorators(*args, **kwargs):
        try:
            auth_header = request.headers['Authorization']
            resp = decode_auth_token(auth_header)
            if resp['status'] is False:
                data = {
                    'Error': resp['response']
                }
                response = make_response(jsonify(data), 401)
                return response
        except KeyError:
            return 'Unauthorized access. Please check your token or\
            Authorization key', 401
        return func(*args, **kwargs)
    return decorators


class BucketList(db.Model, AddUpdateDelete):
    __tablename__ = 'bucketlist'
    bucketlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now,
                              onupdate=datetime.datetime.now)
    items = db.relationship('BucketListItem', backref='bucketlist',
                            cascade='all,delete', passive_deletes=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id',
    #                     onupdate="CASCADE",
    #                     ondelete="CASCADE"), nullable=False)

    def __init__(self, name):
        self.name = name


class BucketListItem(db.Model, AddUpdateDelete):
    __tablename__ = 'bucketlistitem'
    item_id = db.Column(db.Integer, autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now,
                              onupdate=datetime.datetime.now)
    status = db.Column(db.Boolean, default=False)
    bucketlist_id = db.Column(db.Integer, db.ForeignKey(
                                                'bucketlist.bucketlist_id',
                                                onupdate="CASCADE",
                                                ondelete="CASCADE"),
                              nullable=False)

    def __init__(self, name, description, status, bucketlist_id):
        self.name = name
        self.description = description
        self.status = status
        self.bucketlist_id = bucketlist_id
