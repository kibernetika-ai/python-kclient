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


class ApplicationProjectServingJobOutput(object):
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
        'file': 'str',
        'label': 'str',
        'link': 'str'
    }

    attribute_map = {
        'file': 'File',
        'label': 'Label',
        'link': 'Link'
    }

    def __init__(self, file=None, label=None, link=None):  # noqa: E501
        """ApplicationProjectServingJobOutput - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self._label = None
        self._link = None
        self.discriminator = None

        if file is not None:
            self.file = file
        if label is not None:
            self.label = label
        self.link = link

    @property
    def file(self):
        """Gets the file of this ApplicationProjectServingJobOutput.  # noqa: E501


        :return: The file of this ApplicationProjectServingJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ApplicationProjectServingJobOutput.


        :param file: The file of this ApplicationProjectServingJobOutput.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def label(self):
        """Gets the label of this ApplicationProjectServingJobOutput.  # noqa: E501


        :return: The label of this ApplicationProjectServingJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ApplicationProjectServingJobOutput.


        :param label: The label of this ApplicationProjectServingJobOutput.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def link(self):
        """Gets the link of this ApplicationProjectServingJobOutput.  # noqa: E501


        :return: The link of this ApplicationProjectServingJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ApplicationProjectServingJobOutput.


        :param link: The link of this ApplicationProjectServingJobOutput.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

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
        if issubclass(ApplicationProjectServingJobOutput, dict):
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
        if not isinstance(other, ApplicationProjectServingJobOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
