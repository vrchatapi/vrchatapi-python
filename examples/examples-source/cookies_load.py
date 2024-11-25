import vrchatapi
from http.cookiejar import Cookie

from vrchatapi.api import authentication_api


def make_cookie(name, value):
    return Cookie(0, name, value,
                  None, False,
                  "api.vrchat.cloud", True, False,
                  "/", False,
                  False,
                  173106866300,
                  False,
                  None,
                  None, {})


configuration = vrchatapi.Configuration(
    username='username',
    password='password',
)

with vrchatapi.ApiClient(configuration) as api_client:
    api_client.user_agent = "MyProject/1.0 my@email.com"
    api_client.rest_client.cookie_jar.set_cookie(
        make_cookie("auth", "[AUTH_COOKIE_HERE]"))
    api_client.rest_client.cookie_jar.set_cookie(
        make_cookie("twoFactorAuth", "[TWO_FACTOR_AUTH_COOKIE_HERE]"))

    auth_api = authentication_api.AuthenticationApi(api_client)
    current_user = auth_api.get_current_user()
    print("Logged in as:", current_user.display_name)
