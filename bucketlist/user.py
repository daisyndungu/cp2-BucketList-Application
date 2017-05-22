from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256

from bucketlist.models import User, db


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
            hash_password = pbkdf2_sha256.encrypt(user_details['password'],
                                                  rounds=200000, salt_size=16)
            user = User(username=user_details['username'],
                        email=user_details['email'],
                        password=hash_password)
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
            user = User.query.filter_by(username=user_details['username']
                                        ).first()
            if user and pbkdf2_sha256.verify(user_details['password'],
                                             user.password):
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
