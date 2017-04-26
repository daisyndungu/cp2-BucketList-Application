import status
from flask import request, jsonify, make_response, json, g, make_response
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api, Resource, marshal, fields, reqparse
from sqlalchemy.exc import SQLAlchemyError

from bucketlist.models import (User, BucketList, BucketListItem, app, db)
from bucketlist.auth import authorize_token, decode_auth_token
from bucketlist.user import UserRegistration, UserLogin

api = Api(app)


item_output = {
    'item_id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime,
    'status': fields.String,
    'bucketlist_id': fields.Integer
}

bucketlist_output = {
    'bucketlist_id': fields.Integer,
    'name': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime

    }


class BucketlistView(Resource):
    # Add authorization decorator to all
    # functions in this class
    decorators = [authorize_token]

    def get(self, bucketlist_id=None):
        """
        Display one buckectlist
        """
        # Get logged in user Id
        user_id = g.user_id
        if bucketlist_id:
            # Query one bucketlist
            bucketlist = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id, created_by=user_id).first()
            if not bucketlist:
                return {'Error': 'bucketlist does not exist'}, 400
            return marshal(bucketlist, bucketlist_output), 200

        else:
            # Get all bucketlists
            # Set page limit to 20 items per page if the user does not
            # specify a number
            page_limit = request.args.get('limit', 20)
            # Set page offset that controls the starting point within
            # the collection of resource results
            page_offset = request.args.get('offset', 0)
            # Check if request is a search request
            search_name = request.args.get('q')
            if search_name:
                bucketlist = BucketList.query.filter_by(name=search_name,
                                                        created_by=user_id
                                                        ).all()
                return marshal(bucketlist, bucketlist_output), 200
            # If not a search request then gets all bucket lists
            # TODO
            bucketlist = BucketList.query.filter_by(
                created_by=user_id).limit(page_limit).offset(
                    page_offset).all()
            if not bucketlist:
                return {'Error': 'There are no bucketlists at the moment'}, 400
            return marshal(bucketlist, bucketlist_output), 200

    def post(self):
        """
        Add a new bucket list
        """
        user_id = g.user_id
        # Get users input
        request_dict = request.get_json()
        if not request_dict:
            # If no input
            response = {'Error': 'No input data provided'}
            return response, 400
        else:
            try:
                bucketlist = BucketList(name=request_dict["name"],
                                        created_by=user_id)
                bucketlist.add(bucketlist)
                return {'Done': 'Bucketlist saved successfully'}, 201
            except SQLAlchemyError:
                # Returns an error if a bucketlist
                # with the same name already exists
                db.session.rollback()
                response = make_response(jsonify(
                            {"Error": " The bucketlist entered already exists"}
                            ), 400)

                return response

    def put(self, bucketlist_id):
        """
        Edit a bucketlist name
        """
        user_id = g.user_id
        bucketlist = BucketList.query.filter_by(
                    bucketlist_id=bucketlist_id, created_by=user_id).first()
        try:
            if bucketlist:
                bucketlist_dict = request.get_json()
                if bucketlist_dict['name']:
                    bucketlist.name = bucketlist_dict['name']
                    bucketlist.update()
                    return {'Done': 'Bucketlist Updated Successfully'}, 200
            else:
                return {'Error': 'Bucketlist does not exist'}, 400
        except:
            return {'Error': 'A bucketlist with that name exists'}, 400

    def delete(self, bucketlist_id):
        """
        Remove a bucketlist from the database
        """
        user_id = g.user_id
        bucketlist = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id, created_by=user_id).first()
        if bucketlist:
            bucketlist.delete(bucketlist)
            return 'Bucketlist deleted Successfully', 200
        else:
            return 'Invalid Input. Bucketlist does not exist', 400


class BucketListItemView(Resource):
    decorators = [authorize_token]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json',
                                   required=True, help="Item name is required")
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('status', type=str, location='json')
        super(BucketListItemView, self).__init__()

    def post(self, bucketlist_id):
        """
        Save a new bucketlist item
        """
        user_id = g.user_id
        bucketlist_query = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id, created_by=user_id).first()
        if not bucketlist_query:
            return "Invalid bucketlist", 400
        request_dict = self.reqparse.parse_args()
        if request_dict['status']:
            request_dict['status'] = request_dict['status'].lower()
        if request_dict['status'] == "true":
            return {'Error': 'Status can not be true'}, 401
        try:
            item = BucketListItem(name=request_dict['name'],
                                  description=request_dict['description'],
                                  status=request_dict['status'],
                                  bucketlist_id=bucketlist_id)
            item.add(item)
            return {'Done': 'Bucketlist item saved successfully'}, 201
        except SQLAlchemyError:
                # Returns an error if a bucketlist item
                # with the same name already exists
                db.session.rollback()
                return {"Error": " The bucketlist item entered already \
                        exists"}, 400

    def put(self, bucketlist_id, item_id):
        """
        Edit an item's name, description or/and status
        """
        user_id = g.user_id
        bucket_list = BucketList.query.filter_by(bucketlist_id=bucketlist_id,
                                                 created_by=user_id).first()
        if bucket_list:
            bucketlist_item = BucketListItem.query.filter_by(
                        item_id=item_id, bucketlist_id=bucketlist_id).first()
            if not bucketlist_item:
                return {'Error': 'Bucketlist item does not exist'}, 400
            request_dict = self.reqparse.parse_args()
            name = request_dict['name']
            status = request_dict['status']
            description = request_dict['description']
            if request_dict:
                try:
                    if name:
                        bucketlist_item.name = name
                        bucketlist_item.update()
                    if status:
                        bucketlist_item.status = status
                        bucketlist_item.update()
                    if description:
                        bucketlist_item.description = description
                        bucketlist_item.update()
                    return {'Done': 'Bucketlist Updated Successfully'}, 200

                except SQLAlchemyError:
                    return {'Error': 'No changes made. A bucketlist\
                    with that name exists or wrong status included'}, 400

    def delete(self, bucketlist_id, item_id):
        """
        Remove a bucketlist item from the database
        """
        user_id = g.user_id
        bucket_list = BucketList.query.filter_by(bucketlist_id=bucketlist_id,
                                                 created_by=user_id).first()
        if not bucket_list:
            return {'message': 'Bucketlist does not exist'}, 400
        bucketlist_item = BucketListItem.query.filter_by(
                        item_id=item_id, bucketlist_id=bucketlist_id).first()
        if not bucketlist_item:
            return {'Error': 'Bucketlist item does not exist'}, 400
        bucketlist_item.delete(bucketlist_item)
        return {'Done': 'Bucketlist item deleted successfully'}, 200

    def get(self, bucketlist_id, item_id=None):
        """
        Display one buckectlist
        """
        user_id = g.user_id
        if item_id:
            # Query one bucketlist
            if not BucketList.query.filter_by(
                   bucketlist_id=bucketlist_id, created_by=user_id).first():
                return {'Error': 'Unexisting bucket'}, 404
            item = BucketListItem.query.filter_by(
                                            bucketlist_id=bucketlist_id,
                                            item_id=item_id).first()
            if not item:
                return {'Error': 'bucketlist does not exist'}, 400
            return marshal(item, item_output), 200

        # Get all bucketlists items
        # Set page limit to 20 items per page if the user does not
        # specify a number
        page_limit = request.args.get('limit', 20)
        # Set page offset that controls the starting point within
        # the collection of resource results
        page_offset = request.args.get('offset', 0)
        # Check if request is a search request
        search_name = request.args.get('q')
        if not BucketList.query.filter_by(
               bucketlist_id=bucketlist_id, created_by=user_id).first():
            return {'Error': 'Unexisting bucket'}, 404
        if search_name:
            items = BucketListItem.query.filter_by(
                                        bucketlist_id=bucketlist_id,
                                        name=search_name).all()
            return marshal(items, item_output), 200
        # If not a search request then gets all bucket lists
        items = BucketListItem.query.filter_by(
                                        bucketlist_id=bucketlist_id).all()
        return marshal(items, item_output), 200


api.add_resource(BucketlistView, '/bucketlists/', endpoint='add_bucketlist')
api.add_resource(BucketlistView, '/bucketlists/<int:bucketlist_id>',
                 endpoint='bucketlistview')
api.add_resource(BucketListItemView, '/bucketlists/<int:bucketlist_id>/items/',
                 endpoint='create_bucketlist_item')
api.add_resource(BucketListItemView,
                 '/bucketlists/<int:bucketlist_id>/items/<int:item_id>',
                 endpoint='UpdateDelete_bucketlist_item')
api.add_resource(UserRegistration, '/auth/register', endpoint='register')
api.add_resource(UserLogin, '/auth/login', endpoint='login')

if __name__ == '__main__':
    app.run()
