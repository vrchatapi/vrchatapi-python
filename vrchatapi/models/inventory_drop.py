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


class InventoryDrop(object):
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
        'author_id': 'str',
        'created_at': 'datetime',
        'drop_expiry_date': 'datetime',
        'end_drop_date': 'datetime',
        'id': 'str',
        'name': 'str',
        'notification_details': 'InventoryNotificationDetails',
        'start_drop_date': 'datetime',
        'status': 'str',
        'tags': 'list[str]',
        'target_group': 'str',
        'template_ids': 'list[str]',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'author_id': 'authorId',
        'created_at': 'created_at',
        'drop_expiry_date': 'dropExpiryDate',
        'end_drop_date': 'endDropDate',
        'id': 'id',
        'name': 'name',
        'notification_details': 'notificationDetails',
        'start_drop_date': 'startDropDate',
        'status': 'status',
        'tags': 'tags',
        'target_group': 'targetGroup',
        'template_ids': 'templateIds',
        'updated_at': 'updated_at'
    }

    def __init__(self, author_id=None, created_at=None, drop_expiry_date=None, end_drop_date=None, id=None, name=None, notification_details=None, start_drop_date=None, status=None, tags=None, target_group=None, template_ids=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """InventoryDrop - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._author_id = None
        self._created_at = None
        self._drop_expiry_date = None
        self._end_drop_date = None
        self._id = None
        self._name = None
        self._notification_details = None
        self._start_drop_date = None
        self._status = None
        self._tags = None
        self._target_group = None
        self._template_ids = None
        self._updated_at = None
        self.discriminator = None

        self.author_id = author_id
        self.created_at = created_at
        self.drop_expiry_date = drop_expiry_date
        self.end_drop_date = end_drop_date
        self.id = id
        self.name = name
        self.notification_details = notification_details
        self.start_drop_date = start_drop_date
        self.status = status
        self.tags = tags
        self.target_group = target_group
        self.template_ids = template_ids
        self.updated_at = updated_at

    @property
    def author_id(self):
        """Gets the author_id of this InventoryDrop.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The author_id of this InventoryDrop.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this InventoryDrop.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param author_id: The author_id of this InventoryDrop.  # noqa: E501
        :type author_id: str
        """
        if self.local_vars_configuration.client_side_validation and author_id is None:  # noqa: E501
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id

    @property
    def created_at(self):
        """Gets the created_at of this InventoryDrop.  # noqa: E501


        :return: The created_at of this InventoryDrop.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InventoryDrop.


        :param created_at: The created_at of this InventoryDrop.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def drop_expiry_date(self):
        """Gets the drop_expiry_date of this InventoryDrop.  # noqa: E501


        :return: The drop_expiry_date of this InventoryDrop.  # noqa: E501
        :rtype: datetime
        """
        return self._drop_expiry_date

    @drop_expiry_date.setter
    def drop_expiry_date(self, drop_expiry_date):
        """Sets the drop_expiry_date of this InventoryDrop.


        :param drop_expiry_date: The drop_expiry_date of this InventoryDrop.  # noqa: E501
        :type drop_expiry_date: datetime
        """

        self._drop_expiry_date = drop_expiry_date

    @property
    def end_drop_date(self):
        """Gets the end_drop_date of this InventoryDrop.  # noqa: E501


        :return: The end_drop_date of this InventoryDrop.  # noqa: E501
        :rtype: datetime
        """
        return self._end_drop_date

    @end_drop_date.setter
    def end_drop_date(self, end_drop_date):
        """Sets the end_drop_date of this InventoryDrop.


        :param end_drop_date: The end_drop_date of this InventoryDrop.  # noqa: E501
        :type end_drop_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_drop_date is None:  # noqa: E501
            raise ValueError("Invalid value for `end_drop_date`, must not be `None`")  # noqa: E501

        self._end_drop_date = end_drop_date

    @property
    def id(self):
        """Gets the id of this InventoryDrop.  # noqa: E501


        :return: The id of this InventoryDrop.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryDrop.


        :param id: The id of this InventoryDrop.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this InventoryDrop.  # noqa: E501


        :return: The name of this InventoryDrop.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InventoryDrop.


        :param name: The name of this InventoryDrop.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notification_details(self):
        """Gets the notification_details of this InventoryDrop.  # noqa: E501


        :return: The notification_details of this InventoryDrop.  # noqa: E501
        :rtype: InventoryNotificationDetails
        """
        return self._notification_details

    @notification_details.setter
    def notification_details(self, notification_details):
        """Sets the notification_details of this InventoryDrop.


        :param notification_details: The notification_details of this InventoryDrop.  # noqa: E501
        :type notification_details: InventoryNotificationDetails
        """
        if self.local_vars_configuration.client_side_validation and notification_details is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_details`, must not be `None`")  # noqa: E501

        self._notification_details = notification_details

    @property
    def start_drop_date(self):
        """Gets the start_drop_date of this InventoryDrop.  # noqa: E501


        :return: The start_drop_date of this InventoryDrop.  # noqa: E501
        :rtype: datetime
        """
        return self._start_drop_date

    @start_drop_date.setter
    def start_drop_date(self, start_drop_date):
        """Sets the start_drop_date of this InventoryDrop.


        :param start_drop_date: The start_drop_date of this InventoryDrop.  # noqa: E501
        :type start_drop_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_drop_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_drop_date`, must not be `None`")  # noqa: E501

        self._start_drop_date = start_drop_date

    @property
    def status(self):
        """Gets the status of this InventoryDrop.  # noqa: E501


        :return: The status of this InventoryDrop.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InventoryDrop.


        :param status: The status of this InventoryDrop.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this InventoryDrop.  # noqa: E501


        :return: The tags of this InventoryDrop.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InventoryDrop.


        :param tags: The tags of this InventoryDrop.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def target_group(self):
        """Gets the target_group of this InventoryDrop.  # noqa: E501


        :return: The target_group of this InventoryDrop.  # noqa: E501
        :rtype: str
        """
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        """Sets the target_group of this InventoryDrop.


        :param target_group: The target_group of this InventoryDrop.  # noqa: E501
        :type target_group: str
        """
        if self.local_vars_configuration.client_side_validation and target_group is None:  # noqa: E501
            raise ValueError("Invalid value for `target_group`, must not be `None`")  # noqa: E501

        self._target_group = target_group

    @property
    def template_ids(self):
        """Gets the template_ids of this InventoryDrop.  # noqa: E501


        :return: The template_ids of this InventoryDrop.  # noqa: E501
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        """Sets the template_ids of this InventoryDrop.


        :param template_ids: The template_ids of this InventoryDrop.  # noqa: E501
        :type template_ids: list[str]
        """
        if self.local_vars_configuration.client_side_validation and template_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `template_ids`, must not be `None`")  # noqa: E501

        self._template_ids = template_ids

    @property
    def updated_at(self):
        """Gets the updated_at of this InventoryDrop.  # noqa: E501


        :return: The updated_at of this InventoryDrop.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InventoryDrop.


        :param updated_at: The updated_at of this InventoryDrop.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, InventoryDrop):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InventoryDrop):
            return True

        return self.to_dict() != other.to_dict()
