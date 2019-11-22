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

from kclient.models.models_task_form_element import ModelsTaskFormElement  # noqa: F401,E501


class ModelsInferenceVersion(object):
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
        'updated': 'str',
        'form': 'list[ModelsTaskFormElement]',
        'created': 'str',
        'serving_config_template': 'str',
        'version': 'str',
        'edge_config_template': 'str'
    }

    attribute_map = {
        'updated': 'Updated',
        'form': 'Form',
        'created': 'Created',
        'serving_config_template': 'ServingConfigTemplate',
        'version': 'Version',
        'edge_config_template': 'EdgeConfigTemplate'
    }

    def __init__(self, updated=None, form=None, created=None, serving_config_template=None, version=None, edge_config_template=None):  # noqa: E501
        """ModelsInferenceVersion - a model defined in Swagger"""  # noqa: E501

        self._updated = None
        self._form = None
        self._created = None
        self._serving_config_template = None
        self._version = None
        self._edge_config_template = None
        self.discriminator = None

        self.updated = updated
        self.form = form
        self.created = created
        self.serving_config_template = serving_config_template
        self.version = version
        self.edge_config_template = edge_config_template

    @property
    def updated(self):
        """Gets the updated of this ModelsInferenceVersion.  # noqa: E501


        :return: The updated of this ModelsInferenceVersion.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ModelsInferenceVersion.


        :param updated: The updated of this ModelsInferenceVersion.  # noqa: E501
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def form(self):
        """Gets the form of this ModelsInferenceVersion.  # noqa: E501


        :return: The form of this ModelsInferenceVersion.  # noqa: E501
        :rtype: list[ModelsTaskFormElement]
        """
        return self._form

    @form.setter
    def form(self, form):
        """Sets the form of this ModelsInferenceVersion.


        :param form: The form of this ModelsInferenceVersion.  # noqa: E501
        :type: list[ModelsTaskFormElement]
        """
        if form is None:
            raise ValueError("Invalid value for `form`, must not be `None`")  # noqa: E501

        self._form = form

    @property
    def created(self):
        """Gets the created of this ModelsInferenceVersion.  # noqa: E501


        :return: The created of this ModelsInferenceVersion.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsInferenceVersion.


        :param created: The created of this ModelsInferenceVersion.  # noqa: E501
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def serving_config_template(self):
        """Gets the serving_config_template of this ModelsInferenceVersion.  # noqa: E501


        :return: The serving_config_template of this ModelsInferenceVersion.  # noqa: E501
        :rtype: str
        """
        return self._serving_config_template

    @serving_config_template.setter
    def serving_config_template(self, serving_config_template):
        """Sets the serving_config_template of this ModelsInferenceVersion.


        :param serving_config_template: The serving_config_template of this ModelsInferenceVersion.  # noqa: E501
        :type: str
        """
        if serving_config_template is None:
            raise ValueError("Invalid value for `serving_config_template`, must not be `None`")  # noqa: E501

        self._serving_config_template = serving_config_template

    @property
    def version(self):
        """Gets the version of this ModelsInferenceVersion.  # noqa: E501


        :return: The version of this ModelsInferenceVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelsInferenceVersion.


        :param version: The version of this ModelsInferenceVersion.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def edge_config_template(self):
        """Gets the edge_config_template of this ModelsInferenceVersion.  # noqa: E501


        :return: The edge_config_template of this ModelsInferenceVersion.  # noqa: E501
        :rtype: str
        """
        return self._edge_config_template

    @edge_config_template.setter
    def edge_config_template(self, edge_config_template):
        """Sets the edge_config_template of this ModelsInferenceVersion.


        :param edge_config_template: The edge_config_template of this ModelsInferenceVersion.  # noqa: E501
        :type: str
        """
        if edge_config_template is None:
            raise ValueError("Invalid value for `edge_config_template`, must not be `None`")  # noqa: E501

        self._edge_config_template = edge_config_template

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
        if issubclass(ModelsInferenceVersion, dict):
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
        if not isinstance(other, ModelsInferenceVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
