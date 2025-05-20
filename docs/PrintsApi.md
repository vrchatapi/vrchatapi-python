# vrchatapi.PrintsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_print**](PrintsApi.md#delete_print) | **DELETE** /prints/{printId} | Delete Print
[**edit_print**](PrintsApi.md#edit_print) | **POST** /prints/{printId} | Edit Print
[**get_print**](PrintsApi.md#get_print) | **GET** /prints/{printId} | Get Print
[**get_user_prints**](PrintsApi.md#get_user_prints) | **GET** /prints/user/{userId} | Get Own Prints
[**upload_print**](PrintsApi.md#upload_print) | **POST** /prints | Upload Print


# **delete_print**
> delete_print(print_id)

Delete Print

Returns a print.

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
    api_instance = vrchatapi.PrintsApi(api_client)
    print_id = 'prnt_0a0aa0a0-85ea-42eb-b2f7-4840d7f341fa' # str | Print ID.

    try:
        # Delete Print
        api_instance.delete_print(print_id)
    except ApiException as e:
        print("Exception when calling PrintsApi->delete_print: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_id** | **str**| Print ID. | 

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
**200** | Empty response if successful |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_print**
> ModelPrint edit_print(print_id, image, note=note)

Edit Print

Edits a print.

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
    api_instance = vrchatapi.PrintsApi(api_client)
    print_id = 'prnt_0a0aa0a0-85ea-42eb-b2f7-4840d7f341fa' # str | Print ID.
image = '/path/to/file' # file | The binary blob of the png file.
note = 'note_example' # str | The caption for the image. (optional)

    try:
        # Edit Print
        api_response = api_instance.edit_print(print_id, image, note=note)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->edit_print: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_id** | **str**| Print ID. | 
 **image** | **file**| The binary blob of the png file. | 
 **note** | **str**| The caption for the image. | [optional] 

### Return type

[**ModelPrint**](ModelPrint.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Print object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_print**
> ModelPrint get_print(print_id)

Get Print

Returns a print.

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
    api_instance = vrchatapi.PrintsApi(api_client)
    print_id = 'prnt_0a0aa0a0-85ea-42eb-b2f7-4840d7f341fa' # str | Print ID.

    try:
        # Get Print
        api_response = api_instance.get_print(print_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->get_print: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_id** | **str**| Print ID. | 

### Return type

[**ModelPrint**](ModelPrint.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Print object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_prints**
> list[ModelPrint] get_user_prints(user_id)

Get Own Prints

Returns a list of all prints of the user. User id has to be your own userId, as you can't request other user's prints.

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
    api_instance = vrchatapi.PrintsApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Own Prints
        api_response = api_instance.get_user_prints(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->get_user_prints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**list[ModelPrint]**](ModelPrint.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Print objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to request another user&#39;s prints. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_print**
> ModelPrint upload_print(image, timestamp, note=note, world_id=world_id, world_name=world_name)

Upload Print

Uploads and creates a print.

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
    api_instance = vrchatapi.PrintsApi(api_client)
    image = '/path/to/file' # file | The binary blob of the png file.
timestamp = '2013-10-20T19:20:30+01:00' # datetime | The time the image was captured.
note = 'note_example' # str | The caption for the image. (optional)
world_id = 'world_id_example' # str | The id of the world in which the image was captured. (optional)
world_name = 'world_name_example' # str | The name of the world in which the image was captured. (optional)

    try:
        # Upload Print
        api_response = api_instance.upload_print(image, timestamp, note=note, world_id=world_id, world_name=world_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PrintsApi->upload_print: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| The binary blob of the png file. | 
 **timestamp** | **datetime**| The time the image was captured. | 
 **note** | **str**| The caption for the image. | [optional] 
 **world_id** | **str**| The id of the world in which the image was captured. | [optional] 
 **world_name** | **str**| The name of the world in which the image was captured. | [optional] 

### Return type

[**ModelPrint**](ModelPrint.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Print object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

