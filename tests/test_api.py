"""
tests.test_api

Check all the api's we have exposed and make
sure they behave as we expect
"""
import os
import unittest
import json
from project.instance import app
from todo.models import Todo

class ServerTestCase(unittest.TestCase):
    """Check the endpoints we expect"""

    def setUp(self):
        self.client = app.test_client()

    def test_landing_page(self):
        """Test /api/v1/todos"""

        resp =  self.client.get("/api/v1/todos")
        assert resp.status_code == 200
        assert resp.content_type == 'application/json'

    def test_creating_todo_list(self):
        """/api/v1/todos should return the data we have created"""

        t1 = Todo("Test1")
        t1.save()
        t2 = Todo("Test2")
        t2.save()

        resp = self.client.get("/api/v1/todos")
        # need to call json.loads twice because resp.data is forced to string
        data = json.loads(json.loads(resp.data))
        # TODO: Fix initialising db to clear prev data
        assert len(data[0]) >= 2
