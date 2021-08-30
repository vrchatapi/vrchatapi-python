"""
    VRChat API Documentation

    ![VRChat API Banner](https://vrchatapi.github.io/assets/img/api_banner_1500x400.png)  # Welcome to the VRChat API  Before we begin, we would like to state this is a **COMMUNITY DRIVEN PROJECT**. This means that everything you read on here was written by the community itself and is **not** officially supported by VRChat. The documentation is provided \"AS IS\", and any action you take towards VRChat is completely your own responsibility.  The documentation and additional libraries SHALL ONLY be used for applications interacting with VRChat's API in accordance with their [Terms of Service](https://github.com/VRChatAPI), and MUST NOT be used for modifying the client, \"avatar ripping\", or other illegal activities. Malicious usage or spamming the API may result in account termination. Certain parts of the API are also more sensitive than others, for example moderation, so please tread extra carefully and read the warnings when present.  ![Tupper Policy on API](https://i.imgur.com/yLlW7Ok.png)  Finally, use of the API using applications other than the approved methods (website, VRChat application, Unity SDK) is not officially supported. VRChat provides no guarantee or support for external applications using the API. Access to API endpoints may break **at any time, without notice**. Therefore, please **do not ping** VRChat Staff in the VRChat Discord if you are having API problems, as they do not provide API support. We will make a best effort in keeping this documentation and associated language libraries up to date, but things might be outdated or missing. If you find that something is no longer valid, please contact us on Discord or [create an issue](https://github.com/vrchatapi/specification/issues) and tell us so we can fix it.  # Getting Started  The VRChat API can be used to programmatically retrieve or update information regarding your profile, friends, avatars, worlds and more. The API consists of two parts, \"Photon\" which is only used in-game, and the \"Web API\" which is used by both the game and the website. This documentation focuses only on the Web API.  The API is designed around the REST ideology, providing semi-simple and usually predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise.  <div class=\"callout callout-error\">   <strong>🛑 Warning! Do not touch Photon!</strong><br>   Photon is only used by the in-game client and should <b>not</b> be touched. Doing so may result in permanent account termination. </div>  <div class=\"callout callout-info\">   <strong>ℹ️ API Key and Authentication</strong><br>   The API Key has always been the same and is currently <code>JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26</code>.   Read <a href=\"#tag--authentication\">Authentication</a> for how to log in. </div>  # Using the API  For simply exploring what the API can do it is strongly recommended to download [Insomnia](https://insomnia.rest/download), a free and open-source API client that's great for sending requests to the API in an orderly fashion. Insomnia allows you to send data in the format that's required for VRChat's API. It is also possible to try out the API in your browser, by first logging in at [vrchat.com/home](https://vrchat.com/home/) and then going to [vrchat.com/api/1/auth/user](https://vrchat.com/api/1/auth/user), but the information will be much harder to work with.  For more permanent operation such as software development it is instead recommended to use one of the existing language SDKs. This community project maintains API libraries in several languages, which allows you to interact with the API with simple function calls rather than having to implement the HTTP protocol yourself. Most of these libraries are automatically generated from the API specification, sometimes with additional helpful wrapper code to make usage easier. This allows them to be almost automatically updated and expanded upon as soon as a new feature is introduced in the specification itself. The libraries can be found on [GitHub](https://github.com/vrchatapi) or following:  * [NodeJS (JavaScript)](https://www.npmjs.com/package/vrchat) * [Dart](https://pub.dev/packages/vrchat_dart) * [Rust](https://crates.io/crates/vrchatapi) * [C#](https://github.com/vrchatapi/vrchatapi-csharp) * [Python](https://github.com/vrchatapi/VRChatPython)  # Pagination  Most endpoints enforce pagination, meaning they will only return 10 entries by default, and never more than 100.<br> Using both the limit and offset parameters allows you to easily paginate through a large number of objects.  | Query Parameter | Type | Description | | ----------|--|------- | | `limit` | integer  | The number of objects to return. This value often defaults to 10. Highest limit is always 100.| | `offset` | integer  | A zero-based offset from the default object sorting.|  If a request returns fewer objects than the `limit` parameter, there are no more items available to return.  # Contribution  Do you want to get involved in the documentation effort? Do you want to help improve one of the language API libraries? This project is an [OPEN Open Source Project](https://openopensource.org)! This means that individuals making significant and valuable contributions are given commit-access to the project. It also means we are very open and welcoming of new people making contributions, unlike some more guarded open-source projects.  [![Discord](https://img.shields.io/static/v1?label=vrchatapi&message=discord&color=blueviolet&style=for-the-badge)](https://discord.gg/qjZE9C9fkB)  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.api_client import ApiClient, Endpoint as _Endpoint
from vrchatapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
from vrchatapi.model.favorite_group import FavoriteGroup
from vrchatapi.model.inline_object8 import InlineObject8
from vrchatapi.model.inline_object9 import InlineObject9


class FavoritesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __add_favorite(
            self,
            **kwargs
        ):
            """Add Favorite  # noqa: E501

            Add a new favorite.  Friend groups are named `group_0` through `group_3`. Avatar and World groups are named `avatars1` to `avatar4` and `worlds1` to `worlds4`.  You cannot add people whom you are not friends with to your friends list. Destroying a friendship removes the person as favorite on both sides.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.add_favorite(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                inline_object8 (InlineObject8): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Favorite
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.add_favorite = _Endpoint(
            settings={
                'response_type': (Favorite,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites',
                'operation_id': 'add_favorite',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object8',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'inline_object8':
                        (InlineObject8,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object8': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__add_favorite
        )

        def __clear_favorite_group(
            self,
            favorite_group_type,
            favorite_group_name,
            user_id,
            **kwargs
        ):
            """Clear Favorite Group  # noqa: E501

            Clear ALL contents of a specific favorite group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.clear_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
            >>> result = thread.get()

            Args:
                favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
                favorite_group_name (str):
                user_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Error
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['favorite_group_type'] = \
                favorite_group_type
            kwargs['favorite_group_name'] = \
                favorite_group_name
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.clear_favorite_group = _Endpoint(
            settings={
                'response_type': (Error,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'clear_favorite_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__clear_favorite_group
        )

        def __get_favorite(
            self,
            favorite_id,
            **kwargs
        ):
            """Show Favorite  # noqa: E501

            Return information about a specific Favorite.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_favorite(favorite_id, async_req=True)
            >>> result = thread.get()

            Args:
                favorite_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Favorite
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['favorite_id'] = \
                favorite_id
            return self.call_with_http_info(**kwargs)

        self.get_favorite = _Endpoint(
            settings={
                'response_type': (Favorite,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites/{favoriteId}',
                'operation_id': 'get_favorite',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_id',
                ],
                'required': [
                    'favorite_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'favorite_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_id': 'favoriteId',
                },
                'location_map': {
                    'favorite_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_favorite
        )

        def __get_favorite_group(
            self,
            favorite_group_type,
            favorite_group_name,
            user_id,
            **kwargs
        ):
            """Show Favorite Group  # noqa: E501

            Fetch information about a specific favorite group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
            >>> result = thread.get()

            Args:
                favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
                favorite_group_name (str):
                user_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                FavoriteGroup
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['favorite_group_type'] = \
                favorite_group_type
            kwargs['favorite_group_name'] = \
                favorite_group_name
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.get_favorite_group = _Endpoint(
            settings={
                'response_type': (FavoriteGroup,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'get_favorite_group',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_favorite_group
        )

        def __get_favorite_groups(
            self,
            **kwargs
        ):
            """List Favorite Groups  # noqa: E501

            Return a list of favorite groups owned by a user. Returns the same information as `getFavoriteGroups`.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_favorite_groups(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
                offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
                owner_id (str): The owner of whoms favorite groups to return. Must be a UserID.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [FavoriteGroup]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_favorite_groups = _Endpoint(
            settings={
                'response_type': ([FavoriteGroup],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/groups',
                'operation_id': 'get_favorite_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'n',
                    'offset',
                    'owner_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('n',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'n':
                        (int,),
                    'offset':
                        (int,),
                    'owner_id':
                        (str,),
                },
                'attribute_map': {
                    'n': 'n',
                    'offset': 'offset',
                    'owner_id': 'ownerId',
                },
                'location_map': {
                    'n': 'query',
                    'offset': 'query',
                    'owner_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_favorite_groups
        )

        def __get_favorites(
            self,
            **kwargs
        ):
            """List Favorites  # noqa: E501

            Returns a list of favorites.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_favorites(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
                offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
                type (str): The type of favorites to return, FavoriteType.. [optional]
                tag (str): Tags to include (comma-separated).. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Favorite]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.get_favorites = _Endpoint(
            settings={
                'response_type': ([Favorite],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites',
                'operation_id': 'get_favorites',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'n',
                    'offset',
                    'type',
                    'tag',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('n',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'n':
                        (int,),
                    'offset':
                        (int,),
                    'type':
                        (str,),
                    'tag':
                        (str,),
                },
                'attribute_map': {
                    'n': 'n',
                    'offset': 'offset',
                    'type': 'type',
                    'tag': 'tag',
                },
                'location_map': {
                    'n': 'query',
                    'offset': 'query',
                    'type': 'query',
                    'tag': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_favorites
        )

        def __remove_favorite(
            self,
            favorite_id,
            **kwargs
        ):
            """Remove Favorite  # noqa: E501

            Remove a favorite from your favorites list.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.remove_favorite(favorite_id, async_req=True)
            >>> result = thread.get()

            Args:
                favorite_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Error
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['favorite_id'] = \
                favorite_id
            return self.call_with_http_info(**kwargs)

        self.remove_favorite = _Endpoint(
            settings={
                'response_type': (Error,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorites/{favoriteId}',
                'operation_id': 'remove_favorite',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_id',
                ],
                'required': [
                    'favorite_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'favorite_id':
                        (str,),
                },
                'attribute_map': {
                    'favorite_id': 'favoriteId',
                },
                'location_map': {
                    'favorite_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__remove_favorite
        )

        def __update_favorite_group(
            self,
            favorite_group_type,
            favorite_group_name,
            user_id,
            **kwargs
        ):
            """Update Favorite Group  # noqa: E501

            Update information about a specific favorite group.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_favorite_group(favorite_group_type, favorite_group_name, user_id, async_req=True)
            >>> result = thread.get()

            Args:
                favorite_group_type (str): The type of group to fetch, must be a valid FavoriteType.
                favorite_group_name (str):
                user_id (str):

            Keyword Args:
                inline_object9 (InlineObject9): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['favorite_group_type'] = \
                favorite_group_type
            kwargs['favorite_group_name'] = \
                favorite_group_name
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.update_favorite_group = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId}',
                'operation_id': 'update_favorite_group',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                    'inline_object9',
                ],
                'required': [
                    'favorite_group_type',
                    'favorite_group_name',
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'favorite_group_type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('favorite_group_type',): {

                        "WORLD": "world",
                        "FRIEND": "friend",
                        "AVATAR": "avatar"
                    },
                },
                'openapi_types': {
                    'favorite_group_type':
                        (str,),
                    'favorite_group_name':
                        (str,),
                    'user_id':
                        (str,),
                    'inline_object9':
                        (InlineObject9,),
                },
                'attribute_map': {
                    'favorite_group_type': 'favoriteGroupType',
                    'favorite_group_name': 'favoriteGroupName',
                    'user_id': 'userId',
                },
                'location_map': {
                    'favorite_group_type': 'path',
                    'favorite_group_name': 'path',
                    'user_id': 'path',
                    'inline_object9': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_favorite_group
        )
