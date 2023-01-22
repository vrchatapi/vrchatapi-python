# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.11.0
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vrchatapi.api_client import ApiClient
from vrchatapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class InstancesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_instance(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Get Instance  # noqa: E501

        Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  If an invalid instanceId is provided, this endpoint will simply return \"null\"!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instance(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Instance
        """
        kwargs['_return_http_data_only'] = True
        return self.get_instance_with_http_info(world_id, instance_id, **kwargs)  # noqa: E501

    def get_instance_with_http_info(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Get Instance  # noqa: E501

        Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  If an invalid instanceId is provided, this endpoint will simply return \"null\"!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instance_with_http_info(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Instance, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'world_id',
            'instance_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instance" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'world_id' is set
        if self.api_client.client_side_validation and local_var_params.get('world_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `world_id` when calling `get_instance`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instance_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instance_id` when calling `get_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world_id' in local_var_params:
            path_params['worldId'] = local_var_params['world_id']  # noqa: E501
        if 'instance_id' in local_var_params:
            path_params['instanceId'] = local_var_params['instance_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Instance",
            401: "Error",
        }

        return self.api_client.call_api(
            '/instances/{worldId}:{instanceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_instance_by_short_name(self, short_name, **kwargs):  # noqa: E501
        """Get Instance By Short Name  # noqa: E501

        Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instance_by_short_name(short_name, async_req=True)
        >>> result = thread.get()

        :param short_name: Must be a valid instance short name. (required)
        :type short_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Instance
        """
        kwargs['_return_http_data_only'] = True
        return self.get_instance_by_short_name_with_http_info(short_name, **kwargs)  # noqa: E501

    def get_instance_by_short_name_with_http_info(self, short_name, **kwargs):  # noqa: E501
        """Get Instance By Short Name  # noqa: E501

        Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instance_by_short_name_with_http_info(short_name, async_req=True)
        >>> result = thread.get()

        :param short_name: Must be a valid instance short name. (required)
        :type short_name: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Instance, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'short_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_instance_by_short_name" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'short_name' is set
        if self.api_client.client_side_validation and local_var_params.get('short_name') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `short_name` when calling `get_instance_by_short_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'short_name' in local_var_params:
            path_params['shortName'] = local_var_params['short_name']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Instance",
            401: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/instances/s/{shortName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_short_name(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Get Instance Short Name  # noqa: E501

        Returns an instance short name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_short_name(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InstanceShortNameResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_short_name_with_http_info(world_id, instance_id, **kwargs)  # noqa: E501

    def get_short_name_with_http_info(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Get Instance Short Name  # noqa: E501

        Returns an instance short name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_short_name_with_http_info(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InstanceShortNameResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'world_id',
            'instance_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_short_name" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'world_id' is set
        if self.api_client.client_side_validation and local_var_params.get('world_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `world_id` when calling `get_short_name`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instance_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instance_id` when calling `get_short_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world_id' in local_var_params:
            path_params['worldId'] = local_var_params['world_id']  # noqa: E501
        if 'instance_id' in local_var_params:
            path_params['instanceId'] = local_var_params['instance_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "InstanceShortNameResponse",
            401: "Error",
        }

        return self.api_client.call_api(
            '/instances/{worldId}:{instanceId}/shortName', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def send_self_invite(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Send Self Invite  # noqa: E501

        Sends an invite to the instance to yourself.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_self_invite(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Success
        """
        kwargs['_return_http_data_only'] = True
        return self.send_self_invite_with_http_info(world_id, instance_id, **kwargs)  # noqa: E501

    def send_self_invite_with_http_info(self, world_id, instance_id, **kwargs):  # noqa: E501
        """Send Self Invite  # noqa: E501

        Sends an invite to the instance to yourself.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_self_invite_with_http_info(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        :param world_id: Must be a valid world ID. (required)
        :type world_id: str
        :param instance_id: Must be a valid instance ID. (required)
        :type instance_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Success, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'world_id',
            'instance_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_self_invite" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'world_id' is set
        if self.api_client.client_side_validation and local_var_params.get('world_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `world_id` when calling `send_self_invite`")  # noqa: E501
        # verify the required parameter 'instance_id' is set
        if self.api_client.client_side_validation and local_var_params.get('instance_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `instance_id` when calling `send_self_invite`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'world_id' in local_var_params:
            path_params['worldId'] = local_var_params['world_id']  # noqa: E501
        if 'instance_id' in local_var_params:
            path_params['instanceId'] = local_var_params['instance_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Success",
            401: "Error",
        }

        return self.api_client.call_api(
            '/instances/{worldId}:{instanceId}/invite', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
