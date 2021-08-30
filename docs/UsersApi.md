# vrchatapi.UsersApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userId} | Get User by ID
[**get_user_by_name**](UsersApi.md#get_user_by_name) | **GET** /users/{username}/name | Get User by Username
[**search_active_users**](UsersApi.md#search_active_users) | **GET** /users/active | Search Active Users
[**search_users**](UsersApi.md#search_users) | **GET** /users | Search All Users
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{userId} | Update User Info


# **get_user**
> User get_user(user_id)

Get User by ID

Get public user information about a specific user using their ID.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import users_api
from vrchatapi.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get User by ID
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**User**](User.md)

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

# **get_user_by_name**
> User get_user_by_name(username)

Get User by Username

Get public user information about a specific user using their name.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import users_api
from vrchatapi.model.user import User
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
    api_instance = users_api.UsersApi(api_client)
    username = "username_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get User by Username
        api_response = api_instance.get_user_by_name(username)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  |

### Return type

[**User**](User.md)

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

# **search_active_users**
> [LimitedUser] search_active_users(search)

Search Active Users

Search and list any Active users by text query.  **Has been locked down and now always respond with \"Invalid Admin Credentials\".**

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import users_api
from vrchatapi.model.limited_user import LimitedUser
from vrchatapi.model.inline_response403 import InlineResponse403
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
    api_instance = users_api.UsersApi(api_client)
    search = "search_example" # str | Username to search for
    developer_type = "developerType_example" # str | Active user by developer type, none for normal users and internal for moderators (optional)
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60

    # example passing only required values which don't have defaults set
    try:
        # Search Active Users
        api_response = api_instance.search_active_users(search)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->search_active_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Active Users
        api_response = api_instance.search_active_users(search, developer_type=developer_type, offset=offset, n=n)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->search_active_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Username to search for |
 **developer_type** | **str**| Active user by developer type, none for normal users and internal for moderators | [optional]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60

### Return type

[**[LimitedUser]**](LimitedUser.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Error response due to missing Administrator credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users**
> [LimitedUser] search_users()

Search All Users

Search and list any users by text query

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import users_api
from vrchatapi.model.limited_user import LimitedUser
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
    api_instance = users_api.UsersApi(api_client)
    search = "search_example" # str | Searches by `displayName`. Will return empty array if search query is empty or missing. (optional)
    developer_type = "developerType_example" # str | Active user by developer type, none for normal users and internal for moderators (optional)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search All Users
        api_response = api_instance.search_users(search=search, developer_type=developer_type, n=n, offset=offset)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->search_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Searches by &#x60;displayName&#x60;. Will return empty array if search query is empty or missing. | [optional]
 **developer_type** | **str**| Active user by developer type, none for normal users and internal for moderators | [optional]
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]

### Return type

[**[LimitedUser]**](LimitedUser.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Error response when trying to search list of users with an invalid request. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> CurrentUser update_user(user_id)

Update User Info

Update a users information such as the email and birthday.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import users_api
from vrchatapi.model.current_user import CurrentUser
from vrchatapi.model.inline_object2 import InlineObject2
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | 
    inline_object2 = InlineObject2(
        email="email_example",
        birthday=dateutil_parser('1970-01-01').date(),
        accepted_tos_version=3.14,
        tags=[
            Tag("tags_example"),
        ],
        status=UserStatus("active"),
        status_description="status_description_example",
        bio="bio_example",
        bio_links=[
            "bio_links_example",
        ],
        user_icon="https://api.vrchat.cloud/api/1/file/file_76dc2964-0ce8-41df-b2e7-8edf994fee31/1",
    ) # InlineObject2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update User Info
        api_response = api_instance.update_user(user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update User Info
        api_response = api_instance.update_user(user_id, inline_object2=inline_object2)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional]

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

