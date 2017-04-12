import status
from app import app
from flask_restful import Api
from bucketlist.models import User, BucketList, BucketListItem, db

app = app
api = Api(app)


class Bucketlist():
    pass


class BucketListItem():
    pass

api.add_resource(BucketList, "/bucketlist/")
api.add_resource(BucketList, "/bucketlist/<init:id>")
api.add_resource(BucketList, "/bucketlist/<init:id>/items/")
api.add_resource(BucketListItem, "/bucketlists/<id>/items/<item_id>")
