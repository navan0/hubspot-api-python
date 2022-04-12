# coding: utf-8

"""
    CRM Pipelines

    Pipelines represent distinct stages in a workflow, like closing a deal or servicing a support ticket. These endpoints provide access to read and modify pipelines in HubSpot. Pipelines support `deals` and `tickets` object types.  ## Pipeline ID validation  When calling endpoints that take pipelineId as a parameter, that ID must correspond to an existing, un-archived pipeline. Otherwise the request will fail with a `404 Not Found` response.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.pipelines.configuration import Configuration


class PipelineInput(object):
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
    openapi_types = {"label": "str", "display_order": "int", "stages": "list[PipelineStageInput]"}

    attribute_map = {"label": "label", "display_order": "displayOrder", "stages": "stages"}

    def __init__(self, label=None, display_order=None, stages=None, local_vars_configuration=None):  # noqa: E501
        """PipelineInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._display_order = None
        self._stages = None
        self.discriminator = None

        self.label = label
        self.display_order = display_order
        self.stages = stages

    @property
    def label(self):
        """Gets the label of this PipelineInput.  # noqa: E501

        A unique label used to organize pipelines in HubSpot's UI  # noqa: E501

        :return: The label of this PipelineInput.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PipelineInput.

        A unique label used to organize pipelines in HubSpot's UI  # noqa: E501

        :param label: The label of this PipelineInput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def display_order(self):
        """Gets the display_order of this PipelineInput.  # noqa: E501

        The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :return: The display_order of this PipelineInput.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PipelineInput.

        The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :param display_order: The display_order of this PipelineInput.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and display_order is None:  # noqa: E501
            raise ValueError("Invalid value for `display_order`, must not be `None`")  # noqa: E501

        self._display_order = display_order

    @property
    def stages(self):
        """Gets the stages of this PipelineInput.  # noqa: E501

        Pipeline stage inputs used to create the new or replacement pipeline.  # noqa: E501

        :return: The stages of this PipelineInput.  # noqa: E501
        :rtype: list[PipelineStageInput]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this PipelineInput.

        Pipeline stage inputs used to create the new or replacement pipeline.  # noqa: E501

        :param stages: The stages of this PipelineInput.  # noqa: E501
        :type: list[PipelineStageInput]
        """
        if self.local_vars_configuration.client_side_validation and stages is None:  # noqa: E501
            raise ValueError("Invalid value for `stages`, must not be `None`")  # noqa: E501

        self._stages = stages

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
        if not isinstance(other, PipelineInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineInput):
            return True

        return self.to_dict() != other.to_dict()
