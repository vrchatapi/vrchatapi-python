# vrchatapi.InventoryApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory**](InventoryApi.md#get_inventory) | **GET** /inventory | Get Inventory
[**get_inventory_drops**](InventoryApi.md#get_inventory_drops) | **GET** /inventory/drops | List Inventory Drops
[**get_inventory_template**](InventoryApi.md#get_inventory_template) | **GET** /inventory/template/{inventoryTemplateId} | Get Inventory Template
[**get_own_inventory_item**](InventoryApi.md#get_own_inventory_item) | **GET** /inventory/{inventoryItemId} | Get Own Inventory Item
[**spawn_inventory_item**](InventoryApi.md#spawn_inventory_item) | **GET** /inventory/spawn | Spawn Inventory Item


# **get_inventory**
> Inventory get_inventory(n=n, offset=offset, inventory_sort_order=inventory_sort_order, inventory_item_type=inventory_item_type)

Get Inventory

Returns an Inventory object.

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
    api_instance = vrchatapi.InventoryApi(api_client)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
inventory_sort_order = 'inventory_sort_order_example' # str | Sort order for inventory retrieval. (optional)
inventory_item_type = vrchatapi.InventoryItemType() # InventoryItemType | Filter for inventory retrieval. (optional)

    try:
        # Get Inventory
        api_response = api_instance.get_inventory(n=n, offset=offset, inventory_sort_order=inventory_sort_order, inventory_item_type=inventory_item_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryApi->get_inventory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **inventory_sort_order** | **str**| Sort order for inventory retrieval. | [optional] 
 **inventory_item_type** | [**InventoryItemType**](.md)| Filter for inventory retrieval. | [optional] 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an Inventory object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_drops**
> list[InventoryDrop] get_inventory_drops(active=active)

List Inventory Drops

Returns a list of InventoryDrop objects.

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
    api_instance = vrchatapi.InventoryApi(api_client)
    active = True # bool | Filter for users' listings and inventory bundles. (optional)

    try:
        # List Inventory Drops
        api_response = api_instance.get_inventory_drops(active=active)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_drops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Filter for users&#39; listings and inventory bundles. | [optional] 

### Return type

[**list[InventoryDrop]**](InventoryDrop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InventoryDrop objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_template**
> InventoryTemplate get_inventory_template(inventory_template_id)

Get Inventory Template

Returns an InventoryTemplate object.

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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_template_id = 'invt_00000000-0000-0000-0000-000000000000' # str | Must be a valid inventory template ID.

    try:
        # Get Inventory Template
        api_response = api_instance.get_inventory_template(inventory_template_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryApi->get_inventory_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_template_id** | **str**| Must be a valid inventory template ID. | 

### Return type

[**InventoryTemplate**](InventoryTemplate.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryTemplate object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_own_inventory_item**
> InventoryItem get_own_inventory_item(inventory_item_id)

Get Own Inventory Item

Returns an InventoryItem object held by the currently logged in user.

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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inv_00000000-0000-0000-0000-000000000000' # str | Must be a valid inventory item ID.

    try:
        # Get Own Inventory Item
        api_response = api_instance.get_own_inventory_item(inventory_item_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryApi->get_own_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryItem object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spawn_inventory_item**
> InventorySpawn spawn_inventory_item(id)

Spawn Inventory Item

Returns an InventorySpawn object.

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
    api_instance = vrchatapi.InventoryApi(api_client)
    id = 'id_example' # str | Id for inventory item spawning.

    try:
        # Spawn Inventory Item
        api_response = api_instance.spawn_inventory_item(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InventoryApi->spawn_inventory_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id for inventory item spawning. | 

### Return type

[**InventorySpawn**](InventorySpawn.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventorySpawn object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

