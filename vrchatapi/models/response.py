# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.12.0
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


class Response(object):
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
        'message': 'str',
        'status_code': 'int'
    }

    attribute_map = {
        'message': 'message',
        'status_code': 'status_code'
    }

    def __init__(self, message=None, status_code=None, local_vars_configuration=None):  # noqa: E501
        """Response - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._status_code = None
        self.discriminator = None

        if message is not None:
            self.message = message
        self.status_code = status_code

    @property
    def message(self):
        """Gets the message of this Response.  # noqa: E501


        :return: The message of this Response.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Response.


        :param message: The message of this Response.  # noqa: E501
        :type message: str
        """
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 1):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `1`")  # noqa: E501

        self._message = message

    @property
    def status_code(self):
        """Gets the status_code of this Response.  # noqa: E501


        :return: The status_code of this Response.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this Response.


        :param status_code: The status_code of this Response.  # noqa: E501
        :type status_code: int
        """
        if self.local_vars_configuration.client_side_validation and status_code is None:  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status_code is not None and status_code < 100):  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must be a value greater than or equal to `100`")  # noqa: E501

        self._status_code = status_code

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
        if not isinstance(other, Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Response):
            return True

        return self.to_dict() != other.to_dict()
