# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.1
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


class InstanceShortNameResponse(object):
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
        'secure_name': 'str',
        'short_name': 'str'
    }

    attribute_map = {
        'secure_name': 'secureName',
        'short_name': 'shortName'
    }

    def __init__(self, secure_name=None, short_name=None, local_vars_configuration=None):  # noqa: E501
        """InstanceShortNameResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._secure_name = None
        self._short_name = None
        self.discriminator = None

        self.secure_name = secure_name
        if short_name is not None:
            self.short_name = short_name

    @property
    def secure_name(self):
        """Gets the secure_name of this InstanceShortNameResponse.  # noqa: E501


        :return: The secure_name of this InstanceShortNameResponse.  # noqa: E501
        :rtype: str
        """
        return self._secure_name

    @secure_name.setter
    def secure_name(self, secure_name):
        """Sets the secure_name of this InstanceShortNameResponse.


        :param secure_name: The secure_name of this InstanceShortNameResponse.  # noqa: E501
        :type secure_name: str
        """
        if self.local_vars_configuration.client_side_validation and secure_name is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                secure_name is not None and len(secure_name) < 1):
            raise ValueError("Invalid value for `secure_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._secure_name = secure_name

    @property
    def short_name(self):
        """Gets the short_name of this InstanceShortNameResponse.  # noqa: E501


        :return: The short_name of this InstanceShortNameResponse.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this InstanceShortNameResponse.


        :param short_name: The short_name of this InstanceShortNameResponse.  # noqa: E501
        :type short_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                short_name is not None and len(short_name) < 1):
            raise ValueError("Invalid value for `short_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_name = short_name

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
        if not isinstance(other, InstanceShortNameResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceShortNameResponse):
            return True

        return self.to_dict() != other.to_dict()
