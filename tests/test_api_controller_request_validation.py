from fangfangfang.test import BaseTestCase
from flask import json
import unittest
from parameterized import parameterized


class TestAPIControllerRequestValidation(BaseTestCase):
    """APIController request validation integration tests
    """

    @parameterized.expand([
        '/api/defang',
        '/api/refang'
    ])
    def test_invalid_model(self, path):
        """Asserts that passing in an invalid model in the request throws a 400
        response.
        """
        body = {
          "model" : "foo"
        }
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            path,
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        response_data = response.data.decode('utf-8')
        self.assert400(response,
                       'Response body is : ' + response_data)
        response_data_json = json.loads(response_data)
        self.assertEqual(response_data_json['detail'], '\'foo\' is not one of [\'homoglyph\']')


if __name__ == '__main__':
    unittest.main()
