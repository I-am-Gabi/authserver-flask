import unittest
from api.app import create_app
from flask import request

sys.path.append(os.path.abspath(__name__))

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(mode="development")

    def test_request_args(self):
        with self.app.test_client('/user'):
            self.assertEqual(request.args.get('status'), 'ok')