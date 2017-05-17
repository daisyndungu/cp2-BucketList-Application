import json
from unittest import TestCase
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import requests

from bucketlist import config
from bucketlist.config import configurations
from bucketlist.models import User
from bucketlist import db, create_app


class BaseTest(TestCase):
    """ Initialising TestCase"""

    def setUp(self):
        self.app = create_app('testing')
        self.database = db
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.database.drop_all()
        self.database.create_all()

        # create and add a test user
        test_user = User(username='test_user', email='test_user@gmail.com',
                         password='password')
        self.database.session.add(test_user)
        self.database.session.commit()

        """ Generate authentication token"""
        user = {"username": "test_user", "password": "password"}
        response = self.client.post(
            '/auth/login', data=json.dumps(user),
            headers={'Content-Type': 'application/json'})
        response_data = json.loads(response.data)
        token = response_data['Token']
        self.headers = {'Authorization': token,
                        'Content-Type': 'application/json',
                        }

    def tearDown(self):
        self.database.session.remove()
        self.database.drop_all()
        self.app_context.pop()
