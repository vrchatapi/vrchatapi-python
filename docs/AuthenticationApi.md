# vrchatapi.AuthenticationApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_pending2_fa**](AuthenticationApi.md#cancel_pending2_fa) | **DELETE** /auth/twofactorauth/totp/pending | Cancel pending enabling of time-based 2FA codes
[**check_user_exists**](AuthenticationApi.md#check_user_exists) | **GET** /auth/exists | Check User Exists
[**confirm_email**](AuthenticationApi.md#confirm_email) | **GET** /auth/confirmEmail | Confirm Email
[**delete_user**](AuthenticationApi.md#delete_user) | **PUT** /users/{userId}/delete | Delete User
[**disable2_fa**](AuthenticationApi.md#disable2_fa) | **DELETE** /auth/twofactorauth | Disable 2FA
[**enable2_fa**](AuthenticationApi.md#enable2_fa) | **POST** /auth/twofactorauth/totp/pending | Enable time-based 2FA codes
[**get_current_user**](AuthenticationApi.md#get_current_user) | **GET** /auth/user | Login and/or Get Current User Info
[**get_recovery_codes**](AuthenticationApi.md#get_recovery_codes) | **GET** /auth/user/twofactorauth/otp | Get 2FA Recovery codes
[**logout**](AuthenticationApi.md#logout) | **PUT** /logout | Logout
[**register_user_account**](AuthenticationApi.md#register_user_account) | **POST** /auth/register | Register User Account
[**resend_email_confirmation**](AuthenticationApi.md#resend_email_confirmation) | **POST** /auth/user/resendEmail | Resend Email Confirmation
[**verify2_fa**](AuthenticationApi.md#verify2_fa) | **POST** /auth/twofactorauth/totp/verify | Verify 2FA code
[**verify2_fa_email_code**](AuthenticationApi.md#verify2_fa_email_code) | **POST** /auth/twofactorauth/emailotp/verify | Verify 2FA email code
[**verify_auth_token**](AuthenticationApi.md#verify_auth_token) | **GET** /auth | Verify Auth Token
[**verify_login_place**](AuthenticationApi.md#verify_login_place) | **GET** /auth/verifyLoginPlace | Verify Login Place
[**verify_pending2_fa**](AuthenticationApi.md#verify_pending2_fa) | **POST** /auth/twofactorauth/totp/pending/verify | Verify Pending 2FA code
[**verify_recovery_code**](AuthenticationApi.md#verify_recovery_code) | **POST** /auth/twofactorauth/otp/verify | Verify 2FA code with Recovery code


# **cancel_pending2_fa**
> Disable2FAResult cancel_pending2_fa()

Cancel pending enabling of time-based 2FA codes

Cancels the sequence for enabling time-based 2FA.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Cancel pending enabling of time-based 2FA codes
        api_response = api_instance.cancel_pending2_fa()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->cancel_pending2_fa: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Disable2FAResult**](Disable2FAResult.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_exists**
> UserExists check_user_exists(email=email, display_name=display_name, username=username, exclude_user_id=exclude_user_id)

Check User Exists

Checks if a user by a given `username`, `displayName` or `email` exist. This is used during registration to check if a username has already been taken, during change of displayName to check if a displayName is available, and during change of email to check if the email is already used. In the later two cases the `excludeUserId` is used to exclude oneself, otherwise the result would always be true.  It is **REQUIRED** to include **AT LEAST** `username`, `displayName` **or** `email` query parameter. Although they can be combined - in addition with `excludeUserId` (generally to exclude yourself) - to further fine-tune the search.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    email = 'email_example' # str | Filter by email. (optional)
display_name = 'display_name_example' # str | Filter by displayName. (optional)
username = 'username_example' # str | Filter by Username. (optional)
exclude_user_id = 'exclude_user_id_example' # str | Exclude by UserID. (optional)

    try:
        # Check User Exists
        api_response = api_instance.check_user_exists(email=email, display_name=display_name, username=username, exclude_user_id=exclude_user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->check_user_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Filter by email. | [optional] 
 **display_name** | **str**| Filter by displayName. | [optional] 
 **username** | **str**| Filter by Username. | [optional] 
 **exclude_user_id** | **str**| Exclude by UserID. | [optional] 

### Return type

[**UserExists**](UserExists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a response if a user exists or not. |  -  |
**400** | Error response when missing at least 1 of the required parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_email**
> confirm_email(id, verify_email)

Confirm Email

Confirms the email address for a user

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    id = 'usr_00000000-0000-0000-0000-000000000000' # str | Target user for which to verify email.
verify_email = 'eml_00000000-0000-0000-0000-000000000000' # str | Token to verify email.

    try:
        # Confirm Email
        api_instance.confirm_email(id, verify_email)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->confirm_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Target user for which to verify email. | 
 **verify_email** | **str**| Token to verify email. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> CurrentUser delete_user(user_id)

Delete User

Deletes the account with given ID. Normal users only have permission to delete their own account. Account deletion is 14 days from this request, and will be cancelled if you do an authenticated request with the account afterwards.  **VRC+ NOTE:** Despite the 14-days cooldown, any VRC+ subscription will be cancelled **immediately**.  **METHOD NOTE:** Despite this being a Delete action, the method type required is PUT.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Delete User
        api_response = api_instance.delete_user(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**CurrentUser**](CurrentUser.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable2_fa**
> Disable2FAResult disable2_fa()

Disable 2FA

Disables 2FA for the currently logged in account

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Disable 2FA
        api_response = api_instance.disable2_fa()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->disable2_fa: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Disable2FAResult**](Disable2FAResult.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable2_fa**
> Pending2FAResult enable2_fa()

Enable time-based 2FA codes

Begins the sequence for enabling time-based 2FA.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Enable time-based 2FA codes
        api_response = api_instance.enable2_fa()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->enable2_fa: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Pending2FAResult**](Pending2FAResult.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> CurrentUser get_current_user()

Login and/or Get Current User Info

This endpoint does the following two operations:   1) Checks if you are already logged in by looking for a valid `auth` cookie. If you are have a valid auth cookie then no additional auth-related actions are taken. If you are **not** logged in then it will log you in with the `Authorization` header and set the `auth` cookie. The `auth` cookie will only be sent once.   2) If logged in, this function will also return the CurrentUser object containing detailed information about the currently logged in user.  The auth string after `Authorization: Basic {string}` is a base64-encoded string of the username and password, both individually url-encoded, and then joined with a colon.    > base64(urlencode(username):urlencode(password))  **WARNING: Session Limit:** Each authentication with login credentials counts as a separate session, out of which you have a limited amount. Make sure to save and reuse the `auth` cookie if you are often restarting the program. The provided API libraries automatically save cookies during runtime, but does not persist during restart. While it can be fine to use username/password during development, expect in production to very fast run into the rate-limit and be temporarily blocked from making new sessions until older ones expire. The exact number of simultaneous sessions is unknown/undisclosed.

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

# Configure HTTP basic authorization: authHeader
configuration = vrchatapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: twoFactorAuthCookie
configuration.api_key['twoFactorAuthCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['twoFactorAuthCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Login and/or Get Current User Info
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_current_user: %s\n" % e)
```

* Basic Authentication (authHeader):
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

# Configure HTTP basic authorization: authHeader
configuration = vrchatapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: twoFactorAuthCookie
configuration.api_key['twoFactorAuthCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['twoFactorAuthCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Login and/or Get Current User Info
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_current_user: %s\n" % e)
```

* Api Key Authentication (twoFactorAuthCookie):
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

# Configure HTTP basic authorization: authHeader
configuration = vrchatapi.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: twoFactorAuthCookie
configuration.api_key['twoFactorAuthCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['twoFactorAuthCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Login and/or Get Current User Info
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[authCookie](../README.md#authCookie), [authHeader](../README.md#authHeader), [twoFactorAuthCookie](../README.md#twoFactorAuthCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Successful authentication returns an &#x60;auth&#x60; cookie. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recovery_codes**
> TwoFactorRecoveryCodes get_recovery_codes()

Get 2FA Recovery codes

Gets the OTP (One Time Password) recovery codes for accounts with 2FA-protection enabled.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Get 2FA Recovery codes
        api_response = api_instance.get_recovery_codes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_recovery_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TwoFactorRecoveryCodes**](TwoFactorRecoveryCodes.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the two factor recovery codes |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> Success logout()

Logout

Invalidates the login session.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Logout
        api_response = api_instance.logout()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | OK |  * Set-Cookie - Clears the &#x60;auth&#x60; cookie. <br>  * \0Set-Cookie - Clears the &#x60;age&#x60; cookie. <br>  * \0\0Set-Cookie - Clears the &#x60;tos&#x60; cookie. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_account**
> CurrentUser register_user_account(register_user_account_request)

Register User Account

~~Register a new user account.~~  **DEPRECATED:** Automated creation of accounts has no legitimate public third-party use case, and would be in violation of ToS §13.2: *By using the Platform, you agree not to: i. [...] use the Platform in a manner inconsistent with individual human usage* This endpoint is documented in the interest of completeness

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    register_user_account_request = vrchatapi.RegisterUserAccountRequest() # RegisterUserAccountRequest | 

    try:
        # Register User Account
        api_response = api_instance.register_user_account(register_user_account_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->register_user_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_account_request** | [**RegisterUserAccountRequest**](RegisterUserAccountRequest.md)|  | 

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Successful authentication returns an &#x60;auth&#x60; cookie. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_email_confirmation**
> Success resend_email_confirmation()

Resend Email Confirmation

Requests a resend of pending email address confirmation email

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Resend Email Confirmation
        api_response = api_instance.resend_email_confirmation()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->resend_email_confirmation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | OK |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify2_fa**
> Verify2FAResult verify2_fa(two_factor_auth_code)

Verify 2FA code

Finishes the login sequence with a normal 2FA-generated code for accounts with 2FA-protection enabled.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    two_factor_auth_code = vrchatapi.TwoFactorAuthCode() # TwoFactorAuthCode | 

    try:
        # Verify 2FA code
        api_response = api_instance.verify2_fa(two_factor_auth_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify2_fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_auth_code** | [**TwoFactorAuthCode**](TwoFactorAuthCode.md)|  | 

### Return type

[**Verify2FAResult**](Verify2FAResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Provides a &#x60;twoFactorAuth&#x60; cookie, which can be used to bypasses the 2FA requirement for future logins on the same device. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify2_fa_email_code**
> Verify2FAEmailCodeResult verify2_fa_email_code(two_factor_email_code)

Verify 2FA email code

Finishes the login sequence with an 2FA email code.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    two_factor_email_code = vrchatapi.TwoFactorEmailCode() # TwoFactorEmailCode | 

    try:
        # Verify 2FA email code
        api_response = api_instance.verify2_fa_email_code(two_factor_email_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify2_fa_email_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_email_code** | [**TwoFactorEmailCode**](TwoFactorEmailCode.md)|  | 

### Return type

[**Verify2FAEmailCodeResult**](Verify2FAEmailCodeResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Provides a &#x60;twoFactorAuth&#x60; cookie, which can be used to bypasses the 2FA requirement for future logins on the same device. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_auth_token**
> VerifyAuthTokenResult verify_auth_token()

Verify Auth Token

Verify whether the currently provided Auth Token is valid.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    
    try:
        # Verify Auth Token
        api_response = api_instance.verify_auth_token()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify_auth_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VerifyAuthTokenResult**](VerifyAuthTokenResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns wether a provided auth token is valid or not. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_login_place**
> verify_login_place(token, user_id=user_id)

Verify Login Place

Verifies a login attempt for a user

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    token = 'token_example' # str | Token to verify login attempt.
user_id = 'user_id_example' # str | Filter by UserID. (optional)

    try:
        # Verify Login Place
        api_instance.verify_login_place(token, user_id=user_id)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify_login_place: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token to verify login attempt. | 
 **user_id** | **str**| Filter by UserID. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_pending2_fa**
> Verify2FAResult verify_pending2_fa(two_factor_auth_code)

Verify Pending 2FA code

Finishes sequence for enabling time-based 2FA.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    two_factor_auth_code = vrchatapi.TwoFactorAuthCode() # TwoFactorAuthCode | 

    try:
        # Verify Pending 2FA code
        api_response = api_instance.verify_pending2_fa(two_factor_auth_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify_pending2_fa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_auth_code** | [**TwoFactorAuthCode**](TwoFactorAuthCode.md)|  | 

### Return type

[**Verify2FAResult**](Verify2FAResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Provides a &#x60;twoFactorAuth&#x60; cookie, which can be used to bypasses the 2FA requirement for future logins on the same device. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_recovery_code**
> Verify2FAResult verify_recovery_code(two_factor_auth_code)

Verify 2FA code with Recovery code

Finishes the login sequence with an OTP (One Time Password) recovery code for accounts with 2FA-protection enabled.

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
    api_instance = vrchatapi.AuthenticationApi(api_client)
    two_factor_auth_code = vrchatapi.TwoFactorAuthCode() # TwoFactorAuthCode | 

    try:
        # Verify 2FA code with Recovery code
        api_response = api_instance.verify_recovery_code(two_factor_auth_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->verify_recovery_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **two_factor_auth_code** | [**TwoFactorAuthCode**](TwoFactorAuthCode.md)|  | 

### Return type

[**Verify2FAResult**](Verify2FAResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Set-Cookie - Provides a &#x60;twoFactorAuth&#x60; cookie, which can be used to bypasses the 2FA requirement for future logins on the same device. <br>  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

