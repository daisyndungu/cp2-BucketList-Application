import datetime

from flask_jwt import jwt

from bucketlist import db, app


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
    bucketlist = db.relationship('BucketList', backref='user',
                                 cascade='all,delete', passive_deletes=True)

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


class BucketList(db.Model, AddUpdateDelete):
    """
    Create bucketlist model
    """
    __tablename__ = 'bucketlist'
    bucketlist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    date_modified = db.Column(db.DateTime, default=datetime.datetime.now,
                              onupdate=datetime.datetime.now)
    items = db.relationship('BucketListItem', backref='bucketlist',
                            cascade='all,delete', passive_deletes=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id',
                           onupdate="CASCADE",
                           ondelete="CASCADE"), nullable=False)

    def __init__(self, name, created_by):
        self.name = name
        self.created_by = created_by


class BucketListItem(db.Model, AddUpdateDelete):
    """
    Create bucketlist item model
    """
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

    def __init__(self, name, description, bucketlist_id,  status=False):
        self.name = name
        self.description = description
        self.status = status
        self.bucketlist_id = bucketlist_id
