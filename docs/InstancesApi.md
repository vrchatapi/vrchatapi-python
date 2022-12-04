# vrchatapi.InstancesApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instance**](InstancesApi.md#get_instance) | **GET** /instances/{worldId}:{instanceId} | Get Instance
[**get_instance_by_short_name**](InstancesApi.md#get_instance_by_short_name) | **GET** /instances/s/{shortName} | Get Instance By Short Name
[**get_short_name**](InstancesApi.md#get_short_name) | **GET** /instances/{worldId}:{instanceId}/shortName | Get Instance Short Name
[**send_self_invite**](InstancesApi.md#send_self_invite) | **POST** /instances/{worldId}:{instanceId}/invite | Send Self Invite


# **get_instance**
> Instance get_instance(world_id, instance_id)

Get Instance

Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.  If an invalid instanceId is provided, this endpoint will simply return \"null\"!

### Example

* Api Key Authentication (apiKeyCookie):
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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Get Instance
        api_response = api_instance.get_instance(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_instance: %s\n" % e)
```

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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Get Instance
        api_response = api_instance.get_instance(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_instance: %s\n" % e)
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

# **get_instance_by_short_name**
> Instance get_instance_by_short_name(short_name)

Get Instance By Short Name

Returns an instance. Please read [Instances Tutorial](https://vrchatapi.github.io/tutorials/instances/) for more information on Instances.

### Example

* Api Key Authentication (apiKeyCookie):
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
    api_instance = vrchatapi.InstancesApi(api_client)
    short_name = 'short_name_example' # str | 

    try:
        # Get Instance By Short Name
        api_response = api_instance.get_instance_by_short_name(short_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_instance_by_short_name: %s\n" % e)
```

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
    api_instance = vrchatapi.InstancesApi(api_client)
    short_name = 'short_name_example' # str | 

    try:
        # Get Instance By Short Name
        api_response = api_instance.get_instance_by_short_name(short_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_instance_by_short_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_name** | **str**|  | 

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
**404** | Error response due to non existant instance |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_short_name**
> InstanceShortNameResponse get_short_name(world_id, instance_id)

Get Instance Short Name

Returns an instance short name.

### Example

* Api Key Authentication (apiKeyCookie):
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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Get Instance Short Name
        api_response = api_instance.get_short_name(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_short_name: %s\n" % e)
```

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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Get Instance Short Name
        api_response = api_instance.get_short_name(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->get_short_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  | 
 **instance_id** | **str**|  | 

### Return type

[**InstanceShortNameResponse**](InstanceShortNameResponse.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an instance secureName and/or shortName. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_self_invite**
> Success send_self_invite(world_id, instance_id)

Send Self Invite

Sends an invite to the instance to yourself.

### Example

* Api Key Authentication (apiKeyCookie):
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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Send Self Invite
        api_response = api_instance.send_self_invite(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->send_self_invite: %s\n" % e)
```

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
    api_instance = vrchatapi.InstancesApi(api_client)
    world_id = 'world_id_example' # str | 
instance_id = 'instance_id_example' # str | 

    try:
        # Send Self Invite
        api_response = api_instance.send_self_invite(world_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InstancesApi->send_self_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **world_id** | **str**|  | 
 **instance_id** | **str**|  | 

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
**200** | Success response after sending an invite to yourself to the instance. |  -  |
**401** | Error response due to missing apiKey or auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

