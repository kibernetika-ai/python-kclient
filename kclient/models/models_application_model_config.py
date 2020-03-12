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


class ModelsApplicationModelConfig(object):
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
        'is_default': 'bool',
        'serving': 'ModelsApplicationModelConfigServing',
        'serving_spec': 'MlappServingSpec'
    }

    attribute_map = {
        'is_default': 'isDefault',
        'serving': 'serving',
        'serving_spec': 'servingSpec'
    }

    def __init__(self, is_default=None, serving=None, serving_spec=None):  # noqa: E501
        """ModelsApplicationModelConfig - a model defined in Swagger"""  # noqa: E501

        self._is_default = None
        self._serving = None
        self._serving_spec = None
        self.discriminator = None

        if is_default is not None:
            self.is_default = is_default
        if serving is not None:
            self.serving = serving
        if serving_spec is not None:
            self.serving_spec = serving_spec

    @property
    def is_default(self):
        """Gets the is_default of this ModelsApplicationModelConfig.  # noqa: E501


        :return: The is_default of this ModelsApplicationModelConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this ModelsApplicationModelConfig.


        :param is_default: The is_default of this ModelsApplicationModelConfig.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def serving(self):
        """Gets the serving of this ModelsApplicationModelConfig.  # noqa: E501


        :return: The serving of this ModelsApplicationModelConfig.  # noqa: E501
        :rtype: ModelsApplicationModelConfigServing
        """
        return self._serving

    @serving.setter
    def serving(self, serving):
        """Sets the serving of this ModelsApplicationModelConfig.


        :param serving: The serving of this ModelsApplicationModelConfig.  # noqa: E501
        :type: ModelsApplicationModelConfigServing
        """

        self._serving = serving

    @property
    def serving_spec(self):
        """Gets the serving_spec of this ModelsApplicationModelConfig.  # noqa: E501


        :return: The serving_spec of this ModelsApplicationModelConfig.  # noqa: E501
        :rtype: MlappServingSpec
        """
        return self._serving_spec

    @serving_spec.setter
    def serving_spec(self, serving_spec):
        """Sets the serving_spec of this ModelsApplicationModelConfig.


        :param serving_spec: The serving_spec of this ModelsApplicationModelConfig.  # noqa: E501
        :type: MlappServingSpec
        """

        self._serving_spec = serving_spec

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
        if issubclass(ModelsApplicationModelConfig, dict):
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
        if not isinstance(other, ModelsApplicationModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
