import status
from flask import Blueprint, request, jsonify, make_response, json
from flask_restful import Api, Resource
from flask.views import MethodView

# from bucketlist.run import app, db
from models import BucketList, BucketListItem, app, db

api = Api(app)


class BucketlistView(MethodView):
    def get(self):

        pass

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {'Error': 'No input data provided'}
            return response, 400
        else:
            try:
                bucketlist = BucketList(name=request_dict["name"])
                bucketlist.add()
                result = json.dumps(bucketlist.get())
                return result, 201
            except Exception as e:
                db.session.rollback()
                response = jsonify({"error": " Name entered already exists"})
                return response, 400

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

bucketlist_view = BucketlistView.as_view("bucketlist_api")
app.add_url_rule('/bucketlist/', view_func=bucketlist_view, methods=['POST'])
# api.add_resource(BucketList, "/bucketlist/")
# api.add_resource(BucketList, "/bucketlist/<init:id>")
# api.add_resource(BucketList, "/bucketlist/<init:id>/items/")
# api.add_resource(BucketListItem, "/bucketlists/<id>/items/<item_id>")


if __name__ == '__main__':
    app.run()
