"""NOTE: This file is auto generated by OpenAPI Generator (https://openapi-generator.tech).

Do not edit the file manually.
"""
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fangfangfang.models.base_model_ import Model
from fangfangfang.models.model import Model
from fangfangfang import util

from fangfangfang.models.model import Model  # noqa: E501

class RefangRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, model=None, contents=None):  # noqa: E501
        """RefangRequest - a model defined in OpenAPI

        :param model: The model of this RefangRequest.  # noqa: E501
        :type model: Model
        :param contents: The contents of this RefangRequest.  # noqa: E501
        :type contents: List[str]
        """
        self.openapi_types = {
            'model': Model,
            'contents': List[str]
        }

        self.attribute_map = {
            'model': 'model',
            'contents': 'contents'
        }

        self._model = model
        self._contents = contents

    @classmethod
    def from_dict(cls, dikt) -> 'RefangRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RefangRequest of this RefangRequest.  # noqa: E501
        :rtype: RefangRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def model(self):
        """Gets the model of this RefangRequest.


        :return: The model of this RefangRequest.
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this RefangRequest.


        :param model: The model of this RefangRequest.
        :type model: Model
        """

        self._model = model

    @property
    def contents(self):
        """Gets the contents of this RefangRequest.


        :return: The contents of this RefangRequest.
        :rtype: List[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this RefangRequest.


        :param contents: The contents of this RefangRequest.
        :type contents: List[str]
        """
        if contents is None:
            raise ValueError("Invalid value for `contents`, must not be `None`")  # noqa: E501

        self._contents = contents
