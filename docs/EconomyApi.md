# vrchatapi.EconomyApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_licenses**](EconomyApi.md#get_active_licenses) | **GET** /economy/licenses/active | Get Active Licenses
[**get_balance**](EconomyApi.md#get_balance) | **GET** /user/{userId}/balance | Get Balance
[**get_balance_earnings**](EconomyApi.md#get_balance_earnings) | **GET** /user/{userId}/balance/earnings | Get Balance Earnings
[**get_bulk_gift_purchases**](EconomyApi.md#get_bulk_gift_purchases) | **GET** /user/bulk/gift/purchases | Get Bulk Gift Purchases
[**get_current_subscriptions**](EconomyApi.md#get_current_subscriptions) | **GET** /auth/user/subscription | Get Current Subscriptions
[**get_economy_account**](EconomyApi.md#get_economy_account) | **GET** /user/{userId}/economy/account | Get Economy Account
[**get_license_group**](EconomyApi.md#get_license_group) | **GET** /licenseGroups/{licenseGroupId} | Get License Group
[**get_product_listing**](EconomyApi.md#get_product_listing) | **GET** /listing/{productId} | Get Product Listing
[**get_product_listing_alternate**](EconomyApi.md#get_product_listing_alternate) | **GET** /products/{productId} | Get Product Listing (alternate)
[**get_product_listings**](EconomyApi.md#get_product_listings) | **GET** /user/{userId}/listings | Get User Product Listings
[**get_product_purchases**](EconomyApi.md#get_product_purchases) | **GET** /economy/purchases | Get Product Purchases
[**get_recent_subscription**](EconomyApi.md#get_recent_subscription) | **GET** /user/subscription/recent | Get Recent Subscription
[**get_steam_transaction**](EconomyApi.md#get_steam_transaction) | **GET** /Steam/transactions/{transactionId} | Get Steam Transaction
[**get_steam_transactions**](EconomyApi.md#get_steam_transactions) | **GET** /Steam/transactions | List Steam Transactions
[**get_store**](EconomyApi.md#get_store) | **GET** /economy/store | Get Store
[**get_store_shelves**](EconomyApi.md#get_store_shelves) | **GET** /economy/store/shelves | Get Store Shelves
[**get_subscriptions**](EconomyApi.md#get_subscriptions) | **GET** /subscriptions | List Subscriptions
[**get_tilia_status**](EconomyApi.md#get_tilia_status) | **GET** /tilia/status | Get Tilia Status
[**get_tilia_tos**](EconomyApi.md#get_tilia_tos) | **GET** /user/{userId}/tilia/tos | Get Tilia TOS Agreement Status
[**get_token_bundles**](EconomyApi.md#get_token_bundles) | **GET** /tokenBundles | List Token Bundles
[**get_user_credits_eligible**](EconomyApi.md#get_user_credits_eligible) | **GET** /users/{userId}/credits/eligible | Get User Credits Eligiblity
[**get_user_subscription_eligible**](EconomyApi.md#get_user_subscription_eligible) | **GET** /users/{userId}/subscription/eligible | Get User Subscription Eligiblity
[**purchase_product_listing**](EconomyApi.md#purchase_product_listing) | **POST** /economy/purchase/listing | Purchase Product Listing
[**update_tilia_tos**](EconomyApi.md#update_tilia_tos) | **PUT** /user/{userId}/tilia/tos | Update Tilia TOS Agreement Status


# **get_active_licenses**
> list[License] get_active_licenses()

Get Active Licenses

Gets active licenses

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # Get Active Licenses
        api_response = api_instance.get_active_licenses()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_active_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[License]**](License.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of License objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> Balance get_balance(user_id)

Get Balance

Gets the balance of a user

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Balance
        api_response = api_instance.get_balance(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_balance: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_earnings**
> Balance get_balance_earnings(user_id)

Get Balance Earnings

Gets the balance of a user from earnings

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Balance Earnings
        api_response = api_instance.get_balance_earnings(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_balance_earnings: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_gift_purchases**
> list[object] get_bulk_gift_purchases(most_recent=most_recent)

Get Bulk Gift Purchases

Get bulk gift purchases made by the user.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    most_recent = True # bool |  (optional)

    try:
        # Get Bulk Gift Purchases
        api_response = api_instance.get_bulk_gift_purchases(most_recent=most_recent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_bulk_gift_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **most_recent** | **bool**|  | [optional] 

### Return type

**list[object]**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of ??? objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_subscriptions**
> list[UserSubscription] get_current_subscriptions()

Get Current Subscriptions

Get a list of all current user subscriptions.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # Get Current Subscriptions
        api_response = api_instance.get_current_subscriptions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_current_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserSubscription]**](UserSubscription.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of UserSubscription objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economy_account**
> EconomyAccount get_economy_account(user_id)

Get Economy Account

Gets the economy account of a user

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Economy Account
        api_response = api_instance.get_economy_account(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_economy_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**EconomyAccount**](EconomyAccount.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single EconomyAccount object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_group**
> LicenseGroup get_license_group(license_group_id)

Get License Group

Get a single License Group by given ID.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    license_group_id = 'license_group_id_example' # str | Must be a valid license group ID.

    try:
        # Get License Group
        api_response = api_instance.get_license_group(license_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_license_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_group_id** | **str**| Must be a valid license group ID. | 

### Return type

[**LicenseGroup**](LicenseGroup.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single LicenseGroup object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_listing**
> ProductListing get_product_listing(product_id, hydrate=hydrate)

Get Product Listing

Gets a product listing

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
    api_instance = vrchatapi.EconomyApi(api_client)
    product_id = 'product_id_example' # str | Must be a valid product ID.
hydrate = True # bool | Populates some fields and changes types of others for certain objects. (optional)

    try:
        # Get Product Listing
        api_response = api_instance.get_product_listing(product_id, hydrate=hydrate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 
 **hydrate** | **bool**| Populates some fields and changes types of others for certain objects. | [optional] 

### Return type

[**ProductListing**](ProductListing.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductListing object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_listing_alternate**
> ProductListing get_product_listing_alternate(product_id)

Get Product Listing (alternate)

Gets a product listing

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
    api_instance = vrchatapi.EconomyApi(api_client)
    product_id = 'product_id_example' # str | Must be a valid product ID.

    try:
        # Get Product Listing (alternate)
        api_response = api_instance.get_product_listing_alternate(product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_listing_alternate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 

### Return type

[**ProductListing**](ProductListing.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductListing object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_listings**
> list[ProductListing] get_product_listings(user_id, n=n, offset=offset, hydrate=hydrate, group_id=group_id, active=active)

Get User Product Listings

Gets the product listings of a given user

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
hydrate = True # bool | Populates some fields and changes types of others for certain objects. (optional)
group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID. (optional)
active = True # bool | Filter for users' listings and inventory bundles. (optional)

    try:
        # Get User Product Listings
        api_response = api_instance.get_product_listings(user_id, n=n, offset=offset, hydrate=hydrate, group_id=group_id, active=active)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_listings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **hydrate** | **bool**| Populates some fields and changes types of others for certain objects. | [optional] 
 **group_id** | **str**| Must be a valid group ID. | [optional] 
 **active** | **bool**| Filter for users&#39; listings and inventory bundles. | [optional] 

### Return type

[**list[ProductListing]**](ProductListing.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of ProductListing objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchases**
> list[ProductPurchase] get_product_purchases(buyer_id, n=n, offset=offset, most_recent=most_recent, sort=sort, order=order)

Get Product Purchases

Gets product purchases

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
    api_instance = vrchatapi.EconomyApi(api_client)
    buyer_id = 'buyer_id_example' # str | Must be a valid user ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
most_recent = True # bool |  (optional)
sort = vrchatapi.SortOptionProductPurchase() # SortOptionProductPurchase | The sort order of the results. (optional)
order = vrchatapi.OrderOptionShort() # OrderOptionShort | Result ordering (optional)

    try:
        # Get Product Purchases
        api_response = api_instance.get_product_purchases(buyer_id, n=n, offset=offset, most_recent=most_recent, sort=sort, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| Must be a valid user ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **most_recent** | **bool**|  | [optional] 
 **sort** | [**SortOptionProductPurchase**](.md)| The sort order of the results. | [optional] 
 **order** | [**OrderOptionShort**](.md)| Result ordering | [optional] 

### Return type

[**list[ProductPurchase]**](ProductPurchase.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of ProductPurchase objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_subscription**
> UserSubscription get_recent_subscription()

Get Recent Subscription

Get the most recent user subscription.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # Get Recent Subscription
        api_response = api_instance.get_recent_subscription()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_recent_subscription: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSubscription**](UserSubscription.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a UserSubscription object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_steam_transaction**
> Transaction get_steam_transaction(transaction_id)

Get Steam Transaction

Get a single Steam transactions by ID. This returns the exact same information as `getSteamTransactions`, so no point in using this endpoint.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    transaction_id = 'transaction_id_example' # str | Must be a valid transaction ID.

    try:
        # Get Steam Transaction
        api_response = api_instance.get_steam_transaction(transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_steam_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| Must be a valid transaction ID. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Transaction object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_steam_transactions**
> list[Transaction] get_steam_transactions()

List Steam Transactions

Get all own Steam transactions.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # List Steam Transactions
        api_response = api_instance.get_steam_transactions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_steam_transactions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Transaction objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store**
> Store get_store(store_id, hydrate_listings=hydrate_listings, hydrate_products=hydrate_products)

Get Store

Gets a store

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
    api_instance = vrchatapi.EconomyApi(api_client)
    store_id = 'store_id_example' # str | 
hydrate_listings = True # bool | Listings fields will be populated. (optional)
hydrate_products = True # bool | Products fields will be populated. (optional)

    try:
        # Get Store
        api_response = api_instance.get_store(store_id, hydrate_listings=hydrate_listings, hydrate_products=hydrate_products)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **hydrate_listings** | **bool**| Listings fields will be populated. | [optional] 
 **hydrate_products** | **bool**| Products fields will be populated. | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Store object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_shelves**
> list[StoreShelf] get_store_shelves(store_id, hydrate_listings=hydrate_listings, fetch=fetch)

Get Store Shelves

Gets the shelves for a store

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
    api_instance = vrchatapi.EconomyApi(api_client)
    store_id = 'store_id_example' # str | 
hydrate_listings = True # bool | Listings fields will be populated. (optional)
fetch = vrchatapi.StoreView() # StoreView |  (optional)

    try:
        # Get Store Shelves
        api_response = api_instance.get_store_shelves(store_id, hydrate_listings=hydrate_listings, fetch=fetch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_store_shelves: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  | 
 **hydrate_listings** | **bool**| Listings fields will be populated. | [optional] 
 **fetch** | [**StoreView**](.md)|  | [optional] 

### Return type

[**list[StoreShelf]**](StoreShelf.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of StoreShelf objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> list[Subscription] get_subscriptions()

List Subscriptions

List all existing Subscriptions. For example, \"vrchatplus-monthly\" and \"vrchatplus-yearly\".

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # List Subscriptions
        api_response = api_instance.get_subscriptions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_subscriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Subscription objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tilia_status**
> TiliaStatus get_tilia_status()

Get Tilia Status

Gets the status of Tilia integration

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # Get Tilia Status
        api_response = api_instance.get_tilia_status()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_tilia_status: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tilia_tos**
> TiliaTOS get_tilia_tos(user_id)

Get Tilia TOS Agreement Status

Gets the status of the agreement of a user to the Tilia TOS

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Tilia TOS Agreement Status
        api_response = api_instance.get_tilia_tos(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_tilia_tos: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_bundles**
> list[TokenBundle] get_token_bundles()

List Token Bundles

Gets the list of token bundles

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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # List Token Bundles
        api_response = api_instance.get_token_bundles()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_token_bundles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TokenBundle]**](TokenBundle.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of TokenBundle objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_credits_eligible**
> UserCreditsEligible get_user_credits_eligible(user_id, subscription_id)

Get User Credits Eligiblity

Get the user's eligibility status for subscriptions based on available credits.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
subscription_id = 'subscription_id_example' # str | 

    try:
        # Get User Credits Eligiblity
        api_response = api_instance.get_user_credits_eligible(user_id, subscription_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_user_credits_eligible: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscription_eligible**
> UserSubscriptionEligible get_user_subscription_eligible(user_id, steam_id=steam_id)

Get User Subscription Eligiblity

Get the user's eligibility status for subscriptions.

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
steam_id = 'game night' # str | The Steam ID of the user. (optional)

    try:
        # Get User Subscription Eligiblity
        api_response = api_instance.get_user_subscription_eligible(user_id, steam_id=steam_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_user_subscription_eligible: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **steam_id** | **str**| The Steam ID of the user. | [optional] 

### Return type

[**UserSubscriptionEligible**](UserSubscriptionEligible.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single UserSubscriptionEligible object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_product_listing**
> ProductPurchase purchase_product_listing(purchase_product_listing_request=purchase_product_listing_request)

Purchase Product Listing

Purchases a product listing

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
    api_instance = vrchatapi.EconomyApi(api_client)
    purchase_product_listing_request = vrchatapi.PurchaseProductListingRequest() # PurchaseProductListingRequest |  (optional)

    try:
        # Purchase Product Listing
        api_response = api_instance.purchase_product_listing(purchase_product_listing_request=purchase_product_listing_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->purchase_product_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_product_listing_request** | [**PurchaseProductListingRequest**](PurchaseProductListingRequest.md)|  | [optional] 

### Return type

[**ProductPurchase**](ProductPurchase.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductPurchase object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tilia_tos**
> object update_tilia_tos(user_id, update_tilia_tos_request=update_tilia_tos_request)

Update Tilia TOS Agreement Status

Updates the status of the agreement of a user to the Tilia TOS

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
update_tilia_tos_request = vrchatapi.UpdateTiliaTOSRequest() # UpdateTiliaTOSRequest |  (optional)

    try:
        # Update Tilia TOS Agreement Status
        api_response = api_instance.update_tilia_tos(user_id, update_tilia_tos_request=update_tilia_tos_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->update_tilia_tos: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

