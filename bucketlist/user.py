import status

from flask import request, jsonify, make_response, json, g
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api, Resource, marshal, fields, reqparse
from sqlalchemy.exc import SQLAlchemyError

from bucketlist.models import User


class UserRegistration(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, location='json',
                                   required=True,
                                   help="Please enter your username")
        self.reqparse.add_argument('email', type=str, location='json',
                                   required=True,
                                   help="Please enter your email")
        self.reqparse.add_argument('password', type=str, location='json',
                                   required=True,
                                   help="Please enter your password")
        super(UserRegistration, self).__init__()

    def post(self):
        """
        User Registration
        """
        user_details = self.reqparse.parse_args()
        try:
            user = User(username=user_details['username'],
                        email=user_details['email'],
                        password=user_details['password'])
            user.add(user)
            return {'Done': 'User added successfully'}, 201
        except SQLAlchemyError:
                # Returns an error if a user
                # with the same name or email already exists
                db.session.rollback()
                return {"Error": "User with the same username or\
                            email already exists"}, 400


class UserLogin(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, location='json',
                                   required=True,
                                   help="Please enter your username")
        self.reqparse.add_argument('password', type=str, location='json',
                                   required=True,
                                   help="Please enter your password")
        super(UserLogin, self).__init__()

    def post(self):
        """
        Login a user and generate token
        """
        user_details = self.reqparse.parse_args()
        try:
            user = User.query.filter_by(username=user_details['username'],
                                        password=user_details['password']
                                        ).first()
            if user:
                # Generate authentication token
                token = user.generate_auth_token(user.id)
                # Covert Token from bytes to string
                auth_token = token.decode()
                response = make_response(jsonify({'Token': auth_token}), 201)
                return response
            else:
                return{'Error': 'Wrong user name or password'}
        except Exception as e:
                return {"Error": str(e)}, 400
