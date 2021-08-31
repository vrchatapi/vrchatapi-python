"""
    VRChat API Documentation


![](https://github.com/vrchatapi/vrchatapi.github.io/blob/master/assets/img/lang/lang_python_banner_1500x300.png?raw=true)

# VRChat API Library for Python

A Python client to interact with the unofficial VRChat API. Supports all REST calls specified in the [API specification](https://github.com/vrchatapi/specification).

## Disclaimer

This is the official response of the VRChat Team (from Tupper more specifically) on the usage of the VRChat API.

> Use of the API using applications other than the approved methods (website, VRChat application) are not officially supported. You may use the API for your own application, but keep these guidelines in mind:
> * We do not provide documentation or support for the API.
> * Do not make queries to the API more than once per 60 seconds.
> * Abuse of the API may result in account termination.
> * Access to API endpoints may break at any given time, with no warning.

As stated, this documentation was not created with the help of the official VRChat team. Therefore this documentation is not an official documentation of the VRChat API and may not be always up to date with the latest versions. If you find that a page or endpoint is not longer valid please create an issue and tell us so we can fix it.

## Getting Started

First add the package to to your project:
```bash
pip install vrchatapi
```

Below is an example on how to login to the API and fetch your own user information.

```python
# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api, users_api

configuration = vrchatapi.Configuration(
    username = 'username',
    password = 'password',
)

# Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
# Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:

    # Instantiate instances of API classes
    auth_api = authentication_api.AuthenticationApi(api_client)

    try:
        # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
        current_user = auth_api.get_current_user()
        print("Logged in as:", current_user.display_name)
    except vrchatapi.ApiException as e:
        print("Exception when calling API: %s\n", e)
```

See [example.py](https://github.com/vrchatapi/vrchatapi-python/blob/main/example.py) for more example usage on getting started.

## Contributing

Contributions are welcome, but do not add features that should be handled by the OpenAPI specification.

Join the [Discord server](https://discord.gg/Ge2APMhPfD) to get in touch with us.

    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "vrchatapi"
VERSION = "1.1.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="VRChat API Library for Python",
    author="Unofficial VRChat API Documentation Project",
    author_email="me@ruby.js.org",
    url="",
    keywords=["vrchat", "vrchatapi", "vrc"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="The MIT License (MIT)",
long_description_content_type="text/markdown",
    long_description="""\

![](https://github.com/vrchatapi/vrchatapi.github.io/blob/master/assets/img/lang/lang_python_banner_1500x300.png?raw=true)

# VRChat API Library for Python

A Python client to interact with the unofficial VRChat API. Supports all REST calls specified in the [API specification](https://github.com/vrchatapi/specification).

## Disclaimer

This is the official response of the VRChat Team (from Tupper more specifically) on the usage of the VRChat API.

> Use of the API using applications other than the approved methods (website, VRChat application) are not officially supported. You may use the API for your own application, but keep these guidelines in mind:
> * We do not provide documentation or support for the API.
> * Do not make queries to the API more than once per 60 seconds.
> * Abuse of the API may result in account termination.
> * Access to API endpoints may break at any given time, with no warning.

As stated, this documentation was not created with the help of the official VRChat team. Therefore this documentation is not an official documentation of the VRChat API and may not be always up to date with the latest versions. If you find that a page or endpoint is not longer valid please create an issue and tell us so we can fix it.

## Getting Started

First add the package to to your project:
```bash
pip install vrchatapi
```

Below is an example on how to login to the API and fetch your own user information.

```python
# Step 1. We begin with creating a Configuration, which contains the username and password for authentication.
import vrchatapi
from vrchatapi.api import authentication_api, users_api

configuration = vrchatapi.Configuration(
    username = 'username',
    password = 'password',
)

# Step 2. VRChat consists of several API's (WorldsApi, UsersApi, FilesApi, NotificationsApi, FriendsApi, etc...)
# Here we enter a context of the API Client and instantiate the Authentication API which is required for logging in.

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:

    # Instantiate instances of API classes
    auth_api = authentication_api.AuthenticationApi(api_client)

    try:
        # Step 3. Calling getCurrentUser on Authentication API logs you in if the user isn't already logged in.
        current_user = auth_api.get_current_user()
        print("Logged in as:", current_user.display_name)
    except vrchatapi.ApiException as e:
        print("Exception when calling API: %s\n", e)
```

See [example.py](https://github.com/vrchatapi/vrchatapi-python/blob/main/example.py) for more example usage on getting started.

## Contributing

Contributions are welcome, but do not add features that should be handled by the OpenAPI specification.

Join the [Discord server](https://discord.gg/Ge2APMhPfD) to get in touch with us.
    """
)
