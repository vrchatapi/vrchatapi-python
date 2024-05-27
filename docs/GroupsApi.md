# vrchatapi.GroupsApi

All URIs are relative to *https://vrchat.com/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group_gallery_image**](GroupsApi.md#add_group_gallery_image) | **POST** /groups/{groupId}/galleries/{groupGalleryId}/images | Add Group Gallery Image
[**add_group_member_role**](GroupsApi.md#add_group_member_role) | **PUT** /groups/{groupId}/members/{userId}/roles/{groupRoleId} | Add Role to GroupMember
[**add_group_post**](GroupsApi.md#add_group_post) | **POST** /groups/{groupId}/posts | Create a post in a Group
[**ban_group_member**](GroupsApi.md#ban_group_member) | **POST** /groups/{groupId}/bans | Ban Group Member
[**cancel_group_request**](GroupsApi.md#cancel_group_request) | **DELETE** /groups/{groupId}/requests | Cancel Group Join Request
[**create_group**](GroupsApi.md#create_group) | **POST** /groups | Create Group
[**create_group_announcement**](GroupsApi.md#create_group_announcement) | **POST** /groups/{groupId}/announcement | Create Group Announcement
[**create_group_gallery**](GroupsApi.md#create_group_gallery) | **POST** /groups/{groupId}/galleries | Create Group Gallery
[**create_group_invite**](GroupsApi.md#create_group_invite) | **POST** /groups/{groupId}/invites | Invite User to Group
[**create_group_role**](GroupsApi.md#create_group_role) | **POST** /groups/{groupId}/roles | Create GroupRole
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete Group
[**delete_group_announcement**](GroupsApi.md#delete_group_announcement) | **DELETE** /groups/{groupId}/announcement | Delete Group Announcement
[**delete_group_gallery**](GroupsApi.md#delete_group_gallery) | **DELETE** /groups/{groupId}/galleries/{groupGalleryId} | Delete Group Gallery
[**delete_group_gallery_image**](GroupsApi.md#delete_group_gallery_image) | **DELETE** /groups/{groupId}/galleries/{groupGalleryId}/images/{groupGalleryImageId} | Delete Group Gallery Image
[**delete_group_invite**](GroupsApi.md#delete_group_invite) | **DELETE** /groups/{groupId}/invites/{userId} | Delete User Invite
[**delete_group_post**](GroupsApi.md#delete_group_post) | **DELETE** /groups/{groupId}/posts/{notificationId} | Delete a Group post
[**delete_group_role**](GroupsApi.md#delete_group_role) | **DELETE** /groups/{groupId}/roles/{groupRoleId} | Delete Group Role
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{groupId} | Get Group by ID
[**get_group_announcements**](GroupsApi.md#get_group_announcements) | **GET** /groups/{groupId}/announcement | Get Group Announcement
[**get_group_audit_logs**](GroupsApi.md#get_group_audit_logs) | **GET** /groups/{groupId}/auditLogs | Get Group Audit Logs
[**get_group_bans**](GroupsApi.md#get_group_bans) | **GET** /groups/{groupId}/bans | Get Group Bans
[**get_group_gallery_images**](GroupsApi.md#get_group_gallery_images) | **GET** /groups/{groupId}/galleries/{groupGalleryId} | Get Group Gallery Images
[**get_group_instances**](GroupsApi.md#get_group_instances) | **GET** /groups/{groupId}/instances | Get Group Instances
[**get_group_invites**](GroupsApi.md#get_group_invites) | **GET** /groups/{groupId}/invites | Get Group Invites Sent
[**get_group_member**](GroupsApi.md#get_group_member) | **GET** /groups/{groupId}/members/{userId} | Get Group Member
[**get_group_members**](GroupsApi.md#get_group_members) | **GET** /groups/{groupId}/members | List Group Members
[**get_group_permissions**](GroupsApi.md#get_group_permissions) | **GET** /groups/{groupId}/permissions | List Group Permissions
[**get_group_post**](GroupsApi.md#get_group_post) | **GET** /groups/{groupId}/posts | Get posts from a Group
[**get_group_requests**](GroupsApi.md#get_group_requests) | **GET** /groups/{groupId}/requests | Get Group Join Requests
[**get_group_roles**](GroupsApi.md#get_group_roles) | **GET** /groups/{groupId}/roles | Get Group Roles
[**join_group**](GroupsApi.md#join_group) | **POST** /groups/{groupId}/join | Join Group
[**kick_group_member**](GroupsApi.md#kick_group_member) | **DELETE** /groups/{groupId}/members/{userId} | Kick Group Member
[**leave_group**](GroupsApi.md#leave_group) | **POST** /groups/{groupId}/leave | Leave Group
[**remove_group_member_role**](GroupsApi.md#remove_group_member_role) | **DELETE** /groups/{groupId}/members/{userId}/roles/{groupRoleId} | Remove Role from GroupMember
[**respond_group_join_request**](GroupsApi.md#respond_group_join_request) | **PUT** /groups/{groupId}/requests/{userId} | Respond Group Join request
[**search_groups**](GroupsApi.md#search_groups) | **GET** /groups | Search Group
[**unban_group_member**](GroupsApi.md#unban_group_member) | **DELETE** /groups/{groupId}/bans/{userId} | Unban Group Member
[**update_group**](GroupsApi.md#update_group) | **PUT** /groups/{groupId} | Update Group
[**update_group_gallery**](GroupsApi.md#update_group_gallery) | **PUT** /groups/{groupId}/galleries/{groupGalleryId} | Update Group Gallery
[**update_group_member**](GroupsApi.md#update_group_member) | **PUT** /groups/{groupId}/members/{userId} | Update Group Member
[**update_group_post**](GroupsApi.md#update_group_post) | **PUT** /groups/{groupId}/posts/{notificationId} | Edits a Group post
[**update_group_role**](GroupsApi.md#update_group_role) | **PUT** /groups/{groupId}/roles/{groupRoleId} | Update Group Role


# **add_group_gallery_image**
> GroupGalleryImage add_group_gallery_image(group_id, group_gallery_id, add_group_gallery_image_request)

Add Group Gallery Image

Adds an image to a Group gallery.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_gallery_id = 'ggal_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery ID.
add_group_gallery_image_request = vrchatapi.AddGroupGalleryImageRequest() # AddGroupGalleryImageRequest | 

    try:
        # Add Group Gallery Image
        api_response = api_instance.add_group_gallery_image(group_id, group_gallery_id, add_group_gallery_image_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->add_group_gallery_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_gallery_id** | **str**| Must be a valid group gallery ID. | 
 **add_group_gallery_image_request** | [**AddGroupGalleryImageRequest**](AddGroupGalleryImageRequest.md)|  | 

### Return type

[**GroupGalleryImage**](GroupGalleryImage.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupGalleryImage object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_member_role**
> list[str] add_group_member_role(group_id, user_id, group_role_id)

Add Role to GroupMember

Adds a Role to a Group Member

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.
group_role_id = 'grol_00000000-0000-0000-0000-000000000000' # str | Must be a valid group role ID.

    try:
        # Add Role to GroupMember
        api_response = api_instance.add_group_member_role(group_id, user_id, group_role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->add_group_member_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 
 **group_role_id** | **str**| Must be a valid group role ID. | 

### Return type

**list[str]**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupRoleID objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_group_post**
> GroupPost add_group_post(group_id, create_group_post_request)

Create a post in a Group

Create a post in a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_group_post_request = vrchatapi.CreateGroupPostRequest() # CreateGroupPostRequest | 

    try:
        # Create a post in a Group
        api_response = api_instance.add_group_post(group_id, create_group_post_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->add_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_group_post_request** | [**CreateGroupPostRequest**](CreateGroupPostRequest.md)|  | 

### Return type

[**GroupPost**](GroupPost.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a GroupPost object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ban_group_member**
> GroupMember ban_group_member(group_id, ban_group_member_request)

Ban Group Member

Bans a user from a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
ban_group_member_request = vrchatapi.BanGroupMemberRequest() # BanGroupMemberRequest | 

    try:
        # Ban Group Member
        api_response = api_instance.ban_group_member(group_id, ban_group_member_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->ban_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **ban_group_member_request** | [**BanGroupMemberRequest**](BanGroupMemberRequest.md)|  | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**400** | Bad request error response when banning a user |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_group_request**
> cancel_group_request(group_id)

Cancel Group Join Request

Cancels a request sent to join the group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Cancel Group Join Request
        api_instance.cancel_group_request(group_id)
    except ApiException as e:
        print("Exception when calling GroupsApi->cancel_group_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

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
**200** | OK |  -  |
**400** | You can&#39;t cancel a join request if you didn&#39;t request to join․ |  -  |
**403** | Error response when trying to perform operations on a group you are not member of. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(create_group_request)

Create Group

Creates a Group and returns a Group object. **Requires VRC+ Subscription.**

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    create_group_request = vrchatapi.CreateGroupRequest() # CreateGroupRequest | 

    try:
        # Create Group
        api_response = api_instance.create_group(create_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Group object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_announcement**
> GroupAnnouncement create_group_announcement(group_id, create_group_announcement_request)

Create Group Announcement

Creates an Announcement for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_group_announcement_request = vrchatapi.CreateGroupAnnouncementRequest() # CreateGroupAnnouncementRequest | 

    try:
        # Create Group Announcement
        api_response = api_instance.create_group_announcement(group_id, create_group_announcement_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group_announcement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_group_announcement_request** | [**CreateGroupAnnouncementRequest**](CreateGroupAnnouncementRequest.md)|  | 

### Return type

[**GroupAnnouncement**](GroupAnnouncement.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupAnnouncement object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_gallery**
> GroupGallery create_group_gallery(group_id, create_group_gallery_request)

Create Group Gallery

Creates a gallery for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_group_gallery_request = vrchatapi.CreateGroupGalleryRequest() # CreateGroupGalleryRequest | 

    try:
        # Create Group Gallery
        api_response = api_instance.create_group_gallery(group_id, create_group_gallery_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group_gallery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_group_gallery_request** | [**CreateGroupGalleryRequest**](CreateGroupGalleryRequest.md)|  | 

### Return type

[**GroupGallery**](GroupGallery.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupGallery object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_invite**
> create_group_invite(group_id, create_group_invite_request)

Invite User to Group

Sends an invite to a user to join the group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_group_invite_request = vrchatapi.CreateGroupInviteRequest() # CreateGroupInviteRequest | 

    try:
        # Invite User to Group
        api_instance.create_group_invite(group_id, create_group_invite_request)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_group_invite_request** | [**CreateGroupInviteRequest**](CreateGroupInviteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request error response when creating a group invite. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Forbidden error response when creating a group invite. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_role**
> GroupRole create_group_role(group_id, create_group_role_request)

Create GroupRole

Create a Group role.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
create_group_role_request = vrchatapi.CreateGroupRoleRequest() # CreateGroupRoleRequest | 

    try:
        # Create GroupRole
        api_response = api_instance.create_group_role(group_id, create_group_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->create_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **create_group_role_request** | [**CreateGroupRoleRequest**](CreateGroupRoleRequest.md)|  | 

### Return type

[**GroupRole**](GroupRole.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupRole object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> Success delete_group(group_id)

Delete Group

Deletes a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Delete Group
        api_response = api_instance.delete_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

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
**200** | Successful response after deleting a Group. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_announcement**
> Success delete_group_announcement(group_id)

Delete Group Announcement

Deletes the announcement for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Delete Group Announcement
        api_response = api_instance.delete_group_announcement(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_announcement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

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
**200** | Successful response after deleting/clearing the group announcement. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_gallery**
> Success delete_group_gallery(group_id, group_gallery_id)

Delete Group Gallery

Deletes a gallery for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_gallery_id = 'ggal_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery ID.

    try:
        # Delete Group Gallery
        api_response = api_instance.delete_group_gallery(group_id, group_gallery_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_gallery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_gallery_id** | **str**| Must be a valid group gallery ID. | 

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
**200** | Successful response after deleting a group gallery. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_gallery_image**
> Success delete_group_gallery_image(group_id, group_gallery_id, group_gallery_image_id)

Delete Group Gallery Image

Deletes an image from a Group gallery.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_gallery_id = 'ggal_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery ID.
group_gallery_image_id = 'ggim_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery image ID.

    try:
        # Delete Group Gallery Image
        api_response = api_instance.delete_group_gallery_image(group_id, group_gallery_id, group_gallery_image_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_gallery_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_gallery_id** | **str**| Must be a valid group gallery ID. | 
 **group_gallery_image_id** | **str**| Must be a valid group gallery image ID. | 

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
**200** | Successful response after deleting a group gallery image. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to delete a submission to a group&#39;s gallery when the user does not have permission to do so. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_invite**
> delete_group_invite(group_id, user_id)

Delete User Invite

Deletes an Group invite sent to a User

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Delete User Invite
        api_instance.delete_group_invite(group_id, user_id)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 

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
**200** | OK |  -  |
**400** | Bad request error response when deleting a group invite |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_post**
> Success delete_group_post(group_id, notification_id)

Delete a Group post

Delete a Group post

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
notification_id = 'notification_id_example' # str | Must be a valid notification ID.

    try:
        # Delete a Group post
        api_response = api_instance.delete_group_post(group_id, notification_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **notification_id** | **str**| Must be a valid notification ID. | 

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
**200** | Response after deleting a group post. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Response after deleting a group post. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_role**
> list[GroupRole] delete_group_role(group_id, group_role_id)

Delete Group Role

Deletes a Group Role by ID and returns the remaining roles.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_role_id = 'grol_00000000-0000-0000-0000-000000000000' # str | Must be a valid group role ID.

    try:
        # Delete Group Role
        api_response = api_instance.delete_group_role(group_id, group_role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->delete_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_role_id** | **str**| Must be a valid group role ID. | 

### Return type

[**list[GroupRole]**](GroupRole.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupRole objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a group you are not member of. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id, include_roles=include_roles)

Get Group by ID

Returns a single Group by ID.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
include_roles = True # bool | Include roles for the Group object. Defaults to false. (optional)

    try:
        # Get Group by ID
        api_response = api_instance.get_group(group_id, include_roles=include_roles)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **include_roles** | **bool**| Include roles for the Group object. Defaults to false. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Group object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_announcements**
> GroupAnnouncement get_group_announcements(group_id)

Get Group Announcement

Returns the announcement for a Group. If no announcement has been made, then it returns **empty object**.  If an announcement exists, then it will always return all fields except `imageId` and `imageUrl` which may be null.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Get Group Announcement
        api_response = api_instance.get_group_announcements(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_announcements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

### Return type

[**GroupAnnouncement**](GroupAnnouncement.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupAnnouncement object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_audit_logs**
> PaginatedGroupAuditLogEntryList get_group_audit_logs(group_id, n=n, offset=offset, start_date=start_date, end_date=end_date)

Get Group Audit Logs

Returns a list of audit logs for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date of the search range. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date of the search range. (optional)

    try:
        # Get Group Audit Logs
        api_response = api_instance.get_group_audit_logs(group_id, n=n, offset=offset, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **start_date** | **datetime**| The start date of the search range. | [optional] 
 **end_date** | **datetime**| The end date of the search range. | [optional] 

### Return type

[**PaginatedGroupAuditLogEntryList**](PaginatedGroupAuditLogEntryList.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupAudit objects, wrapped in new pagination format. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_bans**
> list[GroupMember] get_group_bans(group_id, n=n, offset=offset)

Get Group Bans

Returns a list of banned users for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # Get Group Bans
        api_response = api_instance.get_group_bans(group_id, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_bans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[GroupMember]**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_gallery_images**
> list[GroupGalleryImage] get_group_gallery_images(group_id, group_gallery_id, n=n, offset=offset, approved=approved)

Get Group Gallery Images

Returns a list of images for a Group gallery.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_gallery_id = 'ggal_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
approved = True # bool | If specified, only returns images that have been approved or not approved. (optional)

    try:
        # Get Group Gallery Images
        api_response = api_instance.get_group_gallery_images(group_id, group_gallery_id, n=n, offset=offset, approved=approved)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_gallery_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_gallery_id** | **str**| Must be a valid group gallery ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **approved** | **bool**| If specified, only returns images that have been approved or not approved. | [optional] 

### Return type

[**list[GroupGalleryImage]**](GroupGalleryImage.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupGalleryImage objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_instances**
> list[GroupInstance] get_group_instances(group_id)

Get Group Instances

Returns a list of group instances

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Get Group Instances
        api_response = api_instance.get_group_instances(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

### Return type

[**list[GroupInstance]**](GroupInstance.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupInstance objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_invites**
> list[GroupMember] get_group_invites(group_id, n=n, offset=offset)

Get Group Invites Sent

Returns a list of members that have been invited to the Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # Get Group Invites Sent
        api_response = api_instance.get_group_invites(group_id, n=n, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_invites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**list[GroupMember]**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to perform operations on a group you are not member of. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_member**
> GroupLimitedMember get_group_member(group_id, user_id)

Get Group Member

Returns a LimitedGroup Member.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Group Member
        api_response = api_instance.get_group_member(group_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**GroupLimitedMember**](GroupLimitedMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_members**
> list[GroupMember] get_group_members(group_id, n=n, offset=offset, sort=sort)

List Group Members

Returns a List of all **other** Group Members. This endpoint will never return the user calling the endpoint. Information about the user calling the endpoint must be found in the `myMember` field of the Group object.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
sort = vrchatapi.GroupSearchSort() # GroupSearchSort | The sort order of Group Member results (optional)

    try:
        # List Group Members
        api_response = api_instance.get_group_members(group_id, n=n, offset=offset, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **sort** | [**GroupSearchSort**](.md)| The sort order of Group Member results | [optional] 

### Return type

[**list[GroupMember]**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**400** | Error response when trying to search list of users with an invalid request. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_permissions**
> list[GroupPermission] get_group_permissions(group_id)

List Group Permissions

Returns a List of all possible/available permissions for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # List Group Permissions
        api_response = api_instance.get_group_permissions(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

### Return type

[**list[GroupPermission]**](GroupPermission.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupPermission objects. |  -  |
**400** | Error response when trying to search list of users with an invalid request. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_post**
> GroupPost get_group_post(group_id, n=n, offset=offset, public_only=public_only)

Get posts from a Group

Get posts from a Group

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
public_only = True # bool | See public posts only. (optional)

    try:
        # Get posts from a Group
        api_response = api_instance.get_group_post(group_id, n=n, offset=offset, public_only=public_only)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **public_only** | **bool**| See public posts only. | [optional] 

### Return type

[**GroupPost**](GroupPost.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a GroupPost object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_requests**
> list[GroupMember] get_group_requests(group_id, n=n, offset=offset, blocked=blocked)

Get Group Join Requests

Returns a list of members that have requested to join the Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
n = 60 # int | The number of objects to return. (optional) (default to 60)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
blocked = True # bool | See blocked join requests (optional)

    try:
        # Get Group Join Requests
        api_response = api_instance.get_group_requests(group_id, n=n, offset=offset, blocked=blocked)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **blocked** | **bool**| See blocked join requests | [optional] 

### Return type

[**list[GroupMember]**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**400** | Bad request error response when responding to a group join request |  -  |
**403** | Error response when trying to perform operations on a group you are not member of. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_roles**
> list[GroupRole] get_group_roles(group_id)

Get Group Roles

Returns a Group Role by ID.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Get Group Roles
        api_response = api_instance.get_group_roles(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->get_group_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

### Return type

[**list[GroupRole]**](GroupRole.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupRole objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_group**
> GroupMember join_group(group_id)

Join Group

Join a Group by ID and returns the member object.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Join Group
        api_response = api_instance.join_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->join_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**400** | Error response when trying to join a group that the user is already a member of. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kick_group_member**
> kick_group_member(group_id, user_id)

Kick Group Member

Kicks a Group Member from the Group. The current user must have the \"Remove Group Members\" permission.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Kick Group Member
        api_instance.kick_group_member(group_id, user_id)
    except ApiException as e:
        print("Exception when calling GroupsApi->kick_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 

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
**200** | OK |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to perform operations on a group you are not member of. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leave_group**
> leave_group(group_id)

Leave Group

Leave a group by ID.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.

    try:
        # Leave Group
        api_instance.leave_group(group_id)
    except ApiException as e:
        print("Exception when calling GroupsApi->leave_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 

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
**200** | OK |  -  |
**403** | Error response when trying to perform operations on a group you are not member of. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_group_member_role**
> list[str] remove_group_member_role(group_id, user_id, group_role_id)

Remove Role from GroupMember

Removes a Role from a Group Member

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.
group_role_id = 'grol_00000000-0000-0000-0000-000000000000' # str | Must be a valid group role ID.

    try:
        # Remove Role from GroupMember
        api_response = api_instance.remove_group_member_role(group_id, user_id, group_role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->remove_group_member_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 
 **group_role_id** | **str**| Must be a valid group role ID. | 

### Return type

**list[str]**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupRoleID objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_group_join_request**
> respond_group_join_request(group_id, user_id, respond_group_join_request)

Respond Group Join request

Responds to a Group Join Request with Accept/Deny

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.
respond_group_join_request = vrchatapi.RespondGroupJoinRequest() # RespondGroupJoinRequest | 

    try:
        # Respond Group Join request
        api_instance.respond_group_join_request(group_id, user_id, respond_group_join_request)
    except ApiException as e:
        print("Exception when calling GroupsApi->respond_group_join_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 
 **respond_group_join_request** | [**RespondGroupJoinRequest**](RespondGroupJoinRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_groups**
> list[LimitedGroup] search_groups(query=query, offset=offset, n=n)

Search Group

Searches Groups by name or shortCode

### Example

```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
)


# Enter a context with an instance of the API client
with vrchatapi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.GroupsApi(api_client)
    query = 'query_example' # str | Query to search for, can be either Group Name or Group shortCode (optional)
offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
n = 60 # int | The number of objects to return. (optional) (default to 60)

    try:
        # Search Group
        api_response = api_instance.search_groups(query=query, offset=offset, n=n)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->search_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query to search for, can be either Group Name or Group shortCode | [optional] 
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]

### Return type

[**list[LimitedGroup]**](LimitedGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of LimitedGroup objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unban_group_member**
> GroupMember unban_group_member(group_id, user_id)

Unban Group Member

Unbans a user from a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Unban Group Member
        api_response = api_instance.unban_group_member(group_id, user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->unban_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(group_id, update_group_request=update_group_request)

Update Group

Updates a Group and returns it.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
update_group_request = vrchatapi.UpdateGroupRequest() # UpdateGroupRequest |  (optional)

    try:
        # Update Group
        api_response = api_instance.update_group(group_id, update_group_request=update_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **update_group_request** | [**UpdateGroupRequest**](UpdateGroupRequest.md)|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Group object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_gallery**
> GroupGallery update_group_gallery(group_id, group_gallery_id, update_group_gallery_request=update_group_gallery_request)

Update Group Gallery

Updates a gallery for a Group.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_gallery_id = 'ggal_00000000-0000-0000-0000-000000000000' # str | Must be a valid group gallery ID.
update_group_gallery_request = vrchatapi.UpdateGroupGalleryRequest() # UpdateGroupGalleryRequest |  (optional)

    try:
        # Update Group Gallery
        api_response = api_instance.update_group_gallery(group_id, group_gallery_id, update_group_gallery_request=update_group_gallery_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group_gallery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_gallery_id** | **str**| Must be a valid group gallery ID. | 
 **update_group_gallery_request** | [**UpdateGroupGalleryRequest**](UpdateGroupGalleryRequest.md)|  | [optional] 

### Return type

[**GroupGallery**](GroupGallery.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single GroupGallery object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_member**
> GroupLimitedMember update_group_member(group_id, user_id, update_group_member_request=update_group_member_request)

Update Group Member

Updates a Group Member

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
user_id = 'user_id_example' # str | Must be a valid user ID.
update_group_member_request = vrchatapi.UpdateGroupMemberRequest() # UpdateGroupMemberRequest |  (optional)

    try:
        # Update Group Member
        api_response = api_instance.update_group_member(group_id, user_id, update_group_member_request=update_group_member_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **user_id** | **str**| Must be a valid user ID. | 
 **update_group_member_request** | [**UpdateGroupMemberRequest**](UpdateGroupMemberRequest.md)|  | [optional] 

### Return type

[**GroupLimitedMember**](GroupLimitedMember.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupMember objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to perform operations on a non-existing group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_post**
> GroupPost update_group_post(group_id, notification_id, create_group_post_request)

Edits a Group post

Edits a Group post

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
notification_id = 'notification_id_example' # str | Must be a valid notification ID.
create_group_post_request = vrchatapi.CreateGroupPostRequest() # CreateGroupPostRequest | 

    try:
        # Edits a Group post
        api_response = api_instance.update_group_post(group_id, notification_id, create_group_post_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **notification_id** | **str**| Must be a valid notification ID. | 
 **create_group_post_request** | [**CreateGroupPostRequest**](CreateGroupPostRequest.md)|  | 

### Return type

[**GroupPost**](GroupPost.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a GroupPost object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Response after deleting a group post. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_role**
> list[GroupRole] update_group_role(group_id, group_role_id, update_group_role_request=update_group_role_request)

Update Group Role

Updates a group role by ID.

### Example

* Api Key Authentication (authCookie):
```python
from __future__ import print_function
import time
import vrchatapi
from vrchatapi.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://vrchat.com/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://vrchat.com/api/1"
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
    api_instance = vrchatapi.GroupsApi(api_client)
    group_id = 'grp_00000000-0000-0000-0000-000000000000' # str | Must be a valid group ID.
group_role_id = 'grol_00000000-0000-0000-0000-000000000000' # str | Must be a valid group role ID.
update_group_role_request = vrchatapi.UpdateGroupRoleRequest() # UpdateGroupRoleRequest |  (optional)

    try:
        # Update Group Role
        api_response = api_instance.update_group_role(group_id, group_role_id, update_group_role_request=update_group_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupsApi->update_group_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Must be a valid group ID. | 
 **group_role_id** | **str**| Must be a valid group role ID. | 
 **update_group_role_request** | [**UpdateGroupRoleRequest**](UpdateGroupRoleRequest.md)|  | [optional] 

### Return type

[**list[GroupRole]**](GroupRole.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of GroupRole objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

