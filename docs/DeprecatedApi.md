# vrchatapi.DeprecatedApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_earnings**](DeprecatedApi.md#get_balance_earnings) | **GET** /user/{userId}/balance/earnings | Get Balance Earnings
[**get_prop_publish_status**](DeprecatedApi.md#get_prop_publish_status) | **GET** /props/{propId}/publish | Get Prop Publish Status
[**get_seller_eligibility**](DeprecatedApi.md#get_seller_eligibility) | **GET** /economy/seller/eligibility | Get Seller Eligibility
[**get_tilia_status**](DeprecatedApi.md#get_tilia_status) | **GET** /tilia/status | Get Tilia Status
[**get_tilia_tos**](DeprecatedApi.md#get_tilia_tos) | **GET** /user/{userId}/tilia/tos | Get Tilia TOS Agreement Status
[**get_user_credits_eligible**](DeprecatedApi.md#get_user_credits_eligible) | **GET** /users/{userId}/credits/eligible | Get User Credits Eligibility
[**publish_prop**](DeprecatedApi.md#publish_prop) | **PUT** /props/{propId}/publish | Publish Prop
[**unpublish_prop**](DeprecatedApi.md#unpublish_prop) | **DELETE** /props/{propId}/publish | Unpublish Prop
[**update_tilia_tos**](DeprecatedApi.md#update_tilia_tos) | **PUT** /user/{userId}/tilia/tos | Update Tilia TOS Agreement Status


# **get_balance_earnings**
> Balance get_balance_earnings(user_id)

Get Balance Earnings

Return the user's balance from earnings.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Balance Earnings
        api_response = api_instance.get_balance_earnings(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_balance_earnings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**Balance**](Balance.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Balance object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prop_publish_status**
> PropPublishStatus get_prop_publish_status(prop_id)

Get Prop Publish Status

Return the PropPublishStatus object. `/props/{propId}` is still served.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    prop_id = 'prop_id_example' # str | Prop ID.

    try:
        # Get Prop Publish Status
        api_response = api_instance.get_prop_publish_status(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_prop_publish_status: %s\n" % e)
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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seller_eligibility**
> SellerEligibility get_seller_eligibility()

Get Seller Eligibility

Return the current user's eligibility to become a seller.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    
    try:
        # Get Seller Eligibility
        api_response = api_instance.get_seller_eligibility()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_seller_eligibility: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SellerEligibility**](SellerEligibility.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single SellerEligibility object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tilia_status**
> TiliaStatus get_tilia_status()

Get Tilia Status

Return the Tilia integration status.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    
    try:
        # Get Tilia Status
        api_response = api_instance.get_tilia_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_tilia_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TiliaStatus**](TiliaStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single TiliaStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tilia_tos**
> TiliaTOS get_tilia_tos(user_id)

Get Tilia TOS Agreement Status

Return the user's Tilia TOS agreement status.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Tilia TOS Agreement Status
        api_response = api_instance.get_tilia_tos(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_tilia_tos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**TiliaTOS**](TiliaTOS.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single TiliaTOS object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_credits_eligible**
> UserCreditsEligible get_user_credits_eligible(user_id, subscription_id)

Get User Credits Eligibility

Return the user's subscription credit eligibility.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
subscription_id = 'subscription_id_example' # str | 

    try:
        # Get User Credits Eligibility
        api_response = api_instance.get_user_credits_eligible(user_id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->get_user_credits_eligible: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **subscription_id** | **str**|  | 

### Return type

[**UserCreditsEligible**](UserCreditsEligible.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single UserCreditsEligible object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_prop**
> PropPublishStatus publish_prop(prop_id)

Publish Prop

Publish a prop and return the updated PropPublishStatus object. `/props/{propId}` is still served.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    prop_id = 'prop_id_example' # str | Prop ID.

    try:
        # Publish Prop
        api_response = api_instance.publish_prop(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->publish_prop: %s\n" % e)
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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unpublish_prop**
> PropPublishStatus unpublish_prop(prop_id)

Unpublish Prop

Unpublish a prop and return the updated PropPublishStatus object. `/props/{propId}` is still served.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    prop_id = 'prop_id_example' # str | Prop ID.

    try:
        # Unpublish Prop
        api_response = api_instance.unpublish_prop(prop_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->unpublish_prop: %s\n" % e)
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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tilia_tos**
> object update_tilia_tos(user_id, update_tilia_tos_request=update_tilia_tos_request)

Update Tilia TOS Agreement Status

Update the user's Tilia TOS agreement status.

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
    api_instance = vrchatapi.DeprecatedApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
update_tilia_tos_request = vrchatapi.UpdateTiliaTOSRequest() # UpdateTiliaTOSRequest |  (optional)

    try:
        # Update Tilia TOS Agreement Status
        api_response = api_instance.update_tilia_tos(user_id, update_tilia_tos_request=update_tilia_tos_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeprecatedApi->update_tilia_tos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **update_tilia_tos_request** | [**UpdateTiliaTOSRequest**](UpdateTiliaTOSRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a UserSubscription object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

