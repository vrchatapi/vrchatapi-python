# vrchatapi.AvatarsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_avatar**](AvatarsApi.md#create_avatar) | **POST** /avatars | Create Avatar
[**delete_avatar**](AvatarsApi.md#delete_avatar) | **DELETE** /avatars/{avatarId} | Delete Avatar
[**get_avatar**](AvatarsApi.md#get_avatar) | **GET** /avatars/{avatarId} | Get Avatar
[**get_favorited_avatars**](AvatarsApi.md#get_favorited_avatars) | **GET** /avatars/favorites | List Favorited Avatars
[**search_avatars**](AvatarsApi.md#search_avatars) | **GET** /avatars | Search Avatars
[**select_avatar**](AvatarsApi.md#select_avatar) | **PUT** /avatars/{avatarId}/select | Select Avatar
[**update_avatar**](AvatarsApi.md#update_avatar) | **PUT** /avatars/{avatarId} | Update Avatar


# **create_avatar**
> Avatar create_avatar()

Create Avatar

Create an avatar. It's possible to optionally specify a ID if you want a custom one. Attempting to create an Avatar with an already claimed ID will result in a DB error.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.inline_object10 import InlineObject10
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
    api_instance = avatars_api.AvatarsApi(api_client)
    inline_object10 = InlineObject10(
        asset_url="asset_url_example",
        id=AvatarID("avtr_912d66a4-4714-43b8-8407-7de2cafbf55b"),
        name="name_example",
        description="description_example",
        tags=[
            Tag("tags_example"),
        ],
        image_url="image_url_example",
        release_status=ReleaseStatus("public"),
        version=1,
        unity_package_url="unity_package_url_example",
    ) # InlineObject10 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Avatar
        api_response = api_instance.create_avatar(inline_object10=inline_object10)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->create_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | [optional]

### Return type

[**Avatar**](Avatar.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response when set featured to true without being an admin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar**
> Avatar delete_avatar(avatar_id)

Delete Avatar

Delete an avatar. Notice an avatar is never fully \"deleted\", only its ReleaseStatus is set to \"hidden\" and the linked Files are deleted. The AvatarID is permanently reserved.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.error import Error
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
    avatar_id = "avatarId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Avatar
        api_response = api_instance.delete_avatar(avatar_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->delete_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**|  |

### Return type

[**Avatar**](Avatar.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar**
> Avatar get_avatar(avatar_id)

Get Avatar

Get information about a specific Avatar.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.error import Error
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
    avatar_id = "avatarId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Avatar
        api_response = api_instance.get_avatar(avatar_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->get_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**|  |

### Return type

[**Avatar**](Avatar.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorited_avatars**
> get_favorited_avatars()

List Favorited Avatars

Search and list favorited avatars by query filters.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
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
        # List Favorited Avatars
        api_instance.get_favorited_avatars(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->get_favorited_avatars: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_avatars**
> [Avatar] search_avatars()

Search Avatars

Search and list avatars by query filters. You can only search your own or featured avatars. It is not possible as a normal user to search other peoples avatars.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
    featured = "featured_example" # str | Filters on featured results. (optional)
    sort = "popularity" # str |  (optional) if omitted the server will use the default value of "popularity"
    user = "me" # str | Set to `me` for searching own avatars. (optional) if omitted the server will use the default value of "me"
    user_id = "userId_example" # str | Filter by author UserID (optional)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    order = "descending" # str |  (optional) if omitted the server will use the default value of "descending"
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)
    notag = "notag_example" # str | Tags to exclude (comma-separated). (optional)
    release_status = "hidden" # str | Filter by ReleaseStatus. (optional) if omitted the server will use the default value of "hidden"
    max_unity_version = "maxUnityVersion_example" # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = "minUnityVersion_example" # str | The minimum Unity version supported by the asset. (optional)
    platform = "platform_example" # str | The platform the asset supports. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Avatars
        api_response = api_instance.search_avatars(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->search_avatars: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **str**| Filters on featured results. | [optional]
 **sort** | **str**|  | [optional] if omitted the server will use the default value of "popularity"
 **user** | **str**| Set to &#x60;me&#x60; for searching own avatars. | [optional] if omitted the server will use the default value of "me"
 **user_id** | **str**| Filter by author UserID | [optional]
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **order** | **str**|  | [optional] if omitted the server will use the default value of "descending"
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]
 **notag** | **str**| Tags to exclude (comma-separated). | [optional]
 **release_status** | **str**| Filter by ReleaseStatus. | [optional] if omitted the server will use the default value of "hidden"
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional]
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional]
 **platform** | **str**| The platform the asset supports. | [optional]

### Return type

[**[Avatar]**](Avatar.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Avatar objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_avatar**
> CurrentUser select_avatar(avatar_id)

Select Avatar

Switches into that avatar.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.current_user import CurrentUser
from vrchatapi.model.error import Error
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
    avatar_id = "avatarId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Select Avatar
        api_response = api_instance.select_avatar(avatar_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->select_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**|  |

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CurrentUser object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar**
> Avatar update_avatar(avatar_id)

Update Avatar

Update information about a specific avatar.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import avatars_api
from vrchatapi.model.avatar import Avatar
from vrchatapi.model.inline_object11 import InlineObject11
from vrchatapi.model.error import Error
from vrchatapi.model.inline_response401 import InlineResponse401
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
    api_instance = avatars_api.AvatarsApi(api_client)
    avatar_id = "avatarId_example" # str | 
    inline_object11 = InlineObject11(
        asset_url="asset_url_example",
        id=AvatarID("avtr_912d66a4-4714-43b8-8407-7de2cafbf55b"),
        name="name_example",
        description="description_example",
        tags=[
            Tag("tags_example"),
        ],
        image_url="image_url_example",
        release_status=ReleaseStatus("public"),
        version=1,
        unity_package_url="unity_package_url_example",
    ) # InlineObject11 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Avatar
        api_response = api_instance.update_avatar(avatar_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->update_avatar: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Avatar
        api_response = api_instance.update_avatar(avatar_id, inline_object11=inline_object11)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling AvatarsApi->update_avatar: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**|  |
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | [optional]

### Return type

[**Avatar**](Avatar.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

