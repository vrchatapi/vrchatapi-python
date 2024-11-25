# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode

configuration = vrchatapi.Configuration(
    username='username',
    password='password',
)

# Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
# Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Set our User-Agent as per VRChat Usage Policy
    api_client.user_agent = "ExampleProgram/0.0.1 my@email.com"

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
