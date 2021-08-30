# vrchatapi.PlayermoderationApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_all_player_moderations**](PlayermoderationApi.md#clear_all_player_moderations) | **DELETE** /auth/user/playermoderations | Clear All Player Moderations
[**delete_player_moderation**](PlayermoderationApi.md#delete_player_moderation) | **DELETE** /auth/user/playermoderations/{playerModerationId} | Delete Player Moderation
[**get_player_moderation**](PlayermoderationApi.md#get_player_moderation) | **GET** /auth/user/playermoderations/{playerModerationId} | Get Player Moderation
[**get_player_moderations**](PlayermoderationApi.md#get_player_moderations) | **GET** /auth/user/playermoderations | Search Player Moderations
[**moderate_user**](PlayermoderationApi.md#moderate_user) | **POST** /auth/user/playermoderations | Moderate User
[**unmoderate_user**](PlayermoderationApi.md#unmoderate_user) | **PUT** /auth/user/unplayermoderate | Unmoderate User


# **clear_all_player_moderations**
> Error clear_all_player_moderations()

Clear All Player Moderations

⚠️ **This will delete every single player moderation you've ever made.**

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear All Player Moderations
        api_response = api_instance.clear_all_player_moderations()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->clear_all_player_moderations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Error**](Error.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after e.g. clearing all player moderations. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_player_moderation**
> Error delete_player_moderation(player_moderation_id)

Delete Player Moderation

Deletes a specific player moderation based on it's `pmod_` ID. The website uses `unmoderateUser` instead. You can delete the same player moderation multiple times successfully.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)
    player_moderation_id = "playerModerationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Player Moderation
        api_response = api_instance.delete_player_moderation(player_moderation_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->delete_player_moderation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_moderation_id** | **str**|  |

### Return type

[**Error**](Error.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after removing a PlayerModeration by ID. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**403** | Error response when trying to delete someone else&#39;s player moderation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_moderation**
> PlayerModeration get_player_moderation(player_moderation_id)

Get Player Moderation

Returns a single Player Moderation. This returns the exact same amount of information as the more generalised `getPlayerModerations`.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
from vrchatapi.model.player_moderation import PlayerModeration
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)
    player_moderation_id = "playerModerationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Player Moderation
        api_response = api_instance.get_player_moderation(player_moderation_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->get_player_moderation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_moderation_id** | **str**|  |

### Return type

[**PlayerModeration**](PlayerModeration.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single PlayerModeration object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent player moderation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_moderations**
> [PlayerModeration] get_player_moderations()

Search Player Moderations

Returns a list of all player moderations made by **you**.  This endpoint does not have pagination, and will return *all* results. Use query parameters to limit your query if needed.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
from vrchatapi.model.player_moderation import PlayerModeration
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)
    type = "type_example" # str | Must be one of PlayerModerationType, except unblock. Unblocking simply removes a block. (optional)
    target_user_id = "targetUserId_example" # str | Must be valid UserID. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Player Moderations
        api_response = api_instance.get_player_moderations(type=type, target_user_id=target_user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->get_player_moderations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Must be one of PlayerModerationType, except unblock. Unblocking simply removes a block. | [optional]
 **target_user_id** | **str**| Must be valid UserID. | [optional]

### Return type

[**[PlayerModeration]**](PlayerModeration.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of PlayerModeration objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **moderate_user**
> PlayerModeration moderate_user()

Moderate User

Moderate a user, e.g. unmute them or show their avatar.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
from vrchatapi.model.player_moderation import PlayerModeration
from vrchatapi.model.inline_object12 import InlineObject12
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)
    inline_object12 = InlineObject12(
        type=PlayerModerationType("showAvatar"),
    ) # InlineObject12 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Moderate User
        api_response = api_instance.moderate_user(inline_object12=inline_object12)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->moderate_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | [optional]

### Return type

[**PlayerModeration**](PlayerModeration.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single PlayerModeration object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmoderate_user**
> Error unmoderate_user()

Unmoderate User

Removes a player moderation previously added through `moderateUser`. E.g if you previuosly have shown their avatar, but now want to reset it to default.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import playermoderation_api
from vrchatapi.model.inline_object13 import InlineObject13
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
    api_instance = playermoderation_api.PlayermoderationApi(api_client)
    inline_object13 = InlineObject13(
        type=PlayerModerationType("showAvatar"),
    ) # InlineObject13 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unmoderate User
        api_response = api_instance.unmoderate_user(inline_object13=inline_object13)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling PlayermoderationApi->unmoderate_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object13** | [**InlineObject13**](InlineObject13.md)|  | [optional]

### Return type

[**Error**](Error.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response after unmoderating a player moderation. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

