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


class GroupPermission(object):
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
        'name': 'str',
        'display_name': 'str',
        'help': 'str',
        'is_management_permission': 'bool',
        'allowed_to_add': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'help': 'help',
        'is_management_permission': 'isManagementPermission',
        'allowed_to_add': 'allowedToAdd'
    }

    def __init__(self, name=None, display_name=None, help=None, is_management_permission=False, allowed_to_add=False, local_vars_configuration=None):  # noqa: E501
        """GroupPermission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._display_name = None
        self._help = None
        self._is_management_permission = None
        self._allowed_to_add = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if help is not None:
            self.help = help
        if is_management_permission is not None:
            self.is_management_permission = is_management_permission
        if allowed_to_add is not None:
            self.allowed_to_add = allowed_to_add

    @property
    def name(self):
        """Gets the name of this GroupPermission.  # noqa: E501

        The name of the permission.  # noqa: E501

        :return: The name of this GroupPermission.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupPermission.

        The name of the permission.  # noqa: E501

        :param name: The name of this GroupPermission.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this GroupPermission.  # noqa: E501

        The display name of the permission.  # noqa: E501

        :return: The display_name of this GroupPermission.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GroupPermission.

        The display name of the permission.  # noqa: E501

        :param display_name: The display_name of this GroupPermission.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def help(self):
        """Gets the help of this GroupPermission.  # noqa: E501

        Human-readable description of the permission.  # noqa: E501

        :return: The help of this GroupPermission.  # noqa: E501
        :rtype: str
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this GroupPermission.

        Human-readable description of the permission.  # noqa: E501

        :param help: The help of this GroupPermission.  # noqa: E501
        :type help: str
        """

        self._help = help

    @property
    def is_management_permission(self):
        """Gets the is_management_permission of this GroupPermission.  # noqa: E501

        Whether this permission is a \"management\" permission.  # noqa: E501

        :return: The is_management_permission of this GroupPermission.  # noqa: E501
        :rtype: bool
        """
        return self._is_management_permission

    @is_management_permission.setter
    def is_management_permission(self, is_management_permission):
        """Sets the is_management_permission of this GroupPermission.

        Whether this permission is a \"management\" permission.  # noqa: E501

        :param is_management_permission: The is_management_permission of this GroupPermission.  # noqa: E501
        :type is_management_permission: bool
        """

        self._is_management_permission = is_management_permission

    @property
    def allowed_to_add(self):
        """Gets the allowed_to_add of this GroupPermission.  # noqa: E501

        Whether the user is allowed to add this permission to a role.  # noqa: E501

        :return: The allowed_to_add of this GroupPermission.  # noqa: E501
        :rtype: bool
        """
        return self._allowed_to_add

    @allowed_to_add.setter
    def allowed_to_add(self, allowed_to_add):
        """Sets the allowed_to_add of this GroupPermission.

        Whether the user is allowed to add this permission to a role.  # noqa: E501

        :param allowed_to_add: The allowed_to_add of this GroupPermission.  # noqa: E501
        :type allowed_to_add: bool
        """

        self._allowed_to_add = allowed_to_add

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
        if not isinstance(other, GroupPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupPermission):
            return True

        return self.to_dict() != other.to_dict()
