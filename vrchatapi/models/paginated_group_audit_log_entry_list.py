# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.20.1
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


class PaginatedGroupAuditLogEntryList(object):
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
        'results': 'list[GroupAuditLogEntry]',
        'total_count': 'int',
        'has_next': 'bool'
    }

    attribute_map = {
        'results': 'results',
        'total_count': 'totalCount',
        'has_next': 'hasNext'
    }

    def __init__(self, results=None, total_count=None, has_next=None, local_vars_configuration=None):  # noqa: E501
        """PaginatedGroupAuditLogEntryList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._results = None
        self._total_count = None
        self._has_next = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if total_count is not None:
            self.total_count = total_count
        if has_next is not None:
            self.has_next = has_next

    @property
    def results(self):
        """Gets the results of this PaginatedGroupAuditLogEntryList.  # noqa: E501

           # noqa: E501

        :return: The results of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :rtype: list[GroupAuditLogEntry]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedGroupAuditLogEntryList.

           # noqa: E501

        :param results: The results of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :type results: list[GroupAuditLogEntry]
        """

        self._results = results

    @property
    def total_count(self):
        """Gets the total_count of this PaginatedGroupAuditLogEntryList.  # noqa: E501

        The total number of results that the query would return if there were no pagination.  # noqa: E501

        :return: The total_count of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginatedGroupAuditLogEntryList.

        The total number of results that the query would return if there were no pagination.  # noqa: E501

        :param total_count: The total_count of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def has_next(self):
        """Gets the has_next of this PaginatedGroupAuditLogEntryList.  # noqa: E501

        Whether there are more results after this page.  # noqa: E501

        :return: The has_next of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this PaginatedGroupAuditLogEntryList.

        Whether there are more results after this page.  # noqa: E501

        :param has_next: The has_next of this PaginatedGroupAuditLogEntryList.  # noqa: E501
        :type has_next: bool
        """

        self._has_next = has_next

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
        if not isinstance(other, PaginatedGroupAuditLogEntryList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaginatedGroupAuditLogEntryList):
            return True

        return self.to_dict() != other.to_dict()
