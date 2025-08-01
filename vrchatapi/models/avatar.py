# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.20.1
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


class Avatar(object):
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
        'acknowledgements': 'str',
        'asset_url': 'str',
        'asset_url_object': 'object',
        'author_id': 'str',
        'author_name': 'str',
        'created_at': 'datetime',
        'description': 'str',
        'featured': 'bool',
        'highest_price': 'int',
        'id': 'str',
        'image_url': 'str',
        'lock': 'bool',
        'lowest_price': 'int',
        'name': 'str',
        'performance': 'AvatarPerformance',
        'product_id': 'str',
        'published_listings': 'list[AvatarPublishedListingsInner]',
        'release_status': 'ReleaseStatus',
        'searchable': 'bool',
        'styles': 'AvatarStyles',
        'tags': 'list[str]',
        'thumbnail_image_url': 'str',
        'unity_package_url': 'str',
        'unity_package_url_object': 'AvatarUnityPackageUrlObject',
        'unity_packages': 'list[UnityPackage]',
        'updated_at': 'datetime',
        'version': 'int'
    }

    attribute_map = {
        'acknowledgements': 'acknowledgements',
        'asset_url': 'assetUrl',
        'asset_url_object': 'assetUrlObject',
        'author_id': 'authorId',
        'author_name': 'authorName',
        'created_at': 'created_at',
        'description': 'description',
        'featured': 'featured',
        'highest_price': 'highestPrice',
        'id': 'id',
        'image_url': 'imageUrl',
        'lock': 'lock',
        'lowest_price': 'lowestPrice',
        'name': 'name',
        'performance': 'performance',
        'product_id': 'productId',
        'published_listings': 'publishedListings',
        'release_status': 'releaseStatus',
        'searchable': 'searchable',
        'styles': 'styles',
        'tags': 'tags',
        'thumbnail_image_url': 'thumbnailImageUrl',
        'unity_package_url': 'unityPackageUrl',
        'unity_package_url_object': 'unityPackageUrlObject',
        'unity_packages': 'unityPackages',
        'updated_at': 'updated_at',
        'version': 'version'
    }

    def __init__(self, acknowledgements=None, asset_url=None, asset_url_object=None, author_id=None, author_name=None, created_at=None, description=None, featured=False, highest_price=None, id=None, image_url=None, lock=None, lowest_price=None, name=None, performance=None, product_id=None, published_listings=None, release_status=None, searchable=False, styles=None, tags=None, thumbnail_image_url=None, unity_package_url=None, unity_package_url_object=None, unity_packages=None, updated_at=None, version=0, local_vars_configuration=None):  # noqa: E501
        """Avatar - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._acknowledgements = None
        self._asset_url = None
        self._asset_url_object = None
        self._author_id = None
        self._author_name = None
        self._created_at = None
        self._description = None
        self._featured = None
        self._highest_price = None
        self._id = None
        self._image_url = None
        self._lock = None
        self._lowest_price = None
        self._name = None
        self._performance = None
        self._product_id = None
        self._published_listings = None
        self._release_status = None
        self._searchable = None
        self._styles = None
        self._tags = None
        self._thumbnail_image_url = None
        self._unity_package_url = None
        self._unity_package_url_object = None
        self._unity_packages = None
        self._updated_at = None
        self._version = None
        self.discriminator = None

        if acknowledgements is not None:
            self.acknowledgements = acknowledgements
        if asset_url is not None:
            self.asset_url = asset_url
        if asset_url_object is not None:
            self.asset_url_object = asset_url_object
        self.author_id = author_id
        self.author_name = author_name
        self.created_at = created_at
        self.description = description
        self.featured = featured
        if highest_price is not None:
            self.highest_price = highest_price
        self.id = id
        self.image_url = image_url
        if lock is not None:
            self.lock = lock
        if lowest_price is not None:
            self.lowest_price = lowest_price
        self.name = name
        self.performance = performance
        if product_id is not None:
            self.product_id = product_id
        if published_listings is not None:
            self.published_listings = published_listings
        self.release_status = release_status
        if searchable is not None:
            self.searchable = searchable
        self.styles = styles
        self.tags = tags
        self.thumbnail_image_url = thumbnail_image_url
        self.unity_package_url = unity_package_url
        self.unity_package_url_object = unity_package_url_object
        self.unity_packages = unity_packages
        self.updated_at = updated_at
        self.version = version

    @property
    def acknowledgements(self):
        """Gets the acknowledgements of this Avatar.  # noqa: E501


        :return: The acknowledgements of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._acknowledgements

    @acknowledgements.setter
    def acknowledgements(self, acknowledgements):
        """Sets the acknowledgements of this Avatar.


        :param acknowledgements: The acknowledgements of this Avatar.  # noqa: E501
        :type acknowledgements: str
        """

        self._acknowledgements = acknowledgements

    @property
    def asset_url(self):
        """Gets the asset_url of this Avatar.  # noqa: E501

        Not present from general search `/avatars`, only on specific requests `/avatars/{avatarId}`.  # noqa: E501

        :return: The asset_url of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._asset_url

    @asset_url.setter
    def asset_url(self, asset_url):
        """Sets the asset_url of this Avatar.

        Not present from general search `/avatars`, only on specific requests `/avatars/{avatarId}`.  # noqa: E501

        :param asset_url: The asset_url of this Avatar.  # noqa: E501
        :type asset_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                asset_url is not None and len(asset_url) < 1):
            raise ValueError("Invalid value for `asset_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._asset_url = asset_url

    @property
    def asset_url_object(self):
        """Gets the asset_url_object of this Avatar.  # noqa: E501

        Not present from general search `/avatars`, only on specific requests `/avatars/{avatarId}`. **Deprecation:** `Object` has unknown usage/fields, and is always empty. Use normal `Url` field instead.  # noqa: E501

        :return: The asset_url_object of this Avatar.  # noqa: E501
        :rtype: object
        """
        return self._asset_url_object

    @asset_url_object.setter
    def asset_url_object(self, asset_url_object):
        """Sets the asset_url_object of this Avatar.

        Not present from general search `/avatars`, only on specific requests `/avatars/{avatarId}`. **Deprecation:** `Object` has unknown usage/fields, and is always empty. Use normal `Url` field instead.  # noqa: E501

        :param asset_url_object: The asset_url_object of this Avatar.  # noqa: E501
        :type asset_url_object: object
        """

        self._asset_url_object = asset_url_object

    @property
    def author_id(self):
        """Gets the author_id of this Avatar.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The author_id of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this Avatar.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param author_id: The author_id of this Avatar.  # noqa: E501
        :type author_id: str
        """
        if self.local_vars_configuration.client_side_validation and author_id is None:  # noqa: E501
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def author_name(self):
        """Gets the author_name of this Avatar.  # noqa: E501


        :return: The author_name of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this Avatar.


        :param author_name: The author_name of this Avatar.  # noqa: E501
        :type author_name: str
        """
        if self.local_vars_configuration.client_side_validation and author_name is None:  # noqa: E501
            raise ValueError("Invalid value for `author_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                author_name is not None and len(author_name) < 1):
            raise ValueError("Invalid value for `author_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._author_name = author_name

    @property
    def created_at(self):
        """Gets the created_at of this Avatar.  # noqa: E501


        :return: The created_at of this Avatar.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Avatar.


        :param created_at: The created_at of this Avatar.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this Avatar.  # noqa: E501


        :return: The description of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Avatar.


        :param description: The description of this Avatar.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def featured(self):
        """Gets the featured of this Avatar.  # noqa: E501


        :return: The featured of this Avatar.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this Avatar.


        :param featured: The featured of this Avatar.  # noqa: E501
        :type featured: bool
        """
        if self.local_vars_configuration.client_side_validation and featured is None:  # noqa: E501
            raise ValueError("Invalid value for `featured`, must not be `None`")  # noqa: E501

        self._featured = featured

    @property
    def highest_price(self):
        """Gets the highest_price of this Avatar.  # noqa: E501


        :return: The highest_price of this Avatar.  # noqa: E501
        :rtype: int
        """
        return self._highest_price

    @highest_price.setter
    def highest_price(self, highest_price):
        """Sets the highest_price of this Avatar.


        :param highest_price: The highest_price of this Avatar.  # noqa: E501
        :type highest_price: int
        """

        self._highest_price = highest_price

    @property
    def id(self):
        """Gets the id of this Avatar.  # noqa: E501


        :return: The id of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Avatar.


        :param id: The id of this Avatar.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_url(self):
        """Gets the image_url of this Avatar.  # noqa: E501


        :return: The image_url of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Avatar.


        :param image_url: The image_url of this Avatar.  # noqa: E501
        :type image_url: str
        """
        if self.local_vars_configuration.client_side_validation and image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `image_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) < 1):
            raise ValueError("Invalid value for `image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_url = image_url

    @property
    def lock(self):
        """Gets the lock of this Avatar.  # noqa: E501


        :return: The lock of this Avatar.  # noqa: E501
        :rtype: bool
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this Avatar.


        :param lock: The lock of this Avatar.  # noqa: E501
        :type lock: bool
        """

        self._lock = lock

    @property
    def lowest_price(self):
        """Gets the lowest_price of this Avatar.  # noqa: E501


        :return: The lowest_price of this Avatar.  # noqa: E501
        :rtype: int
        """
        return self._lowest_price

    @lowest_price.setter
    def lowest_price(self, lowest_price):
        """Sets the lowest_price of this Avatar.


        :param lowest_price: The lowest_price of this Avatar.  # noqa: E501
        :type lowest_price: int
        """

        self._lowest_price = lowest_price

    @property
    def name(self):
        """Gets the name of this Avatar.  # noqa: E501


        :return: The name of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Avatar.


        :param name: The name of this Avatar.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def performance(self):
        """Gets the performance of this Avatar.  # noqa: E501


        :return: The performance of this Avatar.  # noqa: E501
        :rtype: AvatarPerformance
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this Avatar.


        :param performance: The performance of this Avatar.  # noqa: E501
        :type performance: AvatarPerformance
        """
        if self.local_vars_configuration.client_side_validation and performance is None:  # noqa: E501
            raise ValueError("Invalid value for `performance`, must not be `None`")  # noqa: E501

        self._performance = performance

    @property
    def product_id(self):
        """Gets the product_id of this Avatar.  # noqa: E501


        :return: The product_id of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Avatar.


        :param product_id: The product_id of this Avatar.  # noqa: E501
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def published_listings(self):
        """Gets the published_listings of this Avatar.  # noqa: E501


        :return: The published_listings of this Avatar.  # noqa: E501
        :rtype: list[AvatarPublishedListingsInner]
        """
        return self._published_listings

    @published_listings.setter
    def published_listings(self, published_listings):
        """Sets the published_listings of this Avatar.


        :param published_listings: The published_listings of this Avatar.  # noqa: E501
        :type published_listings: list[AvatarPublishedListingsInner]
        """

        self._published_listings = published_listings

    @property
    def release_status(self):
        """Gets the release_status of this Avatar.  # noqa: E501


        :return: The release_status of this Avatar.  # noqa: E501
        :rtype: ReleaseStatus
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        """Sets the release_status of this Avatar.


        :param release_status: The release_status of this Avatar.  # noqa: E501
        :type release_status: ReleaseStatus
        """
        if self.local_vars_configuration.client_side_validation and release_status is None:  # noqa: E501
            raise ValueError("Invalid value for `release_status`, must not be `None`")  # noqa: E501

        self._release_status = release_status

    @property
    def searchable(self):
        """Gets the searchable of this Avatar.  # noqa: E501


        :return: The searchable of this Avatar.  # noqa: E501
        :rtype: bool
        """
        return self._searchable

    @searchable.setter
    def searchable(self, searchable):
        """Sets the searchable of this Avatar.


        :param searchable: The searchable of this Avatar.  # noqa: E501
        :type searchable: bool
        """

        self._searchable = searchable

    @property
    def styles(self):
        """Gets the styles of this Avatar.  # noqa: E501


        :return: The styles of this Avatar.  # noqa: E501
        :rtype: AvatarStyles
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this Avatar.


        :param styles: The styles of this Avatar.  # noqa: E501
        :type styles: AvatarStyles
        """
        if self.local_vars_configuration.client_side_validation and styles is None:  # noqa: E501
            raise ValueError("Invalid value for `styles`, must not be `None`")  # noqa: E501

        self._styles = styles

    @property
    def tags(self):
        """Gets the tags of this Avatar.  # noqa: E501

           # noqa: E501

        :return: The tags of this Avatar.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Avatar.

           # noqa: E501

        :param tags: The tags of this Avatar.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def thumbnail_image_url(self):
        """Gets the thumbnail_image_url of this Avatar.  # noqa: E501


        :return: The thumbnail_image_url of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_image_url

    @thumbnail_image_url.setter
    def thumbnail_image_url(self, thumbnail_image_url):
        """Sets the thumbnail_image_url of this Avatar.


        :param thumbnail_image_url: The thumbnail_image_url of this Avatar.  # noqa: E501
        :type thumbnail_image_url: str
        """
        if self.local_vars_configuration.client_side_validation and thumbnail_image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `thumbnail_image_url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                thumbnail_image_url is not None and len(thumbnail_image_url) < 1):
            raise ValueError("Invalid value for `thumbnail_image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._thumbnail_image_url = thumbnail_image_url

    @property
    def unity_package_url(self):
        """Gets the unity_package_url of this Avatar.  # noqa: E501


        :return: The unity_package_url of this Avatar.  # noqa: E501
        :rtype: str
        """
        return self._unity_package_url

    @unity_package_url.setter
    def unity_package_url(self, unity_package_url):
        """Sets the unity_package_url of this Avatar.


        :param unity_package_url: The unity_package_url of this Avatar.  # noqa: E501
        :type unity_package_url: str
        """
        if self.local_vars_configuration.client_side_validation and unity_package_url is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_package_url`, must not be `None`")  # noqa: E501

        self._unity_package_url = unity_package_url

    @property
    def unity_package_url_object(self):
        """Gets the unity_package_url_object of this Avatar.  # noqa: E501


        :return: The unity_package_url_object of this Avatar.  # noqa: E501
        :rtype: AvatarUnityPackageUrlObject
        """
        return self._unity_package_url_object

    @unity_package_url_object.setter
    def unity_package_url_object(self, unity_package_url_object):
        """Sets the unity_package_url_object of this Avatar.


        :param unity_package_url_object: The unity_package_url_object of this Avatar.  # noqa: E501
        :type unity_package_url_object: AvatarUnityPackageUrlObject
        """
        if self.local_vars_configuration.client_side_validation and unity_package_url_object is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_package_url_object`, must not be `None`")  # noqa: E501

        self._unity_package_url_object = unity_package_url_object

    @property
    def unity_packages(self):
        """Gets the unity_packages of this Avatar.  # noqa: E501


        :return: The unity_packages of this Avatar.  # noqa: E501
        :rtype: list[UnityPackage]
        """
        return self._unity_packages

    @unity_packages.setter
    def unity_packages(self, unity_packages):
        """Sets the unity_packages of this Avatar.


        :param unity_packages: The unity_packages of this Avatar.  # noqa: E501
        :type unity_packages: list[UnityPackage]
        """
        if self.local_vars_configuration.client_side_validation and unity_packages is None:  # noqa: E501
            raise ValueError("Invalid value for `unity_packages`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                unity_packages is not None and len(unity_packages) < 1):
            raise ValueError("Invalid value for `unity_packages`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._unity_packages = unity_packages

    @property
    def updated_at(self):
        """Gets the updated_at of this Avatar.  # noqa: E501


        :return: The updated_at of this Avatar.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Avatar.


        :param updated_at: The updated_at of this Avatar.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def version(self):
        """Gets the version of this Avatar.  # noqa: E501


        :return: The version of this Avatar.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Avatar.


        :param version: The version of this Avatar.  # noqa: E501
        :type version: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and version < 0):  # noqa: E501
            raise ValueError("Invalid value for `version`, must be a value greater than or equal to `0`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, Avatar):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Avatar):
            return True

        return self.to_dict() != other.to_dict()
