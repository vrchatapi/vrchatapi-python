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


class RequestInviteRequest(object):
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
        'message_slot': 'int'
    }

    attribute_map = {
        'message_slot': 'messageSlot'
    }

    def __init__(self, message_slot=None, local_vars_configuration=None):  # noqa: E501
        """RequestInviteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._message_slot = None
        self.discriminator = None

        if message_slot is not None:
            self.message_slot = message_slot

    @property
    def message_slot(self):
        """Gets the message_slot of this RequestInviteRequest.  # noqa: E501


        :return: The message_slot of this RequestInviteRequest.  # noqa: E501
        :rtype: int
        """
        return self._message_slot

    @message_slot.setter
    def message_slot(self, message_slot):
        """Sets the message_slot of this RequestInviteRequest.


        :param message_slot: The message_slot of this RequestInviteRequest.  # noqa: E501
        :type message_slot: int
        """
        if (self.local_vars_configuration.client_side_validation and
                message_slot is not None and message_slot > 11):  # noqa: E501
            raise ValueError("Invalid value for `message_slot`, must be a value less than or equal to `11`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message_slot is not None and message_slot < 0):  # noqa: E501
            raise ValueError("Invalid value for `message_slot`, must be a value greater than or equal to `0`")  # noqa: E501

        self._message_slot = message_slot

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
        if not isinstance(other, RequestInviteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestInviteRequest):
            return True

        return self.to_dict() != other.to_dict()
