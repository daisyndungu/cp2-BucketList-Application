from datetime import datetime
from bucketlist.run import db


class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))


class BucketList(db.Model):
    __tablename__ = 'bucketlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class BucketListItem(db.Model):
    __tablename__ = 'bucketlistitem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    decription = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow)
    done = db.Column(db.Boolean, default=False)
    bucketList_id = db.Column(db.Integer, db.ForeignKey('bucketlist.id'),
                              nullable=False)
