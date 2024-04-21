# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.1
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


class DynamicContentRow(object):
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
        'index': 'int',
        'name': 'str',
        'platform': 'str',
        'sort_heading': 'str',
        'sort_order': 'str',
        'sort_ownership': 'str',
        'tag': 'str',
        'type': 'str'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'platform': 'platform',
        'sort_heading': 'sortHeading',
        'sort_order': 'sortOrder',
        'sort_ownership': 'sortOwnership',
        'tag': 'tag',
        'type': 'type'
    }

    def __init__(self, index=None, name=None, platform=None, sort_heading=None, sort_order=None, sort_ownership=None, tag=None, type=None, local_vars_configuration=None):  # noqa: E501
        """DynamicContentRow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._name = None
        self._platform = None
        self._sort_heading = None
        self._sort_order = None
        self._sort_ownership = None
        self._tag = None
        self._type = None
        self.discriminator = None

        if index is not None:
            self.index = index
        self.name = name
        self.platform = platform
        self.sort_heading = sort_heading
        self.sort_order = sort_order
        self.sort_ownership = sort_ownership
        if tag is not None:
            self.tag = tag
        if type is not None:
            self.type = type

    @property
    def index(self):
        """Gets the index of this DynamicContentRow.  # noqa: E501


        :return: The index of this DynamicContentRow.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DynamicContentRow.


        :param index: The index of this DynamicContentRow.  # noqa: E501
        :type index: int
        """
        if (self.local_vars_configuration.client_side_validation and
                index is not None and index < 0):  # noqa: E501
            raise ValueError("Invalid value for `index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this DynamicContentRow.  # noqa: E501


        :return: The name of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicContentRow.


        :param name: The name of this DynamicContentRow.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def platform(self):
        """Gets the platform of this DynamicContentRow.  # noqa: E501

        Usually \"ThisPlatformSupported\", but can also be other values such as \"all\" or platform specific identifiers.  # noqa: E501

        :return: The platform of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DynamicContentRow.

        Usually \"ThisPlatformSupported\", but can also be other values such as \"all\" or platform specific identifiers.  # noqa: E501

        :param platform: The platform of this DynamicContentRow.  # noqa: E501
        :type platform: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) < 1):
            raise ValueError("Invalid value for `platform`, length must be greater than or equal to `1`")  # noqa: E501

        self._platform = platform

    @property
    def sort_heading(self):
        """Gets the sort_heading of this DynamicContentRow.  # noqa: E501


        :return: The sort_heading of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._sort_heading

    @sort_heading.setter
    def sort_heading(self, sort_heading):
        """Sets the sort_heading of this DynamicContentRow.


        :param sort_heading: The sort_heading of this DynamicContentRow.  # noqa: E501
        :type sort_heading: str
        """
        if self.local_vars_configuration.client_side_validation and sort_heading is None:  # noqa: E501
            raise ValueError("Invalid value for `sort_heading`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sort_heading is not None and len(sort_heading) < 1):
            raise ValueError("Invalid value for `sort_heading`, length must be greater than or equal to `1`")  # noqa: E501

        self._sort_heading = sort_heading

    @property
    def sort_order(self):
        """Gets the sort_order of this DynamicContentRow.  # noqa: E501


        :return: The sort_order of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DynamicContentRow.


        :param sort_order: The sort_order of this DynamicContentRow.  # noqa: E501
        :type sort_order: str
        """
        if self.local_vars_configuration.client_side_validation and sort_order is None:  # noqa: E501
            raise ValueError("Invalid value for `sort_order`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sort_order is not None and len(sort_order) < 1):
            raise ValueError("Invalid value for `sort_order`, length must be greater than or equal to `1`")  # noqa: E501

        self._sort_order = sort_order

    @property
    def sort_ownership(self):
        """Gets the sort_ownership of this DynamicContentRow.  # noqa: E501


        :return: The sort_ownership of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._sort_ownership

    @sort_ownership.setter
    def sort_ownership(self, sort_ownership):
        """Sets the sort_ownership of this DynamicContentRow.


        :param sort_ownership: The sort_ownership of this DynamicContentRow.  # noqa: E501
        :type sort_ownership: str
        """
        if self.local_vars_configuration.client_side_validation and sort_ownership is None:  # noqa: E501
            raise ValueError("Invalid value for `sort_ownership`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                sort_ownership is not None and len(sort_ownership) < 1):
            raise ValueError("Invalid value for `sort_ownership`, length must be greater than or equal to `1`")  # noqa: E501

        self._sort_ownership = sort_ownership

    @property
    def tag(self):
        """Gets the tag of this DynamicContentRow.  # noqa: E501

        Tag to filter content for this row.  # noqa: E501

        :return: The tag of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DynamicContentRow.

        Tag to filter content for this row.  # noqa: E501

        :param tag: The tag of this DynamicContentRow.  # noqa: E501
        :type tag: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tag is not None and len(tag) < 1):
            raise ValueError("Invalid value for `tag`, length must be greater than or equal to `1`")  # noqa: E501

        self._tag = tag

    @property
    def type(self):
        """Gets the type of this DynamicContentRow.  # noqa: E501

        Type is not present if it is a world.  # noqa: E501

        :return: The type of this DynamicContentRow.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicContentRow.

        Type is not present if it is a world.  # noqa: E501

        :param type: The type of this DynamicContentRow.  # noqa: E501
        :type type: str
        """

        self._type = type

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
        if not isinstance(other, DynamicContentRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DynamicContentRow):
            return True

        return self.to_dict() != other.to_dict()
