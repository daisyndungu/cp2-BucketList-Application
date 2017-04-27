from flask_jwt import jwt
from functools import wraps
from flask import request, make_response, jsonify, g

from bucketlist import app


def decode_auth_token(auth_token):
    """
    Decodes the authentication token
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'),
                             algorithms=['HS256'])
        return {'response': payload['sub'], 'status': True}
    except jwt.ExpiredSignatureError:
        return {'response': 'Signature expired. Please log in again.',
                'status': False}
    except jwt.InvalidTokenError as e:
        return {'response': str(e), 'status': False}


def authorize_token(func):
    """
    Create a decorator function that ensures access control
    """
    @wraps(func)
    def decorators(*args, **kwargs):
        try:
            # Get token from the header where the key is Authorization
            auth_header = request.headers['Authorization']
            if not auth_header:
                return 'Unauthorized access. Please check your token', 401
            resp = decode_auth_token(auth_header)
            # If an error occurs during decoding then it returns the
            # error as defined in the decoding function
            if resp['status'] is False:
                data = {
                        'Error': resp['response']
                    }
                response = make_response(jsonify(data), 401)
                return response
            # Get current user id if decoding was successful
            g.user_id = resp['response']
        except KeyError:
            # Returns an informative error if the authorization
            # header is not added
            return 'Please include an Authorization key', 401
        return func(*args, **kwargs)
    return decorators
