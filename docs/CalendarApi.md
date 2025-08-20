# vrchatapi.CalendarApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_calendar_event**](CalendarApi.md#create_group_calendar_event) | **POST** /calendar/{groupId}/event | Create a calendar event
[**delete_group_calendar_event**](CalendarApi.md#delete_group_calendar_event) | **DELETE** /calendar/{groupId}/{calendarId} | Delete a calendar event
[**follow_group_calendar_event**](CalendarApi.md#follow_group_calendar_event) | **POST** /calendar/{groupId}/{calendarId}/follow | Follow a calendar event
[**get_calendar_events**](CalendarApi.md#get_calendar_events) | **GET** /calendar | List calendar events
[**get_featured_calendar_events**](CalendarApi.md#get_featured_calendar_events) | **GET** /calendar/featured | List featured calendar events
[**get_followed_calendar_events**](CalendarApi.md#get_followed_calendar_events) | **GET** /calendar/following | List followed calendar events
[**get_group_calendar_event**](CalendarApi.md#get_group_calendar_event) | **GET** /calendar/{groupId}/{calendarId} | Get a calendar event
[**get_group_calendar_event_ics**](CalendarApi.md#get_group_calendar_event_ics) | **GET** /calendar/{groupId}/{calendarId}.ics | Download calendar event as ICS
[**get_group_calendar_events**](CalendarApi.md#get_group_calendar_events) | **GET** /calendar/{groupId} | List a group&#39;s calendar events
[**update_group_calendar_event**](CalendarApi.md#update_group_calendar_event) | **PUT** /calendar/{groupId}/{calendarId}/event | Update a calendar event


# **create_group_calendar_event**
> CalendarEvent create_group_calendar_event(group_id, create_calendar_event_request)

Create a calendar event

Creates an event for a group on the calendar

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_calendar_event_request = vrchatapi.CreateCalendarEventRequest() # CreateCalendarEventRequest | 

    try:
        # Create a calendar event
        api_response = api_instance.create_group_calendar_event(group_id, create_calendar_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->create_group_calendar_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_calendar_event_request** | [**CreateCalendarEventRequest**](CreateCalendarEventRequest.md)|  | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CalendarEvent object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_calendar_event**
> Success delete_group_calendar_event(group_id, calendar_id)

Delete a calendar event

Delete a group calendar event

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
calendar_id = 'cal_00000000-0000-0000-0000-000000000000' # str | Must be a valid calendar ID.

    try:
        # Delete a calendar event
        api_response = api_instance.delete_group_calendar_event(group_id, calendar_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->delete_group_calendar_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **calendar_id** | **str**| Must be a valid calendar ID. | 

### Return type

[**Success**](Success.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response after deleting a calendar event. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **follow_group_calendar_event**
> CalendarEvent follow_group_calendar_event(group_id, calendar_id, follow_calendar_event_request)

Follow a calendar event

Follow or unfollow an event on a group's calendar

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
calendar_id = 'cal_00000000-0000-0000-0000-000000000000' # str | Must be a valid calendar ID.
follow_calendar_event_request = vrchatapi.FollowCalendarEventRequest() # FollowCalendarEventRequest | 

    try:
        # Follow a calendar event
        api_response = api_instance.follow_group_calendar_event(group_id, calendar_id, follow_calendar_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->follow_group_calendar_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **calendar_id** | **str**| Must be a valid calendar ID. | 
 **follow_calendar_event_request** | [**FollowCalendarEventRequest**](FollowCalendarEventRequest.md)|  | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CalendarEvent object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar_events**
> PaginatedCalendarEventList get_calendar_events(date=date, n=n, offset=offset)

List calendar events

Get a list of a user's calendar events for the month in ?date

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
    api_instance = vrchatapi.CalendarApi(api_client)
    date = '2013-10-20T19:20:30+01:00' # datetime | The month to search in. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List calendar events
        api_response = api_instance.get_calendar_events(date=date, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_calendar_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| The month to search in. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**PaginatedCalendarEventList**](PaginatedCalendarEventList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of CalendarEvent objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_calendar_events**
> PaginatedCalendarEventList get_featured_calendar_events(date=date, n=n, offset=offset)

List featured calendar events

Get a list of a featured calendar events for the month in ?date

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
    api_instance = vrchatapi.CalendarApi(api_client)
    date = '2013-10-20T19:20:30+01:00' # datetime | The month to search in. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List featured calendar events
        api_response = api_instance.get_featured_calendar_events(date=date, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_featured_calendar_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| The month to search in. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**PaginatedCalendarEventList**](PaginatedCalendarEventList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of CalendarEvent objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_followed_calendar_events**
> PaginatedCalendarEventList get_followed_calendar_events(date=date, n=n, offset=offset)

List followed calendar events

Get a list of a followed calendar events for the month in ?date

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
    api_instance = vrchatapi.CalendarApi(api_client)
    date = '2013-10-20T19:20:30+01:00' # datetime | The month to search in. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List followed calendar events
        api_response = api_instance.get_followed_calendar_events(date=date, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_followed_calendar_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **datetime**| The month to search in. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**PaginatedCalendarEventList**](PaginatedCalendarEventList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of CalendarEvent objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_calendar_event**
> CalendarEvent get_group_calendar_event(group_id, calendar_id)

Get a calendar event

Get a group calendar event

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
calendar_id = 'cal_00000000-0000-0000-0000-000000000000' # str | Must be a valid calendar ID.

    try:
        # Get a calendar event
        api_response = api_instance.get_group_calendar_event(group_id, calendar_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_group_calendar_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **calendar_id** | **str**| Must be a valid calendar ID. | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CalendarEvent object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_calendar_event_ics**
> file get_group_calendar_event_ics(group_id, calendar_id)

Download calendar event as ICS

Returns the specified calendar in iCalendar (ICS) format.

### Example

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


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
calendar_id = 'cal_00000000-0000-0000-0000-000000000000' # str | Must be a valid calendar ID.

    try:
        # Download calendar event as ICS
        api_response = api_instance.get_group_calendar_event_ics(group_id, calendar_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_group_calendar_event_ics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **calendar_id** | **str**| Must be a valid calendar ID. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/calendar, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | iCalendar file download |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to download ICS calendar of a non-existent calendar entry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_calendar_events**
> PaginatedCalendarEventList get_group_calendar_events(group_id, date=date, n=n, offset=offset)

List a group's calendar events

Get a list of a group's calendar events

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
date = '2013-10-20T19:20:30+01:00' # datetime | The month to search in. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List a group's calendar events
        api_response = api_instance.get_group_calendar_events(group_id, date=date, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->get_group_calendar_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **date** | **datetime**| The month to search in. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**PaginatedCalendarEventList**](PaginatedCalendarEventList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of CalendarEvent objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_calendar_event**
> CalendarEvent update_group_calendar_event(group_id, calendar_id, update_calendar_event_request)

Update a calendar event

Updates an event for a group on the calendar

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
    api_instance = vrchatapi.CalendarApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
calendar_id = 'cal_00000000-0000-0000-0000-000000000000' # str | Must be a valid calendar ID.
update_calendar_event_request = vrchatapi.UpdateCalendarEventRequest() # UpdateCalendarEventRequest | 

    try:
        # Update a calendar event
        api_response = api_instance.update_group_calendar_event(group_id, calendar_id, update_calendar_event_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CalendarApi->update_group_calendar_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **calendar_id** | **str**| Must be a valid calendar ID. | 
 **update_calendar_event_request** | [**UpdateCalendarEventRequest**](UpdateCalendarEventRequest.md)|  | 

### Return type

[**CalendarEvent**](CalendarEvent.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CalendarEvent object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

