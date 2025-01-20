# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.9
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


class PerformanceLimiterInfo(object):
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
        'allowed': 'bool',
        'max_seats': 'int'
    }

    attribute_map = {
        'allowed': 'allowed',
        'max_seats': 'maxSeats'
    }

    def __init__(self, allowed=None, max_seats=None, local_vars_configuration=None):  # noqa: E501
        """PerformanceLimiterInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._allowed = None
        self._max_seats = None
        self.discriminator = None

        self.allowed = allowed
        self.max_seats = max_seats

    @property
    def allowed(self):
        """Gets the allowed of this PerformanceLimiterInfo.  # noqa: E501


        :return: The allowed of this PerformanceLimiterInfo.  # noqa: E501
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this PerformanceLimiterInfo.


        :param allowed: The allowed of this PerformanceLimiterInfo.  # noqa: E501
        :type allowed: bool
        """
        if self.local_vars_configuration.client_side_validation and allowed is None:  # noqa: E501
            raise ValueError("Invalid value for `allowed`, must not be `None`")  # noqa: E501

        self._allowed = allowed

    @property
    def max_seats(self):
        """Gets the max_seats of this PerformanceLimiterInfo.  # noqa: E501

        Maximum amount of seats. -1 means no limit.  # noqa: E501

        :return: The max_seats of this PerformanceLimiterInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_seats

    @max_seats.setter
    def max_seats(self, max_seats):
        """Sets the max_seats of this PerformanceLimiterInfo.

        Maximum amount of seats. -1 means no limit.  # noqa: E501

        :param max_seats: The max_seats of this PerformanceLimiterInfo.  # noqa: E501
        :type max_seats: int
        """
        if self.local_vars_configuration.client_side_validation and max_seats is None:  # noqa: E501
            raise ValueError("Invalid value for `max_seats`, must not be `None`")  # noqa: E501

        self._max_seats = max_seats

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
        if not isinstance(other, PerformanceLimiterInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceLimiterInfo):
            return True

        return self.to_dict() != other.to_dict()
