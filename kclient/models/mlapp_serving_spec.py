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


class MlappServingSpec(object):
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
        'model': 'str',
        'options': 'MlappServingSpecOptions',
        'out_filter': 'list[str]',
        'out_mime_type': 'str',
        'params': 'list[MlappServingSpecParam]',
        'raw_input': 'bool',
        'response': 'list[MlappServingResponseParam]',
        'signature': 'str',
        'template': 'str'
    }

    attribute_map = {
        'model': 'model',
        'options': 'options',
        'out_filter': 'outFilter',
        'out_mime_type': 'outMimeType',
        'params': 'params',
        'raw_input': 'rawInput',
        'response': 'response',
        'signature': 'signature',
        'template': 'template'
    }

    def __init__(self, model=None, options=None, out_filter=None, out_mime_type=None, params=None, raw_input=None, response=None, signature=None, template=None):  # noqa: E501
        """MlappServingSpec - a model defined in Swagger"""  # noqa: E501

        self._model = None
        self._options = None
        self._out_filter = None
        self._out_mime_type = None
        self._params = None
        self._raw_input = None
        self._response = None
        self._signature = None
        self._template = None
        self.discriminator = None

        if model is not None:
            self.model = model
        if options is not None:
            self.options = options
        if out_filter is not None:
            self.out_filter = out_filter
        if out_mime_type is not None:
            self.out_mime_type = out_mime_type
        if params is not None:
            self.params = params
        if raw_input is not None:
            self.raw_input = raw_input
        if response is not None:
            self.response = response
        if signature is not None:
            self.signature = signature
        if template is not None:
            self.template = template

    @property
    def model(self):
        """Gets the model of this MlappServingSpec.  # noqa: E501


        :return: The model of this MlappServingSpec.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this MlappServingSpec.


        :param model: The model of this MlappServingSpec.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def options(self):
        """Gets the options of this MlappServingSpec.  # noqa: E501


        :return: The options of this MlappServingSpec.  # noqa: E501
        :rtype: MlappServingSpecOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MlappServingSpec.


        :param options: The options of this MlappServingSpec.  # noqa: E501
        :type: MlappServingSpecOptions
        """

        self._options = options

    @property
    def out_filter(self):
        """Gets the out_filter of this MlappServingSpec.  # noqa: E501


        :return: The out_filter of this MlappServingSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._out_filter

    @out_filter.setter
    def out_filter(self, out_filter):
        """Sets the out_filter of this MlappServingSpec.


        :param out_filter: The out_filter of this MlappServingSpec.  # noqa: E501
        :type: list[str]
        """

        self._out_filter = out_filter

    @property
    def out_mime_type(self):
        """Gets the out_mime_type of this MlappServingSpec.  # noqa: E501


        :return: The out_mime_type of this MlappServingSpec.  # noqa: E501
        :rtype: str
        """
        return self._out_mime_type

    @out_mime_type.setter
    def out_mime_type(self, out_mime_type):
        """Sets the out_mime_type of this MlappServingSpec.


        :param out_mime_type: The out_mime_type of this MlappServingSpec.  # noqa: E501
        :type: str
        """

        self._out_mime_type = out_mime_type

    @property
    def params(self):
        """Gets the params of this MlappServingSpec.  # noqa: E501


        :return: The params of this MlappServingSpec.  # noqa: E501
        :rtype: list[MlappServingSpecParam]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this MlappServingSpec.


        :param params: The params of this MlappServingSpec.  # noqa: E501
        :type: list[MlappServingSpecParam]
        """

        self._params = params

    @property
    def raw_input(self):
        """Gets the raw_input of this MlappServingSpec.  # noqa: E501


        :return: The raw_input of this MlappServingSpec.  # noqa: E501
        :rtype: bool
        """
        return self._raw_input

    @raw_input.setter
    def raw_input(self, raw_input):
        """Sets the raw_input of this MlappServingSpec.


        :param raw_input: The raw_input of this MlappServingSpec.  # noqa: E501
        :type: bool
        """

        self._raw_input = raw_input

    @property
    def response(self):
        """Gets the response of this MlappServingSpec.  # noqa: E501


        :return: The response of this MlappServingSpec.  # noqa: E501
        :rtype: list[MlappServingResponseParam]
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this MlappServingSpec.


        :param response: The response of this MlappServingSpec.  # noqa: E501
        :type: list[MlappServingResponseParam]
        """

        self._response = response

    @property
    def signature(self):
        """Gets the signature of this MlappServingSpec.  # noqa: E501


        :return: The signature of this MlappServingSpec.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this MlappServingSpec.


        :param signature: The signature of this MlappServingSpec.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def template(self):
        """Gets the template of this MlappServingSpec.  # noqa: E501


        :return: The template of this MlappServingSpec.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this MlappServingSpec.


        :param template: The template of this MlappServingSpec.  # noqa: E501
        :type: str
        """

        self._template = template

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
        if issubclass(MlappServingSpec, dict):
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
        if not isinstance(other, MlappServingSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
