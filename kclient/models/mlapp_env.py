# coding: utf-8

"""
    Kibernetika project, backend component

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MlappEnv(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'secret_key': 'str',
        'value': 'str',
        'value_from_secret': 'str'
    }

    attribute_map = {
        'name': 'name',
        'secret_key': 'secretKey',
        'value': 'value',
        'value_from_secret': 'valueFromSecret'
    }

    def __init__(self, name=None, secret_key=None, value=None, value_from_secret=None):  # noqa: E501
        """MlappEnv - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._secret_key = None
        self._value = None
        self._value_from_secret = None
        self.discriminator = None

        self.name = name
        if secret_key is not None:
            self.secret_key = secret_key
        if value is not None:
            self.value = value
        if value_from_secret is not None:
            self.value_from_secret = value_from_secret

    @property
    def name(self):
        """Gets the name of this MlappEnv.  # noqa: E501


        :return: The name of this MlappEnv.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MlappEnv.


        :param name: The name of this MlappEnv.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def secret_key(self):
        """Gets the secret_key of this MlappEnv.  # noqa: E501


        :return: The secret_key of this MlappEnv.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this MlappEnv.


        :param secret_key: The secret_key of this MlappEnv.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def value(self):
        """Gets the value of this MlappEnv.  # noqa: E501


        :return: The value of this MlappEnv.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MlappEnv.


        :param value: The value of this MlappEnv.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_from_secret(self):
        """Gets the value_from_secret of this MlappEnv.  # noqa: E501


        :return: The value_from_secret of this MlappEnv.  # noqa: E501
        :rtype: str
        """
        return self._value_from_secret

    @value_from_secret.setter
    def value_from_secret(self, value_from_secret):
        """Sets the value_from_secret of this MlappEnv.


        :param value_from_secret: The value_from_secret of this MlappEnv.  # noqa: E501
        :type: str
        """

        self._value_from_secret = value_from_secret

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MlappEnv, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MlappEnv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
