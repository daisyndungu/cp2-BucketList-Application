import status
from unittest import TestCase
from flask import json

from bucketlist.tests.setup import BaseTest


class InitialTests(BaseTest):

    def test_create_new_bucketlist(self):
        response = self.client.post('/bucketlists/',
                                    data=json.dumps({"name": "Test_BucketList"}
                                                    ),
                                    headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_create_an_existing_buckelist(self):
        # Create a bucketlist
        self.client.post("/bucketlists/",
                         data=json.dumps({"name": "Test_BucketList"}),
                         headers=self.headers)
        # Add the same bucketlist
        response = self.client.post("/bucketlists/",
                                    data=json.dumps({"name": "Test_BucketList"}
                                                    ), headers=self.headers
                                    )
        self.assertEqual(response.status_code, 400)

    def test_update_bucket_list(self):
        new_bucketlist_name = {"name": "Changed Name"}
        self.client.post("/bucketlists/",
                         data=json.dumps({"name": "Test_BucketList"}),
                         headers=self.headers)
        response = self.client.put("/bucketlists/1",
                                   data=json.dumps(new_bucketlist_name),
                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_update_unexisting_bucketlist(self):
        new_bucketlist_name = {"name": "Changed Name"}
        response = self.client.put("/bucketlists/1",
                                   data=json.dumps(new_bucketlist_name),
                                   headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_delete_bucketlist(self):
        self.client.post("/bucketlists/", data=json.dumps(
                         {"name": "Test_BucketList"}), headers=self.headers
                         )
        response = self.client.delete("/bucketlists/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_unexisting_bucketlist(self):
        response = self.client.delete("/bucketlists/1",
                                      headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_one_bucketlist(self):
        self.client.post("/bucketlists/",
                         data=json.dumps({"name": "Test_BucketList"}),
                         headers=self.headers)
        response = self.client.get("/bucketlists/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_unexisting_bucketlist(self):
        response = self.client.get("/bucketlists/1", headers=self.headers)
        self.assertEqual(response.status_code, 400)
