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


class AvatarStyles(object):
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
        'primary': 'str',
        'secondary': 'str',
        'supplementary': 'list[str]'
    }

    attribute_map = {
        'primary': 'primary',
        'secondary': 'secondary',
        'supplementary': 'supplementary'
    }

    def __init__(self, primary=None, secondary=None, supplementary=None, local_vars_configuration=None):  # noqa: E501
        """AvatarStyles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._primary = None
        self._secondary = None
        self._supplementary = None
        self.discriminator = None

        self.primary = primary
        self.secondary = secondary
        if supplementary is not None:
            self.supplementary = supplementary

    @property
    def primary(self):
        """Gets the primary of this AvatarStyles.  # noqa: E501


        :return: The primary of this AvatarStyles.  # noqa: E501
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this AvatarStyles.


        :param primary: The primary of this AvatarStyles.  # noqa: E501
        :type primary: str
        """

        self._primary = primary

    @property
    def secondary(self):
        """Gets the secondary of this AvatarStyles.  # noqa: E501


        :return: The secondary of this AvatarStyles.  # noqa: E501
        :rtype: str
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this AvatarStyles.


        :param secondary: The secondary of this AvatarStyles.  # noqa: E501
        :type secondary: str
        """

        self._secondary = secondary

    @property
    def supplementary(self):
        """Gets the supplementary of this AvatarStyles.  # noqa: E501


        :return: The supplementary of this AvatarStyles.  # noqa: E501
        :rtype: list[str]
        """
        return self._supplementary

    @supplementary.setter
    def supplementary(self, supplementary):
        """Sets the supplementary of this AvatarStyles.


        :param supplementary: The supplementary of this AvatarStyles.  # noqa: E501
        :type supplementary: list[str]
        """

        self._supplementary = supplementary

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
        if not isinstance(other, AvatarStyles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvatarStyles):
            return True

        return self.to_dict() != other.to_dict()
