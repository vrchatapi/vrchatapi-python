import vrchatapi
from vrchatapi.api import authentication_api
from vrchatapi.exceptions import UnauthorizedException
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode

configuration = vrchatapi.Configuration(
    username='username',
    password='password',
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

    cookie_jar = api_client.rest_client.cookie_jar._cookies["vrchat.com"]["/"]
    print("Logged in as:", current_user.display_name)
    print("auth: " + cookie_jar["auth"].value)
    print("twoFactorAuth: " + cookie_jar["twoFactorAuth"].value)
