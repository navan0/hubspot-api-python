# coding: utf-8

"""
    Associations

    Associations define the relationships between objects in HubSpot. These endpoints allow you to create, read, and remove associations.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.associations.api_client import ApiClient
from hubspot.crm.associations.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class TypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """List association types  # noqa: E501

        List all the valid association types available between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponsePublicAssociationDefiniton
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_all_with_http_info(from_object_type, to_object_type, **kwargs)  # noqa: E501

    def get_all_with_http_info(self, from_object_type, to_object_type, **kwargs):  # noqa: E501
        """List association types  # noqa: E501

        List all the valid association types available between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(from_object_type, to_object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str from_object_type: (required)
        :param str to_object_type: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponsePublicAssociationDefiniton, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["from_object_type", "to_object_type"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_all" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and ("from_object_type" not in local_var_params or local_var_params["from_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `get_all`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and ("to_object_type" not in local_var_params or local_var_params["to_object_type"] is None):  # noqa: E501  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/associations/{fromObjectType}/{toObjectType}/types",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponsePublicAssociationDefiniton",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
