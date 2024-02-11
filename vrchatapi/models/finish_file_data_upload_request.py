# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.16.5
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


class FinishFileDataUploadRequest(object):
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
        'etags': 'list[str]',
        'next_part_number': 'str',
        'max_parts': 'str'
    }

    attribute_map = {
        'etags': 'etags',
        'next_part_number': 'nextPartNumber',
        'max_parts': 'maxParts'
    }

    def __init__(self, etags=None, next_part_number='0', max_parts='0', local_vars_configuration=None):  # noqa: E501
        """FinishFileDataUploadRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._etags = None
        self._next_part_number = None
        self._max_parts = None
        self.discriminator = None

        if etags is not None:
            self.etags = etags
        self.next_part_number = next_part_number
        self.max_parts = max_parts

    @property
    def etags(self):
        """Gets the etags of this FinishFileDataUploadRequest.  # noqa: E501

        Array of ETags uploaded.  # noqa: E501

        :return: The etags of this FinishFileDataUploadRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._etags

    @etags.setter
    def etags(self, etags):
        """Sets the etags of this FinishFileDataUploadRequest.

        Array of ETags uploaded.  # noqa: E501

        :param etags: The etags of this FinishFileDataUploadRequest.  # noqa: E501
        :type etags: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                etags is not None and len(etags) < 1):
            raise ValueError("Invalid value for `etags`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._etags = etags

    @property
    def next_part_number(self):
        """Gets the next_part_number of this FinishFileDataUploadRequest.  # noqa: E501

        Always a zero in string form, despite how many parts uploaded.  # noqa: E501

        :return: The next_part_number of this FinishFileDataUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_part_number

    @next_part_number.setter
    def next_part_number(self, next_part_number):
        """Sets the next_part_number of this FinishFileDataUploadRequest.

        Always a zero in string form, despite how many parts uploaded.  # noqa: E501

        :param next_part_number: The next_part_number of this FinishFileDataUploadRequest.  # noqa: E501
        :type next_part_number: str
        """
        if self.local_vars_configuration.client_side_validation and next_part_number is None:  # noqa: E501
            raise ValueError("Invalid value for `next_part_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                next_part_number is not None and len(next_part_number) > 1):
            raise ValueError("Invalid value for `next_part_number`, length must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                next_part_number is not None and len(next_part_number) < 1):
            raise ValueError("Invalid value for `next_part_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._next_part_number = next_part_number

    @property
    def max_parts(self):
        """Gets the max_parts of this FinishFileDataUploadRequest.  # noqa: E501

        Always a zero in string form, despite how many parts uploaded.  # noqa: E501

        :return: The max_parts of this FinishFileDataUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._max_parts

    @max_parts.setter
    def max_parts(self, max_parts):
        """Sets the max_parts of this FinishFileDataUploadRequest.

        Always a zero in string form, despite how many parts uploaded.  # noqa: E501

        :param max_parts: The max_parts of this FinishFileDataUploadRequest.  # noqa: E501
        :type max_parts: str
        """
        if self.local_vars_configuration.client_side_validation and max_parts is None:  # noqa: E501
            raise ValueError("Invalid value for `max_parts`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_parts is not None and len(max_parts) > 1):
            raise ValueError("Invalid value for `max_parts`, length must be less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_parts is not None and len(max_parts) < 1):
            raise ValueError("Invalid value for `max_parts`, length must be greater than or equal to `1`")  # noqa: E501

        self._max_parts = max_parts

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
        if not isinstance(other, FinishFileDataUploadRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FinishFileDataUploadRequest):
            return True

        return self.to_dict() != other.to_dict()
