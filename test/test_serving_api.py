# coding: utf-8

"""
    Kibernetika project, backend component

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.serving_api import ServingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestServingApi(unittest.TestCase):
    """ServingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.serving_api.ServingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_serving_delete(self):
        """Test case for serving_delete

        Delete serving  # noqa: E501
        """
        pass

    def test_serving_info(self):
        """Test case for serving_info

        Return serving's info  # noqa: E501
        """
        pass

    def test_update_serving(self):
        """Test case for update_serving

        Update serving  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
