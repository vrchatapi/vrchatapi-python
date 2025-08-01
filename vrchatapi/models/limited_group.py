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


class LimitedGroup(object):
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
        'id': 'str',
        'name': 'str',
        'short_code': 'str',
        'discriminator': 'str',
        'description': 'str',
        'icon_url': 'str',
        'banner_url': 'str',
        'owner_id': 'str',
        'rules': 'str',
        'icon_id': 'str',
        'banner_id': 'str',
        'member_count': 'int',
        'tags': 'list[str]',
        'created_at': 'datetime',
        'membership_status': 'GroupMemberStatus',
        'is_searchable': 'bool',
        'galleries': 'list[GroupGallery]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'short_code': 'shortCode',
        'discriminator': 'discriminator',
        'description': 'description',
        'icon_url': 'iconUrl',
        'banner_url': 'bannerUrl',
        'owner_id': 'ownerId',
        'rules': 'rules',
        'icon_id': 'iconId',
        'banner_id': 'bannerId',
        'member_count': 'memberCount',
        'tags': 'tags',
        'created_at': 'createdAt',
        'membership_status': 'membershipStatus',
        'is_searchable': 'isSearchable',
        'galleries': 'galleries'
    }

    def __init__(self, id=None, name=None, short_code=None, discriminator=None, description=None, icon_url=None, banner_url=None, owner_id=None, rules=None, icon_id=None, banner_id=None, member_count=None, tags=None, created_at=None, membership_status=None, is_searchable=None, galleries=None, local_vars_configuration=None):  # noqa: E501
        """LimitedGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._short_code = None
        self._discriminator = None
        self._description = None
        self._icon_url = None
        self._banner_url = None
        self._owner_id = None
        self._rules = None
        self._icon_id = None
        self._banner_id = None
        self._member_count = None
        self._tags = None
        self._created_at = None
        self._membership_status = None
        self._is_searchable = None
        self._galleries = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if short_code is not None:
            self.short_code = short_code
        if discriminator is not None:
            self.discriminator = discriminator
        if description is not None:
            self.description = description
        self.icon_url = icon_url
        self.banner_url = banner_url
        if owner_id is not None:
            self.owner_id = owner_id
        self.rules = rules
        self.icon_id = icon_id
        self.banner_id = banner_id
        if member_count is not None:
            self.member_count = member_count
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if membership_status is not None:
            self.membership_status = membership_status
        if is_searchable is not None:
            self.is_searchable = is_searchable
        if galleries is not None:
            self.galleries = galleries

    @property
    def id(self):
        """Gets the id of this LimitedGroup.  # noqa: E501


        :return: The id of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LimitedGroup.


        :param id: The id of this LimitedGroup.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LimitedGroup.  # noqa: E501


        :return: The name of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LimitedGroup.


        :param name: The name of this LimitedGroup.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def short_code(self):
        """Gets the short_code of this LimitedGroup.  # noqa: E501


        :return: The short_code of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this LimitedGroup.


        :param short_code: The short_code of this LimitedGroup.  # noqa: E501
        :type short_code: str
        """

        self._short_code = short_code

    @property
    def discriminator(self):
        """Gets the discriminator of this LimitedGroup.  # noqa: E501


        :return: The discriminator of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this LimitedGroup.


        :param discriminator: The discriminator of this LimitedGroup.  # noqa: E501
        :type discriminator: str
        """

        self._discriminator = discriminator

    @property
    def description(self):
        """Gets the description of this LimitedGroup.  # noqa: E501


        :return: The description of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LimitedGroup.


        :param description: The description of this LimitedGroup.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon_url(self):
        """Gets the icon_url of this LimitedGroup.  # noqa: E501


        :return: The icon_url of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this LimitedGroup.


        :param icon_url: The icon_url of this LimitedGroup.  # noqa: E501
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def banner_url(self):
        """Gets the banner_url of this LimitedGroup.  # noqa: E501


        :return: The banner_url of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._banner_url

    @banner_url.setter
    def banner_url(self, banner_url):
        """Sets the banner_url of this LimitedGroup.


        :param banner_url: The banner_url of this LimitedGroup.  # noqa: E501
        :type banner_url: str
        """

        self._banner_url = banner_url

    @property
    def owner_id(self):
        """Gets the owner_id of this LimitedGroup.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this LimitedGroup.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this LimitedGroup.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def rules(self):
        """Gets the rules of this LimitedGroup.  # noqa: E501


        :return: The rules of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this LimitedGroup.


        :param rules: The rules of this LimitedGroup.  # noqa: E501
        :type rules: str
        """

        self._rules = rules

    @property
    def icon_id(self):
        """Gets the icon_id of this LimitedGroup.  # noqa: E501


        :return: The icon_id of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this LimitedGroup.


        :param icon_id: The icon_id of this LimitedGroup.  # noqa: E501
        :type icon_id: str
        """

        self._icon_id = icon_id

    @property
    def banner_id(self):
        """Gets the banner_id of this LimitedGroup.  # noqa: E501


        :return: The banner_id of this LimitedGroup.  # noqa: E501
        :rtype: str
        """
        return self._banner_id

    @banner_id.setter
    def banner_id(self, banner_id):
        """Sets the banner_id of this LimitedGroup.


        :param banner_id: The banner_id of this LimitedGroup.  # noqa: E501
        :type banner_id: str
        """

        self._banner_id = banner_id

    @property
    def member_count(self):
        """Gets the member_count of this LimitedGroup.  # noqa: E501


        :return: The member_count of this LimitedGroup.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this LimitedGroup.


        :param member_count: The member_count of this LimitedGroup.  # noqa: E501
        :type member_count: int
        """

        self._member_count = member_count

    @property
    def tags(self):
        """Gets the tags of this LimitedGroup.  # noqa: E501

           # noqa: E501

        :return: The tags of this LimitedGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LimitedGroup.

           # noqa: E501

        :param tags: The tags of this LimitedGroup.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this LimitedGroup.  # noqa: E501


        :return: The created_at of this LimitedGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LimitedGroup.


        :param created_at: The created_at of this LimitedGroup.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def membership_status(self):
        """Gets the membership_status of this LimitedGroup.  # noqa: E501


        :return: The membership_status of this LimitedGroup.  # noqa: E501
        :rtype: GroupMemberStatus
        """
        return self._membership_status

    @membership_status.setter
    def membership_status(self, membership_status):
        """Sets the membership_status of this LimitedGroup.


        :param membership_status: The membership_status of this LimitedGroup.  # noqa: E501
        :type membership_status: GroupMemberStatus
        """

        self._membership_status = membership_status

    @property
    def is_searchable(self):
        """Gets the is_searchable of this LimitedGroup.  # noqa: E501


        :return: The is_searchable of this LimitedGroup.  # noqa: E501
        :rtype: bool
        """
        return self._is_searchable

    @is_searchable.setter
    def is_searchable(self, is_searchable):
        """Sets the is_searchable of this LimitedGroup.


        :param is_searchable: The is_searchable of this LimitedGroup.  # noqa: E501
        :type is_searchable: bool
        """

        self._is_searchable = is_searchable

    @property
    def galleries(self):
        """Gets the galleries of this LimitedGroup.  # noqa: E501

           # noqa: E501

        :return: The galleries of this LimitedGroup.  # noqa: E501
        :rtype: list[GroupGallery]
        """
        return self._galleries

    @galleries.setter
    def galleries(self, galleries):
        """Sets the galleries of this LimitedGroup.

           # noqa: E501

        :param galleries: The galleries of this LimitedGroup.  # noqa: E501
        :type galleries: list[GroupGallery]
        """

        self._galleries = galleries

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
        if not isinstance(other, LimitedGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedGroup):
            return True

        return self.to_dict() != other.to_dict()
