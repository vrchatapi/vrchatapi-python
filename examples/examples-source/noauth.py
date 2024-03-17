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