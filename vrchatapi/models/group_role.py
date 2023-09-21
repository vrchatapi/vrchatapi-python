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


class GroupRole(object):
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
        'id': 'str',
        'group_id': 'str',
        'name': 'str',
        'description': 'str',
        'is_self_assignable': 'bool',
        'permissions': 'list[str]',
        'is_management_role': 'bool',
        'requires_two_factor': 'bool',
        'requires_purchase': 'bool',
        'order': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'name': 'name',
        'description': 'description',
        'is_self_assignable': 'isSelfAssignable',
        'permissions': 'permissions',
        'is_management_role': 'isManagementRole',
        'requires_two_factor': 'requiresTwoFactor',
        'requires_purchase': 'requiresPurchase',
        'order': 'order',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, group_id=None, name=None, description=None, is_self_assignable=False, permissions=None, is_management_role=False, requires_two_factor=False, requires_purchase=False, order=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """GroupRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._name = None
        self._description = None
        self._is_self_assignable = None
        self._permissions = None
        self._is_management_role = None
        self._requires_two_factor = None
        self._requires_purchase = None
        self._order = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if is_self_assignable is not None:
            self.is_self_assignable = is_self_assignable
        if permissions is not None:
            self.permissions = permissions
        if is_management_role is not None:
            self.is_management_role = is_management_role
        if requires_two_factor is not None:
            self.requires_two_factor = requires_two_factor
        if requires_purchase is not None:
            self.requires_purchase = requires_purchase
        if order is not None:
            self.order = order
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GroupRole.  # noqa: E501


        :return: The id of this GroupRole.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupRole.


        :param id: The id of this GroupRole.  # noqa: E501
        :type id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'grol_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/grol_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupRole.  # noqa: E501


        :return: The group_id of this GroupRole.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupRole.


        :param group_id: The group_id of this GroupRole.  # noqa: E501
        :type group_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                group_id is not None and not re.search(r'grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', group_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `group_id`, must be a follow pattern or equal to `/grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this GroupRole.  # noqa: E501


        :return: The name of this GroupRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupRole.


        :param name: The name of this GroupRole.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this GroupRole.  # noqa: E501


        :return: The description of this GroupRole.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupRole.


        :param description: The description of this GroupRole.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def is_self_assignable(self):
        """Gets the is_self_assignable of this GroupRole.  # noqa: E501


        :return: The is_self_assignable of this GroupRole.  # noqa: E501
        :rtype: bool
        """
        return self._is_self_assignable

    @is_self_assignable.setter
    def is_self_assignable(self, is_self_assignable):
        """Sets the is_self_assignable of this GroupRole.


        :param is_self_assignable: The is_self_assignable of this GroupRole.  # noqa: E501
        :type is_self_assignable: bool
        """

        self._is_self_assignable = is_self_assignable

    @property
    def permissions(self):
        """Gets the permissions of this GroupRole.  # noqa: E501


        :return: The permissions of this GroupRole.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GroupRole.


        :param permissions: The permissions of this GroupRole.  # noqa: E501
        :type permissions: list[str]
        """

        self._permissions = permissions

    @property
    def is_management_role(self):
        """Gets the is_management_role of this GroupRole.  # noqa: E501


        :return: The is_management_role of this GroupRole.  # noqa: E501
        :rtype: bool
        """
        return self._is_management_role

    @is_management_role.setter
    def is_management_role(self, is_management_role):
        """Sets the is_management_role of this GroupRole.


        :param is_management_role: The is_management_role of this GroupRole.  # noqa: E501
        :type is_management_role: bool
        """

        self._is_management_role = is_management_role

    @property
    def requires_two_factor(self):
        """Gets the requires_two_factor of this GroupRole.  # noqa: E501


        :return: The requires_two_factor of this GroupRole.  # noqa: E501
        :rtype: bool
        """
        return self._requires_two_factor

    @requires_two_factor.setter
    def requires_two_factor(self, requires_two_factor):
        """Sets the requires_two_factor of this GroupRole.


        :param requires_two_factor: The requires_two_factor of this GroupRole.  # noqa: E501
        :type requires_two_factor: bool
        """

        self._requires_two_factor = requires_two_factor

    @property
    def requires_purchase(self):
        """Gets the requires_purchase of this GroupRole.  # noqa: E501


        :return: The requires_purchase of this GroupRole.  # noqa: E501
        :rtype: bool
        """
        return self._requires_purchase

    @requires_purchase.setter
    def requires_purchase(self, requires_purchase):
        """Sets the requires_purchase of this GroupRole.


        :param requires_purchase: The requires_purchase of this GroupRole.  # noqa: E501
        :type requires_purchase: bool
        """

        self._requires_purchase = requires_purchase

    @property
    def order(self):
        """Gets the order of this GroupRole.  # noqa: E501


        :return: The order of this GroupRole.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this GroupRole.


        :param order: The order of this GroupRole.  # noqa: E501
        :type order: int
        """

        self._order = order

    @property
    def created_at(self):
        """Gets the created_at of this GroupRole.  # noqa: E501


        :return: The created_at of this GroupRole.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupRole.


        :param created_at: The created_at of this GroupRole.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GroupRole.  # noqa: E501


        :return: The updated_at of this GroupRole.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GroupRole.


        :param updated_at: The updated_at of this GroupRole.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, GroupRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupRole):
            return True

        return self.to_dict() != other.to_dict()
