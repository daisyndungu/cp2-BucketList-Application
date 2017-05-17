import status
from flask import Flask
from unittest import TestCase
from flask import json

from bucketlist.tests.setup import BaseTest


class InitialTests(BaseTest):

    def bucketlist(self):
        """
            Create a bucketlist
        """
        bucketlist = {"name": "Travel"}
        self.client.post("/bucketlists/",
                         data=json.dumps({"name": "Test Item"}),
                         headers=self.headers)

    def test_create_new_bucketlistitem(self):
        # Create a bucketlist
        self.bucketlist()
        # Create an item for the bucketlist
        response = self.client.post("/bucketlists/1/items/",
                                    data=json.dumps({"name": "Test Item"}),
                                    headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_create_an_existing_buckelistitem(self):
        # Create a bucketlist
        self.bucketlist()
        # Add an item
        res = self.client.post("/bucketlists/1/items/",
                               data=json.dumps({"name": "Test Item"}),
                               headers=self.headers)
        # Add the same bucketlistitem
        response = self.client.post("/bucketlists/1/items/",
                                    data=json.dumps({"name": "Test Item"}),
                                    headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_create_item_for_unexisting_bucketlist(self):
        response = self.client.post("/bucketlists/1/items/",
                                    data=json.dumps({"name": "Test Item"}),
                                    headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_create_item_empty_name(self):
        self.bucketlist()
        bucketlistitem = {"name:": ""}
        response = self.client.post("/bucketlists/1/items/",
                                    data=json.dumps(bucketlistitem),
                                    headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_update_bucket_list_item(self):
        self.bucketlist()
        new_bucketlistitem_name = {"name": "Changed Item"}
        self.client.post("/bucketlists/1/items/",
                         data=json.dumps({"name": "Test Item"}),
                         headers=self.headers)
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name),
                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_update_unexisting_bucketlistitem(self):
        self.bucketlist()
        new_bucketlistitem_name = {"name": "Changed Item"}
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name),
                                   headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_update_unexisting_bucketlistitem_in_unexisting_bucketlist(self):
        new_bucketlistitem_name = {"name": "Changed Item"}
        response = self.client.put("/bucketlists/1/items/1",
                                   data=json.dumps(new_bucketlistitem_name),
                                   headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_delete_bucketlistitem(self):
        self.bucketlist()
        self.client.post("/bucketlists/1/items/",
                         data=json.dumps({"name": "Test Item"}),
                         headers=self.headers)
        response = self.client.delete("/bucketlists/1/items/1",
                                      headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_unexisting_bucketlistitem(self):
        self.bucketlist()
        response = self.client.delete("/bucketlists/1/items/1",
                                      headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_delete_unexisting_bucketlistitem_in_unexisting_bucketlist(self):
        response = self.client.delete("/bucketlists/1/items/1",
                                      headers=self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_one_bucketlistitem(self):
        self.bucketlist()
        self.client.post("/bucketlists/1/items/",
                         data=json.dumps({"name": "Test Item"}),
                         headers=self.headers)
        response = self.client.get("/bucketlists/1/items/1",
                                   headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_unexisting_bucketlistitem_in_unexisting_bucketlist(self):
        response = self.client.get("/bucketlists/1/items/1",
                                   headers=self.headers)
        self.assertEqual(response.status_code, 404)

    def test_get_unexisting_bucketlistitem(self):
        self.bucketlist()
        response = self.client.get("/bucketlists/1/items/1",
                                   headers=self.headers)
        self.assertEqual(response.status_code, 400)
