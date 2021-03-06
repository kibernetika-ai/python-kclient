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


class ApplicationProjectServingJob(object):
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
        'completed': 'bool',
        'name': 'str',
        'outputs': 'list[ApplicationProjectServingJobOutput]',
        'serving_job_id': 'str',
        'start': 'datetime',
        'status': 'str',
        'stop': 'datetime'
    }

    attribute_map = {
        'completed': 'Completed',
        'name': 'Name',
        'outputs': 'Outputs',
        'serving_job_id': 'ServingJobID',
        'start': 'Start',
        'status': 'Status',
        'stop': 'Stop'
    }

    def __init__(self, completed=None, name=None, outputs=None, serving_job_id=None, start=None, status=None, stop=None):  # noqa: E501
        """ApplicationProjectServingJob - a model defined in Swagger"""  # noqa: E501

        self._completed = None
        self._name = None
        self._outputs = None
        self._serving_job_id = None
        self._start = None
        self._status = None
        self._stop = None
        self.discriminator = None

        self.completed = completed
        self.name = name
        self.outputs = outputs
        self.serving_job_id = serving_job_id
        if start is not None:
            self.start = start
        self.status = status
        if stop is not None:
            self.stop = stop

    @property
    def completed(self):
        """Gets the completed of this ApplicationProjectServingJob.  # noqa: E501


        :return: The completed of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ApplicationProjectServingJob.


        :param completed: The completed of this ApplicationProjectServingJob.  # noqa: E501
        :type: bool
        """
        if completed is None:
            raise ValueError("Invalid value for `completed`, must not be `None`")  # noqa: E501

        self._completed = completed

    @property
    def name(self):
        """Gets the name of this ApplicationProjectServingJob.  # noqa: E501


        :return: The name of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationProjectServingJob.


        :param name: The name of this ApplicationProjectServingJob.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this ApplicationProjectServingJob.  # noqa: E501


        :return: The outputs of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: list[ApplicationProjectServingJobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this ApplicationProjectServingJob.


        :param outputs: The outputs of this ApplicationProjectServingJob.  # noqa: E501
        :type: list[ApplicationProjectServingJobOutput]
        """
        if outputs is None:
            raise ValueError("Invalid value for `outputs`, must not be `None`")  # noqa: E501

        self._outputs = outputs

    @property
    def serving_job_id(self):
        """Gets the serving_job_id of this ApplicationProjectServingJob.  # noqa: E501


        :return: The serving_job_id of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: str
        """
        return self._serving_job_id

    @serving_job_id.setter
    def serving_job_id(self, serving_job_id):
        """Sets the serving_job_id of this ApplicationProjectServingJob.


        :param serving_job_id: The serving_job_id of this ApplicationProjectServingJob.  # noqa: E501
        :type: str
        """
        if serving_job_id is None:
            raise ValueError("Invalid value for `serving_job_id`, must not be `None`")  # noqa: E501

        self._serving_job_id = serving_job_id

    @property
    def start(self):
        """Gets the start of this ApplicationProjectServingJob.  # noqa: E501


        :return: The start of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ApplicationProjectServingJob.


        :param start: The start of this ApplicationProjectServingJob.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def status(self):
        """Gets the status of this ApplicationProjectServingJob.  # noqa: E501


        :return: The status of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApplicationProjectServingJob.


        :param status: The status of this ApplicationProjectServingJob.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def stop(self):
        """Gets the stop of this ApplicationProjectServingJob.  # noqa: E501


        :return: The stop of this ApplicationProjectServingJob.  # noqa: E501
        :rtype: datetime
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this ApplicationProjectServingJob.


        :param stop: The stop of this ApplicationProjectServingJob.  # noqa: E501
        :type: datetime
        """

        self._stop = stop

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
        if issubclass(ApplicationProjectServingJob, dict):
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
        if not isinstance(other, ApplicationProjectServingJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
