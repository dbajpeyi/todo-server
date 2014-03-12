import os
import unittest
from project.instance import app
from todo import api

class ServerTestCase(unittest.TestCase):
    """Check the endpoints we expect"""

    def setUp(self):
        self.app = app.test_client()

    def test_landing_page(self):
        """Test /api/v1/todos"""
        resp =  self.app.get("/api/v1/todos")
        assert resp.status_code == 200
        assert resp.content_type == 'application/json'
