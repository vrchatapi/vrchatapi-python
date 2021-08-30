# vrchatapi.WorldsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_world**](WorldsApi.md#create_world) | **POST** /worlds | Create World
[**delete_world**](WorldsApi.md#delete_world) | **DELETE** /worlds/{worldId} | Delete World
[**get_active_worlds**](WorldsApi.md#get_active_worlds) | **GET** /worlds/active | List Active Worlds
[**get_favorited_worlds**](WorldsApi.md#get_favorited_worlds) | **GET** /worlds/favorites | List Favorited Worlds
[**get_recent_worlds**](WorldsApi.md#get_recent_worlds) | **GET** /worlds/recent | List Recent Worlds
[**get_world**](WorldsApi.md#get_world) | **GET** /worlds/{worldId} | Get World by ID
[**get_world_instance**](WorldsApi.md#get_world_instance) | **GET** /worlds/{worldId}/{instanceId} | Get World Instance
[**get_world_metadata**](WorldsApi.md#get_world_metadata) | **GET** /worlds/{worldId}/metadata | Get World Metadata
[**get_world_publish_status**](WorldsApi.md#get_world_publish_status) | **GET** /worlds/{worldId}/publish | Get World Publish Status
[**publish_world**](WorldsApi.md#publish_world) | **PUT** /worlds/{worldId}/publish | Publish World
[**search_worlds**](WorldsApi.md#search_worlds) | **GET** /worlds | Search All Worlds
[**unpublish_world**](WorldsApi.md#unpublish_world) | **DELETE** /worlds/{worldId}/publish | Unpublish World
[**update_world**](WorldsApi.md#update_world) | **PUT** /worlds/{worldId} | Update World


# **create_world**
> World create_world()

Create World

Create a new world. This endpoint requires `assetUrl` to be a valid File object with `.vrcw` file extension, and `imageUrl` to be a valid File object with an image file extension.

### Example

```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.world import World
from vrchatapi.model.error import Error
from vrchatapi.model.inline_object6 import InlineObject6
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    inline_object6 = InlineObject6(
        asset_url="asset_url_example",
        asset_version="asset_version_example",
        author_name="author_name_example",
        capacity=16,
        description="description_example",
        id=WorldID("wrld_ba913a96-fac4-4048-a062-9aa5db092812"),
        image_url="image_url_example",
        name="name_example",
        platform=Platform("standalonewindows"),
        release_status=ReleaseStatus("public"),
        tags=[
            Tag("tags_example"),
        ],
        unity_package_url="unity_package_url_example",
        unity_version="2018.4.20f1",
    ) # InlineObject6 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create World
        api_response = api_instance.create_world(inline_object6=inline_object6)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->create_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object6** | [**InlineObject6**](InlineObject6.md)|  | [optional]

### Return type

[**World**](World.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single World object. |  -  |
**400** | Error response when trying create a world without having the neccesary Trust rank yet. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_world**
> delete_world(world_id)

Delete World

Delete a world. Notice a world is never fully \"deleted\", only its ReleaseStatus is set to \"hidden\" and the linked Files are deleted. The WorldID is permanently reserved.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete World
        api_instance.delete_world(world_id)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->delete_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_worlds**
> [LimitedWorld] get_active_worlds()

List Active Worlds

Search and list currently Active worlds by query filters.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    featured = "featured_example" # str | Filters on featured results. (optional)
    sort = "popularity" # str |  (optional) if omitted the server will use the default value of "popularity"
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    order = "descending" # str |  (optional) if omitted the server will use the default value of "descending"
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    search = "search_example" # str | Filters by world name. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)
    notag = "notag_example" # str | Tags to exclude (comma-separated). (optional)
    release_status = "hidden" # str | Filter by ReleaseStatus. (optional) if omitted the server will use the default value of "hidden"
    max_unity_version = "maxUnityVersion_example" # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = "minUnityVersion_example" # str | The minimum Unity version supported by the asset. (optional)
    platform = "platform_example" # str | The platform the asset supports. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Active Worlds
        api_response = api_instance.get_active_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_active_worlds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **str**| Filters on featured results. | [optional]
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "popularity"
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **order** | **str**|  | [optional] if omitted the server will use the default value of "descending"
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **search** | **str**| Filters by world name. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]
 **notag** | **str**| Tags to exclude (comma-separated). | [optional]
 **release_status** | **str**| Filter by ReleaseStatus. | [optional] if omitted the server will use the default value of "hidden"
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional]
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional]
 **platform** | **str**| The platform the asset supports. | [optional]

### Return type

[**[LimitedWorld]**](LimitedWorld.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorited_worlds**
> [LimitedWorld] get_favorited_worlds()

List Favorited Worlds

Search and list favorited worlds by query filters.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    featured = "featured_example" # str | Filters on featured results. (optional)
    sort = "popularity" # str |  (optional) if omitted the server will use the default value of "popularity"
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    order = "descending" # str |  (optional) if omitted the server will use the default value of "descending"
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    search = "search_example" # str | Filters by world name. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)
    notag = "notag_example" # str | Tags to exclude (comma-separated). (optional)
    release_status = "hidden" # str | Filter by ReleaseStatus. (optional) if omitted the server will use the default value of "hidden"
    max_unity_version = "maxUnityVersion_example" # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = "minUnityVersion_example" # str | The minimum Unity version supported by the asset. (optional)
    platform = "platform_example" # str | The platform the asset supports. (optional)
    user_id = "userId_example" # str | Target user to see information on, admin-only. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Favorited Worlds
        api_response = api_instance.get_favorited_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_favorited_worlds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **str**| Filters on featured results. | [optional]
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "popularity"
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **order** | **str**|  | [optional] if omitted the server will use the default value of "descending"
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **search** | **str**| Filters by world name. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]
 **notag** | **str**| Tags to exclude (comma-separated). | [optional]
 **release_status** | **str**| Filter by ReleaseStatus. | [optional] if omitted the server will use the default value of "hidden"
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional]
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional]
 **platform** | **str**| The platform the asset supports. | [optional]
 **user_id** | **str**| Target user to see information on, admin-only. | [optional]

### Return type

[**[LimitedWorld]**](LimitedWorld.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**403** | Error response when trying to see favourites of another user without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_worlds**
> [LimitedWorld] get_recent_worlds()

List Recent Worlds

Search and list recently visited worlds by query filters.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    featured = "featured_example" # str | Filters on featured results. (optional)
    sort = "popularity" # str |  (optional) if omitted the server will use the default value of "popularity"
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    order = "descending" # str |  (optional) if omitted the server will use the default value of "descending"
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    search = "search_example" # str | Filters by world name. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)
    notag = "notag_example" # str | Tags to exclude (comma-separated). (optional)
    release_status = "hidden" # str | Filter by ReleaseStatus. (optional) if omitted the server will use the default value of "hidden"
    max_unity_version = "maxUnityVersion_example" # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = "minUnityVersion_example" # str | The minimum Unity version supported by the asset. (optional)
    platform = "platform_example" # str | The platform the asset supports. (optional)
    user_id = "userId_example" # str | Target user to see information on, admin-only. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Recent Worlds
        api_response = api_instance.get_recent_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_recent_worlds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **str**| Filters on featured results. | [optional]
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "popularity"
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **order** | **str**|  | [optional] if omitted the server will use the default value of "descending"
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **search** | **str**| Filters by world name. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]
 **notag** | **str**| Tags to exclude (comma-separated). | [optional]
 **release_status** | **str**| Filter by ReleaseStatus. | [optional] if omitted the server will use the default value of "hidden"
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional]
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional]
 **platform** | **str**| The platform the asset supports. | [optional]
 **user_id** | **str**| Target user to see information on, admin-only. | [optional]

### Return type

[**[LimitedWorld]**](LimitedWorld.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**403** | Error response when trying to accept a see recently visited worlds of another user without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world**
> World get_world(world_id)

Get World by ID

Get information about a specific World.

### Example

```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.world import World
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get World by ID
        api_response = api_instance.get_world(world_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

[**World**](World.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single World object. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world_instance**
> Instance get_world_instance(world_id, instance_id)

Get World Instance

Returns a worlds instance.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.error import Error
from vrchatapi.model.instance import Instance
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 
    instance_id = "instanceId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get World Instance
        api_response = api_instance.get_world_instance(world_id, instance_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_world_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |
 **instance_id** | **str**|  |

### Return type

[**Instance**](Instance.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Instance object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world_metadata**
> InlineResponse2006 get_world_metadata(world_id)

Get World Metadata

Return a worlds custom metadata. This is currently believed to be unused. Metadata can be set with `updateWorld` and can be any arbitrary object.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.error import Error
from vrchatapi.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get World Metadata
        api_response = api_instance.get_world_metadata(world_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_world_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world_publish_status**
> InlineResponse2007 get_world_publish_status(world_id)

Get World Publish Status

Returns a worlds publish status.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.inline_response2007 import InlineResponse2007
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get World Publish Status
        api_response = api_instance.get_world_publish_status(world_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->get_world_publish_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_world**
> publish_world(world_id)

Publish World

Publish a world. You can only publish one world per week.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Publish World
        api_instance.publish_world(world_id)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->publish_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TODO |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_worlds**
> [LimitedWorld] search_worlds()

Search All Worlds

Search and list any worlds by query filters.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    featured = "featured_example" # str | Filters on featured results. (optional)
    sort = "popularity" # str |  (optional) if omitted the server will use the default value of "popularity"
    user = "me" # str | Set to `me` for searching own worlds. (optional) if omitted the server will use the default value of "me"
    user_id = "userId_example" # str | Filter by author UserID (optional)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    order = "descending" # str |  (optional) if omitted the server will use the default value of "descending"
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    search = "search_example" # str | Filters by world name. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)
    notag = "notag_example" # str | Tags to exclude (comma-separated). (optional)
    release_status = "hidden" # str | Filter by ReleaseStatus. (optional) if omitted the server will use the default value of "hidden"
    max_unity_version = "maxUnityVersion_example" # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = "minUnityVersion_example" # str | The minimum Unity version supported by the asset. (optional)
    platform = "platform_example" # str | The platform the asset supports. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search All Worlds
        api_response = api_instance.search_worlds(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->search_worlds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **str**| Filters on featured results. | [optional]
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "popularity"
 **user** | **str**| Set to &#x60;me&#x60; for searching own worlds. | [optional] if omitted the server will use the default value of "me"
 **user_id** | **str**| Filter by author UserID | [optional]
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **order** | **str**|  | [optional] if omitted the server will use the default value of "descending"
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **search** | **str**| Filters by world name. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]
 **notag** | **str**| Tags to exclude (comma-separated). | [optional]
 **release_status** | **str**| Filter by ReleaseStatus. | [optional] if omitted the server will use the default value of "hidden"
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional]
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional]
 **platform** | **str**| The platform the asset supports. | [optional]

### Return type

[**[LimitedWorld]**](LimitedWorld.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_world**
> unpublish_world(world_id)

Unpublish World

Unpublish a world.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Unpublish World
        api_instance.unpublish_world(world_id)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->unpublish_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_world**
> World update_world(world_id)

Update World

Update information about a specific World.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import worlds_api
from vrchatapi.model.inline_object7 import InlineObject7
from vrchatapi.model.world import World
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worlds_api.WorldsApi(api_client)
    world_id = "worldId_example" # str | 
    inline_object7 = InlineObject7(
        asset_url="asset_url_example",
        asset_version="asset_version_example",
        author_name="author_name_example",
        capacity=16,
        description="description_example",
        id=WorldID("wrld_ba913a96-fac4-4048-a062-9aa5db092812"),
        image_url="image_url_example",
        name="name_example",
        platform=Platform("standalonewindows"),
        release_status=ReleaseStatus("public"),
        tags=[
            Tag("tags_example"),
        ],
        unity_package_url="unity_package_url_example",
        unity_version="2018.4.20f1",
    ) # InlineObject7 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update World
        api_response = api_instance.update_world(world_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->update_world: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update World
        api_response = api_instance.update_world(world_id, inline_object7=inline_object7)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling WorldsApi->update_world: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  |
 **inline_object7** | [**InlineObject7**](InlineObject7.md)|  | [optional]

### Return type

[**World**](World.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single World object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

