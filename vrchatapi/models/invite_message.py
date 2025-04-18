# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.19.2
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


class InviteMessage(object):
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
        'can_be_updated': 'bool',
        'id': 'str',
        'message': 'str',
        'message_type': 'InviteMessageType',
        'remaining_cooldown_minutes': 'int',
        'slot': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'can_be_updated': 'canBeUpdated',
        'id': 'id',
        'message': 'message',
        'message_type': 'messageType',
        'remaining_cooldown_minutes': 'remainingCooldownMinutes',
        'slot': 'slot',
        'updated_at': 'updatedAt'
    }

    def __init__(self, can_be_updated=True, id=None, message=None, message_type=None, remaining_cooldown_minutes=0, slot=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """InviteMessage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._can_be_updated = None
        self._id = None
        self._message = None
        self._message_type = None
        self._remaining_cooldown_minutes = None
        self._slot = None
        self._updated_at = None
        self.discriminator = None

        self.can_be_updated = can_be_updated
        self.id = id
        self.message = message
        self.message_type = message_type
        self.remaining_cooldown_minutes = remaining_cooldown_minutes
        self.slot = slot
        self.updated_at = updated_at

    @property
    def can_be_updated(self):
        """Gets the can_be_updated of this InviteMessage.  # noqa: E501


        :return: The can_be_updated of this InviteMessage.  # noqa: E501
        :rtype: bool
        """
        return self._can_be_updated

    @can_be_updated.setter
    def can_be_updated(self, can_be_updated):
        """Sets the can_be_updated of this InviteMessage.


        :param can_be_updated: The can_be_updated of this InviteMessage.  # noqa: E501
        :type can_be_updated: bool
        """
        if self.local_vars_configuration.client_side_validation and can_be_updated is None:  # noqa: E501
            raise ValueError("Invalid value for `can_be_updated`, must not be `None`")  # noqa: E501

        self._can_be_updated = can_be_updated

    @property
    def id(self):
        """Gets the id of this InviteMessage.  # noqa: E501


        :return: The id of this InviteMessage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InviteMessage.


        :param id: The id of this InviteMessage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def message(self):
        """Gets the message of this InviteMessage.  # noqa: E501


        :return: The message of this InviteMessage.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InviteMessage.


        :param message: The message of this InviteMessage.  # noqa: E501
        :type message: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def message_type(self):
        """Gets the message_type of this InviteMessage.  # noqa: E501


        :return: The message_type of this InviteMessage.  # noqa: E501
        :rtype: InviteMessageType
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this InviteMessage.


        :param message_type: The message_type of this InviteMessage.  # noqa: E501
        :type message_type: InviteMessageType
        """
        if self.local_vars_configuration.client_side_validation and message_type is None:  # noqa: E501
            raise ValueError("Invalid value for `message_type`, must not be `None`")  # noqa: E501

        self._message_type = message_type

    @property
    def remaining_cooldown_minutes(self):
        """Gets the remaining_cooldown_minutes of this InviteMessage.  # noqa: E501

        Changes to 60 when updated, although probably server-side configurable.  # noqa: E501

        :return: The remaining_cooldown_minutes of this InviteMessage.  # noqa: E501
        :rtype: int
        """
        return self._remaining_cooldown_minutes

    @remaining_cooldown_minutes.setter
    def remaining_cooldown_minutes(self, remaining_cooldown_minutes):
        """Sets the remaining_cooldown_minutes of this InviteMessage.

        Changes to 60 when updated, although probably server-side configurable.  # noqa: E501

        :param remaining_cooldown_minutes: The remaining_cooldown_minutes of this InviteMessage.  # noqa: E501
        :type remaining_cooldown_minutes: int
        """
        if self.local_vars_configuration.client_side_validation and remaining_cooldown_minutes is None:  # noqa: E501
            raise ValueError("Invalid value for `remaining_cooldown_minutes`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                remaining_cooldown_minutes is not None and remaining_cooldown_minutes < 0):  # noqa: E501
            raise ValueError("Invalid value for `remaining_cooldown_minutes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._remaining_cooldown_minutes = remaining_cooldown_minutes

    @property
    def slot(self):
        """Gets the slot of this InviteMessage.  # noqa: E501


        :return: The slot of this InviteMessage.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this InviteMessage.


        :param slot: The slot of this InviteMessage.  # noqa: E501
        :type slot: int
        """
        if self.local_vars_configuration.client_side_validation and slot is None:  # noqa: E501
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slot is not None and slot > 11):  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value less than or equal to `11`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                slot is not None and slot < 0):  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value greater than or equal to `0`")  # noqa: E501

        self._slot = slot

    @property
    def updated_at(self):
        """Gets the updated_at of this InviteMessage.  # noqa: E501


        :return: The updated_at of this InviteMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InviteMessage.


        :param updated_at: The updated_at of this InviteMessage.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, InviteMessage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteMessage):
            return True

        return self.to_dict() != other.to_dict()
