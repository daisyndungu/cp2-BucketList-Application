from flask_jwt import jwt
from flask import Flask
import datetime
import time
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

    def hash_password(self, password):
        pass

    def generate_auth_token(self, expiration=3600000):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user


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
