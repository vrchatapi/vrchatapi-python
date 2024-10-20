# vrchatapi.WorldsApi

All URIs are relative to *https://vrchat.com/api/1*

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
> World create_world(create_world_request=create_world_request)

Create World

Create a new world. This endpoint requires `assetUrl` to be a valid File object with `.vrcw` file extension, and `imageUrl` to be a valid File object with an image file extension.

### Example

```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    create_world_request = vrchatapi.CreateWorldRequest() # CreateWorldRequest |  (optional)

    try:
        # Create World
        api_response = api_instance.create_world(create_world_request=create_world_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->create_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_world_request** | [**CreateWorldRequest**](CreateWorldRequest.md)|  | [optional] 

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
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_world**
> delete_world(world_id)

Delete World

Delete a world. Notice a world is never fully \"deleted\", only its ReleaseStatus is set to \"hidden\" and the linked Files are deleted. The WorldID is permanently reserved.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Delete World
        api_instance.delete_world(world_id)
    except ApiException as e:
        print("Exception when calling WorldsApi->delete_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_worlds**
> list[LimitedWorld] get_active_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform)

List Active Worlds

Search and list currently Active worlds by query filters.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
sort = vrchatapi.SortOption() # SortOption | The sort order of the results. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
order = vrchatapi.OrderOption() # OrderOption | Result ordering (optional)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
search = 'search_example' # str | Filters by world name. (optional)
tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
release_status = vrchatapi.ReleaseStatus() # ReleaseStatus | Filter by ReleaseStatus. (optional)
max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
platform = 'platform_example' # str | The platform the asset supports. (optional)

    try:
        # List Active Worlds
        api_response = api_instance.get_active_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_active_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] 
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **search** | **str**| Filters by world name. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] 
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 

### Return type

[**list[LimitedWorld]**](LimitedWorld.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorited_worlds**
> list[FavoritedWorld] get_favorited_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)

List Favorited Worlds

Search and list favorited worlds by query filters.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
sort = vrchatapi.SortOption() # SortOption | The sort order of the results. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
order = vrchatapi.OrderOption() # OrderOption | Result ordering (optional)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
search = 'search_example' # str | Filters by world name. (optional)
tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
release_status = vrchatapi.ReleaseStatus() # ReleaseStatus | Filter by ReleaseStatus. (optional)
max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
platform = 'platform_example' # str | The platform the asset supports. (optional)
user_id = 'user_id_example' # str | Target user to see information on, admin-only. (optional)

    try:
        # List Favorited Worlds
        api_response = api_instance.get_favorited_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_favorited_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] 
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **search** | **str**| Filters by world name. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] 
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 
 **user_id** | **str**| Target user to see information on, admin-only. | [optional] 

### Return type

[**list[FavoritedWorld]**](FavoritedWorld.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of FavoritedWorld objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to see favourited worlds of another user without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_worlds**
> list[LimitedWorld] get_recent_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)

List Recent Worlds

Search and list recently visited worlds by query filters.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
sort = vrchatapi.SortOption() # SortOption | The sort order of the results. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
order = vrchatapi.OrderOption() # OrderOption | Result ordering (optional)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
search = 'search_example' # str | Filters by world name. (optional)
tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
release_status = vrchatapi.ReleaseStatus() # ReleaseStatus | Filter by ReleaseStatus. (optional)
max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
platform = 'platform_example' # str | The platform the asset supports. (optional)
user_id = 'user_id_example' # str | Target user to see information on, admin-only. (optional)

    try:
        # List Recent Worlds
        api_response = api_instance.get_recent_worlds(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_recent_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] 
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **search** | **str**| Filters by world name. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] 
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 
 **user_id** | **str**| Target user to see information on, admin-only. | [optional] 

### Return type

[**list[LimitedWorld]**](LimitedWorld.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to see recently visited worlds of another user without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world**
> World get_world(world_id)

Get World by ID

Get information about a specific World. Works unauthenticated but when so will always return `0` for certain fields.

### Example

```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Get World by ID
        api_response = api_instance.get_world(world_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

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

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.
instance_id = 'instance_id_example' # str | Must be a valid instance ID.

    try:
        # Get World Instance
        api_response = api_instance.get_world_instance(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_world_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 
 **instance_id** | **str**| Must be a valid instance ID. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Instance object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_world_metadata**
> WorldMetadata get_world_metadata(world_id)

Get World Metadata

Return a worlds custom metadata. This is currently believed to be unused. Metadata can be set with `updateWorld` and can be any arbitrary object.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Get World Metadata
        api_response = api_instance.get_world_metadata(world_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_world_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

### Return type

[**WorldMetadata**](WorldMetadata.md)

### Authorization

[authCookie](../README.md#authCookie)

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
> WorldPublishStatus get_world_publish_status(world_id)

Get World Publish Status

Returns a worlds publish status.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Get World Publish Status
        api_response = api_instance.get_world_publish_status(world_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->get_world_publish_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

### Return type

[**WorldPublishStatus**](WorldPublishStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single WorldPublishStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_world**
> publish_world(world_id)

Publish World

Publish a world. You can only publish one world per week.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Publish World
        api_instance.publish_world(world_id)
    except ApiException as e:
        print("Exception when calling WorldsApi->publish_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TODO |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_worlds**
> list[LimitedWorld] search_worlds(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, fuzzy=fuzzy)

Search All Worlds

Search and list any worlds by query filters.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
sort = vrchatapi.SortOption() # SortOption | The sort order of the results. (optional)
user = 'user_example' # str | Set to `me` for searching own worlds. (optional)
user_id = 'user_id_example' # str | Filter by UserID. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
order = vrchatapi.OrderOption() # OrderOption | Result ordering (optional)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
search = 'search_example' # str | Filters by world name. (optional)
tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
release_status = vrchatapi.ReleaseStatus() # ReleaseStatus | Filter by ReleaseStatus. (optional)
max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
platform = 'platform_example' # str | The platform the asset supports. (optional)
fuzzy = True # bool |  (optional)

    try:
        # Search All Worlds
        api_response = api_instance.search_worlds(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, fuzzy=fuzzy)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->search_worlds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] 
 **user** | **str**| Set to &#x60;me&#x60; for searching own worlds. | [optional] 
 **user_id** | **str**| Filter by UserID. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] 
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **search** | **str**| Filters by world name. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] 
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 
 **fuzzy** | **bool**|  | [optional] 

### Return type

[**list[LimitedWorld]**](LimitedWorld.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedWorld objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_world**
> unpublish_world(world_id)

Unpublish World

Unpublish a world.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.

    try:
        # Unpublish World
        api_instance.unpublish_world(world_id)
    except ApiException as e:
        print("Exception when calling WorldsApi->unpublish_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_world**
> World update_world(world_id, update_world_request=update_world_request)

Update World

Update information about a specific World.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.WorldsApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.
update_world_request = vrchatapi.UpdateWorldRequest() # UpdateWorldRequest |  (optional)

    try:
        # Update World
        api_response = api_instance.update_world(world_id, update_world_request=update_world_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorldsApi->update_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 
 **update_world_request** | [**UpdateWorldRequest**](UpdateWorldRequest.md)|  | [optional] 

### Return type

[**World**](World.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single World object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent world. Sometimes returns with &#x60;model &lt;worldId&gt; not found&#x60; instead of &#x60;World &lt;worldId not found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

