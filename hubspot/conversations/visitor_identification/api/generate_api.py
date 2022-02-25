# coding: utf-8

"""
    Visitor Identification

    The Visitor Identification API allows you to pass identification information to the HubSpot chat widget for otherwise unknown visitors that were verified by your own authentication system.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.conversations.visitor_identification.api_client import ApiClient
from hubspot.conversations.visitor_identification.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class GenerateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def generate_token(self, identification_token_generation_request, **kwargs):  # noqa: E501
        """Generate a token  # noqa: E501

        Generates a new visitor identification token. This token will be unique every time this endpoint is called, even if called with the same email address. This token is temporary and will expire after 12 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_token(identification_token_generation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IdentificationTokenGenerationRequest identification_token_generation_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: IdentificationTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.generate_token_with_http_info(identification_token_generation_request, **kwargs)  # noqa: E501

    def generate_token_with_http_info(self, identification_token_generation_request, **kwargs):  # noqa: E501
        """Generate a token  # noqa: E501

        Generates a new visitor identification token. This token will be unique every time this endpoint is called, even if called with the same email address. This token is temporary and will expire after 12 hours  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_token_with_http_info(identification_token_generation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param IdentificationTokenGenerationRequest identification_token_generation_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(IdentificationTokenResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["identification_token_generation_request"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method generate_token" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'identification_token_generation_request' is set
        if self.api_client.client_side_validation and (
            "identification_token_generation_request" not in local_var_params or local_var_params["identification_token_generation_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError("Missing the required parameter `identification_token_generation_request` when calling `generate_token`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "identification_token_generation_request" in local_var_params:
            body_params = local_var_params["identification_token_generation_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])  # noqa: E501  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/conversations/v3/visitor-identification/tokens/create",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="IdentificationTokenResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
