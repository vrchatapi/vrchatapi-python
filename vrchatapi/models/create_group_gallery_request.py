# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.9.1
    Contact: me@ariesclark.com
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


class CreateGroupGalleryRequest(object):
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
        'description': 'str',
        'members_only': 'bool',
        'role_ids_to_view': 'list[str]',
        'role_ids_to_submit': 'list[str]',
        'role_ids_to_auto_approve': 'list[str]',
        'role_ids_to_manage': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'members_only': 'membersOnly',
        'role_ids_to_view': 'roleIdsToView',
        'role_ids_to_submit': 'roleIdsToSubmit',
        'role_ids_to_auto_approve': 'roleIdsToAutoApprove',
        'role_ids_to_manage': 'roleIdsToManage'
    }

    def __init__(self, name=None, description=None, members_only=False, role_ids_to_view=None, role_ids_to_submit=None, role_ids_to_auto_approve=None, role_ids_to_manage=None, local_vars_configuration=None):  # noqa: E501
        """CreateGroupGalleryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._members_only = None
        self._role_ids_to_view = None
        self._role_ids_to_submit = None
        self._role_ids_to_auto_approve = None
        self._role_ids_to_manage = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if members_only is not None:
            self.members_only = members_only
        self.role_ids_to_view = role_ids_to_view
        self.role_ids_to_submit = role_ids_to_submit
        self.role_ids_to_auto_approve = role_ids_to_auto_approve
        self.role_ids_to_manage = role_ids_to_manage

    @property
    def name(self):
        """Gets the name of this CreateGroupGalleryRequest.  # noqa: E501

        Name of the gallery.  # noqa: E501

        :return: The name of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateGroupGalleryRequest.

        Name of the gallery.  # noqa: E501

        :param name: The name of this CreateGroupGalleryRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateGroupGalleryRequest.  # noqa: E501

        Description of the gallery.  # noqa: E501

        :return: The description of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateGroupGalleryRequest.

        Description of the gallery.  # noqa: E501

        :param description: The description of this CreateGroupGalleryRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def members_only(self):
        """Gets the members_only of this CreateGroupGalleryRequest.  # noqa: E501

        Whether the gallery is members only.  # noqa: E501

        :return: The members_only of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._members_only

    @members_only.setter
    def members_only(self, members_only):
        """Sets the members_only of this CreateGroupGalleryRequest.

        Whether the gallery is members only.  # noqa: E501

        :param members_only: The members_only of this CreateGroupGalleryRequest.  # noqa: E501
        :type members_only: bool
        """

        self._members_only = members_only

    @property
    def role_ids_to_view(self):
        """Gets the role_ids_to_view of this CreateGroupGalleryRequest.  # noqa: E501

           # noqa: E501

        :return: The role_ids_to_view of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids_to_view

    @role_ids_to_view.setter
    def role_ids_to_view(self, role_ids_to_view):
        """Sets the role_ids_to_view of this CreateGroupGalleryRequest.

           # noqa: E501

        :param role_ids_to_view: The role_ids_to_view of this CreateGroupGalleryRequest.  # noqa: E501
        :type role_ids_to_view: list[str]
        """

        self._role_ids_to_view = role_ids_to_view

    @property
    def role_ids_to_submit(self):
        """Gets the role_ids_to_submit of this CreateGroupGalleryRequest.  # noqa: E501

           # noqa: E501

        :return: The role_ids_to_submit of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids_to_submit

    @role_ids_to_submit.setter
    def role_ids_to_submit(self, role_ids_to_submit):
        """Sets the role_ids_to_submit of this CreateGroupGalleryRequest.

           # noqa: E501

        :param role_ids_to_submit: The role_ids_to_submit of this CreateGroupGalleryRequest.  # noqa: E501
        :type role_ids_to_submit: list[str]
        """

        self._role_ids_to_submit = role_ids_to_submit

    @property
    def role_ids_to_auto_approve(self):
        """Gets the role_ids_to_auto_approve of this CreateGroupGalleryRequest.  # noqa: E501

           # noqa: E501

        :return: The role_ids_to_auto_approve of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids_to_auto_approve

    @role_ids_to_auto_approve.setter
    def role_ids_to_auto_approve(self, role_ids_to_auto_approve):
        """Sets the role_ids_to_auto_approve of this CreateGroupGalleryRequest.

           # noqa: E501

        :param role_ids_to_auto_approve: The role_ids_to_auto_approve of this CreateGroupGalleryRequest.  # noqa: E501
        :type role_ids_to_auto_approve: list[str]
        """

        self._role_ids_to_auto_approve = role_ids_to_auto_approve

    @property
    def role_ids_to_manage(self):
        """Gets the role_ids_to_manage of this CreateGroupGalleryRequest.  # noqa: E501

           # noqa: E501

        :return: The role_ids_to_manage of this CreateGroupGalleryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids_to_manage

    @role_ids_to_manage.setter
    def role_ids_to_manage(self, role_ids_to_manage):
        """Sets the role_ids_to_manage of this CreateGroupGalleryRequest.

           # noqa: E501

        :param role_ids_to_manage: The role_ids_to_manage of this CreateGroupGalleryRequest.  # noqa: E501
        :type role_ids_to_manage: list[str]
        """

        self._role_ids_to_manage = role_ids_to_manage

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
        if not isinstance(other, CreateGroupGalleryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGroupGalleryRequest):
            return True

        return self.to_dict() != other.to_dict()
