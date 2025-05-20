# vrchatapi.FavoritesApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_favorite**](FavoritesApi.md#add_favorite) | **POST** /favorites | Add Favorite
[**clear_favorite_group**](FavoritesApi.md#clear_favorite_group) | **DELETE** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Clear Favorite Group
[**get_favorite_group**](FavoritesApi.md#get_favorite_group) | **GET** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Show Favorite Group
[**get_favorite_groups**](FavoritesApi.md#get_favorite_groups) | **GET** /favorite/groups | List Favorite Groups
[**get_favorite_limits**](FavoritesApi.md#get_favorite_limits) | **GET** /auth/user/favoritelimits | Get Favorite Limits
[**get_favorites**](FavoritesApi.md#get_favorites) | **GET** /favorites | List Favorites
[**remove_favorite**](FavoritesApi.md#remove_favorite) | **DELETE** /favorites/{favoriteId} | Remove Favorite
[**update_favorite_group**](FavoritesApi.md#update_favorite_group) | **PUT** /favorite/group/{favoriteGroupType}/{favoriteGroupName}/{userId} | Update Favorite Group


# **add_favorite**
> Favorite add_favorite(add_favorite_request=add_favorite_request)

Add Favorite

Add a new favorite.  Friend groups are named `group_0` through `group_3`. Avatar and World groups are named `avatars1` to `avatars4` and `worlds1` to `worlds4`.  You cannot add people whom you are not friends with to your friends list. Destroying a friendship removes the person as favorite on both sides.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    add_favorite_request = {"type":"friend","favoriteId":"usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469","tags":["group_0"]} # AddFavoriteRequest |  (optional)

    try:
        # Add Favorite
        api_response = api_instance.add_favorite(add_favorite_request=add_favorite_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->add_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_favorite_request** | [**AddFavoriteRequest**](AddFavoriteRequest.md)|  | [optional] 

### Return type

[**Favorite**](Favorite.md)

### Authorization

[authCookie](../README.md#authCookie)

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

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    favorite_group_type = 'favorite_group_type_example' # str | The type of group to fetch, must be a valid FavoriteType.
favorite_group_name = 'favorite_group_name_example' # str | The name of the group to fetch, must be a name of a FavoriteGroup.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Clear Favorite Group
        api_response = api_instance.clear_favorite_group(favorite_group_type, favorite_group_name, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->clear_favorite_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. | 
 **favorite_group_name** | **str**| The name of the group to fetch, must be a name of a FavoriteGroup. | 
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**Success**](Success.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after clearing a favorite group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_group**
> FavoriteGroup get_favorite_group(favorite_group_type, favorite_group_name, user_id)

Show Favorite Group

Fetch information about a specific favorite group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    favorite_group_type = 'favorite_group_type_example' # str | The type of group to fetch, must be a valid FavoriteType.
favorite_group_name = 'favorite_group_name_example' # str | The name of the group to fetch, must be a name of a FavoriteGroup.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Show Favorite Group
        api_response = api_instance.get_favorite_group(favorite_group_type, favorite_group_name, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. | 
 **favorite_group_name** | **str**| The name of the group to fetch, must be a name of a FavoriteGroup. | 
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**FavoriteGroup**](FavoriteGroup.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FavoriteGroup object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_groups**
> list[FavoriteGroup] get_favorite_groups(n=n, offset=offset, user_id=user_id, owner_id=owner_id)

List Favorite Groups

Return a list of favorite groups owned by a user. Returns the same information as `getFavoriteGroups`.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
user_id = 'user_id_example' # str | Target user to see information on, admin-only. (optional)
owner_id = 'owner_id_example' # str | The owner of whoms favorite groups to return. Must be a UserID. (optional)

    try:
        # List Favorite Groups
        api_response = api_instance.get_favorite_groups(n=n, offset=offset, user_id=user_id, owner_id=owner_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **user_id** | **str**| Target user to see information on, admin-only. | [optional] 
 **owner_id** | **str**| The owner of whoms favorite groups to return. Must be a UserID. | [optional] 

### Return type

[**list[FavoriteGroup]**](FavoriteGroup.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of FavoriteGroup objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorite_limits**
> FavoriteLimits get_favorite_limits()

Get Favorite Limits

Return information about a specific Favorite.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    
    try:
        # Get Favorite Limits
        api_response = api_instance.get_favorite_limits()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->get_favorite_limits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FavoriteLimits**](FavoriteLimits.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FavoriteLimits object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites**
> list[Favorite] get_favorites(n=n, offset=offset, type=type, tag=tag)

List Favorites

Returns a list of favorites.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
type = 'type_example' # str | The type of favorites to return, FavoriteType. (optional)
tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)

    try:
        # List Favorites
        api_response = api_instance.get_favorites(n=n, offset=offset, type=type, tag=tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->get_favorites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **type** | **str**| The type of favorites to return, FavoriteType. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 

### Return type

[**list[Favorite]**](Favorite.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Favorite objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_favorite**
> Success remove_favorite(favorite_id)

Remove Favorite

Remove a favorite from your favorites list.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    favorite_id = 'favorite_id_example' # str | Must be a valid favorite ID.

    try:
        # Remove Favorite
        api_response = api_instance.remove_favorite(favorite_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FavoritesApi->remove_favorite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_id** | **str**| Must be a valid favorite ID. | 

### Return type

[**Success**](Success.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after removing a favorite. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent favorite. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_favorite_group**
> update_favorite_group(favorite_group_type, favorite_group_name, user_id, update_favorite_group_request=update_favorite_group_request)

Update Favorite Group

Update information about a specific favorite group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
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

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.FavoritesApi(api_client)
    favorite_group_type = 'favorite_group_type_example' # str | The type of group to fetch, must be a valid FavoriteType.
favorite_group_name = 'favorite_group_name_example' # str | The name of the group to fetch, must be a name of a FavoriteGroup.
user_id = 'user_id_example' # str | Must be a valid user ID.
update_favorite_group_request = vrchatapi.UpdateFavoriteGroupRequest() # UpdateFavoriteGroupRequest |  (optional)

    try:
        # Update Favorite Group
        api_instance.update_favorite_group(favorite_group_type, favorite_group_name, user_id, update_favorite_group_request=update_favorite_group_request)
    except ApiException as e:
        print("Exception when calling FavoritesApi->update_favorite_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_group_type** | **str**| The type of group to fetch, must be a valid FavoriteType. | 
 **favorite_group_name** | **str**| The name of the group to fetch, must be a name of a FavoriteGroup. | 
 **user_id** | **str**| Must be a valid user ID. | 
 **update_favorite_group_request** | [**UpdateFavoriteGroupRequest**](UpdateFavoriteGroupRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

