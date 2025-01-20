# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.9
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


class FileAnalysis(object):
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
        'avatar_stats': 'FileAnalysisAvatarStats',
        'created_at': 'datetime',
        'file_size': 'int',
        'success': 'bool',
        'uncompressed_size': 'int'
    }

    attribute_map = {
        'avatar_stats': 'avatarStats',
        'created_at': 'created_at',
        'file_size': 'fileSize',
        'success': 'success',
        'uncompressed_size': 'uncompressedSize'
    }

    def __init__(self, avatar_stats=None, created_at=None, file_size=None, success=None, uncompressed_size=None, local_vars_configuration=None):  # noqa: E501
        """FileAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._avatar_stats = None
        self._created_at = None
        self._file_size = None
        self._success = None
        self._uncompressed_size = None
        self.discriminator = None

        self.avatar_stats = avatar_stats
        if created_at is not None:
            self.created_at = created_at
        self.file_size = file_size
        self.success = success
        self.uncompressed_size = uncompressed_size

    @property
    def avatar_stats(self):
        """Gets the avatar_stats of this FileAnalysis.  # noqa: E501


        :return: The avatar_stats of this FileAnalysis.  # noqa: E501
        :rtype: FileAnalysisAvatarStats
        """
        return self._avatar_stats

    @avatar_stats.setter
    def avatar_stats(self, avatar_stats):
        """Sets the avatar_stats of this FileAnalysis.


        :param avatar_stats: The avatar_stats of this FileAnalysis.  # noqa: E501
        :type avatar_stats: FileAnalysisAvatarStats
        """
        if self.local_vars_configuration.client_side_validation and avatar_stats is None:  # noqa: E501
            raise ValueError("Invalid value for `avatar_stats`, must not be `None`")  # noqa: E501

        self._avatar_stats = avatar_stats

    @property
    def created_at(self):
        """Gets the created_at of this FileAnalysis.  # noqa: E501


        :return: The created_at of this FileAnalysis.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileAnalysis.


        :param created_at: The created_at of this FileAnalysis.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def file_size(self):
        """Gets the file_size of this FileAnalysis.  # noqa: E501


        :return: The file_size of this FileAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this FileAnalysis.


        :param file_size: The file_size of this FileAnalysis.  # noqa: E501
        :type file_size: int
        """
        if self.local_vars_configuration.client_side_validation and file_size is None:  # noqa: E501
            raise ValueError("Invalid value for `file_size`, must not be `None`")  # noqa: E501

        self._file_size = file_size

    @property
    def success(self):
        """Gets the success of this FileAnalysis.  # noqa: E501


        :return: The success of this FileAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this FileAnalysis.


        :param success: The success of this FileAnalysis.  # noqa: E501
        :type success: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def uncompressed_size(self):
        """Gets the uncompressed_size of this FileAnalysis.  # noqa: E501


        :return: The uncompressed_size of this FileAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._uncompressed_size

    @uncompressed_size.setter
    def uncompressed_size(self, uncompressed_size):
        """Sets the uncompressed_size of this FileAnalysis.


        :param uncompressed_size: The uncompressed_size of this FileAnalysis.  # noqa: E501
        :type uncompressed_size: int
        """
        if self.local_vars_configuration.client_side_validation and uncompressed_size is None:  # noqa: E501
            raise ValueError("Invalid value for `uncompressed_size`, must not be `None`")  # noqa: E501

        self._uncompressed_size = uncompressed_size

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
        if not isinstance(other, FileAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileAnalysis):
            return True

        return self.to_dict() != other.to_dict()
