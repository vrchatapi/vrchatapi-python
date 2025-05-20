# vrchatapi.InviteApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invite_message**](InviteApi.md#get_invite_message) | **GET** /message/{userId}/{messageType}/{slot} | Get Invite Message
[**get_invite_messages**](InviteApi.md#get_invite_messages) | **GET** /message/{userId}/{messageType} | List Invite Messages
[**invite_myself_to**](InviteApi.md#invite_myself_to) | **POST** /invite/myself/to/{worldId}:{instanceId} | Invite Myself To Instance
[**invite_user**](InviteApi.md#invite_user) | **POST** /invite/{userId} | Invite User
[**invite_user_with_photo**](InviteApi.md#invite_user_with_photo) | **POST** /invite/{userId}/photo | Invite User with photo
[**request_invite**](InviteApi.md#request_invite) | **POST** /requestInvite/{userId} | Request Invite
[**request_invite_with_photo**](InviteApi.md#request_invite_with_photo) | **POST** /requestInvite/{userId}/photo | Request Invite with photo
[**reset_invite_message**](InviteApi.md#reset_invite_message) | **DELETE** /message/{userId}/{messageType}/{slot} | Reset Invite Message
[**respond_invite**](InviteApi.md#respond_invite) | **POST** /invite/{notificationId}/response | Respond Invite
[**respond_invite_with_photo**](InviteApi.md#respond_invite_with_photo) | **POST** /invite/{notificationId}/response/photo | Respond Invite with photo
[**update_invite_message**](InviteApi.md#update_invite_message) | **PUT** /message/{userId}/{messageType}/{slot} | Update Invite Message


# **get_invite_message**
> InviteMessage get_invite_message(user_id, message_type, slot)

Get Invite Message

Returns a single Invite Message. This returns the exact same information but less than `getInviteMessages`. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
message_type = vrchatapi.InviteMessageType() # InviteMessageType | The type of message to fetch, must be a valid InviteMessageType.
slot = 56 # int | The message slot to fetch of a given message type.

    try:
        # Get Invite Message
        api_response = api_instance.get_invite_message(user_id, message_type, slot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->get_invite_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **message_type** | [**InviteMessageType**](.md)| The type of message to fetch, must be a valid InviteMessageType. | 
 **slot** | **int**| The message slot to fetch of a given message type. | 

### Return type

[**InviteMessage**](InviteMessage.md)

### Authorization

[authCookie](../README.md#authCookie)

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
> list[InviteMessage] get_invite_messages(user_id, message_type)

List Invite Messages

Returns a list of all the users Invite Messages. Admin Credentials are required to view messages of other users!  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
message_type = vrchatapi.InviteMessageType() # InviteMessageType | The type of message to fetch, must be a valid InviteMessageType.

    try:
        # List Invite Messages
        api_response = api_instance.get_invite_messages(user_id, message_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->get_invite_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **message_type** | [**InviteMessageType**](.md)| The type of message to fetch, must be a valid InviteMessageType. | 

### Return type

[**list[InviteMessage]**](InviteMessage.md)

### Authorization

[authCookie](../README.md#authCookie)

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

# **invite_myself_to**
> SentNotification invite_myself_to(world_id, instance_id)

Invite Myself To Instance

Sends self an invite to an instance

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
    api_instance = vrchatapi.InviteApi(api_client)
    world_id = 'world_id_example' # str | Must be a valid world ID.
instance_id = 'instance_id_example' # str | Must be a valid instance ID.

    try:
        # Invite Myself To Instance
        api_response = api_instance.invite_myself_to(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->invite_myself_to: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**| Must be a valid world ID. | 
 **instance_id** | **str**| Must be a valid instance ID. | 

### Return type

[**SentNotification**](SentNotification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single SentNotifcation object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response due to non existant instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> SentNotification invite_user(user_id, invite_request)

Invite User

Sends an invite to a user. Returns the Notification of type `invite` that was sent.

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
invite_request = vrchatapi.InviteRequest() # InviteRequest | Slot number of the Invite Message to use when inviting a user.

    try:
        # Invite User
        api_response = api_instance.invite_user(user_id, invite_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->invite_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **invite_request** | [**InviteRequest**](InviteRequest.md)| Slot number of the Invite Message to use when inviting a user. | 

### Return type

[**SentNotification**](SentNotification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single SentNotifcation object. |  -  |
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_with_photo**
> SentNotification invite_user_with_photo(user_id, image, data)

Invite User with photo

Sends an photo invite to a user. Returns the Notification of type `invite` that was sent.

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
image = '/path/to/file' # file | The binary blob of the png file.
data = vrchatapi.InviteRequest() # InviteRequest | 

    try:
        # Invite User with photo
        api_response = api_instance.invite_user_with_photo(user_id, image, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->invite_user_with_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **image** | **file**| The binary blob of the png file. | 
 **data** | [**InviteRequest**](InviteRequest.md)|  | 

### Return type

[**SentNotification**](SentNotification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single SentNotifcation object. |  -  |
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_invite**
> Notification request_invite(user_id, request_invite_request=request_invite_request)

Request Invite

Requests an invite from a user. Returns the Notification of type `requestInvite` that was sent.

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
request_invite_request = vrchatapi.RequestInviteRequest() # RequestInviteRequest | Slot number of the Request Message to use when request an invite. (optional)

    try:
        # Request Invite
        api_response = api_instance.request_invite(user_id, request_invite_request=request_invite_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->request_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **request_invite_request** | [**RequestInviteRequest**](RequestInviteRequest.md)| Slot number of the Request Message to use when request an invite. | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_invite_with_photo**
> Notification request_invite_with_photo(user_id, image, data)

Request Invite with photo

Requests with photo an invite from a user. Returns the Notification of type `requestInvite` that was sent.

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
image = '/path/to/file' # file | The binary blob of the png file.
data = vrchatapi.RequestInviteRequest() # RequestInviteRequest | 

    try:
        # Request Invite with photo
        api_response = api_instance.request_invite_with_photo(user_id, image, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->request_invite_with_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **image** | **file**| The binary blob of the png file. | 
 **data** | [**RequestInviteRequest**](RequestInviteRequest.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**403** | Error response when trying to invite someome whom you are not friends with. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_invite_message**
> list[InviteMessage] reset_invite_message(user_id, message_type, slot)

Reset Invite Message

Resets a single Invite Message back to its original message, and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Resetting a message respects the rate-limit, so it is not possible to reset within the 60 minutes countdown. Resetting it does however not set the rate-limit to 60 like when editing it. It is possible to edit it right after resetting it. Trying to edit a message before the cooldown timer expires results in a 429 \"Too Fast Error\".  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite  The DELETE endpoint does not have/require any request body.

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
message_type = vrchatapi.InviteMessageType() # InviteMessageType | The type of message to fetch, must be a valid InviteMessageType.
slot = 56 # int | The message slot to fetch of a given message type.

    try:
        # Reset Invite Message
        api_response = api_instance.reset_invite_message(user_id, message_type, slot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->reset_invite_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **message_type** | [**InviteMessageType**](.md)| The type of message to fetch, must be a valid InviteMessageType. | 
 **slot** | **int**| The message slot to fetch of a given message type. | 

### Return type

[**list[InviteMessage]**](InviteMessage.md)

### Authorization

[authCookie](../README.md#authCookie)

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
> Notification respond_invite(notification_id, invite_response)

Respond Invite

Respond to an invite or invite request without accepting it. `:notificationId` is the ID of the requesting notification.  In case the notification being replied to is an invite, the `responseSlot` refers to a response message from the the `message` collection. In case the notification is an invite request, it will refer to one from the `requestResponse` collection instead.

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
    api_instance = vrchatapi.InviteApi(api_client)
    notification_id = 'notification_id_example' # str | Must be a valid notification ID.
invite_response = vrchatapi.InviteResponse() # InviteResponse | Slot number of the Response Message to use when responding to a user.

    try:
        # Respond Invite
        api_response = api_instance.respond_invite(notification_id, invite_response)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->respond_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Must be a valid notification ID. | 
 **invite_response** | [**InviteResponse**](InviteResponse.md)| Slot number of the Response Message to use when responding to a user. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**400** | Error response when trying to respond to an invite and something went wrong. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_invite_with_photo**
> Notification respond_invite_with_photo(notification_id, image, data)

Respond Invite with photo

Respond with photo to an invite or invite request without accepting it. `:notificationId` is the ID of the requesting notification.  In case the notification being replied to is an invite, the `responseSlot` refers to a response message from the the `message` collection. In case the notification is an invite request, it will refer to one from the `requestResponse` collection instead.'

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
    api_instance = vrchatapi.InviteApi(api_client)
    notification_id = 'notification_id_example' # str | Must be a valid notification ID.
image = '/path/to/file' # file | The binary blob of the png file.
data = vrchatapi.InviteResponse() # InviteResponse | 

    try:
        # Respond Invite with photo
        api_response = api_instance.respond_invite_with_photo(notification_id, image, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->respond_invite_with_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**| Must be a valid notification ID. | 
 **image** | **file**| The binary blob of the png file. | 
 **data** | [**InviteResponse**](InviteResponse.md)|  | 

### Return type

[**Notification**](Notification.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Notifcation object. |  -  |
**400** | Error response when trying to respond to an invite and something went wrong. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invite_message**
> list[InviteMessage] update_invite_message(user_id, message_type, slot, update_invite_message_request=update_invite_message_request)

Update Invite Message

Updates a single Invite Message and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Updating a message automatically sets the cooldown timer to 60 minutes. Trying to edit a message before the cooldown timer expires results in a 429 \"Too Fast Error\".  Message type refers to a different collection of messages, used during different types of responses.  * `message` = Message during a normal invite * `response` = Message when replying to a message * `request` = Message when requesting an invite * `requestResponse` = Message when replying to a request for invite

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
    api_instance = vrchatapi.InviteApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
message_type = vrchatapi.InviteMessageType() # InviteMessageType | The type of message to fetch, must be a valid InviteMessageType.
slot = 56 # int | The message slot to fetch of a given message type.
update_invite_message_request = vrchatapi.UpdateInviteMessageRequest() # UpdateInviteMessageRequest | Message of what to set the invite message to. (optional)

    try:
        # Update Invite Message
        api_response = api_instance.update_invite_message(user_id, message_type, slot, update_invite_message_request=update_invite_message_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InviteApi->update_invite_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **message_type** | [**InviteMessageType**](.md)| The type of message to fetch, must be a valid InviteMessageType. | 
 **slot** | **int**| The message slot to fetch of a given message type. | 
 **update_invite_message_request** | [**UpdateInviteMessageRequest**](UpdateInviteMessageRequest.md)| Message of what to set the invite message to. | [optional] 

### Return type

[**list[InviteMessage]**](InviteMessage.md)

### Authorization

[authCookie](../README.md#authCookie)

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

