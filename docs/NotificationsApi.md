# vrchatapi.NotificationsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_friend_request**](NotificationsApi.md#accept_friend_request) | **PUT** /auth/user/notifications/{notificationId}/accept | Accept Friend Request
[**clear_notifications**](NotificationsApi.md#clear_notifications) | **PUT** /auth/user/notifications/clear | Clear All Notifications
[**delete_notification**](NotificationsApi.md#delete_notification) | **PUT** /auth/user/notifications/{notificationId}/hide | Delete Notification
[**get_notifications**](NotificationsApi.md#get_notifications) | **GET** /auth/user/notifications | List Notifications
[**mark_notification_as_read**](NotificationsApi.md#mark_notification_as_read) | **PUT** /auth/user/notifications/{notificationId}/see | Mark Notification As Read


# **accept_friend_request**
> Success accept_friend_request(notification_id)

Accept Friend Request

Accept a friend request by notification `frq_` ID. Friend requests can be found using the NotificationsAPI `getNotifications` by filtering of type `friendRequest`.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import notifications_api
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
    api_instance = notifications_api.NotificationsApi(api_client)
    notification_id = "notificationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Accept Friend Request
        api_response = api_instance.accept_friend_request(notification_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling NotificationsApi->accept_friend_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  |

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
**200** | Successful response after friending a user. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |
**404** | Error response when trying to accept a non-existent friend request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_notifications**
> Success clear_notifications()

Clear All Notifications

Clear **all** notifications.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import notifications_api
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
    api_instance = notifications_api.NotificationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Clear All Notifications
        api_response = api_instance.clear_notifications()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling NotificationsApi->clear_notifications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Successful response after clearing all notifications. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> Notification delete_notification(notification_id)

Delete Notification

Delete a notification.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import notifications_api
from vrchatapi.model.notification import Notification
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
    api_instance = notifications_api.NotificationsApi(api_client)
    notification_id = "notificationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Notification
        api_response = api_instance.delete_notification(notification_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling NotificationsApi->delete_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  |

### Return type

[**Notification**](Notification.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications**
> [Notification] get_notifications()

List Notifications

Retrieve all of the current user's notifications.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import notifications_api
from vrchatapi.model.notification import Notification
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
    api_instance = notifications_api.NotificationsApi(api_client)
    type = "all" # str | Only send notifications of this type (can use `all` for all). This parameter no longer does anything, and is deprecated. (optional)
    sent = True # bool | Return notifications sent by the user. Must be false or omitted. (optional)
    hidden = True # bool | Whether to return hidden or non-hidden notifications. True only allowed on type `friendRequest`. (optional)
    after = "five_minutes_ago" # str | Only return notifications sent after this Date. Ignored if type is `friendRequest`. (optional)
    n = 60 # int | The number of objects to return. (optional) if omitted the server will use the default value of 60
    offset = 0 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Notifications
        api_response = api_instance.get_notifications(type=type, sent=sent, hidden=hidden, after=after, n=n, offset=offset)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling NotificationsApi->get_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Only send notifications of this type (can use &#x60;all&#x60; for all). This parameter no longer does anything, and is deprecated. | [optional]
 **sent** | **bool**| Return notifications sent by the user. Must be false or omitted. | [optional]
 **hidden** | **bool**| Whether to return hidden or non-hidden notifications. True only allowed on type &#x60;friendRequest&#x60;. | [optional]
 **after** | **str**| Only return notifications sent after this Date. Ignored if type is &#x60;friendRequest&#x60;. | [optional]
 **n** | **int**| The number of objects to return. | [optional] if omitted the server will use the default value of 60
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional]

### Return type

[**[Notification]**](Notification.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Notifcation objects. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_notification_as_read**
> Notification mark_notification_as_read(notification_id)

Mark Notification As Read

Mark a notification as seen.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import notifications_api
from vrchatapi.model.notification import Notification
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
    api_instance = notifications_api.NotificationsApi(api_client)
    notification_id = "notificationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Mark Notification As Read
        api_response = api_instance.mark_notification_as_read(notification_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling NotificationsApi->mark_notification_as_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  |

### Return type

[**Notification**](Notification.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

