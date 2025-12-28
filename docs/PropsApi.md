# vrchatapi.PropsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_prop**](PropsApi.md#create_prop) | **POST** /props | Create Prop
[**delete_prop**](PropsApi.md#delete_prop) | **DELETE** /props/{propId} | Delete Prop
[**get_prop**](PropsApi.md#get_prop) | **GET** /props/{propId} | Get Prop
[**get_prop_publish_status**](PropsApi.md#get_prop_publish_status) | **GET** /props/{propId}/publish | Get Prop Publish Status
[**list_props**](PropsApi.md#list_props) | **GET** /props | List Props
[**publish_prop**](PropsApi.md#publish_prop) | **PUT** /props/{propId}/publish | Publish Prop
[**unpublish_prop**](PropsApi.md#unpublish_prop) | **DELETE** /props/{propId}/publish | Unpublish Prop
[**update_prop**](PropsApi.md#update_prop) | **PUT** /props/{propId} | Update Prop


# **create_prop**
> Prop create_prop(create_prop_request)

Create Prop

Create a Prop and return the new Prop object.

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
    api_instance = vrchatapi.PropsApi(api_client)
    create_prop_request = vrchatapi.CreatePropRequest() # CreatePropRequest | 

    try:
        # Create Prop
        api_response = api_instance.create_prop(create_prop_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->create_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_prop_request** | [**CreatePropRequest**](CreatePropRequest.md)|  | 

### Return type

[**Prop**](Prop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Prop object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prop**
> delete_prop(prop_id)

Delete Prop

Delete a Prop.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.

    try:
        # Delete Prop
        api_instance.delete_prop(prop_id)
    except ApiException as e:
        print("Exception when calling PropsApi->delete_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 

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
**200** | The Prop is successfully deleted. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prop**
> Prop get_prop(prop_id)

Get Prop

Returns a Prop object.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.

    try:
        # Get Prop
        api_response = api_instance.get_prop(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->get_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 

### Return type

[**Prop**](Prop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Prop object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prop_publish_status**
> PropPublishStatus get_prop_publish_status(prop_id)

Get Prop Publish Status

Returns a PropPublishStatus object.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.

    try:
        # Get Prop Publish Status
        api_response = api_instance.get_prop_publish_status(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->get_prop_publish_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 

### Return type

[**PropPublishStatus**](PropPublishStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single PropPublishStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_props**
> list[Prop] list_props(author_id, n=n, offset=offset)

List Props

Returns a list Prop objects.

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
    api_instance = vrchatapi.PropsApi(api_client)
    author_id = 'author_id_example' # str | Must be a valid user ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List Props
        api_response = api_instance.list_props(author_id, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->list_props: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **author_id** | **str**| Must be a valid user ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[Prop]**](Prop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Prop objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_prop**
> PropPublishStatus publish_prop(prop_id)

Publish Prop

Publish a Prop and return the updated PropPublishStatus object.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.

    try:
        # Publish Prop
        api_response = api_instance.publish_prop(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->publish_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 

### Return type

[**PropPublishStatus**](PropPublishStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single PropPublishStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_prop**
> PropPublishStatus unpublish_prop(prop_id)

Unpublish Prop

Unpublish a Prop and return the updated PropPublishStatus object.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.

    try:
        # Unpublish Prop
        api_response = api_instance.unpublish_prop(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->unpublish_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 

### Return type

[**PropPublishStatus**](PropPublishStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single PropPublishStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prop**
> Prop update_prop(prop_id, update_prop_request)

Update Prop

Updates a Prop and returns the updated Prop object. When updating the asset bundle, all of `name`, `assetUrl`, `platform`, `unityVersion`, `assetVersion`, `spawnType`, and `worldPlacementMask` must be present, as well as `propSignature` if this value is not blank.

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
    api_instance = vrchatapi.PropsApi(api_client)
    prop_id = 'prop_829ba6f6-b837-49d9-b9a9-056b82103b58' # str | Prop ID.
update_prop_request = vrchatapi.UpdatePropRequest() # UpdatePropRequest | 

    try:
        # Update Prop
        api_response = api_instance.update_prop(prop_id, update_prop_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PropsApi->update_prop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prop_id** | **str**| Prop ID. | 
 **update_prop_request** | [**UpdatePropRequest**](UpdatePropRequest.md)|  | 

### Return type

[**Prop**](Prop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Prop object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to perform operations on a non-existing prop. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

