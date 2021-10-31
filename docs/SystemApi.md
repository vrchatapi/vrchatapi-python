# vrchatapi.SystemApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config**](SystemApi.md#get_config) | **GET** /config | Fetch API Config
[**get_css**](SystemApi.md#get_css) | **GET** /css/app.css | Download CSS
[**get_current_online_users**](SystemApi.md#get_current_online_users) | **GET** /visits | Current Online Users
[**get_health**](SystemApi.md#get_health) | **GET** /health | Check API Health
[**get_java_script**](SystemApi.md#get_java_script) | **GET** /js/app.js | Download JavaScript
[**get_system_time**](SystemApi.md#get_system_time) | **GET** /time | Current System Time


# **get_config**
> APIConfig get_config()

Fetch API Config

API config contains configuration that the clients needs to work properly.  Currently the most important value here is `clientApiKey` which is used for all other API endpoints.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from vrchatapi.model.api_config import APIConfig
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch API Config
        api_response = api_instance.get_config()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_config: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**APIConfig**](APIConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the API&#39;s config. |  * Set-Cookie -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_css**
> str get_css()

Download CSS

Fetches the CSS code to the frontend React website.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)
    variant = "public" # str | Specifies which `variant` of the site. Public is the end-user site, while `internal` is the staff-only site with special pages for moderation and management. (optional) if omitted the server will use the default value of "public"
    branch = "main" # str | Specifies which git branch the site should load frontend source code from. (optional) if omitted the server will use the default value of "main"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download CSS
        api_response = api_instance.get_css(variant=variant, branch=branch)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_css: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant** | **str**| Specifies which &#x60;variant&#x60; of the site. Public is the end-user site, while &#x60;internal&#x60; is the staff-only site with special pages for moderation and management. | [optional] if omitted the server will use the default value of "public"
 **branch** | **str**| Specifies which git branch the site should load frontend source code from. | [optional] if omitted the server will use the default value of "main"

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/css, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | **Note:** VRChat uses 302 Redirect to Cloudfront. The implementing library **must** support and follow redirects natively. |  -  |
**400** | Error response when trying to download non-public and non-main JavaScript or CSS without Admin Credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_online_users**
> int get_current_online_users()

Current Online Users

Returns the current number of online users.  **NOTE:** The response type is not a JSON object, but a simple JSON integer.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Current Online Users
        api_response = api_instance.get_current_online_users()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_current_online_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health**
> APIHealth get_health()

Check API Health

~~Gets the overall health status, the server name, and the current build version tag of the API.~~  **DEPRECATED:** VRChat has suddenly restricted this endpoint for unknown reasons, and now always return 401 Unauthorized.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from vrchatapi.model.api_health import APIHealth
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Check API Health
        api_response = api_instance.get_health()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_health: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**APIHealth**](APIHealth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the API&#39;s health. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_java_script**
> str get_java_script()

Download JavaScript

Fetches the JavaScript code to the frontend React website.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from vrchatapi.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)
    variant = "public" # str | Specifies which `variant` of the site. Public is the end-user site, while `internal` is the staff-only site with special pages for moderation and management. (optional) if omitted the server will use the default value of "public"
    branch = "main" # str | Specifies which git branch the site should load frontend source code from. (optional) if omitted the server will use the default value of "main"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Download JavaScript
        api_response = api_instance.get_java_script(variant=variant, branch=branch)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_java_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variant** | **str**| Specifies which &#x60;variant&#x60; of the site. Public is the end-user site, while &#x60;internal&#x60; is the staff-only site with special pages for moderation and management. | [optional] if omitted the server will use the default value of "public"
 **branch** | **str**| Specifies which git branch the site should load frontend source code from. | [optional] if omitted the server will use the default value of "main"

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | **Note:** VRChat uses 302 Redirect to Cloudfront. The implementing library **must** support and follow redirects natively. |  -  |
**400** | Error response when trying to download non-public and non-main JavaScript or CSS without Admin Credentials. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_time**
> datetime get_system_time()

Current System Time

Returns the current time of the API server.  **NOTE:** The response type is not a JSON object, but a simple JSON string.

### Example


```python
import time
import vrchatapi
from vrchatapi.api import system_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = system_api.SystemApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Current System Time
        api_response = api_instance.get_system_time()
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling SystemApi->get_system_time: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**datetime**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

