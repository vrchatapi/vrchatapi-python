# vrchatapi.InviteApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invite_message**](InviteApi.md#get_invite_message) | **GET** /message/{userId}/{messageType}/{slot} | Get Invite Message
[**get_invite_messages**](InviteApi.md#get_invite_messages) | **GET** /message/{userId}/{messageType} | List Invite Messages
[**invite_user**](InviteApi.md#invite_user) | **POST** /invite/{userId} | Invite User
[**request_invite**](InviteApi.md#request_invite) | **POST** /requestInvite/{userId} | Request Invite
[**reset_invite_message**](InviteApi.md#reset_invite_message) | **DELETE** /message/{userId}/{messageType}/{slot} | Reset Invite Message
[**respond_invite**](InviteApi.md#respond_invite) | **POST** /invite/{notificationId}/response | Respond Invite
[**update_invite_message**](InviteApi.md#update_invite_message) | **PUT** /message/{userId}/{messageType}/{slot} | Update Invite Message


# **get_invite_message**
> InviteMessage get_invite_message(user_id, message_type, slot)

Get Invite Message

Returns a single Invite Message. This returns the exact same information but less than `getInviteMessages`. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.invite_message import InviteMessage
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_type = "message" # str | 
    slot = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Invite Message
        api_response = api_instance.get_invite_message(user_id, message_type, slot)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->get_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_type** | **str**|  |
 **slot** | **int**|  |

### Return type

[**InviteMessage**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single InviteMessage object. |  -  |
**400** | Error response when trying to get an Invite Message with a negative slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |
**404** | Error response when trying to get an Invite Message with a too high slot number. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite_messages**
> [InviteMessage] get_invite_messages(user_id, message_type)

List Invite Messages

Returns a list of all the users Invite Messages. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.invite_message import InviteMessage
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_type = "message" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List Invite Messages
        api_response = api_instance.get_invite_messages(user_id, message_type)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->get_invite_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_type** | **str**|  |

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with an invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> Notification invite_user(user_id)

Invite User

Sends an invite to a user. Returns the Notification of type `invite` that was sent.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.notification import Notification
from vrchatapi.model.invite_request import InviteRequest
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    invite_request = InviteRequest(
        instance_id=InstanceID("wrld_ba913a96-fac4-4048-a062-9aa5db092812:12345~hidden(usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469)~region(eu)~nonce(27e8414a-59a0-4f3d-af1f-f27557eb49a2)"),
    ) # InviteRequest | Slot number of the Invite Message to use when inviting a user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invite User
        api_response = api_instance.invite_user(user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->invite_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invite User
        api_response = api_instance.invite_user(user_id, invite_request=invite_request)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->invite_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **invite_request** | [**InviteRequest**](InviteRequest.md)| Slot number of the Invite Message to use when inviting a user. | [optional]

### Return type

[**Notification**](Notification.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_invite**
> Notification request_invite(user_id)

Request Invite

Requests an invite from a user. Returns the Notification of type `requestInvite` that was sent.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Request Invite
        api_response = api_instance.request_invite(user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->request_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

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
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_invite_message**
> [InviteMessage] reset_invite_message(user_id, message_type, slot)

Reset Invite Message

Resets a single Invite Message back to its original message, and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Resetting a message respects the rate-limit, so it is not possible to reset within the 60 minutes countdown. Resetting it does however not set the rate-limit to 60 like when editing it. It is possible to edit it right after resetting it. Trying to edit a message before the cooldown timer expires results in a 429 \"Too Fast Error\".  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  The DELETE endpoint does not have/require any request body.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.invite_message import InviteMessage
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_type = "message" # str | 
    slot = 0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reset Invite Message
        api_response = api_instance.reset_invite_message(user_id, message_type, slot)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->reset_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_type** | **str**|  |
 **slot** | **int**|  |

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with an invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |
**404** | Error response when trying to reset an Invite Message whos slot doesn&#39;t exist. |  -  |
**429** | Error response when trying to update an Invite Message before the cooldown has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_invite**
> Notification respond_invite(notification_id)

Respond Invite

Respond to an invite request by sending a world invite to the requesting user. `:notificationId` is the ID of the requesting notification.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.notification import Notification
from vrchatapi.model.invite_response import InviteResponse
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
    api_instance = invite_api.InviteApi(api_client)
    notification_id = "notificationId_example" # str | 
    invite_response = InviteResponse(
        response_slot=0,
    ) # InviteResponse | Instance ID when inviting a user. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Respond Invite
        api_response = api_instance.respond_invite(notification_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->respond_invite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Respond Invite
        api_response = api_instance.respond_invite(notification_id, invite_response=invite_response)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->respond_invite: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  |
 **invite_response** | [**InviteResponse**](InviteResponse.md)| Instance ID when inviting a user. | [optional]

### Return type

[**Notification**](Notification.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**400** | Error response when trying to respond to an invite and something went wrong. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invite_message**
> [InviteMessage] update_invite_message(user_id, message_type, slot)

Update Invite Message

Updates a single Invite Message and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Updating a message automatically sets the cooldown timer to 60 minutes. Trying to edit a message before the cooldown timer expires results in a 429 \"Too Fast Error\".  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):

```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.update_invite_message_request import UpdateInviteMessageRequest
from vrchatapi.model.invite_message import InviteMessage
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
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_type = "message" # str | 
    slot = 0 # int | 
    update_invite_message_request = UpdateInviteMessageRequest(
        message="message_example",
    ) # UpdateInviteMessageRequest | Message of what to set the invite message to. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Invite Message
        api_response = api_instance.update_invite_message(user_id, message_type, slot)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->update_invite_message: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Invite Message
        api_response = api_instance.update_invite_message(user_id, message_type, slot, update_invite_message_request=update_invite_message_request)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->update_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_type** | **str**|  |
 **slot** | **int**|  |
 **update_invite_message_request** | [**UpdateInviteMessageRequest**](UpdateInviteMessageRequest.md)| Message of what to set the invite message to. | [optional]

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with an invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |
**429** | Error response when trying to update an Invite Message before the cooldown has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

