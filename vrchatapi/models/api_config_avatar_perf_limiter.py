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


class APIConfigAvatarPerfLimiter(object):
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
        'android_mobile': 'PerformanceLimiterInfo',
        'pc': 'PerformanceLimiterInfo',
        'pico': 'PerformanceLimiterInfo',
        'quest': 'PerformanceLimiterInfo',
        'xr_elite': 'PerformanceLimiterInfo',
        'i_os_mobile': 'PerformanceLimiterInfo'
    }

    attribute_map = {
        'android_mobile': 'AndroidMobile',
        'pc': 'PC',
        'pico': 'Pico',
        'quest': 'Quest',
        'xr_elite': 'XRElite',
        'i_os_mobile': 'iOSMobile'
    }

    def __init__(self, android_mobile=None, pc=None, pico=None, quest=None, xr_elite=None, i_os_mobile=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigAvatarPerfLimiter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._android_mobile = None
        self._pc = None
        self._pico = None
        self._quest = None
        self._xr_elite = None
        self._i_os_mobile = None
        self.discriminator = None

        self.android_mobile = android_mobile
        self.pc = pc
        self.pico = pico
        self.quest = quest
        self.xr_elite = xr_elite
        self.i_os_mobile = i_os_mobile

    @property
    def android_mobile(self):
        """Gets the android_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The android_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._android_mobile

    @android_mobile.setter
    def android_mobile(self, android_mobile):
        """Sets the android_mobile of this APIConfigAvatarPerfLimiter.


        :param android_mobile: The android_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type android_mobile: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and android_mobile is None:  # noqa: E501
            raise ValueError("Invalid value for `android_mobile`, must not be `None`")  # noqa: E501

        self._android_mobile = android_mobile

    @property
    def pc(self):
        """Gets the pc of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The pc of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._pc

    @pc.setter
    def pc(self, pc):
        """Sets the pc of this APIConfigAvatarPerfLimiter.


        :param pc: The pc of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type pc: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and pc is None:  # noqa: E501
            raise ValueError("Invalid value for `pc`, must not be `None`")  # noqa: E501

        self._pc = pc

    @property
    def pico(self):
        """Gets the pico of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The pico of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._pico

    @pico.setter
    def pico(self, pico):
        """Sets the pico of this APIConfigAvatarPerfLimiter.


        :param pico: The pico of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type pico: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and pico is None:  # noqa: E501
            raise ValueError("Invalid value for `pico`, must not be `None`")  # noqa: E501

        self._pico = pico

    @property
    def quest(self):
        """Gets the quest of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The quest of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._quest

    @quest.setter
    def quest(self, quest):
        """Sets the quest of this APIConfigAvatarPerfLimiter.


        :param quest: The quest of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type quest: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and quest is None:  # noqa: E501
            raise ValueError("Invalid value for `quest`, must not be `None`")  # noqa: E501

        self._quest = quest

    @property
    def xr_elite(self):
        """Gets the xr_elite of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The xr_elite of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._xr_elite

    @xr_elite.setter
    def xr_elite(self, xr_elite):
        """Sets the xr_elite of this APIConfigAvatarPerfLimiter.


        :param xr_elite: The xr_elite of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type xr_elite: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and xr_elite is None:  # noqa: E501
            raise ValueError("Invalid value for `xr_elite`, must not be `None`")  # noqa: E501

        self._xr_elite = xr_elite

    @property
    def i_os_mobile(self):
        """Gets the i_os_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501


        :return: The i_os_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :rtype: PerformanceLimiterInfo
        """
        return self._i_os_mobile

    @i_os_mobile.setter
    def i_os_mobile(self, i_os_mobile):
        """Sets the i_os_mobile of this APIConfigAvatarPerfLimiter.


        :param i_os_mobile: The i_os_mobile of this APIConfigAvatarPerfLimiter.  # noqa: E501
        :type i_os_mobile: PerformanceLimiterInfo
        """
        if self.local_vars_configuration.client_side_validation and i_os_mobile is None:  # noqa: E501
            raise ValueError("Invalid value for `i_os_mobile`, must not be `None`")  # noqa: E501

        self._i_os_mobile = i_os_mobile

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
        if not isinstance(other, APIConfigAvatarPerfLimiter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigAvatarPerfLimiter):
            return True

        return self.to_dict() != other.to_dict()
