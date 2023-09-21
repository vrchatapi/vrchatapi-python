# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.14.0
    Contact: vrchatapi.lpv0t@aries.fyi
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


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_user(self, user_id, **kwargs):  # noqa: E501
        """Get User by ID  # noqa: E501

        Get public user information about a specific user using their ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: User
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_with_http_info(user_id, **kwargs)  # noqa: E501

    def get_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get User by ID  # noqa: E501

        Get public user information about a specific user using their ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: tuple(User, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'user_id'
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
                    " to method get_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `get_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "User",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users/{userId}', 'GET',
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

    def get_user_by_name(self, username, **kwargs):  # noqa: E501
        """Get User by Username  # noqa: E501

        ~~Get public user information about a specific user using their name.~~  **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429). This endpoint now require Admin Credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_by_name(username, async_req=True)
        >>> result = thread.get()

        :param username: Username of the user (required)
        :type username: str
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
        :rtype: User
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_by_name_with_http_info(username, **kwargs)  # noqa: E501

    def get_user_by_name_with_http_info(self, username, **kwargs):  # noqa: E501
        """Get User by Username  # noqa: E501

        ~~Get public user information about a specific user using their name.~~  **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429). This endpoint now require Admin Credentials.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_by_name_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param username: Username of the user (required)
        :type username: str
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
        :rtype: tuple(User, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'username'
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
                    " to method get_user_by_name" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'username' is set
        if self.api_client.client_side_validation and local_var_params.get('username') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `username` when calling `get_user_by_name`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'username' in local_var_params:
            path_params['username'] = local_var_params['username']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "User",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users/{username}/name', 'GET',
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

    def get_user_group_requests(self, user_id, **kwargs):  # noqa: E501
        """Get User Group Requests  # noqa: E501

        Returns a list of Groups the user has requested to be invited into.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_group_requests(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: list[Group]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_group_requests_with_http_info(user_id, **kwargs)  # noqa: E501

    def get_user_group_requests_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get User Group Requests  # noqa: E501

        Returns a list of Groups the user has requested to be invited into.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_group_requests_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: tuple(list[Group], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'user_id'
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
                    " to method get_user_group_requests" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `get_user_group_requests`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "list[Group]",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users/{userId}/groups/requested', 'GET',
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

    def get_user_groups(self, user_id, **kwargs):  # noqa: E501
        """Get User Groups  # noqa: E501

        Get user's public groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_groups(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: list[Group]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_groups_with_http_info(user_id, **kwargs)  # noqa: E501

    def get_user_groups_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Get User Groups  # noqa: E501

        Get user's public groups  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_groups_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
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
        :rtype: tuple(list[Group], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'user_id'
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
                    " to method get_user_groups" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `get_user_groups`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "list[Group]",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users/{userId}/groups', 'GET',
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

    def search_users(self, **kwargs):  # noqa: E501
        """Search All Users  # noqa: E501

        Search and list any users by text query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_users(async_req=True)
        >>> result = thread.get()

        :param search: Searches by `displayName`. Will return empty array if search query is empty or missing.
        :type search: str
        :param developer_type: Active user by developer type, none for normal users and internal for moderators
        :type developer_type: str
        :param n: The number of objects to return.
        :type n: int
        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
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
        :rtype: list[LimitedUser]
        """
        kwargs['_return_http_data_only'] = True
        return self.search_users_with_http_info(**kwargs)  # noqa: E501

    def search_users_with_http_info(self, **kwargs):  # noqa: E501
        """Search All Users  # noqa: E501

        Search and list any users by text query  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_users_with_http_info(async_req=True)
        >>> result = thread.get()

        :param search: Searches by `displayName`. Will return empty array if search query is empty or missing.
        :type search: str
        :param developer_type: Active user by developer type, none for normal users and internal for moderators
        :type developer_type: str
        :param n: The number of objects to return.
        :type n: int
        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
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
        :rtype: tuple(list[LimitedUser], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'search',
            'developer_type',
            'n',
            'offset'
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
                    " to method search_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('search' in local_var_params and  # noqa: E501
                                                        len(local_var_params['search']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `search` when calling `search_users`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `search_users`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `search_users`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `search_users`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('search') is not None:  # noqa: E501
            query_params.append(('search', local_var_params['search']))  # noqa: E501
        if local_var_params.get('developer_type') is not None:  # noqa: E501
            query_params.append(('developerType', local_var_params['developer_type']))  # noqa: E501
        if local_var_params.get('n') is not None:  # noqa: E501
            query_params.append(('n', local_var_params['n']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "list[LimitedUser]",
            400: "Error",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users', 'GET',
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

    def update_user(self, user_id, **kwargs):  # noqa: E501
        """Update User Info  # noqa: E501

        Update a users information such as the email and birthday.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
        :param update_user_request:
        :type update_user_request: UpdateUserRequest
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
        :rtype: CurrentUser
        """
        kwargs['_return_http_data_only'] = True
        return self.update_user_with_http_info(user_id, **kwargs)  # noqa: E501

    def update_user_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Update User Info  # noqa: E501

        Update a users information such as the email and birthday.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_with_http_info(user_id, async_req=True)
        >>> result = thread.get()

        :param user_id: Must be a valid user ID. (required)
        :type user_id: str
        :param update_user_request:
        :type update_user_request: UpdateUserRequest
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
        :rtype: tuple(CurrentUser, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'user_id',
            'update_user_request'
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
                    " to method update_user" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `update_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_id' in local_var_params:
            path_params['userId'] = local_var_params['user_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_user_request' in local_var_params:
            body_params = local_var_params['update_user_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'PUT', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['authCookie']  # noqa: E501

        response_types_map = {
            200: "CurrentUser",
            401: "Error",
        }

        return self.api_client.call_api(
            '/users/{userId}', 'PUT',
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
