# vrchatapi.PropsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_prop**](PropsApi.md#get_prop) | **GET** /props/{propId} | Get Prop


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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

