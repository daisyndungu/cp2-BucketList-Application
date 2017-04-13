import unittest
import status
from flask import Flask
from flask import Flask, jsonify, g, request, make_response, current_app, json
from unittest import TestCase

from bucketlist.run import create_app
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
        self.bucketlist = {"name": "Test BucketList"}

    def tearDown(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_create_new_bucketlist(self):
        response = self.client.post("/bucketlist/",
                                    data=json.dumps(self.bucketlist))
        self.assertEqual(response.status_code, 201)

    def test_create_an_existing_buckelist(self):
        # Create a bucketlist
        self.client.post("/bucketlist/", data=json.dumps(self.bucketlist))
        # Add the same bucketlist
        response = self.client.post("/bucketlist/",
                                    data=json.dumps(self.bucketlist))
        self.assertEqual(response.status_code, 400)

    def test_update_bucket_list(self):
        new_bucketlist_name = {"name": "Changed Name"}
        self.client.post("/bucketlist/", data=json.dumps(self.bucketlist))
        response = self.client.put("/bucketlist/1",
                                   data=json.dumps(new_bucketlist_name))
        self.assertEqual(response.status_code, 200)

    def test_update_unexisting_bucketlist(self):
        new_bucketlist_name = {"name": "Changed Name"}
        response = self.client.put("/bucketlist/1",
                                   data=json.dumps(new_bucketlist_name))
        self.assertEqual(response.status_code, 400)

    def test_delete_bucketlist(self):
        self.client.post("/bucketlist/", data=json.dumps(self.bucketlist))
        response = self.client.delete("/bucketlist/1")
        self.assertEqual(response.status_code, 204)

    def test_delete_unexisting_bucketlist(self):
        response = self.client.delete("/bucketlist/1")
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
