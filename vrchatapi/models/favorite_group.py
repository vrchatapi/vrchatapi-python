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


class FavoriteGroup(object):
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
        'display_name': 'str',
        'id': 'str',
        'name': 'str',
        'owner_display_name': 'str',
        'owner_id': 'str',
        'tags': 'list[str]',
        'type': 'FavoriteType',
        'visibility': 'FavoriteGroupVisibility'
    }

    attribute_map = {
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name',
        'owner_display_name': 'ownerDisplayName',
        'owner_id': 'ownerId',
        'tags': 'tags',
        'type': 'type',
        'visibility': 'visibility'
    }

    def __init__(self, display_name=None, id=None, name=None, owner_display_name=None, owner_id=None, tags=None, type=None, visibility=None, local_vars_configuration=None):  # noqa: E501
        """FavoriteGroup - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._id = None
        self._name = None
        self._owner_display_name = None
        self._owner_id = None
        self._tags = None
        self._type = None
        self._visibility = None
        self.discriminator = None

        self.display_name = display_name
        self.id = id
        self.name = name
        self.owner_display_name = owner_display_name
        self.owner_id = owner_id
        self.tags = tags
        self.type = type
        self.visibility = visibility

    @property
    def display_name(self):
        """Gets the display_name of this FavoriteGroup.  # noqa: E501


        :return: The display_name of this FavoriteGroup.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FavoriteGroup.


        :param display_name: The display_name of this FavoriteGroup.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this FavoriteGroup.  # noqa: E501


        :return: The id of this FavoriteGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FavoriteGroup.


        :param id: The id of this FavoriteGroup.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'fvgrp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/fvgrp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FavoriteGroup.  # noqa: E501


        :return: The name of this FavoriteGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FavoriteGroup.


        :param name: The name of this FavoriteGroup.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def owner_display_name(self):
        """Gets the owner_display_name of this FavoriteGroup.  # noqa: E501


        :return: The owner_display_name of this FavoriteGroup.  # noqa: E501
        :rtype: str
        """
        return self._owner_display_name

    @owner_display_name.setter
    def owner_display_name(self, owner_display_name):
        """Sets the owner_display_name of this FavoriteGroup.


        :param owner_display_name: The owner_display_name of this FavoriteGroup.  # noqa: E501
        :type owner_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and owner_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                owner_display_name is not None and len(owner_display_name) < 1):
            raise ValueError("Invalid value for `owner_display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._owner_display_name = owner_display_name

    @property
    def owner_id(self):
        """Gets the owner_id of this FavoriteGroup.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this FavoriteGroup.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this FavoriteGroup.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this FavoriteGroup.  # noqa: E501
        :type owner_id: str
        """
        if self.local_vars_configuration.client_side_validation and owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def tags(self):
        """Gets the tags of this FavoriteGroup.  # noqa: E501

           # noqa: E501

        :return: The tags of this FavoriteGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FavoriteGroup.

           # noqa: E501

        :param tags: The tags of this FavoriteGroup.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this FavoriteGroup.  # noqa: E501


        :return: The type of this FavoriteGroup.  # noqa: E501
        :rtype: FavoriteType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FavoriteGroup.


        :param type: The type of this FavoriteGroup.  # noqa: E501
        :type type: FavoriteType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def visibility(self):
        """Gets the visibility of this FavoriteGroup.  # noqa: E501


        :return: The visibility of this FavoriteGroup.  # noqa: E501
        :rtype: FavoriteGroupVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this FavoriteGroup.


        :param visibility: The visibility of this FavoriteGroup.  # noqa: E501
        :type visibility: FavoriteGroupVisibility
        """
        if self.local_vars_configuration.client_side_validation and visibility is None:  # noqa: E501
            raise ValueError("Invalid value for `visibility`, must not be `None`")  # noqa: E501

        self._visibility = visibility

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
        if not isinstance(other, FavoriteGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FavoriteGroup):
            return True

        return self.to_dict() != other.to_dict()
