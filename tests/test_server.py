import os
import unittest
import sys
print sys.path
from todo import server

class ServerTestCase(unittest.TestCase):
    """Check the endpoints we expect"""

    def setUp(self):
        self.app = server.app.test_client()

    def test_landing_page(self):
        """Test /"""
        resp =  self.app.get("/")
        assert resp.status_code == 200
        assert resp.data == "Hello world!"

