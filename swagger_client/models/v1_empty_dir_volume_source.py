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


class V1EmptyDirVolumeSource(object):
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
        'size_limit': 'str',
        'medium': 'str'
    }

    attribute_map = {
        'size_limit': 'sizeLimit',
        'medium': 'medium'
    }

    def __init__(self, size_limit=None, medium=None):  # noqa: E501
        """V1EmptyDirVolumeSource - a model defined in Swagger"""  # noqa: E501

        self._size_limit = None
        self._medium = None
        self.discriminator = None

        if size_limit is not None:
            self.size_limit = size_limit
        if medium is not None:
            self.medium = medium

    @property
    def size_limit(self):
        """Gets the size_limit of this V1EmptyDirVolumeSource.  # noqa: E501

        Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir  # noqa: E501

        :return: The size_limit of this V1EmptyDirVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._size_limit

    @size_limit.setter
    def size_limit(self, size_limit):
        """Sets the size_limit of this V1EmptyDirVolumeSource.

        Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir  # noqa: E501

        :param size_limit: The size_limit of this V1EmptyDirVolumeSource.  # noqa: E501
        :type: str
        """

        self._size_limit = size_limit

    @property
    def medium(self):
        """Gets the medium of this V1EmptyDirVolumeSource.  # noqa: E501

        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir  # noqa: E501

        :return: The medium of this V1EmptyDirVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._medium

    @medium.setter
    def medium(self, medium):
        """Sets the medium of this V1EmptyDirVolumeSource.

        What type of storage medium should back this directory. The default is \"\" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir  # noqa: E501

        :param medium: The medium of this V1EmptyDirVolumeSource.  # noqa: E501
        :type: str
        """

        self._medium = medium

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
        if issubclass(V1EmptyDirVolumeSource, dict):
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
        if not isinstance(other, V1EmptyDirVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
