import status
from app import app
from flask_restful import Api
from bucketlist.models import User, BucketList, BucketListItem, db

app = app
api = Api(app)


class Bucketlist():
    pass

api.add_resource(BucketList, "/bucketlist/")
api.add_resource(BucketList, "/bucketlist/<init:id>")
