import unittest
import requests


class SmokeTest(unittest.TestCase):
    def test_maths(self):
        self.assertEquals(6, 2 + 4)

    def test_home_page_is_about_todo_lists(self):
        request = requests.get('http://localhost:5000')
        self.assertTrue(
            request.content.startswith(b'\n\n<!doctype html>\n'))
        self.assertIn(
            '<title>\n  \n    To-Do\n  \n    \n  </title>\n',
            request.text)
        self.assertTrue(request.content.endswith(b'</body>\n</html>\n'))

class TestMainPage:
    """WebTest test for title"""

    def test_main_page_returns_200(self, user, testapp):
        """Login successful."""
        # Goes to homepage
        res = testapp.get('/')
        assert res.status_code == 200

    def test_main_page_returns_expected_title(self, user, testapp):
        res = testapp.get('/')
        assert '<title>\n  \n    To-Do\n  \n    \n  </title>\n' in res

    # def test_main_page_returns_expected_content(self, user, testapp):
    #     res = testapp.get('/')
