"""NOTE: This file is auto generated by OpenAPI Generator (https://openapi-generator.tech).

Do not edit the file manually.
"""

import connexion

from fangfangfang.controllers.impl import ui_controller_impl


def favicon():  # noqa: E501
    """Returns the favicon

     # noqa: E501


    :rtype: file
    """
    return ui_controller_impl.favicon()


def index():  # noqa: E501
    """Displays the home page

     # noqa: E501


    :rtype: str
    """
    return ui_controller_impl.index()


def logo():  # noqa: E501
    """Returns the logo

     # noqa: E501


    :rtype: file
    """
    return ui_controller_impl.logo()