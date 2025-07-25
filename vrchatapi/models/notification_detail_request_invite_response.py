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


class NotificationDetailRequestInviteResponse(object):
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
        'in_response_to': 'str',
        'request_message': 'str'
    }

    attribute_map = {
        'in_response_to': 'inResponseTo',
        'request_message': 'requestMessage'
    }

    def __init__(self, in_response_to=None, request_message=None, local_vars_configuration=None):  # noqa: E501
        """NotificationDetailRequestInviteResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._in_response_to = None
        self._request_message = None
        self.discriminator = None

        self.in_response_to = in_response_to
        if request_message is not None:
            self.request_message = request_message

    @property
    def in_response_to(self):
        """Gets the in_response_to of this NotificationDetailRequestInviteResponse.  # noqa: E501


        :return: The in_response_to of this NotificationDetailRequestInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._in_response_to

    @in_response_to.setter
    def in_response_to(self, in_response_to):
        """Sets the in_response_to of this NotificationDetailRequestInviteResponse.


        :param in_response_to: The in_response_to of this NotificationDetailRequestInviteResponse.  # noqa: E501
        :type in_response_to: str
        """
        if self.local_vars_configuration.client_side_validation and in_response_to is None:  # noqa: E501
            raise ValueError("Invalid value for `in_response_to`, must not be `None`")  # noqa: E501

        self._in_response_to = in_response_to

    @property
    def request_message(self):
        """Gets the request_message of this NotificationDetailRequestInviteResponse.  # noqa: E501

        Used when using InviteMessage Slot.  # noqa: E501

        :return: The request_message of this NotificationDetailRequestInviteResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this NotificationDetailRequestInviteResponse.

        Used when using InviteMessage Slot.  # noqa: E501

        :param request_message: The request_message of this NotificationDetailRequestInviteResponse.  # noqa: E501
        :type request_message: str
        """

        self._request_message = request_message

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
        if not isinstance(other, NotificationDetailRequestInviteResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationDetailRequestInviteResponse):
            return True

        return self.to_dict() != other.to_dict()
