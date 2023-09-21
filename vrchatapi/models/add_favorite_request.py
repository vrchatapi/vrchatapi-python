# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.14.0
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


class AddFavoriteRequest(object):
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
        'type': 'FavoriteType',
        'favorite_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'favorite_id': 'favoriteId',
        'tags': 'tags'
    }

    def __init__(self, type=None, favorite_id=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """AddFavoriteRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._favorite_id = None
        self._tags = None
        self.discriminator = None

        self.type = type
        self.favorite_id = favorite_id
        self.tags = tags

    @property
    def type(self):
        """Gets the type of this AddFavoriteRequest.  # noqa: E501


        :return: The type of this AddFavoriteRequest.  # noqa: E501
        :rtype: FavoriteType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddFavoriteRequest.


        :param type: The type of this AddFavoriteRequest.  # noqa: E501
        :type type: FavoriteType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def favorite_id(self):
        """Gets the favorite_id of this AddFavoriteRequest.  # noqa: E501

        Must be either AvatarID, WorldID or UserID.  # noqa: E501

        :return: The favorite_id of this AddFavoriteRequest.  # noqa: E501
        :rtype: str
        """
        return self._favorite_id

    @favorite_id.setter
    def favorite_id(self, favorite_id):
        """Sets the favorite_id of this AddFavoriteRequest.

        Must be either AvatarID, WorldID or UserID.  # noqa: E501

        :param favorite_id: The favorite_id of this AddFavoriteRequest.  # noqa: E501
        :type favorite_id: str
        """
        if self.local_vars_configuration.client_side_validation and favorite_id is None:  # noqa: E501
            raise ValueError("Invalid value for `favorite_id`, must not be `None`")  # noqa: E501

        self._favorite_id = favorite_id

    @property
    def tags(self):
        """Gets the tags of this AddFavoriteRequest.  # noqa: E501

        Tags indicate which group this favorite belongs to. Adding multiple groups makes it show up in all. Removing it from one in that case removes it from all.  # noqa: E501

        :return: The tags of this AddFavoriteRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AddFavoriteRequest.

        Tags indicate which group this favorite belongs to. Adding multiple groups makes it show up in all. Removing it from one in that case removes it from all.  # noqa: E501

        :param tags: The tags of this AddFavoriteRequest.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, AddFavoriteRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddFavoriteRequest):
            return True

        return self.to_dict() != other.to_dict()
