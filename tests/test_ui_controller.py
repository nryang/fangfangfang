import unittest

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

    def test_logo(self):
        """Test case for logo

        Returns the logo
        """
        headers = {
            'Accept': 'image/png',
        }
        response = self.client.open(
            '/images/logo.png',
            method='GET',
            headers=headers)
        self.assert200(response)


if __name__ == '__main__':
    unittest.main()
