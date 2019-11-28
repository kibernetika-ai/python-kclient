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


class ModelsTaskFormElement(object):
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
        'elements': 'list[ModelsTaskFormElement]',
        'hidden': 'bool',
        'label': 'str',
        'list_type': 'str',
        'name': 'str',
        'options': 'list[str]',
        'required': 'bool',
        'type': 'str',
        'value': 'ModelsTaskFormElementValue',
        'width': 'int'
    }

    attribute_map = {
        'elements': 'elements',
        'hidden': 'hidden',
        'label': 'label',
        'list_type': 'listType',
        'name': 'name',
        'options': 'options',
        'required': 'required',
        'type': 'type',
        'value': 'value',
        'width': 'width'
    }

    def __init__(self, elements=None, hidden=None, label=None, list_type=None, name=None, options=None, required=None, type=None, value=None, width=None):  # noqa: E501
        """ModelsTaskFormElement - a model defined in Swagger"""  # noqa: E501

        self._elements = None
        self._hidden = None
        self._label = None
        self._list_type = None
        self._name = None
        self._options = None
        self._required = None
        self._type = None
        self._value = None
        self._width = None
        self.discriminator = None

        if elements is not None:
            self.elements = elements
        if hidden is not None:
            self.hidden = hidden
        if label is not None:
            self.label = label
        if list_type is not None:
            self.list_type = list_type
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if required is not None:
            self.required = required
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if width is not None:
            self.width = width

    @property
    def elements(self):
        """Gets the elements of this ModelsTaskFormElement.  # noqa: E501


        :return: The elements of this ModelsTaskFormElement.  # noqa: E501
        :rtype: list[ModelsTaskFormElement]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """Sets the elements of this ModelsTaskFormElement.


        :param elements: The elements of this ModelsTaskFormElement.  # noqa: E501
        :type: list[ModelsTaskFormElement]
        """

        self._elements = elements

    @property
    def hidden(self):
        """Gets the hidden of this ModelsTaskFormElement.  # noqa: E501


        :return: The hidden of this ModelsTaskFormElement.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ModelsTaskFormElement.


        :param hidden: The hidden of this ModelsTaskFormElement.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def label(self):
        """Gets the label of this ModelsTaskFormElement.  # noqa: E501


        :return: The label of this ModelsTaskFormElement.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelsTaskFormElement.


        :param label: The label of this ModelsTaskFormElement.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def list_type(self):
        """Gets the list_type of this ModelsTaskFormElement.  # noqa: E501


        :return: The list_type of this ModelsTaskFormElement.  # noqa: E501
        :rtype: str
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """Sets the list_type of this ModelsTaskFormElement.


        :param list_type: The list_type of this ModelsTaskFormElement.  # noqa: E501
        :type: str
        """

        self._list_type = list_type

    @property
    def name(self):
        """Gets the name of this ModelsTaskFormElement.  # noqa: E501


        :return: The name of this ModelsTaskFormElement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsTaskFormElement.


        :param name: The name of this ModelsTaskFormElement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this ModelsTaskFormElement.  # noqa: E501


        :return: The options of this ModelsTaskFormElement.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ModelsTaskFormElement.


        :param options: The options of this ModelsTaskFormElement.  # noqa: E501
        :type: list[str]
        """

        self._options = options

    @property
    def required(self):
        """Gets the required of this ModelsTaskFormElement.  # noqa: E501


        :return: The required of this ModelsTaskFormElement.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ModelsTaskFormElement.


        :param required: The required of this ModelsTaskFormElement.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def type(self):
        """Gets the type of this ModelsTaskFormElement.  # noqa: E501


        :return: The type of this ModelsTaskFormElement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelsTaskFormElement.


        :param type: The type of this ModelsTaskFormElement.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this ModelsTaskFormElement.  # noqa: E501


        :return: The value of this ModelsTaskFormElement.  # noqa: E501
        :rtype: ModelsTaskFormElementValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelsTaskFormElement.


        :param value: The value of this ModelsTaskFormElement.  # noqa: E501
        :type: ModelsTaskFormElementValue
        """

        self._value = value

    @property
    def width(self):
        """Gets the width of this ModelsTaskFormElement.  # noqa: E501


        :return: The width of this ModelsTaskFormElement.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ModelsTaskFormElement.


        :param width: The width of this ModelsTaskFormElement.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(ModelsTaskFormElement, dict):
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
        if not isinstance(other, ModelsTaskFormElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
