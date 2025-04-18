# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.19.2
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


class FileVersion(object):
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
        'created_at': 'datetime',
        'deleted': 'bool',
        'delta': 'FileData',
        'file': 'FileData',
        'signature': 'FileData',
        'status': 'FileStatus',
        'version': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'deleted': 'deleted',
        'delta': 'delta',
        'file': 'file',
        'signature': 'signature',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, created_at=None, deleted=True, delta=None, file=None, signature=None, status=None, version=0, local_vars_configuration=None):  # noqa: E501
        """FileVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._deleted = None
        self._delta = None
        self._file = None
        self._signature = None
        self._status = None
        self._version = None
        self.discriminator = None

        self.created_at = created_at
        if deleted is not None:
            self.deleted = deleted
        if delta is not None:
            self.delta = delta
        if file is not None:
            self.file = file
        if signature is not None:
            self.signature = signature
        self.status = status
        self.version = version

    @property
    def created_at(self):
        """Gets the created_at of this FileVersion.  # noqa: E501


        :return: The created_at of this FileVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileVersion.


        :param created_at: The created_at of this FileVersion.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def deleted(self):
        """Gets the deleted of this FileVersion.  # noqa: E501

        Usually only present if `true`  # noqa: E501

        :return: The deleted of this FileVersion.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this FileVersion.

        Usually only present if `true`  # noqa: E501

        :param deleted: The deleted of this FileVersion.  # noqa: E501
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def delta(self):
        """Gets the delta of this FileVersion.  # noqa: E501


        :return: The delta of this FileVersion.  # noqa: E501
        :rtype: FileData
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """Sets the delta of this FileVersion.


        :param delta: The delta of this FileVersion.  # noqa: E501
        :type delta: FileData
        """

        self._delta = delta

    @property
    def file(self):
        """Gets the file of this FileVersion.  # noqa: E501


        :return: The file of this FileVersion.  # noqa: E501
        :rtype: FileData
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileVersion.


        :param file: The file of this FileVersion.  # noqa: E501
        :type file: FileData
        """

        self._file = file

    @property
    def signature(self):
        """Gets the signature of this FileVersion.  # noqa: E501


        :return: The signature of this FileVersion.  # noqa: E501
        :rtype: FileData
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this FileVersion.


        :param signature: The signature of this FileVersion.  # noqa: E501
        :type signature: FileData
        """

        self._signature = signature

    @property
    def status(self):
        """Gets the status of this FileVersion.  # noqa: E501


        :return: The status of this FileVersion.  # noqa: E501
        :rtype: FileStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileVersion.


        :param status: The status of this FileVersion.  # noqa: E501
        :type status: FileStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def version(self):
        """Gets the version of this FileVersion.  # noqa: E501

        Incremental version counter, can only be increased.  # noqa: E501

        :return: The version of this FileVersion.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileVersion.

        Incremental version counter, can only be increased.  # noqa: E501

        :param version: The version of this FileVersion.  # noqa: E501
        :type version: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and version < 0):  # noqa: E501
            raise ValueError("Invalid value for `version`, must be a value greater than or equal to `0`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, FileVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileVersion):
            return True

        return self.to_dict() != other.to_dict()
