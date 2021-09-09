# vrchatapi.FavoritesApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_favorite**](FavoritesApi.md#add_favorite) | **POST** /favorites | Add Favorite
[**clear_favorite_group**](FavoritesApi.md#clear_favorite_group) | **DELETE** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Clear Favorite Group
[**get_favorite**](FavoritesApi.md#get_favorite) | **GET** /favorites/{favoriteId} | Show Favorite
[**get_favorite_group**](FavoritesApi.md#get_favorite_group) | **GET** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Show Favorite Group
[**get_favorite_groups**](FavoritesApi.md#get_favorite_groups) | **GET** /favorite/groups | List Favorite Groups
[**get_favorites**](FavoritesApi.md#get_favorites) | **GET** /favorites | List Favorites
[**remove_favorite**](FavoritesApi.md#remove_favorite) | **DELETE** /favorites/{favoriteId} | Remove Favorite
[**update_favorite_group**](FavoritesApi.md#update_favorite_group) | **PUT** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Update Favorite Group


# **add_favorite**
> Favorite add_favorite()

Add Favorite

Add a new favorite.  Friend groups are named `group_0` through `group_3`. Avatar and World groups are named `avatars1` to `avatar4` and `worlds1` to `worlds4`.  You cannot add people whom you are not friends with to your friends list. Destroying a friendship removes the person as favorite on both sides.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.inline_object8 import InlineObject8
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
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
    api_instance = favorites_api.FavoritesApi(api_client)
    inline_object8 = InlineObject8(
        type=FavoriteType("world"),
        favorite_id="favorite_id_example",
        tags=[
            Tag("tags_example"),
        ],
    ) # InlineObject8 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Favorite
        api_response = api_instance.add_favorite(inline_object8=inline_object8)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->add_favorite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object8** | [**InlineObject8**](InlineObject8.md)|  | [optional]

### Return type

[**Favorite**](Favorite.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Favorite object. |  -  |
**400** | Error response when trying favorite someone or something when already having it/them favorited. |  -  |
**403** | Error response when trying favorite someone whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_favorite_group**
> Success clear_favorite_group(favorite_group_type, favorite_group_name, user_id)

Clear Favorite Group

Clear ALL contents of a specific favorite group.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.success import Success
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
    api_instance = favorites_api.FavoritesApi(api_client)
    favorite_group_type = "world" # str | The type of group to fetch, must be a valid FavoriteType.
    favorite_group_name = "favoriteGroupName_example" # str | 
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Clear Favorite Group
        api_response = api_instance.clear_favorite_group(favorite_group_type, favorite_group_name, user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->clear_favorite_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. |
 **favorite_group_name** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**Success**](Success.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after clearing a favorite group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite**
> Favorite get_favorite(favorite_id)

Show Favorite

Return information about a specific Favorite.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
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
    api_instance = favorites_api.FavoritesApi(api_client)
    favorite_id = "favoriteId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Show Favorite
        api_response = api_instance.get_favorite(favorite_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_id** | **str**|  |

### Return type

[**Favorite**](Favorite.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Favorite object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent favorite. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_group**
> FavoriteGroup get_favorite_group(favorite_group_type, favorite_group_name, user_id)

Show Favorite Group

Fetch information about a specific favorite group.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.favorite_group import FavoriteGroup
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
    api_instance = favorites_api.FavoritesApi(api_client)
    favorite_group_type = "world" # str | The type of group to fetch, must be a valid FavoriteType.
    favorite_group_name = "favoriteGroupName_example" # str | 
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Show Favorite Group
        api_response = api_instance.get_favorite_group(favorite_group_type, favorite_group_name, user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. |
 **favorite_group_name** | **str**|  |
 **user_id** | **str**|  |

### Return type

[**FavoriteGroup**](FavoriteGroup.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FavoriteGroup object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_groups**
> [FavoriteGroup] get_favorite_groups()

List Favorite Groups

Return a list of favorite groups owned by a user. Returns the same information as `getFavoriteGroups`.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.favorite_group import FavoriteGroup
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
    api_instance = favorites_api.FavoritesApi(api_client)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    owner_id = "ownerId_example" # str | The owner of whoms favorite groups to return. Must be a UserID. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Favorite Groups
        api_response = api_instance.get_favorite_groups(n=n, offset=offset, owner_id=owner_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **owner_id** | **str**| The owner of whoms favorite groups to return. Must be a UserID. | [optional]

### Return type

[**[FavoriteGroup]**](FavoriteGroup.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of FavoriteGroup objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites**
> [Favorite] get_favorites()

List Favorites

Returns a list of favorites.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
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
    api_instance = favorites_api.FavoritesApi(api_client)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    type = "type_example" # str | The type of favorites to return, FavoriteType. (optional)
    tag = "tag_example" # str | Tags to include (comma-separated). (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Favorites
        api_response = api_instance.get_favorites(n=n, offset=offset, type=type, tag=tag)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->get_favorites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **type** | **str**| The type of favorites to return, FavoriteType. | [optional]
 **tag** | **str**| Tags to include (comma-separated). | [optional]

### Return type

[**[Favorite]**](Favorite.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Favorite objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_favorite**
> Success remove_favorite(favorite_id)

Remove Favorite

Remove a favorite from your favorites list.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.success import Success
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
    api_instance = favorites_api.FavoritesApi(api_client)
    favorite_id = "favoriteId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Remove Favorite
        api_response = api_instance.remove_favorite(favorite_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->remove_favorite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_id** | **str**|  |

### Return type

[**Success**](Success.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after removing a favorite. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent favorite. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_favorite_group**
> update_favorite_group(favorite_group_type, favorite_group_name, user_id)

Update Favorite Group

Update information about a specific favorite group.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import favorites_api
from vrchatapi.model.inline_object9 import InlineObject9
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
    api_instance = favorites_api.FavoritesApi(api_client)
    favorite_group_type = "world" # str | The type of group to fetch, must be a valid FavoriteType.
    favorite_group_name = "favoriteGroupName_example" # str | 
    user_id = "userId_example" # str | 
    inline_object9 = InlineObject9(
        display_name="display_name_example",
        visibility=FavoriteGroupVisibility("private"),
        tags=[
            Tag("tags_example"),
        ],
    ) # InlineObject9 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Favorite Group
        api_instance.update_favorite_group(favorite_group_type, favorite_group_name, user_id)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->update_favorite_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Favorite Group
        api_instance.update_favorite_group(favorite_group_type, favorite_group_name, user_id, inline_object9=inline_object9)
    except vrchatapi.ApiException as e:
        print("Exception when calling FavoritesApi->update_favorite_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. |
 **favorite_group_name** | **str**|  |
 **user_id** | **str**|  |
 **inline_object9** | [**InlineObject9**](InlineObject9.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

