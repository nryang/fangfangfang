import unittest
from parameterized import parameterized
from fangfangfang.test import BaseTestCase


class TestUIController(BaseTestCase):
    """UIController integration test stubs
    """

    def test_index(self):
        """Test case for index

        Displays the home page
        """
        headers = {
            'Accept': 'text/html',
        }
        response = self.client.open(
            '/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @parameterized.expand([
        ('/images/logo.png', 'image/png'),
        ('/images/favicon.ico', 'image/x-icon')
    ])
    def test_binaries(self, path, mime_type):
        """Test case for binaries
        """
        headers = {
            'Accept': mime_type,
        }
        response = self.client.open(
            path,
            method='GET',
            headers=headers)
        self.assert200(response)


if __name__ == '__main__':
    unittest.main()
