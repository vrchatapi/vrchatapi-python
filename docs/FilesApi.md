# vrchatapi.FilesApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /file | Create File
[**create_file_version**](FilesApi.md#create_file_version) | **POST** /file/{fileId} | Create File Version
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /file/{fileId} | Delete File
[**delete_file_version**](FilesApi.md#delete_file_version) | **DELETE** /file/{fileId}/{versionId} | Delete File Version
[**download_file_version**](FilesApi.md#download_file_version) | **GET** /file/{fileId}/{versionId} | Download File Version
[**finish_file_data_upload**](FilesApi.md#finish_file_data_upload) | **PUT** /file/{fileId}/{versionId}/{fileType}/finish | Finish FileData Upload
[**get_file**](FilesApi.md#get_file) | **GET** /file/{fileId} | Show File
[**get_file_analysis**](FilesApi.md#get_file_analysis) | **GET** /analysis/{fileId}/{versionId} | Get File Version Analysis
[**get_file_analysis_security**](FilesApi.md#get_file_analysis_security) | **GET** /analysis/{fileId}/{versionId}/security | Get File Version Analysis Security
[**get_file_analysis_standard**](FilesApi.md#get_file_analysis_standard) | **GET** /analysis/{fileId}/{versionId}/standard | Get File Version Analysis Standard
[**get_file_data_upload_status**](FilesApi.md#get_file_data_upload_status) | **GET** /file/{fileId}/{versionId}/{fileType}/status | Check FileData Upload Status
[**get_files**](FilesApi.md#get_files) | **GET** /files | List Files
[**start_file_data_upload**](FilesApi.md#start_file_data_upload) | **PUT** /file/{fileId}/{versionId}/{fileType}/start | Start FileData Upload


# **create_file**
> File create_file(create_file_request=create_file_request)

Create File

Creates a new File object

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
    api_instance = vrchatapi.FilesApi(api_client)
    create_file_request = vrchatapi.CreateFileRequest() # CreateFileRequest |  (optional)

    try:
        # Create File
        api_response = api_instance.create_file(create_file_request=create_file_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_file_request** | [**CreateFileRequest**](CreateFileRequest.md)|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_version**
> File create_file_version(file_id, create_file_version_request=create_file_version_request)

Create File Version

Creates a new FileVersion. Once a Version has been created, proceed to the `/file/{fileId}/{versionId}/file/start` endpoint to start a file upload.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
create_file_version_request = vrchatapi.CreateFileVersionRequest() # CreateFileVersionRequest |  (optional)

    try:
        # Create File Version
        api_response = api_instance.create_file_version(file_id, create_file_version_request=create_file_version_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->create_file_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **create_file_version_request** | [**CreateFileVersionRequest**](CreateFileVersionRequest.md)|  | [optional] 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> File delete_file(file_id)

Delete File

Deletes a File object.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.

    try:
        # Delete File
        api_response = api_instance.delete_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |
**404** | Error response when trying to delete a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_version**
> File delete_file_version(file_id, version_id)

Delete File Version

Delete a specific version of a file. You can only delete the latest version.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.

    try:
        # Delete File Version
        api_response = api_instance.delete_file_version(file_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->delete_file_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |
**400** | Error response when trying to delete the initial version of a file. Delete the main File object instead. |  -  |
**500** | Error response when trying to delete any version of a file that is not the last one. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_version**
> download_file_version(file_id, version_id)

Download File Version

Downloads the file with the provided version number.  **Version Note:** Version 0 is always when the file was created. The real data is usually always located in version 1 and up.  **Extension Note:** Files are not guaranteed to have a file extensions. UnityPackage files tends to have it, images through this endpoint do not. You are responsible for appending file extension from the `extension` field when neccesary.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.

    try:
        # Download File Version
        api_instance.download_file_version(file_id, version_id)
    except ApiException as e:
        print("Exception when calling FilesApi->download_file_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 

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
**200** | Raw file |  -  |
**404** | Error response when trying to show information about a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish_file_data_upload**
> File finish_file_data_upload(file_id, version_id, file_type, finish_file_data_upload_request=finish_file_data_upload_request)

Finish FileData Upload

Finish an upload of a FileData. This will mark it as \"complete\". After uploading the `file` for Avatars and Worlds you then have to upload a `signature` file.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.
file_type = 'file' # str | Type of file.
finish_file_data_upload_request = {"etags":["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"],"nextPartNumber":"0","maxParts":"0"} # FinishFileDataUploadRequest | Please see documentation on ETag's: [https://teppen.io/2018/06/23/aws_s3_etags/](https://teppen.io/2018/06/23/aws_s3_etags/)  ETag's should NOT be present when uploading a `signature`. (optional)

    try:
        # Finish FileData Upload
        api_response = api_instance.finish_file_data_upload(file_id, version_id, file_type, finish_file_data_upload_request=finish_file_data_upload_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->finish_file_data_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 
 **file_type** | **str**| Type of file. | 
 **finish_file_data_upload_request** | [**FinishFileDataUploadRequest**](FinishFileDataUploadRequest.md)| Please see documentation on ETag&#39;s: [https://teppen.io/2018/06/23/aws_s3_etags/](https://teppen.io/2018/06/23/aws_s3_etags/)  ETag&#39;s should NOT be present when uploading a &#x60;signature&#x60;. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> File get_file(file_id)

Show File

Shows general information about the \"File\" object. Each File can have several \"Version\"'s, and each Version can have multiple real files or \"Data\" blobs.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.

    try:
        # Show File
        api_response = api_instance.get_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 

### Return type

[**File**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single File object. |  -  |
**404** | Error response when trying to show information about a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_analysis**
> FileAnalysis get_file_analysis(file_id, version_id)

Get File Version Analysis

Get the performance analysis for the uploaded assets of an avatar

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.

    try:
        # Get File Version Analysis
        api_response = api_instance.get_file_analysis(file_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file_analysis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 

### Return type

[**FileAnalysis**](FileAnalysis.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FileAnalysis object. |  -  |
**202** | Error response when requesting file Analysis that is not yet available. |  -  |
**404** | Error response when trying to show information about a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_analysis_security**
> FileAnalysis get_file_analysis_security(file_id, version_id)

Get File Version Analysis Security

Get the security performance analysis for the uploaded assets of an avatar

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.

    try:
        # Get File Version Analysis Security
        api_response = api_instance.get_file_analysis_security(file_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file_analysis_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 

### Return type

[**FileAnalysis**](FileAnalysis.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FileAnalysis object. |  -  |
**202** | Error response when requesting file Analysis that is not yet available. |  -  |
**404** | Error response when trying to show information about a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_analysis_standard**
> FileAnalysis get_file_analysis_standard(file_id, version_id)

Get File Version Analysis Standard

Get the standard performance analysis for the uploaded assets of an avatar

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.

    try:
        # Get File Version Analysis Standard
        api_response = api_instance.get_file_analysis_standard(file_id, version_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file_analysis_standard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 

### Return type

[**FileAnalysis**](FileAnalysis.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single FileAnalysis object. |  -  |
**202** | Error response when requesting file Analysis that is not yet available. |  -  |
**404** | Error response when trying to show information about a non-existent file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_data_upload_status**
> FileVersionUploadStatus get_file_data_upload_status(file_id, version_id, file_type)

Check FileData Upload Status

Retrieves the upload status for file upload. Can currently only be accessed when `status` is `waiting`. Trying to access it on a file version already uploaded currently times out.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.
file_type = 'file' # str | Type of file.

    try:
        # Check FileData Upload Status
        api_response = api_instance.get_file_data_upload_status(file_id, version_id, file_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_file_data_upload_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 
 **file_type** | **str**| Type of file. | 

### Return type

[**FileVersionUploadStatus**](FileVersionUploadStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current FileVersion upload status. Contains the uploadId needed for uploading, as well as the already uploaded parts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> list[File] get_files(tag=tag, user_id=user_id, n=n, offset=offset)

List Files

Returns a list of files

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
    api_instance = vrchatapi.FilesApi(api_client)
    tag = 'tag_example' # str | Tag, for example \"icon\" or \"gallery\", not included by default. (optional)
user_id = 'user_id_example' # str | UserID, will always generate a 500 permission error. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List Files
        api_response = api_instance.get_files(tag=tag, user_id=user_id, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag, for example \&quot;icon\&quot; or \&quot;gallery\&quot;, not included by default. | [optional] 
 **user_id** | **str**| UserID, will always generate a 500 permission error. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[File]**](File.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of File objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_file_data_upload**
> FileUploadURL start_file_data_upload(file_id, version_id, file_type, part_number=part_number)

Start FileData Upload

Starts an upload of a specific FilePart. This endpoint will return an AWS URL which you can PUT data to. You need to call this and receive a new AWS API URL for each `partNumber`. Please see AWS's REST documentation on \"PUT Object to S3\" on how to upload. Once all parts has been uploaded, proceed to `/finish` endpoint.  **Note:** `nextPartNumber` seems like it is always ignored. Despite it returning 0, first partNumber is always 1.

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
    api_instance = vrchatapi.FilesApi(api_client)
    file_id = 'file_00000000-0000-0000-0000-000000000000' # str | Must be a valid file ID.
version_id = 1 # int | Version ID of the asset.
file_type = 'file' # str | Type of file.
part_number = 1 # int | The part number to start uploading. If not provided, the first part will be started. (optional)

    try:
        # Start FileData Upload
        api_response = api_instance.start_file_data_upload(file_id, version_id, file_type, part_number=part_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->start_file_data_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| Must be a valid file ID. | 
 **version_id** | **int**| Version ID of the asset. | 
 **file_type** | **str**| Type of file. | 
 **part_number** | **int**| The part number to start uploading. If not provided, the first part will be started. | [optional] 

### Return type

[**FileUploadURL**](FileUploadURL.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | See [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](AWS REST docs - PUT Object) |  -  |
**400** | Error response when trying to start an upload against a FileVersion that is already marked as  &#x60;complete&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

