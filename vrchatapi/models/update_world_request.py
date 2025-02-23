# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.19.1
    Contact: vrchatapi.lpv0t@aries.fyi
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from vrchatapi.configuration import Configuration


class UpdateWorldRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'asset_url': 'str',
        'asset_version': 'str',
        'author_id': 'str',
        'author_name': 'str',
        'capacity': 'int',
        'description': 'str',
        'image_url': 'str',
        'name': 'str',
        'platform': 'str',
        'release_status': 'ReleaseStatus',
        'tags': 'list[str]',
        'unity_package_url': 'str',
        'unity_version': 'str'
    }

    attribute_map = {
        'asset_url': 'assetUrl',
        'asset_version': 'assetVersion',
        'author_id': 'authorId',
        'author_name': 'authorName',
        'capacity': 'capacity',
        'description': 'description',
        'image_url': 'imageUrl',
        'name': 'name',
        'platform': 'platform',
        'release_status': 'releaseStatus',
        'tags': 'tags',
        'unity_package_url': 'unityPackageUrl',
        'unity_version': 'unityVersion'
    }

    def __init__(self, asset_url=None, asset_version=None, author_id=None, author_name=None, capacity=None, description=None, image_url=None, name=None, platform=None, release_status=None, tags=None, unity_package_url=None, unity_version='5.3.4p1', local_vars_configuration=None):  # noqa: E501
        """UpdateWorldRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._asset_url = None
        self._asset_version = None
        self._author_id = None
        self._author_name = None
        self._capacity = None
        self._description = None
        self._image_url = None
        self._name = None
        self._platform = None
        self._release_status = None
        self._tags = None
        self._unity_package_url = None
        self._unity_version = None
        self.discriminator = None

        if asset_url is not None:
            self.asset_url = asset_url
        if asset_version is not None:
            self.asset_version = asset_version
        if author_id is not None:
            self.author_id = author_id
        if author_name is not None:
            self.author_name = author_name
        if capacity is not None:
            self.capacity = capacity
        if description is not None:
            self.description = description
        if image_url is not None:
            self.image_url = image_url
        if name is not None:
            self.name = name
        if platform is not None:
            self.platform = platform
        if release_status is not None:
            self.release_status = release_status
        if tags is not None:
            self.tags = tags
        if unity_package_url is not None:
            self.unity_package_url = unity_package_url
        if unity_version is not None:
            self.unity_version = unity_version

    @property
    def asset_url(self):
        """Gets the asset_url of this UpdateWorldRequest.  # noqa: E501


        :return: The asset_url of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        """Sets the asset_url of this UpdateWorldRequest.


        :param asset_url: The asset_url of this UpdateWorldRequest.  # noqa: E501
        :type asset_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                asset_url is not None and len(asset_url) < 1):
            raise ValueError("Invalid value for `asset_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._asset_url = asset_url

    @property
    def asset_version(self):
        """Gets the asset_version of this UpdateWorldRequest.  # noqa: E501


        :return: The asset_version of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this UpdateWorldRequest.


        :param asset_version: The asset_version of this UpdateWorldRequest.  # noqa: E501
        :type asset_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                asset_version is not None and len(asset_version) < 1):
            raise ValueError("Invalid value for `asset_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._asset_version = asset_version

    @property
    def author_id(self):
        """Gets the author_id of this UpdateWorldRequest.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The author_id of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this UpdateWorldRequest.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param author_id: The author_id of this UpdateWorldRequest.  # noqa: E501
        :type author_id: str
        """

        self._author_id = author_id

    @property
    def author_name(self):
        """Gets the author_name of this UpdateWorldRequest.  # noqa: E501


        :return: The author_name of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this UpdateWorldRequest.


        :param author_name: The author_name of this UpdateWorldRequest.  # noqa: E501
        :type author_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                author_name is not None and len(author_name) < 1):
            raise ValueError("Invalid value for `author_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._author_name = author_name

    @property
    def capacity(self):
        """Gets the capacity of this UpdateWorldRequest.  # noqa: E501


        :return: The capacity of this UpdateWorldRequest.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this UpdateWorldRequest.


        :param capacity: The capacity of this UpdateWorldRequest.  # noqa: E501
        :type capacity: int
        """
        if (self.local_vars_configuration.client_side_validation and
                capacity is not None and capacity > 40):  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                capacity is not None and capacity < 0):  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def description(self):
        """Gets the description of this UpdateWorldRequest.  # noqa: E501


        :return: The description of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateWorldRequest.


        :param description: The description of this UpdateWorldRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def image_url(self):
        """Gets the image_url of this UpdateWorldRequest.  # noqa: E501


        :return: The image_url of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this UpdateWorldRequest.


        :param image_url: The image_url of this UpdateWorldRequest.  # noqa: E501
        :type image_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) < 1):
            raise ValueError("Invalid value for `image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_url = image_url

    @property
    def name(self):
        """Gets the name of this UpdateWorldRequest.  # noqa: E501


        :return: The name of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateWorldRequest.


        :param name: The name of this UpdateWorldRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def platform(self):
        """Gets the platform of this UpdateWorldRequest.  # noqa: E501

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :return: The platform of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this UpdateWorldRequest.

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :param platform: The platform of this UpdateWorldRequest.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def release_status(self):
        """Gets the release_status of this UpdateWorldRequest.  # noqa: E501


        :return: The release_status of this UpdateWorldRequest.  # noqa: E501
        :rtype: ReleaseStatus
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this UpdateWorldRequest.


        :param release_status: The release_status of this UpdateWorldRequest.  # noqa: E501
        :type release_status: ReleaseStatus
        """

        self._release_status = release_status

    @property
    def tags(self):
        """Gets the tags of this UpdateWorldRequest.  # noqa: E501

           # noqa: E501

        :return: The tags of this UpdateWorldRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateWorldRequest.

           # noqa: E501

        :param tags: The tags of this UpdateWorldRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def unity_package_url(self):
        """Gets the unity_package_url of this UpdateWorldRequest.  # noqa: E501


        :return: The unity_package_url of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._unity_package_url

    @unity_package_url.setter
    def unity_package_url(self, unity_package_url):
        """Sets the unity_package_url of this UpdateWorldRequest.


        :param unity_package_url: The unity_package_url of this UpdateWorldRequest.  # noqa: E501
        :type unity_package_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unity_package_url is not None and len(unity_package_url) < 1):
            raise ValueError("Invalid value for `unity_package_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._unity_package_url = unity_package_url

    @property
    def unity_version(self):
        """Gets the unity_version of this UpdateWorldRequest.  # noqa: E501


        :return: The unity_version of this UpdateWorldRequest.  # noqa: E501
        :rtype: str
        """
        return self._unity_version

    @unity_version.setter
    def unity_version(self, unity_version):
        """Sets the unity_version of this UpdateWorldRequest.


        :param unity_version: The unity_version of this UpdateWorldRequest.  # noqa: E501
        :type unity_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                unity_version is not None and len(unity_version) < 1):
            raise ValueError("Invalid value for `unity_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._unity_version = unity_version

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateWorldRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateWorldRequest):
            return True

        return self.to_dict() != other.to_dict()
