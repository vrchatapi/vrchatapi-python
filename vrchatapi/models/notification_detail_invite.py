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


class NotificationDetailInvite(object):
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
        'invite_message': 'str',
        'world_id': 'str',
        'world_name': 'str'
    }

    attribute_map = {
        'invite_message': 'inviteMessage',
        'world_id': 'worldId',
        'world_name': 'worldName'
    }

    def __init__(self, invite_message=None, world_id=None, world_name=None, local_vars_configuration=None):  # noqa: E501
        """NotificationDetailInvite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._invite_message = None
        self._world_id = None
        self._world_name = None
        self.discriminator = None

        if invite_message is not None:
            self.invite_message = invite_message
        self.world_id = world_id
        self.world_name = world_name

    @property
    def invite_message(self):
        """Gets the invite_message of this NotificationDetailInvite.  # noqa: E501


        :return: The invite_message of this NotificationDetailInvite.  # noqa: E501
        :rtype: str
        """
        return self._invite_message

    @invite_message.setter
    def invite_message(self, invite_message):
        """Sets the invite_message of this NotificationDetailInvite.


        :param invite_message: The invite_message of this NotificationDetailInvite.  # noqa: E501
        :type invite_message: str
        """

        self._invite_message = invite_message

    @property
    def world_id(self):
        """Gets the world_id of this NotificationDetailInvite.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The world_id of this NotificationDetailInvite.  # noqa: E501
        :rtype: str
        """
        return self._world_id

    @world_id.setter
    def world_id(self, world_id):
        """Sets the world_id of this NotificationDetailInvite.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param world_id: The world_id of this NotificationDetailInvite.  # noqa: E501
        :type world_id: str
        """
        if self.local_vars_configuration.client_side_validation and world_id is None:  # noqa: E501
            raise ValueError("Invalid value for `world_id`, must not be `None`")  # noqa: E501

        self._world_id = world_id

    @property
    def world_name(self):
        """Gets the world_name of this NotificationDetailInvite.  # noqa: E501


        :return: The world_name of this NotificationDetailInvite.  # noqa: E501
        :rtype: str
        """
        return self._world_name

    @world_name.setter
    def world_name(self, world_name):
        """Sets the world_name of this NotificationDetailInvite.


        :param world_name: The world_name of this NotificationDetailInvite.  # noqa: E501
        :type world_name: str
        """
        if self.local_vars_configuration.client_side_validation and world_name is None:  # noqa: E501
            raise ValueError("Invalid value for `world_name`, must not be `None`")  # noqa: E501

        self._world_name = world_name

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
        if not isinstance(other, NotificationDetailInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationDetailInvite):
            return True

        return self.to_dict() != other.to_dict()
