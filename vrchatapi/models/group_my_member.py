# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.1
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


class GroupMyMember(object):
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
        'group_id': 'str',
        'user_id': 'str',
        'role_ids': 'list[str]',
        'manager_notes': 'str',
        'membership_status': 'str',
        'is_subscribed_to_announcements': 'bool',
        'visibility': 'str',
        'is_representing': 'bool',
        'joined_at': 'datetime',
        'banned_at': 'str',
        'has2_fa': 'bool',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'user_id': 'userId',
        'role_ids': 'roleIds',
        'manager_notes': 'managerNotes',
        'membership_status': 'membershipStatus',
        'is_subscribed_to_announcements': 'isSubscribedToAnnouncements',
        'visibility': 'visibility',
        'is_representing': 'isRepresenting',
        'joined_at': 'joinedAt',
        'banned_at': 'bannedAt',
        'has2_fa': 'has2FA',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, group_id=None, user_id=None, role_ids=None, manager_notes=None, membership_status=None, is_subscribed_to_announcements=True, visibility=None, is_representing=False, joined_at=None, banned_at=None, has2_fa=False, permissions=None, local_vars_configuration=None):  # noqa: E501
        """GroupMyMember - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._user_id = None
        self._role_ids = None
        self._manager_notes = None
        self._membership_status = None
        self._is_subscribed_to_announcements = None
        self._visibility = None
        self._is_representing = None
        self._joined_at = None
        self._banned_at = None
        self._has2_fa = None
        self._permissions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if user_id is not None:
            self.user_id = user_id
        if role_ids is not None:
            self.role_ids = role_ids
        if manager_notes is not None:
            self.manager_notes = manager_notes
        if membership_status is not None:
            self.membership_status = membership_status
        if is_subscribed_to_announcements is not None:
            self.is_subscribed_to_announcements = is_subscribed_to_announcements
        if visibility is not None:
            self.visibility = visibility
        if is_representing is not None:
            self.is_representing = is_representing
        if joined_at is not None:
            self.joined_at = joined_at
        self.banned_at = banned_at
        if has2_fa is not None:
            self.has2_fa = has2_fa
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this GroupMyMember.  # noqa: E501


        :return: The id of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupMyMember.


        :param id: The id of this GroupMyMember.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupMyMember.  # noqa: E501


        :return: The group_id of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupMyMember.


        :param group_id: The group_id of this GroupMyMember.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def user_id(self):
        """Gets the user_id of this GroupMyMember.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The user_id of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupMyMember.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param user_id: The user_id of this GroupMyMember.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def role_ids(self):
        """Gets the role_ids of this GroupMyMember.  # noqa: E501


        :return: The role_ids of this GroupMyMember.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this GroupMyMember.


        :param role_ids: The role_ids of this GroupMyMember.  # noqa: E501
        :type role_ids: list[str]
        """

        self._role_ids = role_ids

    @property
    def manager_notes(self):
        """Gets the manager_notes of this GroupMyMember.  # noqa: E501


        :return: The manager_notes of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._manager_notes

    @manager_notes.setter
    def manager_notes(self, manager_notes):
        """Sets the manager_notes of this GroupMyMember.


        :param manager_notes: The manager_notes of this GroupMyMember.  # noqa: E501
        :type manager_notes: str
        """

        self._manager_notes = manager_notes

    @property
    def membership_status(self):
        """Gets the membership_status of this GroupMyMember.  # noqa: E501


        :return: The membership_status of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._membership_status

    @membership_status.setter
    def membership_status(self, membership_status):
        """Sets the membership_status of this GroupMyMember.


        :param membership_status: The membership_status of this GroupMyMember.  # noqa: E501
        :type membership_status: str
        """

        self._membership_status = membership_status

    @property
    def is_subscribed_to_announcements(self):
        """Gets the is_subscribed_to_announcements of this GroupMyMember.  # noqa: E501


        :return: The is_subscribed_to_announcements of this GroupMyMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribed_to_announcements

    @is_subscribed_to_announcements.setter
    def is_subscribed_to_announcements(self, is_subscribed_to_announcements):
        """Sets the is_subscribed_to_announcements of this GroupMyMember.


        :param is_subscribed_to_announcements: The is_subscribed_to_announcements of this GroupMyMember.  # noqa: E501
        :type is_subscribed_to_announcements: bool
        """

        self._is_subscribed_to_announcements = is_subscribed_to_announcements

    @property
    def visibility(self):
        """Gets the visibility of this GroupMyMember.  # noqa: E501


        :return: The visibility of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GroupMyMember.


        :param visibility: The visibility of this GroupMyMember.  # noqa: E501
        :type visibility: str
        """

        self._visibility = visibility

    @property
    def is_representing(self):
        """Gets the is_representing of this GroupMyMember.  # noqa: E501


        :return: The is_representing of this GroupMyMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_representing

    @is_representing.setter
    def is_representing(self, is_representing):
        """Sets the is_representing of this GroupMyMember.


        :param is_representing: The is_representing of this GroupMyMember.  # noqa: E501
        :type is_representing: bool
        """

        self._is_representing = is_representing

    @property
    def joined_at(self):
        """Gets the joined_at of this GroupMyMember.  # noqa: E501


        :return: The joined_at of this GroupMyMember.  # noqa: E501
        :rtype: datetime
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        """Sets the joined_at of this GroupMyMember.


        :param joined_at: The joined_at of this GroupMyMember.  # noqa: E501
        :type joined_at: datetime
        """

        self._joined_at = joined_at

    @property
    def banned_at(self):
        """Gets the banned_at of this GroupMyMember.  # noqa: E501


        :return: The banned_at of this GroupMyMember.  # noqa: E501
        :rtype: str
        """
        return self._banned_at

    @banned_at.setter
    def banned_at(self, banned_at):
        """Sets the banned_at of this GroupMyMember.


        :param banned_at: The banned_at of this GroupMyMember.  # noqa: E501
        :type banned_at: str
        """

        self._banned_at = banned_at

    @property
    def has2_fa(self):
        """Gets the has2_fa of this GroupMyMember.  # noqa: E501


        :return: The has2_fa of this GroupMyMember.  # noqa: E501
        :rtype: bool
        """
        return self._has2_fa

    @has2_fa.setter
    def has2_fa(self, has2_fa):
        """Sets the has2_fa of this GroupMyMember.


        :param has2_fa: The has2_fa of this GroupMyMember.  # noqa: E501
        :type has2_fa: bool
        """

        self._has2_fa = has2_fa

    @property
    def permissions(self):
        """Gets the permissions of this GroupMyMember.  # noqa: E501


        :return: The permissions of this GroupMyMember.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupMyMember.


        :param permissions: The permissions of this GroupMyMember.  # noqa: E501
        :type permissions: list[str]
        """

        self._permissions = permissions

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
        if not isinstance(other, GroupMyMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupMyMember):
            return True

        return self.to_dict() != other.to_dict()
