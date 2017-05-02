import status
from unittest import TestCase

from flask_sqlalchemy import SQLAlchemy
from flask import (g, request, make_response, current_app,
                   json, url_for, json)

from bucketlist.models import BucketList, BucketListItem, User, db, app
from bucketlist.config import configurations


class InitialTests(TestCase):

    def setUp(self):
        app.config.from_object(configurations['testing'])
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        self.bucketlist = {"name": "Test_BucketList"}

    def test_create_new_bucketlist(self):
        response = self.client.post('/bucketlists/',
                                    data=json.dumps(self.bucketlist),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Title can't be empty",
                      response.get_data(as_text=True))

    def test_create_an_existing_buckelist(self):
        # Create a bucketlist
        self.client.post("/bucketlists/", data=json.dumps(self.bucketlist))
        # Add the same bucketlist
        response = self.client.post("/bucketlists/",
                                    data=json.dumps(self.bucketlist))
        self.assertEqual(response.status_code, 400)

    def test_update_bucket_list(self):
        new_bucketlist_name = {"name": "Changed Name"}
        self.client.post("/bucketlists/", data=json.dumps(self.bucketlist))
        response = self.client.put("/bucketlists/1",
                                   data=json.dumps(new_bucketlist_name))
        self.assertEqual(response.status_code, 200)

    def test_update_unexisting_bucketlist(self):
        new_bucketlist_name = {"name": "Changed Name"}
        response = self.client.put("/bucketlists/1",
                                   data=json.dumps(new_bucketlist_name))
        self.assertEqual(response.status_code, 400)

    def test_delete_bucketlist(self):
        self.client.post("/bucketlists/", data=json.dumps(self.bucketlist))
        response = self.client.delete("/bucketlists/1")
        self.assertEqual(response.status_code, 204)

    def test_delete_unexisting_bucketlist(self):
        response = self.client.delete("/bucketlists/1")
        self.assertEqual(response.status_code, 400)

    def test_get_one_bucketlist(self):
        self.client.post("/bucketlists/", data=json.dumps(self.bucketlist))
        response = self.client.get("/bucketlists/1")
        self.assertEqual(response.status_code, 200)

    def test_get_unexisting_bucketlist(self):
        response = self.client.get("/bucketlists/1")
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        # db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
    unittest.main()
