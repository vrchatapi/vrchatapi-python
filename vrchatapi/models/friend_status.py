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


class FriendStatus(object):
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
        'incoming_request': 'bool',
        'is_friend': 'bool',
        'outgoing_request': 'bool'
    }

    attribute_map = {
        'incoming_request': 'incomingRequest',
        'is_friend': 'isFriend',
        'outgoing_request': 'outgoingRequest'
    }

    def __init__(self, incoming_request=False, is_friend=False, outgoing_request=False, local_vars_configuration=None):  # noqa: E501
        """FriendStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._incoming_request = None
        self._is_friend = None
        self._outgoing_request = None
        self.discriminator = None

        self.incoming_request = incoming_request
        self.is_friend = is_friend
        self.outgoing_request = outgoing_request

    @property
    def incoming_request(self):
        """Gets the incoming_request of this FriendStatus.  # noqa: E501


        :return: The incoming_request of this FriendStatus.  # noqa: E501
        :rtype: bool
        """
        return self._incoming_request

    @incoming_request.setter
    def incoming_request(self, incoming_request):
        """Sets the incoming_request of this FriendStatus.


        :param incoming_request: The incoming_request of this FriendStatus.  # noqa: E501
        :type incoming_request: bool
        """
        if self.local_vars_configuration.client_side_validation and incoming_request is None:  # noqa: E501
            raise ValueError("Invalid value for `incoming_request`, must not be `None`")  # noqa: E501

        self._incoming_request = incoming_request

    @property
    def is_friend(self):
        """Gets the is_friend of this FriendStatus.  # noqa: E501


        :return: The is_friend of this FriendStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_friend

    @is_friend.setter
    def is_friend(self, is_friend):
        """Sets the is_friend of this FriendStatus.


        :param is_friend: The is_friend of this FriendStatus.  # noqa: E501
        :type is_friend: bool
        """
        if self.local_vars_configuration.client_side_validation and is_friend is None:  # noqa: E501
            raise ValueError("Invalid value for `is_friend`, must not be `None`")  # noqa: E501

        self._is_friend = is_friend

    @property
    def outgoing_request(self):
        """Gets the outgoing_request of this FriendStatus.  # noqa: E501


        :return: The outgoing_request of this FriendStatus.  # noqa: E501
        :rtype: bool
        """
        return self._outgoing_request

    @outgoing_request.setter
    def outgoing_request(self, outgoing_request):
        """Sets the outgoing_request of this FriendStatus.


        :param outgoing_request: The outgoing_request of this FriendStatus.  # noqa: E501
        :type outgoing_request: bool
        """
        if self.local_vars_configuration.client_side_validation and outgoing_request is None:  # noqa: E501
            raise ValueError("Invalid value for `outgoing_request`, must not be `None`")  # noqa: E501

        self._outgoing_request = outgoing_request

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
        if not isinstance(other, FriendStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FriendStatus):
            return True

        return self.to_dict() != other.to_dict()
