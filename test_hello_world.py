import unittest
from hello_world import app, greet, generate_html


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_greet_function(self):
        expected_greeting = 'Welcome to CI/CD 101 using GitHub Actions!'
        self.assertEqual(greet(), expected_greeting)

    def test_generate_html_function(self):
        message = "Test Message"
        html_output = generate_html(message)
        self.assertIn(message, html_output)
        self.assertIn("<html>", html_output)
        self.assertIn("</html>", html_output)

    def test_hello_world_route(self):
        response = self.app.get('/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to CI/CD 101 using GitHub Actions!',
                      response.data)
        self.assertIn(b'<html>', response.data)
        self.assertIn(b'</html>', response.data)


if __name__ == '__main__':
    unittest.main()
