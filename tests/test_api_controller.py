"""NOTE: This file is auto generated by OpenAPI Generator (https://openapi-generator.tech).

Do not edit the file manually.
"""
# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json

from fangfangfang.test import BaseTestCase


class TestAPIController(BaseTestCase):
    """APIController integration test stubs

    NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def test_defang(self):
        """Test case for defang

        Defang content
        """
        body = {
  "contents" : [ "The quick brown fox.com jumps over the lazy dog.meow", "The quick brown fox.com jumps over the lazy dog.meow" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/defang',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_refang(self):
        """Test case for refang

        Refang content
        """
        body = {
  "contents" : [ "The quick brown ſᴏ×.ᴄᴏm jumps over the lazy ⅆᴏƍ.m℮ᴏɯ", "The quick brown ſᴏ×.ᴄᴏm jumps over the lazy ⅆᴏƍ.m℮ᴏɯ" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/refang',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()