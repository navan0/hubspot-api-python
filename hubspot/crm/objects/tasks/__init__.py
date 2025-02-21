# coding: utf-8

# flake8: noqa

"""
    Tasks

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.objects.tasks.api.associations_api import AssociationsApi
from hubspot.crm.objects.tasks.api.basic_api import BasicApi
from hubspot.crm.objects.tasks.api.batch_api import BatchApi
from hubspot.crm.objects.tasks.api.search_api import SearchApi

# import ApiClient
from hubspot.crm.objects.tasks.api_client import ApiClient
from hubspot.crm.objects.tasks.configuration import Configuration
from hubspot.crm.objects.tasks.exceptions import OpenApiException
from hubspot.crm.objects.tasks.exceptions import ApiTypeError
from hubspot.crm.objects.tasks.exceptions import ApiValueError
from hubspot.crm.objects.tasks.exceptions import ApiKeyError
from hubspot.crm.objects.tasks.exceptions import ApiException

# import models into sdk package
from hubspot.crm.objects.tasks.models.associated_id import AssociatedId
from hubspot.crm.objects.tasks.models.batch_input_simple_public_object_batch_input import BatchInputSimplePublicObjectBatchInput
from hubspot.crm.objects.tasks.models.batch_input_simple_public_object_id import BatchInputSimplePublicObjectId
from hubspot.crm.objects.tasks.models.batch_input_simple_public_object_input import BatchInputSimplePublicObjectInput
from hubspot.crm.objects.tasks.models.batch_read_input_simple_public_object_id import BatchReadInputSimplePublicObjectId
from hubspot.crm.objects.tasks.models.batch_response_simple_public_object import BatchResponseSimplePublicObject
from hubspot.crm.objects.tasks.models.batch_response_simple_public_object_with_errors import BatchResponseSimplePublicObjectWithErrors
from hubspot.crm.objects.tasks.models.collection_response_associated_id import CollectionResponseAssociatedId
from hubspot.crm.objects.tasks.models.collection_response_associated_id_forward_paging import CollectionResponseAssociatedIdForwardPaging
from hubspot.crm.objects.tasks.models.collection_response_simple_public_object_with_associations_forward_paging import CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
from hubspot.crm.objects.tasks.models.collection_response_with_total_simple_public_object_forward_paging import CollectionResponseWithTotalSimplePublicObjectForwardPaging
from hubspot.crm.objects.tasks.models.error import Error
from hubspot.crm.objects.tasks.models.error_category import ErrorCategory
from hubspot.crm.objects.tasks.models.error_detail import ErrorDetail
from hubspot.crm.objects.tasks.models.filter import Filter
from hubspot.crm.objects.tasks.models.filter_group import FilterGroup
from hubspot.crm.objects.tasks.models.forward_paging import ForwardPaging
from hubspot.crm.objects.tasks.models.next_page import NextPage
from hubspot.crm.objects.tasks.models.paging import Paging
from hubspot.crm.objects.tasks.models.previous_page import PreviousPage
from hubspot.crm.objects.tasks.models.public_object_search_request import PublicObjectSearchRequest
from hubspot.crm.objects.tasks.models.simple_public_object import SimplePublicObject
from hubspot.crm.objects.tasks.models.simple_public_object_batch_input import SimplePublicObjectBatchInput
from hubspot.crm.objects.tasks.models.simple_public_object_id import SimplePublicObjectId
from hubspot.crm.objects.tasks.models.simple_public_object_input import SimplePublicObjectInput
from hubspot.crm.objects.tasks.models.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from hubspot.crm.objects.tasks.models.standard_error import StandardError
from hubspot.crm.objects.tasks.models.value_with_timestamp import ValueWithTimestamp
