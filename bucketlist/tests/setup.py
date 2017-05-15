import json
from flask_testing import TestCase
from bucketlist.config import configurations
from bucketlist.models import User
from bucketlist import db, app


class BaseTest(TestCase):
    """ Initialising TestCase"""

    def create_app(self, app=app):
        """ Initialize app"""
        app.config.from_object(configurations['testing'])
        return app

    def setUp(self):
        self.client = self.create_app().test_client()
        db.create_all()

        # create and add a test user
        test_user = User(username='test_user', email='test_user@gmail.com',
                         password='password')
        db.session.add(test_user)
        db.session.commit()

    def get_header(self):
        """ Generate authentication token"""
        user = {"username": "test_user", "password": "password"}
        response = self.client.post(
            '/auth/login', data=json.dumps(user),
            content_type='application/json')
        response_data = response.json()
        token = response_data['Token']
        return {'Authorization': str(token),
                'Content-Type': 'application/json',
                }

    def tearDown(self):
        db.drop_all()
