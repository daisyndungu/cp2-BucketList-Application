import time
import datetime
from flask_jwt import jwt
from functools import wraps
from flask import request, make_response, jsonify, g

from models import User, app


def decode_auth_token(auth_token):
    """
    Decodes the auth token
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
    @wraps(func)
    def decorators(*args, **kwargs):
        try:
            auth_header = request.headers['Authorization']
            if not auth_header:
                return 'Unauthorized access. Please check your token', 401
            resp = decode_auth_token(auth_header)
            if resp['status'] is False:
                data = {
                        'Error': resp['response']
                    }
                response = make_response(jsonify(data), 401)
                return response
            g.user_id = resp['response']
        except KeyError:
            return 'Please include an Authorization key', 401
        return func(*args, **kwargs)
    return decorators
