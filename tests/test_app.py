# tests/test_app.py
import unittest
from app import app  # Import your Flask app from app.py


class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    # Add more tests here as needed


if __name__ == "__main__":
    unittest.main()
