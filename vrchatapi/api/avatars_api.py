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
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.current_user import CurrentUser
from vrchatapi.model.error import Error
from vrchatapi.model.inline_object10 import InlineObject10
from vrchatapi.model.inline_object11 import InlineObject11


class AvatarsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_avatar(
            self,
            **kwargs
        ):
            """Create Avatar  # noqa: E501

            Create an avatar. It's possible to optionally specify a ID if you want a custom one. Attempting to create an Avatar with an already claimed ID will result in a DB error.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_avatar(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                inline_object10 (InlineObject10): [optional]
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
                Avatar
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

        self.create_avatar = _Endpoint(
            settings={
                'response_type': (Avatar,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars',
                'operation_id': 'create_avatar',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object10',
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
                    'inline_object10':
                        (InlineObject10,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object10': 'body',
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
            callable=__create_avatar
        )

        def __delete_avatar(
            self,
            avatar_id,
            **kwargs
        ):
            """Delete Avatar  # noqa: E501

            Delete an avatar. Notice an avatar is never fully \"deleted\", only its ReleaseStatus is set to \"hidden\" and the linked Files are deleted. The AvatarID is permanently reserved.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_avatar(avatar_id, async_req=True)
            >>> result = thread.get()

            Args:
                avatar_id (str):

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
                Avatar
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
            kwargs['avatar_id'] = \
                avatar_id
            return self.call_with_http_info(**kwargs)

        self.delete_avatar = _Endpoint(
            settings={
                'response_type': (Avatar,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars/{avatarId}',
                'operation_id': 'delete_avatar',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'avatar_id',
                ],
                'required': [
                    'avatar_id',
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
                    'avatar_id':
                        (str,),
                },
                'attribute_map': {
                    'avatar_id': 'avatarId',
                },
                'location_map': {
                    'avatar_id': 'path',
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
            callable=__delete_avatar
        )

        def __get_avatar(
            self,
            avatar_id,
            **kwargs
        ):
            """Get Avatar  # noqa: E501

            Get information about a specific Avatar.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_avatar(avatar_id, async_req=True)
            >>> result = thread.get()

            Args:
                avatar_id (str):

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
                Avatar
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
            kwargs['avatar_id'] = \
                avatar_id
            return self.call_with_http_info(**kwargs)

        self.get_avatar = _Endpoint(
            settings={
                'response_type': (Avatar,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars/{avatarId}',
                'operation_id': 'get_avatar',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'avatar_id',
                ],
                'required': [
                    'avatar_id',
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
                    'avatar_id':
                        (str,),
                },
                'attribute_map': {
                    'avatar_id': 'avatarId',
                },
                'location_map': {
                    'avatar_id': 'path',
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
            callable=__get_avatar
        )

        def __get_favorited_avatars(
            self,
            **kwargs
        ):
            """List Favorited Avatars  # noqa: E501

            Search and list favorited avatars by query filters.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_favorited_avatars(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                featured (str): Filters on featured results.. [optional]
                sort (str): [optional] if omitted the server will use the default value of "popularity"
                n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
                order (str): [optional] if omitted the server will use the default value of "descending"
                offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
                search (str): Filters by world name.. [optional]
                tag (str): Tags to include (comma-separated).. [optional]
                notag (str): Tags to exclude (comma-separated).. [optional]
                release_status (str): Filter by ReleaseStatus.. [optional] if omitted the server will use the default value of "hidden"
                max_unity_version (str): The maximum Unity version supported by the asset.. [optional]
                min_unity_version (str): The minimum Unity version supported by the asset.. [optional]
                platform (str): The platform the asset supports.. [optional]
                user_id (str): Target user to see information on, admin-only.. [optional]
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
            return self.call_with_http_info(**kwargs)

        self.get_favorited_avatars = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars/favorites',
                'operation_id': 'get_favorited_avatars',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'featured',
                    'sort',
                    'n',
                    'order',
                    'offset',
                    'search',
                    'tag',
                    'notag',
                    'release_status',
                    'max_unity_version',
                    'min_unity_version',
                    'platform',
                    'user_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'order',
                    'release_status',
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
                    ('sort',): {

                        "POPULARITY": "popularity",
                        "HEAT": "heat",
                        "TRUST": "trust",
                        "SHUFFLE": "shuffle",
                        "RANDOM": "random",
                        "FAVORITES": "favorites",
                        "REPORTSCORE": "reportScore",
                        "REPORTCOUNT": "reportCount",
                        "PUBLICATIONDATE": "publicationDate",
                        "LABSPUBLICATIONDATE": "labsPublicationDate",
                        "CREATED": "created",
                        "_CREATED_AT": "_created_at",
                        "UPDATED": "updated",
                        "_UPDATED_AT": "_updated_at",
                        "ORDER": "order",
                        "RELEVANCE": "relevance",
                        "MAGIC": "magic",
                        "NAME": "name"
                    },
                    ('order',): {

                        "ASCENDING": "ascending",
                        "DESCENDING": "descending"
                    },
                    ('release_status',): {

                        "PUBLIC": "public",
                        "PRIVATE": "private",
                        "HIDDEN": "hidden"
                    },
                },
                'openapi_types': {
                    'featured':
                        (str,),
                    'sort':
                        (str,),
                    'n':
                        (int,),
                    'order':
                        (str,),
                    'offset':
                        (int,),
                    'search':
                        (str,),
                    'tag':
                        (str,),
                    'notag':
                        (str,),
                    'release_status':
                        (str,),
                    'max_unity_version':
                        (str,),
                    'min_unity_version':
                        (str,),
                    'platform':
                        (str,),
                    'user_id':
                        (str,),
                },
                'attribute_map': {
                    'featured': 'featured',
                    'sort': 'sort',
                    'n': 'n',
                    'order': 'order',
                    'offset': 'offset',
                    'search': 'search',
                    'tag': 'tag',
                    'notag': 'notag',
                    'release_status': 'releaseStatus',
                    'max_unity_version': 'maxUnityVersion',
                    'min_unity_version': 'minUnityVersion',
                    'platform': 'platform',
                    'user_id': 'userId',
                },
                'location_map': {
                    'featured': 'query',
                    'sort': 'query',
                    'n': 'query',
                    'order': 'query',
                    'offset': 'query',
                    'search': 'query',
                    'tag': 'query',
                    'notag': 'query',
                    'release_status': 'query',
                    'max_unity_version': 'query',
                    'min_unity_version': 'query',
                    'platform': 'query',
                    'user_id': 'query',
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
            callable=__get_favorited_avatars
        )

        def __search_avatars(
            self,
            **kwargs
        ):
            """Search Avatars  # noqa: E501

            Search and list avatars by query filters. You can only search your own or featured avatars. It is not possible as a normal user to search other peoples avatars.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_avatars(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                featured (str): Filters on featured results.. [optional]
                sort (str): [optional] if omitted the server will use the default value of "popularity"
                user (str): Set to `me` for searching own avatars.. [optional] if omitted the server will use the default value of "me"
                user_id (str): Filter by author UserID. [optional]
                n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
                order (str): [optional] if omitted the server will use the default value of "descending"
                offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
                tag (str): Tags to include (comma-separated).. [optional]
                notag (str): Tags to exclude (comma-separated).. [optional]
                release_status (str): Filter by ReleaseStatus.. [optional] if omitted the server will use the default value of "hidden"
                max_unity_version (str): The maximum Unity version supported by the asset.. [optional]
                min_unity_version (str): The minimum Unity version supported by the asset.. [optional]
                platform (str): The platform the asset supports.. [optional]
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
                [Avatar]
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

        self.search_avatars = _Endpoint(
            settings={
                'response_type': ([Avatar],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars',
                'operation_id': 'search_avatars',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'featured',
                    'sort',
                    'user',
                    'user_id',
                    'n',
                    'order',
                    'offset',
                    'tag',
                    'notag',
                    'release_status',
                    'max_unity_version',
                    'min_unity_version',
                    'platform',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'user',
                    'order',
                    'release_status',
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
                    ('sort',): {

                        "POPULARITY": "popularity",
                        "HEAT": "heat",
                        "TRUST": "trust",
                        "SHUFFLE": "shuffle",
                        "RANDOM": "random",
                        "FAVORITES": "favorites",
                        "REPORTSCORE": "reportScore",
                        "REPORTCOUNT": "reportCount",
                        "PUBLICATIONDATE": "publicationDate",
                        "LABSPUBLICATIONDATE": "labsPublicationDate",
                        "CREATED": "created",
                        "_CREATED_AT": "_created_at",
                        "UPDATED": "updated",
                        "_UPDATED_AT": "_updated_at",
                        "ORDER": "order",
                        "RELEVANCE": "relevance",
                        "MAGIC": "magic",
                        "NAME": "name"
                    },
                    ('user',): {

                        "ME": "me"
                    },
                    ('order',): {

                        "ASCENDING": "ascending",
                        "DESCENDING": "descending"
                    },
                    ('release_status',): {

                        "PUBLIC": "public",
                        "PRIVATE": "private",
                        "HIDDEN": "hidden"
                    },
                },
                'openapi_types': {
                    'featured':
                        (str,),
                    'sort':
                        (str,),
                    'user':
                        (str,),
                    'user_id':
                        (str,),
                    'n':
                        (int,),
                    'order':
                        (str,),
                    'offset':
                        (int,),
                    'tag':
                        (str,),
                    'notag':
                        (str,),
                    'release_status':
                        (str,),
                    'max_unity_version':
                        (str,),
                    'min_unity_version':
                        (str,),
                    'platform':
                        (str,),
                },
                'attribute_map': {
                    'featured': 'featured',
                    'sort': 'sort',
                    'user': 'user',
                    'user_id': 'userId',
                    'n': 'n',
                    'order': 'order',
                    'offset': 'offset',
                    'tag': 'tag',
                    'notag': 'notag',
                    'release_status': 'releaseStatus',
                    'max_unity_version': 'maxUnityVersion',
                    'min_unity_version': 'minUnityVersion',
                    'platform': 'platform',
                },
                'location_map': {
                    'featured': 'query',
                    'sort': 'query',
                    'user': 'query',
                    'user_id': 'query',
                    'n': 'query',
                    'order': 'query',
                    'offset': 'query',
                    'tag': 'query',
                    'notag': 'query',
                    'release_status': 'query',
                    'max_unity_version': 'query',
                    'min_unity_version': 'query',
                    'platform': 'query',
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
            callable=__search_avatars
        )

        def __select_avatar(
            self,
            avatar_id,
            **kwargs
        ):
            """Select Avatar  # noqa: E501

            Switches into that avatar.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.select_avatar(avatar_id, async_req=True)
            >>> result = thread.get()

            Args:
                avatar_id (str):

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
                CurrentUser
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
            kwargs['avatar_id'] = \
                avatar_id
            return self.call_with_http_info(**kwargs)

        self.select_avatar = _Endpoint(
            settings={
                'response_type': (CurrentUser,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars/{avatarId}/select',
                'operation_id': 'select_avatar',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'avatar_id',
                ],
                'required': [
                    'avatar_id',
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
                    'avatar_id':
                        (str,),
                },
                'attribute_map': {
                    'avatar_id': 'avatarId',
                },
                'location_map': {
                    'avatar_id': 'path',
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
            callable=__select_avatar
        )

        def __update_avatar(
            self,
            avatar_id,
            **kwargs
        ):
            """Update Avatar  # noqa: E501

            Update information about a specific avatar.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_avatar(avatar_id, async_req=True)
            >>> result = thread.get()

            Args:
                avatar_id (str):

            Keyword Args:
                inline_object11 (InlineObject11): [optional]
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
                Avatar
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
            kwargs['avatar_id'] = \
                avatar_id
            return self.call_with_http_info(**kwargs)

        self.update_avatar = _Endpoint(
            settings={
                'response_type': (Avatar,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/avatars/{avatarId}',
                'operation_id': 'update_avatar',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'avatar_id',
                    'inline_object11',
                ],
                'required': [
                    'avatar_id',
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
                    'avatar_id':
                        (str,),
                    'inline_object11':
                        (InlineObject11,),
                },
                'attribute_map': {
                    'avatar_id': 'avatarId',
                },
                'location_map': {
                    'avatar_id': 'path',
                    'inline_object11': 'body',
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
            callable=__update_avatar
        )
