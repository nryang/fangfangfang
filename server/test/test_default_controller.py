# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from server.models.defang_request import DefangRequest  # noqa: E501
from server.models.defang_response import DefangResponse  # noqa: E501
from server.models.refang_request import RefangRequest  # noqa: E501
from server.models.refang_response import RefangResponse  # noqa: E501
from server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs

    NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def test_defang(self):
        """Test case for defang

        Defang content
        """
        defang_request = {
  "contents" : [ "https://somewebsite.com", "https://somewebsite.com" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/defang',
            method='POST',
            headers=headers,
            data=json.dumps(defang_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_refang(self):
        """Test case for refang

        Refang content
        """
        refang_request = {
  "contents" : [ "hxxp:\\/\\/somewebsite[dot]com", "hxxp:\\/\\/somewebsite[dot]com" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/refang',
            method='POST',
            headers=headers,
            data=json.dumps(refang_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()