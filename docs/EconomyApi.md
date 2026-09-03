# vrchatapi.EconomyApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](EconomyApi.md#create_product) | **POST** /products | Create Product
[**create_product_listing_direct**](EconomyApi.md#create_product_listing_direct) | **POST** /listing | Create Product Listing
[**delete_product**](EconomyApi.md#delete_product) | **DELETE** /products/{productId} | Delete Product
[**delete_product_listing_direct**](EconomyApi.md#delete_product_listing_direct) | **DELETE** /listing/{productId} | Delete Product Listing
[**get_active_licenses**](EconomyApi.md#get_active_licenses) | **GET** /economy/licenses/active | Get Active Licenses
[**get_balance**](EconomyApi.md#get_balance) | **GET** /user/{userId}/balance | Get Balance
[**get_balance_earnings**](EconomyApi.md#get_balance_earnings) | **GET** /user/{userId}/balance/earnings | Get Balance Earnings
[**get_bulk_gift_purchases**](EconomyApi.md#get_bulk_gift_purchases) | **GET** /user/bulk/gift/purchases | Get Bulk Gift Purchases
[**get_current_subscriptions**](EconomyApi.md#get_current_subscriptions) | **GET** /auth/user/subscription | Get Current Subscriptions
[**get_earnings_metrics**](EconomyApi.md#get_earnings_metrics) | **GET** /economy/metrics/earnings | Get Earnings Metrics
[**get_economy_account**](EconomyApi.md#get_economy_account) | **GET** /user/{userId}/economy/account | Get Economy Account
[**get_economy_balances**](EconomyApi.md#get_economy_balances) | **GET** /user/{userId}/economy/balances | Get Economy Balances
[**get_economy_payout_status**](EconomyApi.md#get_economy_payout_status) | **GET** /user/{userId}/economy/payouts/status | Get Economy Payout Status
[**get_economy_payouts**](EconomyApi.md#get_economy_payouts) | **GET** /user/{userId}/economy/payouts/list | Get Economy Payouts
[**get_license_group**](EconomyApi.md#get_license_group) | **GET** /licenseGroups/{licenseGroupId} | Get License Group
[**get_product_listing**](EconomyApi.md#get_product_listing) | **GET** /listing/{productId} | Get Product Listing
[**get_product_listing_alternate**](EconomyApi.md#get_product_listing_alternate) | **GET** /products/{productId} | Get Product Listing (alternate)
[**get_product_listings**](EconomyApi.md#get_product_listings) | **GET** /user/{userId}/listings | Get User Product Listings
[**get_product_purchase**](EconomyApi.md#get_product_purchase) | **GET** /economy/purchases/{productPurchaseId} | Get Product Purchase
[**get_product_purchase_history**](EconomyApi.md#get_product_purchase_history) | **GET** /user/{userId}/economy/transactions | Get Product Purchase History
[**get_product_purchase_stacks**](EconomyApi.md#get_product_purchase_stacks) | **GET** /economy/purchases/{productPurchaseId}/stacks | Get Product Purchase Stacks
[**get_product_purchases**](EconomyApi.md#get_product_purchases) | **GET** /economy/purchases | Get Product Purchases
[**get_recent_subscription**](EconomyApi.md#get_recent_subscription) | **GET** /user/subscription/recent | Get Recent Subscription
[**get_seller_eligibility**](EconomyApi.md#get_seller_eligibility) | **GET** /economy/seller/eligibility | Get Seller Eligibility
[**get_steam_transaction**](EconomyApi.md#get_steam_transaction) | **GET** /Steam/transactions/{transactionId} | Get Steam Transaction
[**get_steam_transactions**](EconomyApi.md#get_steam_transactions) | **GET** /Steam/transactions | List Steam Transactions
[**get_store**](EconomyApi.md#get_store) | **GET** /economy/store | Get Store
[**get_store_shelves**](EconomyApi.md#get_store_shelves) | **GET** /economy/store/shelves | Get Store Shelves
[**get_subscriptions**](EconomyApi.md#get_subscriptions) | **GET** /subscriptions | List Subscriptions
[**get_tilia_status**](EconomyApi.md#get_tilia_status) | **GET** /tilia/status | Get Tilia Status
[**get_tilia_tos**](EconomyApi.md#get_tilia_tos) | **GET** /user/{userId}/tilia/tos | Get Tilia TOS Agreement Status
[**get_token_bundles**](EconomyApi.md#get_token_bundles) | **GET** /tokenBundles | List Token Bundles
[**get_user_credits_eligible**](EconomyApi.md#get_user_credits_eligible) | **GET** /users/{userId}/credits/eligible | Get User Credits Eligibility
[**get_user_subscription_eligible**](EconomyApi.md#get_user_subscription_eligible) | **GET** /users/{userId}/subscription/eligible | Get User Subscription Eligibility
[**get_user_tilia_kyc**](EconomyApi.md#get_user_tilia_kyc) | **GET** /user/{userId}/tilia/kyc | Get User Tilia KYC
[**list_stores**](EconomyApi.md#list_stores) | **GET** /economy/stores | List Stores
[**list_user_products**](EconomyApi.md#list_user_products) | **GET** /user/{userId}/products | List User Products
[**purchase_product_listing**](EconomyApi.md#purchase_product_listing) | **POST** /economy/purchase/listing | Purchase Product Listing
[**update_product**](EconomyApi.md#update_product) | **PUT** /products/{productId} | Update Product
[**update_product_listing_direct**](EconomyApi.md#update_product_listing_direct) | **PUT** /listing/{productId} | Update Product Listing
[**update_tilia_tos**](EconomyApi.md#update_tilia_tos) | **PUT** /user/{userId}/tilia/tos | Update Tilia TOS Agreement Status


# **create_product**
> Product create_product(create_product_request)

Create Product

Creates a product and returns the new Product object.

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
    create_product_request = vrchatapi.CreateProductRequest() # CreateProductRequest | 

    try:
        # Create Product
        api_response = api_instance.create_product(create_product_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_product_request** | [**CreateProductRequest**](CreateProductRequest.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Product object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_product_listing_direct**
> ProductListing create_product_listing_direct(create_listing_request)

Create Product Listing

Creates a listing and returns the new ProductListing object. The request body is based on observed fields and may be incomplete.

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
    create_listing_request = vrchatapi.CreateListingRequest() # CreateListingRequest | 

    try:
        # Create Product Listing
        api_response = api_instance.create_product_listing_direct(create_listing_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->create_product_listing_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_listing_request** | [**CreateListingRequest**](CreateListingRequest.md)|  | 

### Return type

[**ProductListing**](ProductListing.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductListing object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product**
> SuccessFlag delete_product(product_id)

Delete Product

Deletes a product.

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
        # Delete Product
        api_response = api_instance.delete_product(product_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 

### Return type

[**SuccessFlag**](SuccessFlag.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an SuccessFlag object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_listing_direct**
> SuccessFlag delete_product_listing_direct(product_id, hydrate=hydrate)

Delete Product Listing

Deletes a listing.

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
        # Delete Product Listing
        api_response = api_instance.delete_product_listing_direct(product_id, hydrate=hydrate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->delete_product_listing_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 
 **hydrate** | **bool**| Populates some fields and changes types of others for certain objects. | [optional] 

### Return type

[**SuccessFlag**](SuccessFlag.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an SuccessFlag object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

Return the balance of a user.

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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

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

# **get_earnings_metrics**
> EarningsMetrics get_earnings_metrics(metric_date_start=metric_date_start, metric_date_end=metric_date_end, seller_id=seller_id, group_by_duration=group_by_duration)

Get Earnings Metrics

Gets earnings totals and breakdown metrics for the currently authenticated user.

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
    metric_date_start = '2026-03-28T23:00:00.000Z' # str | Lower bound for economy metrics queries. Observed formats include both date-only and full ISO timestamps. (optional)
metric_date_end = '2026-04-04T21:59:59.999Z' # str | Upper bound for economy metrics queries. Observed formats include both date-only and full ISO timestamps. (optional)
seller_id = 'seller_id_example' # str | Filter results by seller. (optional)
group_by_duration = 'days' # str | Time bucket size for economy metrics. Observed values include `days` and `years`. (optional)

    try:
        # Get Earnings Metrics
        api_response = api_instance.get_earnings_metrics(metric_date_start=metric_date_start, metric_date_end=metric_date_end, seller_id=seller_id, group_by_duration=group_by_duration)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_earnings_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_date_start** | **str**| Lower bound for economy metrics queries. Observed formats include both date-only and full ISO timestamps. | [optional] 
 **metric_date_end** | **str**| Upper bound for economy metrics queries. Observed formats include both date-only and full ISO timestamps. | [optional] 
 **seller_id** | **str**| Filter results by seller. | [optional] 
 **group_by_duration** | **str**| Time bucket size for economy metrics. Observed values include &#x60;days&#x60; and &#x60;years&#x60;. | [optional] 

### Return type

[**EarningsMetrics**](EarningsMetrics.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single EarningsMetrics object. |  -  |
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

# **get_economy_balances**
> EconomyBalances get_economy_balances(user_id)

Get Economy Balances

Gets the combined balances for a user.

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
        # Get Economy Balances
        api_response = api_instance.get_economy_balances(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_economy_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**EconomyBalances**](EconomyBalances.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an EconomyBalances object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economy_payout_status**
> EconomyPayoutStatus get_economy_payout_status(user_id)

Get Economy Payout Status

Gets the current payout status and eligibility information for a user.

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
        # Get Economy Payout Status
        api_response = api_instance.get_economy_payout_status(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_economy_payout_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**EconomyPayoutStatus**](EconomyPayoutStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an EconomyPayoutStatus object. |  -  |
**400** | Error response when the account is not in a state that supports the request, such as an account never onboarded for payouts. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_economy_payouts**
> EconomyPayoutList get_economy_payouts(user_id)

Get Economy Payouts

Gets the payout history for a user.

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
        # Get Economy Payouts
        api_response = api_instance.get_economy_payouts(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_economy_payouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**EconomyPayoutList**](EconomyPayoutList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an EconomyPayoutList object. |  -  |
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
> list[ProductListing] get_product_listings(user_id, n=n, offset=offset, hydrate=hydrate, listing_type=listing_type, group_id=group_id, active=active)

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
listing_type = 'otp' # str | Filter user listings by category. Observed values include `otp` and `subscription`. (optional)
group_id = 'group_id_example' # str | Must be a valid group ID. (optional)
active = True # bool | Filter for users' listings and inventory bundles. (optional)

    try:
        # Get User Product Listings
        api_response = api_instance.get_product_listings(user_id, n=n, offset=offset, hydrate=hydrate, listing_type=listing_type, group_id=group_id, active=active)
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
 **listing_type** | **str**| Filter user listings by category. Observed values include &#x60;otp&#x60; and &#x60;subscription&#x60;. | [optional] 
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
**403** | Error response when requesting another user&#39;s product listings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchase**
> ProductPurchase get_product_purchase(product_purchase_id)

Get Product Purchase

Gets a single product purchase

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
    product_purchase_id = 'product_purchase_id_example' # str | Must be a valid purchase ID.

    try:
        # Get Product Purchase
        api_response = api_instance.get_product_purchase(product_purchase_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_purchase: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_purchase_id** | **str**| Must be a valid purchase ID. | 

### Return type

[**ProductPurchase**](ProductPurchase.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductPurchase object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchase_history**
> ProductPurchaseHistory get_product_purchase_history(user_id, n=n, date_min=date_min, date_max=date_max, from_user_id=from_user_id, to_user_id=to_user_id, sort=sort, order=order)

Get Product Purchase History

Gets a history of product purchases

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
date_min = '2013-10-20T19:20:30+01:00' # datetime | The start date of the search range. (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | The end date of the search range. (optional)
from_user_id = 'from_user_id_example' # str | Must be a valid user ID. (optional)
to_user_id = 'to_user_id_example' # str | Must be a valid user ID. (optional)
sort = vrchatapi.SortOptionProductPurchase() # SortOptionProductPurchase | The sort order of the results. (optional)
order = vrchatapi.OrderOptionShort() # OrderOptionShort | Result ordering (optional)

    try:
        # Get Product Purchase History
        api_response = api_instance.get_product_purchase_history(user_id, n=n, date_min=date_min, date_max=date_max, from_user_id=from_user_id, to_user_id=to_user_id, sort=sort, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_purchase_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **date_min** | **datetime**| The start date of the search range. | [optional] 
 **date_max** | **datetime**| The end date of the search range. | [optional] 
 **from_user_id** | **str**| Must be a valid user ID. | [optional] 
 **to_user_id** | **str**| Must be a valid user ID. | [optional] 
 **sort** | [**SortOptionProductPurchase**](.md)| The sort order of the results. | [optional] 
 **order** | [**OrderOptionShort**](.md)| Result ordering | [optional] 

### Return type

[**ProductPurchaseHistory**](ProductPurchaseHistory.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductPurchaseHistory object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchase_stacks**
> list[object] get_product_purchase_stacks(product_purchase_id)

Get Product Purchase Stacks

Gets stacks for a product purchase

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
    product_purchase_id = 'product_purchase_id_example' # str | Must be a valid purchase ID.

    try:
        # Get Product Purchase Stacks
        api_response = api_instance.get_product_purchase_stacks(product_purchase_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_purchase_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_purchase_id** | **str**| Must be a valid purchase ID. | 

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
**200** | Returns a list of stacks for a product purchase. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_purchases**
> list[ProductPurchase] get_product_purchases(buyer_id, seller_id=seller_id, n=n, offset=offset, most_recent=most_recent, sort=sort, order=order)

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
seller_id = 'seller_id_example' # str | Filter results by seller. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
most_recent = True # bool |  (optional)
sort = vrchatapi.SortOptionProductPurchase() # SortOptionProductPurchase | The sort order of the results. (optional)
order = vrchatapi.OrderOptionShort() # OrderOptionShort | Result ordering (optional)

    try:
        # Get Product Purchases
        api_response = api_instance.get_product_purchases(buyer_id, seller_id=seller_id, n=n, offset=offset, most_recent=most_recent, sort=sort, order=order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_product_purchases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buyer_id** | **str**| Must be a valid user ID. | 
 **seller_id** | **str**| Filter results by seller. | [optional] 
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
    api_instance = vrchatapi.EconomyApi(api_client)
    
    try:
        # Get Seller Eligibility
        api_response = api_instance.get_seller_eligibility()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_seller_eligibility: %s\n" % e)
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
> list[Subscription] get_subscriptions(gifts=gifts, recurring=recurring)

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
    gifts = True # bool | Return giftable subscriptions instead of standard ones. (optional)
recurring = True # bool | Return recurring subscriptions instead of standard ones. (optional)

    try:
        # List Subscriptions
        api_response = api_instance.get_subscriptions(gifts=gifts, recurring=recurring)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gifts** | **bool**| Return giftable subscriptions instead of standard ones. | [optional] 
 **recurring** | **bool**| Return recurring subscriptions instead of standard ones. | [optional] 

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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

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
    api_instance = vrchatapi.EconomyApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
subscription_id = 'subscription_id_example' # str | 

    try:
        # Get User Credits Eligibility
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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_subscription_eligible**
> UserSubscriptionEligible get_user_subscription_eligible(user_id, steam_id=steam_id)

Get User Subscription Eligibility

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
        # Get User Subscription Eligibility
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

# **get_user_tilia_kyc**
> TiliaKyc get_user_tilia_kyc(user_id)

Get User Tilia KYC

Gets KYC status details for a user's Tilia account.

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
        # Get User Tilia KYC
        api_response = api_instance.get_user_tilia_kyc(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->get_user_tilia_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**TiliaKyc**](TiliaKyc.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a TiliaKyc object. |  -  |
**400** | Error response when the account is not in a state that supports the request, such as an account never onboarded for payouts. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stores**
> list[Store] list_stores(seller_id, management_pov=management_pov, n=n, offset=offset)

List Stores

List a seller's stores, adjusted for management views.

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
    seller_id = 'seller_id_example' # str | Seller to scope the results to.
management_pov = true # bool | Return stores from the seller management point of view. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List Stores
        api_response = api_instance.list_stores(seller_id, management_pov=management_pov, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->list_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seller_id** | **str**| Seller to scope the results to. | 
 **management_pov** | **bool**| Return stores from the seller management point of view. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[Store]**](Store.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Store objects. |  -  |
**400** | The request failed validation. VRChat validates the request before it looks up the resource, so this response is returned even when the ID in the path does not exist. The message names the offending field or parameter. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when the seller&#39;s stores are unavailable to the caller. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_products**
> list[Product] list_user_products(user_id, n=n, offset=offset)

List User Products

Gets the products of a given user.

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

    try:
        # List User Products
        api_response = api_instance.list_user_products(user_id, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->list_user_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[Product]**](Product.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Product objects. |  -  |
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

# **update_product**
> Product update_product(product_id, update_product_request)

Update Product

Updates a product and returns the updated Product object.

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
update_product_request = vrchatapi.UpdateProductRequest() # UpdateProductRequest | 

    try:
        # Update Product
        api_response = api_instance.update_product(product_id, update_product_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 
 **update_product_request** | [**UpdateProductRequest**](UpdateProductRequest.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Product object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_listing_direct**
> ProductListing update_product_listing_direct(product_id, update_listing_request, hydrate=hydrate)

Update Product Listing

Updates the active state of a listing. Setting `active` to `true` publishes the listing, while `false` unpublishes it.

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
update_listing_request = vrchatapi.UpdateListingRequest() # UpdateListingRequest | 
hydrate = True # bool | Populates some fields and changes types of others for certain objects. (optional)

    try:
        # Update Product Listing
        api_response = api_instance.update_product_listing_direct(product_id, update_listing_request, hydrate=hydrate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EconomyApi->update_product_listing_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Must be a valid product ID. | 
 **update_listing_request** | [**UpdateListingRequest**](UpdateListingRequest.md)|  | 
 **hydrate** | **bool**| Populates some fields and changes types of others for certain objects. | [optional] 

### Return type

[**ProductListing**](ProductListing.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single ProductListing object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

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
**404** | VRChat does not serve this route. A live route answers 200 or 401. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

