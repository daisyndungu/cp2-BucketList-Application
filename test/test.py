import os

import unittest
import status
from flask import Flask
from flask import Flask, jsonify, g, request, make_response, current_app, json
from unittest import TestCase

from bucketlist.app import create_app
from bucketlist.models import db
from bucketlist import config


class InitialTests(TestCase):

    def setUp(self):
        self.app = create_app("test")
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db
        self.db.create_all()
        self.bucketlist = {
            "name": "Test BucketList"
        }

    def tearDown(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_create_new_bucketlist(self):
        new_bucket_list = {"name": "Travel"}

        response = self.client.post("/bucketlist",
                                    data=json.dumps(new_bucket_list))
        self.assertEqual(response.status_code, 201)

    def test_create_an_existing_buckelist(self):
        bucketlist = {
            "name": "Test BucketList"
        }
        response = self.client.post("/bucketlist",
                                    data=json.dumps(bucketlist))
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
