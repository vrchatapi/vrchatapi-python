# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.12.0
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


class GroupLimitedMember(object):
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
        'is_representing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'user_id': 'userId',
        'is_representing': 'isRepresenting'
    }

    def __init__(self, id=None, group_id=None, user_id=None, is_representing=False, local_vars_configuration=None):  # noqa: E501
        """GroupLimitedMember - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._user_id = None
        self._is_representing = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if user_id is not None:
            self.user_id = user_id
        if is_representing is not None:
            self.is_representing = is_representing

    @property
    def id(self):
        """Gets the id of this GroupLimitedMember.  # noqa: E501


        :return: The id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupLimitedMember.


        :param id: The id of this GroupLimitedMember.  # noqa: E501
        :type id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'gmem_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/gmem_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupLimitedMember.  # noqa: E501


        :return: The group_id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupLimitedMember.


        :param group_id: The group_id of this GroupLimitedMember.  # noqa: E501
        :type group_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                group_id is not None and not re.search(r'grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', group_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `group_id`, must be a follow pattern or equal to `/grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._group_id = group_id

    @property
    def user_id(self):
        """Gets the user_id of this GroupLimitedMember.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The user_id of this GroupLimitedMember.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this GroupLimitedMember.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param user_id: The user_id of this GroupLimitedMember.  # noqa: E501
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def is_representing(self):
        """Gets the is_representing of this GroupLimitedMember.  # noqa: E501


        :return: The is_representing of this GroupLimitedMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_representing

    @is_representing.setter
    def is_representing(self, is_representing):
        """Sets the is_representing of this GroupLimitedMember.


        :param is_representing: The is_representing of this GroupLimitedMember.  # noqa: E501
        :type is_representing: bool
        """

        self._is_representing = is_representing

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
        if not isinstance(other, GroupLimitedMember):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupLimitedMember):
            return True

        return self.to_dict() != other.to_dict()
