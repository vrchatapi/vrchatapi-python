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


class LimitedUserGroups(object):
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
        'icon_id': 'str',
        'icon_url': 'str',
        'banner_id': 'str',
        'banner_url': 'str',
        'privacy': 'str',
        'last_post_created_at': 'datetime',
        'owner_id': 'str',
        'member_count': 'int',
        'group_id': 'str',
        'member_visibility': 'str',
        'is_representing': 'bool',
        'mutual_group': 'bool',
        'last_post_read_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'short_code': 'shortCode',
        'discriminator': 'discriminator',
        'description': 'description',
        'icon_id': 'iconId',
        'icon_url': 'iconUrl',
        'banner_id': 'bannerId',
        'banner_url': 'bannerUrl',
        'privacy': 'privacy',
        'last_post_created_at': 'lastPostCreatedAt',
        'owner_id': 'ownerId',
        'member_count': 'memberCount',
        'group_id': 'groupId',
        'member_visibility': 'memberVisibility',
        'is_representing': 'isRepresenting',
        'mutual_group': 'mutualGroup',
        'last_post_read_at': 'lastPostReadAt'
    }

    def __init__(self, id=None, name=None, short_code=None, discriminator=None, description=None, icon_id=None, icon_url=None, banner_id=None, banner_url=None, privacy=None, last_post_created_at=None, owner_id=None, member_count=None, group_id=None, member_visibility=None, is_representing=None, mutual_group=None, last_post_read_at=None, local_vars_configuration=None):  # noqa: E501
        """LimitedUserGroups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._short_code = None
        self._discriminator = None
        self._description = None
        self._icon_id = None
        self._icon_url = None
        self._banner_id = None
        self._banner_url = None
        self._privacy = None
        self._last_post_created_at = None
        self._owner_id = None
        self._member_count = None
        self._group_id = None
        self._member_visibility = None
        self._is_representing = None
        self._mutual_group = None
        self._last_post_read_at = None
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
        self.icon_id = icon_id
        self.icon_url = icon_url
        self.banner_id = banner_id
        self.banner_url = banner_url
        if privacy is not None:
            self.privacy = privacy
        self.last_post_created_at = last_post_created_at
        if owner_id is not None:
            self.owner_id = owner_id
        if member_count is not None:
            self.member_count = member_count
        if group_id is not None:
            self.group_id = group_id
        if member_visibility is not None:
            self.member_visibility = member_visibility
        if is_representing is not None:
            self.is_representing = is_representing
        if mutual_group is not None:
            self.mutual_group = mutual_group
        self.last_post_read_at = last_post_read_at

    @property
    def id(self):
        """Gets the id of this LimitedUserGroups.  # noqa: E501


        :return: The id of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LimitedUserGroups.


        :param id: The id of this LimitedUserGroups.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LimitedUserGroups.  # noqa: E501


        :return: The name of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LimitedUserGroups.


        :param name: The name of this LimitedUserGroups.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def short_code(self):
        """Gets the short_code of this LimitedUserGroups.  # noqa: E501


        :return: The short_code of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this LimitedUserGroups.


        :param short_code: The short_code of this LimitedUserGroups.  # noqa: E501
        :type short_code: str
        """

        self._short_code = short_code

    @property
    def discriminator(self):
        """Gets the discriminator of this LimitedUserGroups.  # noqa: E501


        :return: The discriminator of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._discriminator

    @discriminator.setter
    def discriminator(self, discriminator):
        """Sets the discriminator of this LimitedUserGroups.


        :param discriminator: The discriminator of this LimitedUserGroups.  # noqa: E501
        :type discriminator: str
        """

        self._discriminator = discriminator

    @property
    def description(self):
        """Gets the description of this LimitedUserGroups.  # noqa: E501


        :return: The description of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LimitedUserGroups.


        :param description: The description of this LimitedUserGroups.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def icon_id(self):
        """Gets the icon_id of this LimitedUserGroups.  # noqa: E501


        :return: The icon_id of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this LimitedUserGroups.


        :param icon_id: The icon_id of this LimitedUserGroups.  # noqa: E501
        :type icon_id: str
        """

        self._icon_id = icon_id

    @property
    def icon_url(self):
        """Gets the icon_url of this LimitedUserGroups.  # noqa: E501


        :return: The icon_url of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this LimitedUserGroups.


        :param icon_url: The icon_url of this LimitedUserGroups.  # noqa: E501
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def banner_id(self):
        """Gets the banner_id of this LimitedUserGroups.  # noqa: E501


        :return: The banner_id of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._banner_id

    @banner_id.setter
    def banner_id(self, banner_id):
        """Sets the banner_id of this LimitedUserGroups.


        :param banner_id: The banner_id of this LimitedUserGroups.  # noqa: E501
        :type banner_id: str
        """

        self._banner_id = banner_id

    @property
    def banner_url(self):
        """Gets the banner_url of this LimitedUserGroups.  # noqa: E501


        :return: The banner_url of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._banner_url

    @banner_url.setter
    def banner_url(self, banner_url):
        """Sets the banner_url of this LimitedUserGroups.


        :param banner_url: The banner_url of this LimitedUserGroups.  # noqa: E501
        :type banner_url: str
        """

        self._banner_url = banner_url

    @property
    def privacy(self):
        """Gets the privacy of this LimitedUserGroups.  # noqa: E501


        :return: The privacy of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this LimitedUserGroups.


        :param privacy: The privacy of this LimitedUserGroups.  # noqa: E501
        :type privacy: str
        """

        self._privacy = privacy

    @property
    def last_post_created_at(self):
        """Gets the last_post_created_at of this LimitedUserGroups.  # noqa: E501


        :return: The last_post_created_at of this LimitedUserGroups.  # noqa: E501
        :rtype: datetime
        """
        return self._last_post_created_at

    @last_post_created_at.setter
    def last_post_created_at(self, last_post_created_at):
        """Sets the last_post_created_at of this LimitedUserGroups.


        :param last_post_created_at: The last_post_created_at of this LimitedUserGroups.  # noqa: E501
        :type last_post_created_at: datetime
        """

        self._last_post_created_at = last_post_created_at

    @property
    def owner_id(self):
        """Gets the owner_id of this LimitedUserGroups.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this LimitedUserGroups.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this LimitedUserGroups.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def member_count(self):
        """Gets the member_count of this LimitedUserGroups.  # noqa: E501


        :return: The member_count of this LimitedUserGroups.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this LimitedUserGroups.


        :param member_count: The member_count of this LimitedUserGroups.  # noqa: E501
        :type member_count: int
        """

        self._member_count = member_count

    @property
    def group_id(self):
        """Gets the group_id of this LimitedUserGroups.  # noqa: E501


        :return: The group_id of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this LimitedUserGroups.


        :param group_id: The group_id of this LimitedUserGroups.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def member_visibility(self):
        """Gets the member_visibility of this LimitedUserGroups.  # noqa: E501


        :return: The member_visibility of this LimitedUserGroups.  # noqa: E501
        :rtype: str
        """
        return self._member_visibility

    @member_visibility.setter
    def member_visibility(self, member_visibility):
        """Sets the member_visibility of this LimitedUserGroups.


        :param member_visibility: The member_visibility of this LimitedUserGroups.  # noqa: E501
        :type member_visibility: str
        """

        self._member_visibility = member_visibility

    @property
    def is_representing(self):
        """Gets the is_representing of this LimitedUserGroups.  # noqa: E501


        :return: The is_representing of this LimitedUserGroups.  # noqa: E501
        :rtype: bool
        """
        return self._is_representing

    @is_representing.setter
    def is_representing(self, is_representing):
        """Sets the is_representing of this LimitedUserGroups.


        :param is_representing: The is_representing of this LimitedUserGroups.  # noqa: E501
        :type is_representing: bool
        """

        self._is_representing = is_representing

    @property
    def mutual_group(self):
        """Gets the mutual_group of this LimitedUserGroups.  # noqa: E501


        :return: The mutual_group of this LimitedUserGroups.  # noqa: E501
        :rtype: bool
        """
        return self._mutual_group

    @mutual_group.setter
    def mutual_group(self, mutual_group):
        """Sets the mutual_group of this LimitedUserGroups.


        :param mutual_group: The mutual_group of this LimitedUserGroups.  # noqa: E501
        :type mutual_group: bool
        """

        self._mutual_group = mutual_group

    @property
    def last_post_read_at(self):
        """Gets the last_post_read_at of this LimitedUserGroups.  # noqa: E501


        :return: The last_post_read_at of this LimitedUserGroups.  # noqa: E501
        :rtype: datetime
        """
        return self._last_post_read_at

    @last_post_read_at.setter
    def last_post_read_at(self, last_post_read_at):
        """Sets the last_post_read_at of this LimitedUserGroups.


        :param last_post_read_at: The last_post_read_at of this LimitedUserGroups.  # noqa: E501
        :type last_post_read_at: datetime
        """

        self._last_post_read_at = last_post_read_at

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
        if not isinstance(other, LimitedUserGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LimitedUserGroups):
            return True

        return self.to_dict() != other.to_dict()
