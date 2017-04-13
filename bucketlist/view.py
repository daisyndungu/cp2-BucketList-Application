import status
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from flask.views import MethodView

# from bucketlist.run import app, db
from bucketlist.models import User, BucketList, BucketListItem


class Bucketlist(MethodView, Resource):
    def get(self, id=None):
        if id:
            bucketlist = BucketList.query.get_or_404(id)
            return json.dump(bucketlist)
        else:
            bucketlists = bucketlist.query.all()
            return json.dump(bucketlists)

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class BucketListItem():
    def get(self):
        pass

    def post(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(BucketList, "/bucketlist/")
api.add_resource(BucketList, "/bucketlist/<init:id>")
api.add_resource(BucketList, "/bucketlist/<init:id>/items/")
api.add_resource(BucketListItem, "/bucketlists/<id>/items/<item_id>")


if __name__ == '__main__':
    app.run()
