# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.20.1
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


class FriendsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_friend_request(self, user_id, **kwargs):  # noqa: E501
        """Delete Friend Request  # noqa: E501

        Deletes an outgoing pending friend request to another user. To delete an incoming friend request, use the `deleteNotification` endpoint instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_friend_request(user_id, async_req=True)
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
        :rtype: Success
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_friend_request_with_http_info(user_id, **kwargs)  # noqa: E501

    def delete_friend_request_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Delete Friend Request  # noqa: E501

        Deletes an outgoing pending friend request to another user. To delete an incoming friend request, use the `deleteNotification` endpoint instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_friend_request_with_http_info(user_id, async_req=True)
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
        :rtype: tuple(Success, status_code(int), headers(HTTPHeaderDict))
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
                    " to method delete_friend_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `delete_friend_request`")  # noqa: E501

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
            200: "Success",
            401: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/user/{userId}/friendRequest', 'DELETE',
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

    def friend(self, user_id, **kwargs):  # noqa: E501
        """Send Friend Request  # noqa: E501

        Send a friend request to another user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.friend(user_id, async_req=True)
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
        :rtype: Notification
        """
        kwargs['_return_http_data_only'] = True
        return self.friend_with_http_info(user_id, **kwargs)  # noqa: E501

    def friend_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Send Friend Request  # noqa: E501

        Send a friend request to another user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.friend_with_http_info(user_id, async_req=True)
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
        :rtype: tuple(Notification, status_code(int), headers(HTTPHeaderDict))
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
                    " to method friend" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `friend`")  # noqa: E501

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
            200: "Notification",
            400: "Error",
            401: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/user/{userId}/friendRequest', 'POST',
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

    def get_friend_status(self, user_id, **kwargs):  # noqa: E501
        """Check Friend Status  # noqa: E501

        Retrieve if the user is currently a friend with a given user, if they have an outgoing friend request, and if they have an incoming friend request. The proper way to receive and accept friend request is by checking if the user has an incoming `Notification` of type `friendRequest`, and then accepting that notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_friend_status(user_id, async_req=True)
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
        :rtype: FriendStatus
        """
        kwargs['_return_http_data_only'] = True
        return self.get_friend_status_with_http_info(user_id, **kwargs)  # noqa: E501

    def get_friend_status_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Check Friend Status  # noqa: E501

        Retrieve if the user is currently a friend with a given user, if they have an outgoing friend request, and if they have an incoming friend request. The proper way to receive and accept friend request is by checking if the user has an incoming `Notification` of type `friendRequest`, and then accepting that notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_friend_status_with_http_info(user_id, async_req=True)
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
        :rtype: tuple(FriendStatus, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_friend_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `get_friend_status`")  # noqa: E501

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
            200: "FriendStatus",
            401: "Error",
        }

        return self.api_client.call_api(
            '/user/{userId}/friendStatus', 'GET',
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

    def get_friends(self, **kwargs):  # noqa: E501
        """List Friends  # noqa: E501

        List information about friends.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_friends(async_req=True)
        >>> result = thread.get()

        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
        :param n: The number of objects to return.
        :type n: int
        :param offline: Returns *only* offline users if true, returns only online and active users if false
        :type offline: bool
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
        :rtype: list[LimitedUserFriend]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_friends_with_http_info(**kwargs)  # noqa: E501

    def get_friends_with_http_info(self, **kwargs):  # noqa: E501
        """List Friends  # noqa: E501

        List information about friends.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_friends_with_http_info(async_req=True)
        >>> result = thread.get()

        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
        :param n: The number of objects to return.
        :type n: int
        :param offline: Returns *only* offline users if true, returns only online and active users if false
        :type offline: bool
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
        :rtype: tuple(list[LimitedUserFriend], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'n',
            'offline'
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
                    " to method get_friends" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_friends`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `get_friends`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `get_friends`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if local_var_params.get('n') is not None:  # noqa: E501
            query_params.append(('n', local_var_params['n']))  # noqa: E501
        if local_var_params.get('offline') is not None:  # noqa: E501
            query_params.append(('offline', local_var_params['offline']))  # noqa: E501

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
            200: "list[LimitedUserFriend]",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/friends', 'GET',
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

    def unfriend(self, user_id, **kwargs):  # noqa: E501
        """Unfriend  # noqa: E501

        Unfriend a user by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.unfriend(user_id, async_req=True)
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
        :rtype: Success
        """
        kwargs['_return_http_data_only'] = True
        return self.unfriend_with_http_info(user_id, **kwargs)  # noqa: E501

    def unfriend_with_http_info(self, user_id, **kwargs):  # noqa: E501
        """Unfriend  # noqa: E501

        Unfriend a user by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.unfriend_with_http_info(user_id, async_req=True)
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
        :rtype: tuple(Success, status_code(int), headers(HTTPHeaderDict))
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
                    " to method unfriend" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_id' is set
        if self.api_client.client_side_validation and local_var_params.get('user_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_id` when calling `unfriend`")  # noqa: E501

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
            200: "Success",
            400: "Error",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/friends/{userId}', 'DELETE',
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
