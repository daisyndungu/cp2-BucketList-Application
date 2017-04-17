import status
from flask import Blueprint, request, jsonify, make_response, json
from flask_restful import Api, Resource, marshal, fields
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from models import BucketList, BucketListItem, app, db

api = Api(app)


bucketlist_format = {
    'bucketlist_id': fields.Integer,
    'name': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime

    }


class BucketlistView(Resource):
    def get(self, bucketlist_id=None):
        """
        Get one buckect list
        """
        if bucketlist_id:
            try:
                bucketlist_query = BucketList.query.filter_by(
                    bucketlist_id=bucketlist_id).first()
                if bucketlist_query:
                    return marshal(bucketlist_query, bucketlist_format), 200
                # return jsonify({'bucketlist': bucketlist_query})
                else:
                    return "bucketlist does not exist"
            except AttributeError as e:
                # Returns an error if bucketlist does not exist
                return "Error: Bucketlist does not exist", 400
        else:
            bucketlist = BucketList.query.all()
            return marshal(bucketlist, bucketlist_format), 200

    def post(self):
        """
        Get user's input and save it to database(POST request)
        """
        request_dict = request.get_json()
        if not request_dict:
            response = {'Error': 'No input data provided'}
            return response, 400
        else:
            try:
                bucketlist = BucketList(name=request_dict["name"])
                bucketlist.add()
                # result = json.dumps(bucketlist.get())
                return 'Bucketlist saved successfully', 201
            except SQLAlchemyError:
                # Returns an error if a bucketlist
                # with the same name already exists
                db.session.rollback()
                response = jsonify(
                    {"Error": " The bucketlist entered already exists"})
                return response, 400

    def put(self, bucketlist_id):
        # if bucketlist_id
        bucketlist = BucketList.query.filter_by(
                    bucketlist_id=bucketlist_id).first()
        try:
            if bucketlist:
                bucketlist_dict = request.get_json()
                if bucketlist_dict['name']:
                    bucketlist.name = bucketlist_dict['name']
                    bucketlist.update()
                    return jsonify("Bucketlist Updated Successfully"), 200
            else:
                return "Bucketlist does not exist", 400
        except:
            return "A bucketlist with that name exists", 400

    def delete(self, bucketlist_id):
        bucketlist = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id).first()
        if bucketlist:
            bucketlist.delete()
            return "Bucketlist deleted Successfully", 200
        else:
            return "Invalid Input. Bucketlist does not exist", 400


api.add_resource(BucketlistView, '/bucketlist/', endpoint="add_bucketlist")
api.add_resource(BucketlistView, '/bucketlist/<int:bucketlist_id>',
                 endpoint="bucketlistview")
api.add_resource(BucketListItem, '/bucketlist/<int:bucketlist_id>/items/')


if __name__ == '__main__':
    app.run()
