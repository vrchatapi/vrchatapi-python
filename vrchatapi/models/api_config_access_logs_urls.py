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


class APIConfigAccessLogsUrls(object):
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
        'default': 'str',
        'pico': 'str',
        'quest': 'str',
        'xr_elite': 'str'
    }

    attribute_map = {
        'default': 'Default',
        'pico': 'Pico',
        'quest': 'Quest',
        'xr_elite': 'XRElite'
    }

    def __init__(self, default=None, pico=None, quest=None, xr_elite=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigAccessLogsUrls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._default = None
        self._pico = None
        self._quest = None
        self._xr_elite = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if pico is not None:
            self.pico = pico
        if quest is not None:
            self.quest = quest
        if xr_elite is not None:
            self.xr_elite = xr_elite

    @property
    def default(self):
        """Gets the default of this APIConfigAccessLogsUrls.  # noqa: E501


        :return: The default of this APIConfigAccessLogsUrls.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this APIConfigAccessLogsUrls.


        :param default: The default of this APIConfigAccessLogsUrls.  # noqa: E501
        :type default: str
        """

        self._default = default

    @property
    def pico(self):
        """Gets the pico of this APIConfigAccessLogsUrls.  # noqa: E501


        :return: The pico of this APIConfigAccessLogsUrls.  # noqa: E501
        :rtype: str
        """
        return self._pico

    @pico.setter
    def pico(self, pico):
        """Sets the pico of this APIConfigAccessLogsUrls.


        :param pico: The pico of this APIConfigAccessLogsUrls.  # noqa: E501
        :type pico: str
        """

        self._pico = pico

    @property
    def quest(self):
        """Gets the quest of this APIConfigAccessLogsUrls.  # noqa: E501


        :return: The quest of this APIConfigAccessLogsUrls.  # noqa: E501
        :rtype: str
        """
        return self._quest

    @quest.setter
    def quest(self, quest):
        """Sets the quest of this APIConfigAccessLogsUrls.


        :param quest: The quest of this APIConfigAccessLogsUrls.  # noqa: E501
        :type quest: str
        """

        self._quest = quest

    @property
    def xr_elite(self):
        """Gets the xr_elite of this APIConfigAccessLogsUrls.  # noqa: E501


        :return: The xr_elite of this APIConfigAccessLogsUrls.  # noqa: E501
        :rtype: str
        """
        return self._xr_elite

    @xr_elite.setter
    def xr_elite(self, xr_elite):
        """Sets the xr_elite of this APIConfigAccessLogsUrls.


        :param xr_elite: The xr_elite of this APIConfigAccessLogsUrls.  # noqa: E501
        :type xr_elite: str
        """

        self._xr_elite = xr_elite

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
        if not isinstance(other, APIConfigAccessLogsUrls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigAccessLogsUrls):
            return True

        return self.to_dict() != other.to_dict()
