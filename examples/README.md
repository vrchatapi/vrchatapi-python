## Getting Started Examples

### Logging In

```Python
# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode

configuration = vrchatapi.Configuration(
    username = 'username',
    password = 'password',
)

# Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
# Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Set our User-Agent as per VRChat Usage Policy
    api_client.user_agent = "MyProject/1.0 my@email.com"

    # Instantiate instances of API classes
    auth_api = authentication_api.AuthenticationApi(api_client)

    try:
        # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
        current_user = auth_api.get_current_user()
    except UnauthorizedException as e:
        if e.status == 200:
            if "Email 2 Factor Authentication" in e.reason:
                # Step 3.5. Calling email verify2fa if the account has 2FA disabled
                auth_api.verify2_fa_email_code(two_factor_email_code=TwoFactorEmailCode(input("Email 2FA Code: ")))
            elif "2 Factor Authentication" in e.reason:
                # Step 3.5. Calling verify2fa if the account has 2FA enabled
                auth_api.verify2_fa(two_factor_auth_code=TwoFactorAuthCode(input("2FA Code: ")))
            current_user = auth_api.get_current_user()
        else:
            print("Exception when calling API: %s\n", e)
    except vrchatapi.ApiException as e:
        print("Exception when calling API: %s\n", e)

    print("Logged in as:", current_user.display_name)
```

### Using The API

Okay, cool, we can log in, but what now?  

The openapi generator splits each section of the API into it's own class. As such, we need to import each section of the API we want to use seperately. Expanding on our log-in example:

```Python
import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode

# We import the class that corrisponds to the section of the API we want to use
from vrchatapi.api.worlds_api import WorldsApi

configuration = vrchatapi.Configuration(
    username = 'username',
    password = 'password',
)

with vrchatapi.ApiClient(configuration) as api_client:
    api_client.user_agent = "MyProject/1.0 my@email.com"
    auth_api = authentication_api.AuthenticationApi(api_client)

    try:
        current_user = auth_api.get_current_user()
    except UnauthorizedException as e:
        if e.status == 200:
            if "Email 2 Factor Authentication" in e.reason:
                auth_api.verify2_fa_email_code(two_factor_email_code=TwoFactorEmailCode(input("Email 2FA Code: ")))
            elif "2 Factor Authentication" in e.reason:
                auth_api.verify2_fa(two_factor_auth_code=TwoFactorAuthCode(input("2FA Code: ")))
            current_user = auth_api.get_current_user()
        else:
            print("Exception when calling API: %s\n", e)
    except vrchatapi.ApiException as e:
        print("Exception when calling API: %s\n", e)

    print("Logged in as:", current_user.display_name)

    # Now we are logged in, we can init and use the API class :)
    worlds_api = WorldsApi(api_client) # All API section classes require an ApiClient object to be passed!
    active_worlds = worlds_api.get_active_worlds()
```

Here is a list of [all sections of the API:](https://github.com/vrchatapi/vrchatapi-python/tree/main/vrchatapi/api)
- `authentication_api.AuthenticationApi`
- `avatars_api.AvatarsApi`
- `economy_api.EconomyApi`
- `favorites_api.FavoritesApi`
- `files_api.FilesApi`
- `friends_api.FriendsApi`
- `groups_api.GroupsApi`
- `instances_api.InstancesApi`
- `invite_api.InviteApi`
- `notifications_api.NotificationsApi`
- `permissions_api.PermissionsApi`
- `playermoderation_api.PlayermoderationApi`
- `system_api.SystemApi`
- `users_api.UsersApi`
- `worlds_api.WorldsApi`

### No Auth Requests

But some requests don't require Authentication, so how do we use them without logging in?

```Python
import vrchatapi

# We import the class that corrisponds to the section of the API we want to use
from vrchatapi.api.worlds_api import WorldsApi

# We don't add a configuration file/set a username and password
with vrchatapi.ApiClient() as api_client:
    api_client.user_agent = "MyProject/1.0 my@email.com"

    # We don't use the authentication API at all, since we don't need to
    world_api = WorldsApi(api_client)
    world = world_api.get_world("wrld_000000000-0000-0000-0000-000000000000")

    print(f"World `{world.name}` was made by `{world.author_name}` ({world.author_id})")
```