import status
import unittest
from flask import Flask
from unittest import TestCase
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, g, request, make_response, current_app, json

from bucketlist.models import db


class InitialTests(TestCase):

    def setUp(self):
        self.app = Flask("test")
        self.app.config.from_object("bucketlist.config.TestingConfig")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = SQLAlchemy(self.app)
        self.db.create_all()
        self.bucketlistitem = {"name": "Test Item"}

    def tearDown(self):
        self.db = db
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def bucketlist(self):
        bucketlist = {"name": "Travel"}
        self.client.post("/bucketlist/", data=json.dumps(bucketlist))

    def test_create_new_bucketlistitem(self):
        # Create a bucketlist
        self.bucketlist()
        # Create an item for the bucketlist
        response = self.client.post("/bucketlist/1/item/",
                                    data=json.dumps(self.bucketlistitem))
        self.assertEqual(response.status_code, 201)

    def test_create_an_existing_buckelistitem(self):
        # Create a bucketlist
        self.bucketlist()
        # Add an item
        self.client.post("/bucketlist/1/item/",
                         data=json.dumps(self.bucketlistitem))
        # Add the same bucketlistitem
        response = self.client.post("/bucketlist/1/item/",
                                    data=json.dumps(self.bucketlistitem))
        self.assertEqual(response.status_code, 400)

    def test_create_item_for_unexisting_bucketlist(self):
        response = self.client.post("/bucketlist/1/item/",
                                    data=json.dumps(self.bucketlistitem))
        self.assertEqual(response.status_code, 400)

    def test_create_item_empty_name(self):
        self.bucketlist()
        bucketlistitem = {"name:": ""}
        response = self.client.post("/bucketlist/1/item/",
                                    data=json.dumps(bucketlistitem))
        self.assertEqual(response.status_code, 400)

    def test_update_bucket_list_item(self):
        self.bucketlist()
        new_bucketlistitem_name = {"name": "Changed Item"}
        self.client.post("/bucketlist/1", data=json.dumps(self.bucketlistitem))
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name))
        self.assertEqual(response.status_code, 200)

    def test_update_unexisting_bucketlistitem(self):
        self.bucketlist()
        new_bucketlistitem_name = {"name": "Changed Item"}
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name))
        self.assertEqual(response.status_code, 400)

    def test_update_unexisting_bucketlistitem_in_unexisting_bucketlist(self):
        new_bucketlistitem_name = {"name": "Changed Item"}
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name))
        self.assertEqual(response.status_code, 400)

    def test_delete_bucketlistitem(self):
        self.bucketlist()
        self.client.post("/bucketlist/1/item",
                         data=json.dumps(self.bucketlistitem))
        response = self.client.delete("/bucketlist/1/item/1")
        self.assertEqual(response.status_code, 204)

    def test_delete_unexisting_bucketlistitem(self):
        self.bucketlist()
        response = self.client.delete("/bucketlist/1/item/1")
        self.assertEqual(response.status_code, 400)

    def test_delete_unexisting_bucketlistitem_in_unexisting_bucketlist(self):
        response = self.client.delete("/bucketlist/1/item/1")
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
