# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.15.0
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


class InfoPushDataClickable(object):
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
        'command': 'str',
        'parameters': 'list[str]'
    }

    attribute_map = {
        'command': 'command',
        'parameters': 'parameters'
    }

    def __init__(self, command=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """InfoPushDataClickable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._command = None
        self._parameters = None
        self.discriminator = None

        self.command = command
        if parameters is not None:
            self.parameters = parameters

    @property
    def command(self):
        """Gets the command of this InfoPushDataClickable.  # noqa: E501


        :return: The command of this InfoPushDataClickable.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this InfoPushDataClickable.


        :param command: The command of this InfoPushDataClickable.  # noqa: E501
        :type command: str
        """
        if self.local_vars_configuration.client_side_validation and command is None:  # noqa: E501
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501
        allowed_values = ["OpenURL", "OpenVRCPlusMenu", "OpenSafetyMenu", "CannedWorldSearch"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and command not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `command` ({0}), must be one of {1}"  # noqa: E501
                .format(command, allowed_values)
            )

        self._command = command

    @property
    def parameters(self):
        """Gets the parameters of this InfoPushDataClickable.  # noqa: E501

        In case of OpenURL, this would contain the link.  # noqa: E501

        :return: The parameters of this InfoPushDataClickable.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InfoPushDataClickable.

        In case of OpenURL, this would contain the link.  # noqa: E501

        :param parameters: The parameters of this InfoPushDataClickable.  # noqa: E501
        :type parameters: list[str]
        """

        self._parameters = parameters

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
        if not isinstance(other, InfoPushDataClickable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfoPushDataClickable):
            return True

        return self.to_dict() != other.to_dict()
