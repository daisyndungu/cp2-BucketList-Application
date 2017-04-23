import status
from flask import request, jsonify, make_response, json
from flask_restful import Api, Resource, marshal, fields, reqparse
from sqlalchemy.exc import SQLAlchemyError

from models import BucketList, BucketListItem, app, db

api = Api(app)

item_output = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime,
    'status': fields.String
}

bucketlist_output = {
    'bucketlist_id': fields.Integer,
    'name': fields.String,
    'date_created': fields.DateTime,
    'date_modified': fields.DateTime

    }


class BucketlistView(Resource):
    def get(self, bucketlist_id=None):
        """
        Display one buckectlist
        """
        if bucketlist_id:
            # Query one bucketlist
            bucketlist_query = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id).first()
            items = BucketListItem.query.filter_by(
                                            bucketlist_id=bucketlist_id).all()
            if bucketlist_query:
                return marshal(bucketlist_query, bucketlist_output), 200
            else:
                return {'Error': 'bucketlist does not exist'}, 400
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
                bucketlist = BucketList.query.whoosh_search(search_name).all()
                return marshal(bucketlist, bucketlist_output), 200

            # If not a search request then gets all bucket lists
            bucketlist = BucketList.query.limit(page_limit
                                                ).offset(page_offset).all()
            return marshal(bucketlist, bucketlist_output), 200

    def post(self):
        """
        Add a new bucket list
        """
        # Get users input
        request_dict = request.get_json()
        if not request_dict:
            # If no input
            response = {'Error': 'No input data provided'}
            return response, 400
        else:
            try:
                bucketlist = BucketList(name=request_dict["name"])
                bucketlist.add(bucketlist)
                return {'Done': 'Bucketlist saved successfully'}, 201
            except SQLAlchemyError:
                # Returns an error if a bucketlist
                # with the same name already exists
                db.session.rollback()

                return {"Error": " The bucketlist entered already exists"}, 400

    def put(self, bucketlist_id):
        """
        Edit a bucketlist name
        """
        bucketlist = BucketList.query.filter_by(
                    bucketlist_id=bucketlist_id).first()
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
        bucketlist = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id).first()
        if bucketlist:
            bucketlist.delete(bucketlist)
            return 'Bucketlist deleted Successfully', 200
        else:
            return 'Invalid Input. Bucketlist does not exist', 400


class BucketListItemView(Resource):
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

        bucketlist_query = BucketList.query.filter_by(
                bucketlist_id=bucketlist_id).first()
        if not bucketlist_query:
            return "Invalid bucketlist", 400
        request_dict = self.reqparse.parse_args()
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
        bucket_list = BucketList.query.filter_by(bucketlist_id=bucketlist_id
                                                 ).first()
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
        bucket_list = BucketList.query.filter_by(bucketlist_id=bucketlist_id
                                                 ).first()
        if not bucket_list:
            return {'message': 'Bucketlist does not exist'}, 400
        bucketlist_item = BucketListItem.query.filter_by(
                        item_id=item_id, bucketlist_id=bucketlist_id).first()
        if not bucketlist_item:
            return {'Error': 'Bucketlist item does not exist'}, 400
        bucketlist_item.delete(bucketlist_item)
        return {'Done': 'Bucketlist item deleted successfully'}, 200


api.add_resource(BucketlistView, '/bucketlists/', endpoint='add_bucketlist')
api.add_resource(BucketlistView, '/bucketlists/<int:bucketlist_id>',
                 endpoint='bucketlistview')
api.add_resource(BucketListItemView, '/bucketlists/<int:bucketlist_id>/items/',
                 endpoint='create_bucketlist_item')
api.add_resource(BucketListItemView,
                 '/bucketlists/<int:bucketlist_id>/items/<int:item_id>',
                 endpoint='UpdateDelete_bucketlist_item')

if __name__ == '__main__':
    app.run()
