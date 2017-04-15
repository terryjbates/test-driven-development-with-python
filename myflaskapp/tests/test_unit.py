import unittest
import requests


class SmokeTest(unittest.TestCase):
    def test_maths(self):
        self.assertEquals(6, 2 + 4)

    def test_home_page_is_about_todo_lists(self):
        request = requests.get('http://localhost:5000')
        self.assertTrue(
            request.content.startswith(bytes('\n\n<!doctype html>\n', 'utf-8')))
        self.assertIn(
            '<title>\n  \n    tdd_with_python\n  \n    \n  </title>\n',
            request.text)
        self.assertTrue(
            request.content.endswith(bytes('</body>\n</html>\n', 'utf-8')))
