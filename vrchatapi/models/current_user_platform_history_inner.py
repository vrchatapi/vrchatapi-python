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


class CurrentUserPlatformHistoryInner(object):
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
        'is_mobile': 'bool',
        'platform': 'str',
        'recorded': 'datetime'
    }

    attribute_map = {
        'is_mobile': 'isMobile',
        'platform': 'platform',
        'recorded': 'recorded'
    }

    def __init__(self, is_mobile=None, platform=None, recorded=None, local_vars_configuration=None):  # noqa: E501
        """CurrentUserPlatformHistoryInner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_mobile = None
        self._platform = None
        self._recorded = None
        self.discriminator = None

        if is_mobile is not None:
            self.is_mobile = is_mobile
        self.platform = platform
        if recorded is not None:
            self.recorded = recorded

    @property
    def is_mobile(self):
        """Gets the is_mobile of this CurrentUserPlatformHistoryInner.  # noqa: E501


        :return: The is_mobile of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_mobile

    @is_mobile.setter
    def is_mobile(self, is_mobile):
        """Sets the is_mobile of this CurrentUserPlatformHistoryInner.


        :param is_mobile: The is_mobile of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :type is_mobile: bool
        """

        self._is_mobile = is_mobile

    @property
    def platform(self):
        """Gets the platform of this CurrentUserPlatformHistoryInner.  # noqa: E501


        :return: The platform of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this CurrentUserPlatformHistoryInner.


        :param platform: The platform of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def recorded(self):
        """Gets the recorded of this CurrentUserPlatformHistoryInner.  # noqa: E501


        :return: The recorded of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :rtype: datetime
        """
        return self._recorded

    @recorded.setter
    def recorded(self, recorded):
        """Sets the recorded of this CurrentUserPlatformHistoryInner.


        :param recorded: The recorded of this CurrentUserPlatformHistoryInner.  # noqa: E501
        :type recorded: datetime
        """

        self._recorded = recorded

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
        if not isinstance(other, CurrentUserPlatformHistoryInner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentUserPlatformHistoryInner):
            return True

        return self.to_dict() != other.to_dict()
