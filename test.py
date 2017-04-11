import os

import status
from flask import Flask, jsonify, g, request, make_response, current_app
from unittest import TestCase

from .app.models import User, BucketList, BucketListItem
from .app import views
from .app.app import create_app
from .app import config


class InitialTests(TestCase):

    def setUp(self):
        self.app = create_app('test')
        self.app.config['TESTING'] = True
        self.db = views.db
        self.test_user_name = 'testuser'
        self.test_user_password = 'T3s!p4s5w0RDd12#'
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db.create_all()

    def tearDown(self):
        db = views.db
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_login(self):
        user = {
            "username": 'testuser',
            "password": 'T3s!p4s5w0RDd12#'
        }
        user = User()
        self.db.session.add(user)
        self.db.session.commit()
        assert user in self.db.session
        # # headers = self.get_accept_content_type_headers()
        response = request.post('/auth/login', data=jsonify(user))
        self.assertEqual(response.status_code, 200)
        # response_data = json.loads(response.get_data(as_text=True))
        # self.assertIn('OK', response_data)

    def test_user_registration(self):
        user = {
            "username": "daisy",
            "email": "daisywndungu@gmail.com",
            "password": '1234'
        }
        response = request.post("/auth/register", user_data=user)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
