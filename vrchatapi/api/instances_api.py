"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.6.9
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
from vrchatapi.model.instance import Instance
from vrchatapi.model.success import Success


class InstancesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_instance_endpoint = _Endpoint(
            settings={
                'response_type': (Instance,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/instances/{worldId}:{instanceId}',
                'operation_id': 'get_instance',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'world_id',
                    'instance_id',
                ],
                'required': [
                    'world_id',
                    'instance_id',
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
                    'world_id':
                        (str,),
                    'instance_id':
                        (str,),
                },
                'attribute_map': {
                    'world_id': 'worldId',
                    'instance_id': 'instanceId',
                },
                'location_map': {
                    'world_id': 'path',
                    'instance_id': 'path',
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
            api_client=api_client
        )
        self.get_short_name_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/instances/{worldId}:{instanceId}/shortName',
                'operation_id': 'get_short_name',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'world_id',
                    'instance_id',
                ],
                'required': [
                    'world_id',
                    'instance_id',
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
                    'world_id':
                        (str,),
                    'instance_id':
                        (str,),
                },
                'attribute_map': {
                    'world_id': 'worldId',
                    'instance_id': 'instanceId',
                },
                'location_map': {
                    'world_id': 'path',
                    'instance_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.send_self_invite_endpoint = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/instances/{worldId}:{instanceId}/invite',
                'operation_id': 'send_self_invite',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'world_id',
                    'instance_id',
                ],
                'required': [
                    'world_id',
                    'instance_id',
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
                    'world_id':
                        (str,),
                    'instance_id':
                        (str,),
                },
                'attribute_map': {
                    'world_id': 'worldId',
                    'instance_id': 'instanceId',
                },
                'location_map': {
                    'world_id': 'path',
                    'instance_id': 'path',
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
            api_client=api_client
        )

    def get_instance(
        self,
        world_id,
        instance_id,
        **kwargs
    ):
        """Get Instance  # noqa: E501

        Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  If an invalid instanceId is provided, this endpoint will simply return \"null\"!  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_instance(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            world_id (str):
            instance_id (str):

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
            Instance
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
        kwargs['world_id'] = \
            world_id
        kwargs['instance_id'] = \
            instance_id
        return self.get_instance_endpoint.call_with_http_info(**kwargs)

    def get_short_name(
        self,
        world_id,
        instance_id,
        **kwargs
    ):
        """Get Instance Short Name  # noqa: E501

        Returns an instance short name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_short_name(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            world_id (str):
            instance_id (str):

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
            str
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
        kwargs['world_id'] = \
            world_id
        kwargs['instance_id'] = \
            instance_id
        return self.get_short_name_endpoint.call_with_http_info(**kwargs)

    def send_self_invite(
        self,
        world_id,
        instance_id,
        **kwargs
    ):
        """Send Self Invite  # noqa: E501

        Sends an invite to the instance to yourself.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_self_invite(world_id, instance_id, async_req=True)
        >>> result = thread.get()

        Args:
            world_id (str):
            instance_id (str):

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
            Success
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
        kwargs['world_id'] = \
            world_id
        kwargs['instance_id'] = \
            instance_id
        return self.send_self_invite_endpoint.call_with_http_info(**kwargs)

