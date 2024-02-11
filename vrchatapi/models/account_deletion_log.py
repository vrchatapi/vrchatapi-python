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


class AccountDeletionLog(object):
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
        'deletion_scheduled': 'datetime',
        'date_time': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'deletion_scheduled': 'deletionScheduled',
        'date_time': 'dateTime'
    }

    def __init__(self, message='Deletion requested', deletion_scheduled=None, date_time=None, local_vars_configuration=None):  # noqa: E501
        """AccountDeletionLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._deletion_scheduled = None
        self._date_time = None
        self.discriminator = None

        if message is not None:
            self.message = message
        self.deletion_scheduled = deletion_scheduled
        if date_time is not None:
            self.date_time = date_time

    @property
    def message(self):
        """Gets the message of this AccountDeletionLog.  # noqa: E501

        Typically \"Deletion requested\" or \"Deletion canceled\". Other messages like \"Deletion completed\" may exist, but are these are not possible to see as a regular user.  # noqa: E501

        :return: The message of this AccountDeletionLog.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AccountDeletionLog.

        Typically \"Deletion requested\" or \"Deletion canceled\". Other messages like \"Deletion completed\" may exist, but are these are not possible to see as a regular user.  # noqa: E501

        :param message: The message of this AccountDeletionLog.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def deletion_scheduled(self):
        """Gets the deletion_scheduled of this AccountDeletionLog.  # noqa: E501

        When the deletion is scheduled to happen, standard is 14 days after the request.  # noqa: E501

        :return: The deletion_scheduled of this AccountDeletionLog.  # noqa: E501
        :rtype: datetime
        """
        return self._deletion_scheduled

    @deletion_scheduled.setter
    def deletion_scheduled(self, deletion_scheduled):
        """Sets the deletion_scheduled of this AccountDeletionLog.

        When the deletion is scheduled to happen, standard is 14 days after the request.  # noqa: E501

        :param deletion_scheduled: The deletion_scheduled of this AccountDeletionLog.  # noqa: E501
        :type deletion_scheduled: datetime
        """

        self._deletion_scheduled = deletion_scheduled

    @property
    def date_time(self):
        """Gets the date_time of this AccountDeletionLog.  # noqa: E501

        Date and time of the deletion request.  # noqa: E501

        :return: The date_time of this AccountDeletionLog.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this AccountDeletionLog.

        Date and time of the deletion request.  # noqa: E501

        :param date_time: The date_time of this AccountDeletionLog.  # noqa: E501
        :type date_time: datetime
        """

        self._date_time = date_time

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
        if not isinstance(other, AccountDeletionLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDeletionLog):
            return True

        return self.to_dict() != other.to_dict()
