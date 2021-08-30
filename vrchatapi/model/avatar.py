"""
    VRChat API Documentation

    ![VRChat API Banner](https://vrchatapi.github.io/assets/img/api_banner_1500x400.png)  # Welcome to the VRChat API  Before we begin, we would like to state this is a **COMMUNITY DRIVEN PROJECT**. This means that everything you read on here was written by the community itself and is **not** officially supported by VRChat. The documentation is provided \"AS IS\", and any action you take towards VRChat is completely your own responsibility.  The documentation and additional libraries SHALL ONLY be used for applications interacting with VRChat's API in accordance with their [Terms of Service](https://github.com/VRChatAPI), and MUST NOT be used for modifying the client, \"avatar ripping\", or other illegal activities. Malicious usage or spamming the API may result in account termination. Certain parts of the API are also more sensitive than others, for example moderation, so please tread extra carefully and read the warnings when present.  ![Tupper Policy on API](https://i.imgur.com/yLlW7Ok.png)  Finally, use of the API using applications other than the approved methods (website, VRChat application, Unity SDK) is not officially supported. VRChat provides no guarantee or support for external applications using the API. Access to API endpoints may break **at any time, without notice**. Therefore, please **do not ping** VRChat Staff in the VRChat Discord if you are having API problems, as they do not provide API support. We will make a best effort in keeping this documentation and associated language libraries up to date, but things might be outdated or missing. If you find that something is no longer valid, please contact us on Discord or [create an issue](https://github.com/vrchatapi/specification/issues) and tell us so we can fix it.  # Getting Started  The VRChat API can be used to programmatically retrieve or update information regarding your profile, friends, avatars, worlds and more. The API consists of two parts, \"Photon\" which is only used in-game, and the \"Web API\" which is used by both the game and the website. This documentation focuses only on the Web API.  The API is designed around the REST ideology, providing semi-simple and usually predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise.  <div class=\"callout callout-error\">   <strong>🛑 Warning! Do not touch Photon!</strong><br>   Photon is only used by the in-game client and should <b>not</b> be touched. Doing so may result in permanent account termination. </div>  <div class=\"callout callout-info\">   <strong>ℹ️ API Key and Authentication</strong><br>   The API Key has always been the same and is currently <code>JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26</code>.   Read <a href=\"#tag--authentication\">Authentication</a> for how to log in. </div>  # Using the API  For simply exploring what the API can do it is strongly recommended to download [Insomnia](https://insomnia.rest/download), a free and open-source API client that's great for sending requests to the API in an orderly fashion. Insomnia allows you to send data in the format that's required for VRChat's API. It is also possible to try out the API in your browser, by first logging in at [vrchat.com/home](https://vrchat.com/home/) and then going to [vrchat.com/api/1/auth/user](https://vrchat.com/api/1/auth/user), but the information will be much harder to work with.  For more permanent operation such as software development it is instead recommended to use one of the existing language SDKs. This community project maintains API libraries in several languages, which allows you to interact with the API with simple function calls rather than having to implement the HTTP protocol yourself. Most of these libraries are automatically generated from the API specification, sometimes with additional helpful wrapper code to make usage easier. This allows them to be almost automatically updated and expanded upon as soon as a new feature is introduced in the specification itself. The libraries can be found on [GitHub](https://github.com/vrchatapi) or following:  * [NodeJS (JavaScript)](https://www.npmjs.com/package/vrchat) * [Dart](https://pub.dev/packages/vrchat_dart) * [Rust](https://crates.io/crates/vrchatapi) * [C#](https://github.com/vrchatapi/vrchatapi-csharp) * [Python](https://github.com/vrchatapi/VRChatPython)  # Pagination  Most endpoints enforce pagination, meaning they will only return 10 entries by default, and never more than 100.<br> Using both the limit and offset parameters allows you to easily paginate through a large number of objects.  | Query Parameter | Type | Description | | ----------|--|------- | | `limit` | integer  | The number of objects to return. This value often defaults to 10. Highest limit is always 100.| | `offset` | integer  | A zero-based offset from the default object sorting.|  If a request returns fewer objects than the `limit` parameter, there are no more items available to return.  # Contribution  Do you want to get involved in the documentation effort? Do you want to help improve one of the language API libraries? This project is an [OPEN Open Source Project](https://openopensource.org)! This means that individuals making significant and valuable contributions are given commit-access to the project. It also means we are very open and welcoming of new people making contributions, unlike some more guarded open-source projects.  [![Discord](https://img.shields.io/static/v1?label=vrchatapi&message=discord&color=blueviolet&style=for-the-badge)](https://discord.gg/qjZE9C9fkB)  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from vrchatapi.exceptions import ApiAttributeError


def lazy_import():
    from vrchatapi.model.avatar_id import AvatarID
    from vrchatapi.model.avatar_unity_package_url_object import AvatarUnityPackageUrlObject
    from vrchatapi.model.release_status import ReleaseStatus
    from vrchatapi.model.tag import Tag
    from vrchatapi.model.unity_package import UnityPackage
    globals()['AvatarID'] = AvatarID
    globals()['AvatarUnityPackageUrlObject'] = AvatarUnityPackageUrlObject
    globals()['ReleaseStatus'] = ReleaseStatus
    globals()['Tag'] = Tag
    globals()['UnityPackage'] = UnityPackage


class Avatar(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('author_name',): {
            'min_length': 1,
        },
        ('description',): {
            'min_length': 0,
        },
        ('image_url',): {
            'min_length': 1,
        },
        ('name',): {
            'min_length': 1,
        },
        ('thumbnail_image_url',): {
            'min_length': 1,
        },
        ('unity_packages',): {
            'min_items': 1,
        },
        ('version',): {
            'inclusive_minimum': 0,
        },
        ('asset_url',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'author_id': (str,),  # noqa: E501
            'author_name': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'featured': (bool,),  # noqa: E501
            'id': (AvatarID,),  # noqa: E501
            'image_url': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'release_status': (ReleaseStatus,),  # noqa: E501
            'tags': ([Tag],),  # noqa: E501
            'thumbnail_image_url': (str,),  # noqa: E501
            'unity_packages': ([UnityPackage],),  # noqa: E501
            'unity_package_url': (str,),  # noqa: E501
            'unity_package_url_object': (AvatarUnityPackageUrlObject,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'version': (float,),  # noqa: E501
            'asset_url': (str,),  # noqa: E501
            'asset_url_object': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'author_id': 'authorId',  # noqa: E501
        'author_name': 'authorName',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'description': 'description',  # noqa: E501
        'featured': 'featured',  # noqa: E501
        'id': 'id',  # noqa: E501
        'image_url': 'imageUrl',  # noqa: E501
        'name': 'name',  # noqa: E501
        'release_status': 'releaseStatus',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'thumbnail_image_url': 'thumbnailImageUrl',  # noqa: E501
        'unity_packages': 'unityPackages',  # noqa: E501
        'unity_package_url': 'unityPackageUrl',  # noqa: E501
        'unity_package_url_object': 'unityPackageUrlObject',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'version': 'version',  # noqa: E501
        'asset_url': 'assetUrl',  # noqa: E501
        'asset_url_object': 'assetUrlObject',  # noqa: E501
    }

    read_only_vars = {
        'author_id',  # noqa: E501
        'author_name',  # noqa: E501
        'created_at',  # noqa: E501
        'version',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, author_id, author_name, created_at, description, id, image_url, name, release_status, tags, thumbnail_image_url, unity_packages, unity_package_url, unity_package_url_object, updated_at, *args, **kwargs):  # noqa: E501
        """Avatar - a model defined in OpenAPI

        Args:
            author_id (str):
            author_name (str):
            created_at (datetime):
            description (str):
            id (AvatarID):
            image_url (str):
            name (str):
            release_status (ReleaseStatus):
            tags ([Tag]):
            thumbnail_image_url (str):
            unity_packages ([UnityPackage]):
            unity_package_url (str):
            unity_package_url_object (AvatarUnityPackageUrlObject):
            updated_at (datetime):

        Keyword Args:
            featured (bool): defaults to False  # noqa: E501
            version (float): defaults to 0  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            asset_url (str): Not present from general serach `/avatars`, only on specific requests `/avatars/{avatarId}`.. [optional]  # noqa: E501
            asset_url_object ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Not present from general serach `/avatars`, only on specific requests `/avatars/{avatarId}`. **Deprecation:** `Object` has unknown usage/fields, and is always empty. Use normal `Url` field instead.. [optional]  # noqa: E501
        """

        featured = kwargs.get('featured', False)
        version = kwargs.get('version', 0)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.author_id = author_id
        self.author_name = author_name
        self.created_at = created_at
        self.description = description
        self.featured = featured
        self.id = id
        self.image_url = image_url
        self.name = name
        self.release_status = release_status
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_packages = unity_packages
        self.unity_package_url = unity_package_url
        self.unity_package_url_object = unity_package_url_object
        self.updated_at = updated_at
        self.version = version
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, description, id, image_url, name, release_status, tags, thumbnail_image_url, unity_packages, unity_package_url, unity_package_url_object, updated_at, *args, **kwargs):  # noqa: E501
        """Avatar - a model defined in OpenAPI

            description (str):
            id (AvatarID):
            image_url (str):
            name (str):
            release_status (ReleaseStatus):
            tags ([Tag]):
            thumbnail_image_url (str):
            unity_packages ([UnityPackage]):
            unity_package_url (str):
            unity_package_url_object (AvatarUnityPackageUrlObject):
            updated_at (datetime):
        Keyword Args:
            featured (bool): defaults to False  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            asset_url (str): Not present from general serach `/avatars`, only on specific requests `/avatars/{avatarId}`.. [optional]  # noqa: E501
            asset_url_object ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Not present from general serach `/avatars`, only on specific requests `/avatars/{avatarId}`. **Deprecation:** `Object` has unknown usage/fields, and is always empty. Use normal `Url` field instead.. [optional]  # noqa: E501
        """

        featured = kwargs.get('featured', False)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.description = description
        self.featured = featured
        self.id = id
        self.image_url = image_url
        self.name = name
        self.release_status = release_status
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_packages = unity_packages
        self.unity_package_url = unity_package_url
        self.unity_package_url_object = unity_package_url_object
        self.updated_at = updated_at
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
