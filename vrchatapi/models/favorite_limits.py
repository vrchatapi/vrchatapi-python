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


class FavoriteLimits(object):
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
        'default_max_favorite_groups': 'int',
        'default_max_favorites_per_group': 'int',
        'max_favorite_groups': 'FavoriteGroupLimits',
        'max_favorites_per_group': 'FavoriteGroupLimits'
    }

    attribute_map = {
        'default_max_favorite_groups': 'defaultMaxFavoriteGroups',
        'default_max_favorites_per_group': 'defaultMaxFavoritesPerGroup',
        'max_favorite_groups': 'maxFavoriteGroups',
        'max_favorites_per_group': 'maxFavoritesPerGroup'
    }

    def __init__(self, default_max_favorite_groups=None, default_max_favorites_per_group=None, max_favorite_groups=None, max_favorites_per_group=None, local_vars_configuration=None):  # noqa: E501
        """FavoriteLimits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._default_max_favorite_groups = None
        self._default_max_favorites_per_group = None
        self._max_favorite_groups = None
        self._max_favorites_per_group = None
        self.discriminator = None

        self.default_max_favorite_groups = default_max_favorite_groups
        self.default_max_favorites_per_group = default_max_favorites_per_group
        self.max_favorite_groups = max_favorite_groups
        self.max_favorites_per_group = max_favorites_per_group

    @property
    def default_max_favorite_groups(self):
        """Gets the default_max_favorite_groups of this FavoriteLimits.  # noqa: E501


        :return: The default_max_favorite_groups of this FavoriteLimits.  # noqa: E501
        :rtype: int
        """
        return self._default_max_favorite_groups

    @default_max_favorite_groups.setter
    def default_max_favorite_groups(self, default_max_favorite_groups):
        """Sets the default_max_favorite_groups of this FavoriteLimits.


        :param default_max_favorite_groups: The default_max_favorite_groups of this FavoriteLimits.  # noqa: E501
        :type default_max_favorite_groups: int
        """
        if self.local_vars_configuration.client_side_validation and default_max_favorite_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `default_max_favorite_groups`, must not be `None`")  # noqa: E501

        self._default_max_favorite_groups = default_max_favorite_groups

    @property
    def default_max_favorites_per_group(self):
        """Gets the default_max_favorites_per_group of this FavoriteLimits.  # noqa: E501


        :return: The default_max_favorites_per_group of this FavoriteLimits.  # noqa: E501
        :rtype: int
        """
        return self._default_max_favorites_per_group

    @default_max_favorites_per_group.setter
    def default_max_favorites_per_group(self, default_max_favorites_per_group):
        """Sets the default_max_favorites_per_group of this FavoriteLimits.


        :param default_max_favorites_per_group: The default_max_favorites_per_group of this FavoriteLimits.  # noqa: E501
        :type default_max_favorites_per_group: int
        """
        if self.local_vars_configuration.client_side_validation and default_max_favorites_per_group is None:  # noqa: E501
            raise ValueError("Invalid value for `default_max_favorites_per_group`, must not be `None`")  # noqa: E501

        self._default_max_favorites_per_group = default_max_favorites_per_group

    @property
    def max_favorite_groups(self):
        """Gets the max_favorite_groups of this FavoriteLimits.  # noqa: E501


        :return: The max_favorite_groups of this FavoriteLimits.  # noqa: E501
        :rtype: FavoriteGroupLimits
        """
        return self._max_favorite_groups

    @max_favorite_groups.setter
    def max_favorite_groups(self, max_favorite_groups):
        """Sets the max_favorite_groups of this FavoriteLimits.


        :param max_favorite_groups: The max_favorite_groups of this FavoriteLimits.  # noqa: E501
        :type max_favorite_groups: FavoriteGroupLimits
        """
        if self.local_vars_configuration.client_side_validation and max_favorite_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `max_favorite_groups`, must not be `None`")  # noqa: E501

        self._max_favorite_groups = max_favorite_groups

    @property
    def max_favorites_per_group(self):
        """Gets the max_favorites_per_group of this FavoriteLimits.  # noqa: E501


        :return: The max_favorites_per_group of this FavoriteLimits.  # noqa: E501
        :rtype: FavoriteGroupLimits
        """
        return self._max_favorites_per_group

    @max_favorites_per_group.setter
    def max_favorites_per_group(self, max_favorites_per_group):
        """Sets the max_favorites_per_group of this FavoriteLimits.


        :param max_favorites_per_group: The max_favorites_per_group of this FavoriteLimits.  # noqa: E501
        :type max_favorites_per_group: FavoriteGroupLimits
        """
        if self.local_vars_configuration.client_side_validation and max_favorites_per_group is None:  # noqa: E501
            raise ValueError("Invalid value for `max_favorites_per_group`, must not be `None`")  # noqa: E501

        self._max_favorites_per_group = max_favorites_per_group

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
        if not isinstance(other, FavoriteLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FavoriteLimits):
            return True

        return self.to_dict() != other.to_dict()
