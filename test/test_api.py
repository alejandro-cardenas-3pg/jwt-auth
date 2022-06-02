import unittest
from main import create_flask_app


class ApiTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print("Creating Flask App")
        self.app = create_flask_app().test_client()

    def tearDown(self) -> None:
        print("Tear down.")
        pass

    def test_root(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Hello, World')


if __name__ == '__main__':
    unittest.main()
