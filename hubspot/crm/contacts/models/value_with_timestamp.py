# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.contacts.configuration import Configuration


class ValueWithTimestamp(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"value": "str", "timestamp": "datetime", "source_type": "str", "source_id": "str", "source_label": "str", "updated_by_user_id": "int"}

    attribute_map = {"value": "value", "timestamp": "timestamp", "source_type": "sourceType", "source_id": "sourceId", "source_label": "sourceLabel", "updated_by_user_id": "updatedByUserId"}

    def __init__(self, value=None, timestamp=None, source_type=None, source_id=None, source_label=None, updated_by_user_id=None, local_vars_configuration=None):  # noqa: E501
        """ValueWithTimestamp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._timestamp = None
        self._source_type = None
        self._source_id = None
        self._source_label = None
        self._updated_by_user_id = None
        self.discriminator = None

        self.value = value
        self.timestamp = timestamp
        self.source_type = source_type
        if source_id is not None:
            self.source_id = source_id
        if source_label is not None:
            self.source_label = source_label
        if updated_by_user_id is not None:
            self.updated_by_user_id = updated_by_user_id

    @property
    def value(self):
        """Gets the value of this ValueWithTimestamp.  # noqa: E501


        :return: The value of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ValueWithTimestamp.


        :param value: The value of this ValueWithTimestamp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def timestamp(self):
        """Gets the timestamp of this ValueWithTimestamp.  # noqa: E501


        :return: The timestamp of this ValueWithTimestamp.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ValueWithTimestamp.


        :param timestamp: The timestamp of this ValueWithTimestamp.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def source_type(self):
        """Gets the source_type of this ValueWithTimestamp.  # noqa: E501


        :return: The source_type of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ValueWithTimestamp.


        :param source_type: The source_type of this ValueWithTimestamp.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type`, must not be `None`")  # noqa: E501

        self._source_type = source_type

    @property
    def source_id(self):
        """Gets the source_id of this ValueWithTimestamp.  # noqa: E501


        :return: The source_id of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ValueWithTimestamp.


        :param source_id: The source_id of this ValueWithTimestamp.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def source_label(self):
        """Gets the source_label of this ValueWithTimestamp.  # noqa: E501


        :return: The source_label of this ValueWithTimestamp.  # noqa: E501
        :rtype: str
        """
        return self._source_label

    @source_label.setter
    def source_label(self, source_label):
        """Sets the source_label of this ValueWithTimestamp.


        :param source_label: The source_label of this ValueWithTimestamp.  # noqa: E501
        :type: str
        """

        self._source_label = source_label

    @property
    def updated_by_user_id(self):
        """Gets the updated_by_user_id of this ValueWithTimestamp.  # noqa: E501


        :return: The updated_by_user_id of this ValueWithTimestamp.  # noqa: E501
        :rtype: int
        """
        return self._updated_by_user_id

    @updated_by_user_id.setter
    def updated_by_user_id(self, updated_by_user_id):
        """Sets the updated_by_user_id of this ValueWithTimestamp.


        :param updated_by_user_id: The updated_by_user_id of this ValueWithTimestamp.  # noqa: E501
        :type: int
        """

        self._updated_by_user_id = updated_by_user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValueWithTimestamp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValueWithTimestamp):
            return True

        return self.to_dict() != other.to_dict()
