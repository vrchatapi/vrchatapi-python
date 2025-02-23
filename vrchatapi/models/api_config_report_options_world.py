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


class APIConfigReportOptionsWorld(object):
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
        'environment': 'list[str]',
        'text': 'list[str]',
        'warnings': 'list[str]',
        'worldimage': 'list[str]',
        'worldstore': 'list[str]'
    }

    attribute_map = {
        'environment': 'environment',
        'text': 'text',
        'warnings': 'warnings',
        'worldimage': 'worldimage',
        'worldstore': 'worldstore'
    }

    def __init__(self, environment=None, text=None, warnings=None, worldimage=None, worldstore=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigReportOptionsWorld - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._environment = None
        self._text = None
        self._warnings = None
        self._worldimage = None
        self._worldstore = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if text is not None:
            self.text = text
        if warnings is not None:
            self.warnings = warnings
        if worldimage is not None:
            self.worldimage = worldimage
        if worldstore is not None:
            self.worldstore = worldstore

    @property
    def environment(self):
        """Gets the environment of this APIConfigReportOptionsWorld.  # noqa: E501


        :return: The environment of this APIConfigReportOptionsWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this APIConfigReportOptionsWorld.


        :param environment: The environment of this APIConfigReportOptionsWorld.  # noqa: E501
        :type environment: list[str]
        """

        self._environment = environment

    @property
    def text(self):
        """Gets the text of this APIConfigReportOptionsWorld.  # noqa: E501


        :return: The text of this APIConfigReportOptionsWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this APIConfigReportOptionsWorld.


        :param text: The text of this APIConfigReportOptionsWorld.  # noqa: E501
        :type text: list[str]
        """

        self._text = text

    @property
    def warnings(self):
        """Gets the warnings of this APIConfigReportOptionsWorld.  # noqa: E501


        :return: The warnings of this APIConfigReportOptionsWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this APIConfigReportOptionsWorld.


        :param warnings: The warnings of this APIConfigReportOptionsWorld.  # noqa: E501
        :type warnings: list[str]
        """

        self._warnings = warnings

    @property
    def worldimage(self):
        """Gets the worldimage of this APIConfigReportOptionsWorld.  # noqa: E501


        :return: The worldimage of this APIConfigReportOptionsWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._worldimage

    @worldimage.setter
    def worldimage(self, worldimage):
        """Sets the worldimage of this APIConfigReportOptionsWorld.


        :param worldimage: The worldimage of this APIConfigReportOptionsWorld.  # noqa: E501
        :type worldimage: list[str]
        """

        self._worldimage = worldimage

    @property
    def worldstore(self):
        """Gets the worldstore of this APIConfigReportOptionsWorld.  # noqa: E501


        :return: The worldstore of this APIConfigReportOptionsWorld.  # noqa: E501
        :rtype: list[str]
        """
        return self._worldstore

    @worldstore.setter
    def worldstore(self, worldstore):
        """Sets the worldstore of this APIConfigReportOptionsWorld.


        :param worldstore: The worldstore of this APIConfigReportOptionsWorld.  # noqa: E501
        :type worldstore: list[str]
        """

        self._worldstore = worldstore

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
        if not isinstance(other, APIConfigReportOptionsWorld):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigReportOptionsWorld):
            return True

        return self.to_dict() != other.to_dict()
