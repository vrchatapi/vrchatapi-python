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


class PlayerModeration(object):
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
        'created': 'datetime',
        'id': 'str',
        'source_display_name': 'str',
        'source_user_id': 'str',
        'target_display_name': 'str',
        'target_user_id': 'str',
        'type': 'PlayerModerationType'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'source_display_name': 'sourceDisplayName',
        'source_user_id': 'sourceUserId',
        'target_display_name': 'targetDisplayName',
        'target_user_id': 'targetUserId',
        'type': 'type'
    }

    def __init__(self, created=None, id=None, source_display_name=None, source_user_id=None, target_display_name=None, target_user_id=None, type=None, local_vars_configuration=None):  # noqa: E501
        """PlayerModeration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._id = None
        self._source_display_name = None
        self._source_user_id = None
        self._target_display_name = None
        self._target_user_id = None
        self._type = None
        self.discriminator = None

        self.created = created
        self.id = id
        self.source_display_name = source_display_name
        self.source_user_id = source_user_id
        self.target_display_name = target_display_name
        self.target_user_id = target_user_id
        self.type = type

    @property
    def created(self):
        """Gets the created of this PlayerModeration.  # noqa: E501


        :return: The created of this PlayerModeration.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PlayerModeration.


        :param created: The created of this PlayerModeration.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this PlayerModeration.  # noqa: E501


        :return: The id of this PlayerModeration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayerModeration.


        :param id: The id of this PlayerModeration.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def source_display_name(self):
        """Gets the source_display_name of this PlayerModeration.  # noqa: E501


        :return: The source_display_name of this PlayerModeration.  # noqa: E501
        :rtype: str
        """
        return self._source_display_name

    @source_display_name.setter
    def source_display_name(self, source_display_name):
        """Sets the source_display_name of this PlayerModeration.


        :param source_display_name: The source_display_name of this PlayerModeration.  # noqa: E501
        :type source_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and source_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `source_display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                source_display_name is not None and len(source_display_name) < 1):
            raise ValueError("Invalid value for `source_display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._source_display_name = source_display_name

    @property
    def source_user_id(self):
        """Gets the source_user_id of this PlayerModeration.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The source_user_id of this PlayerModeration.  # noqa: E501
        :rtype: str
        """
        return self._source_user_id

    @source_user_id.setter
    def source_user_id(self, source_user_id):
        """Sets the source_user_id of this PlayerModeration.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param source_user_id: The source_user_id of this PlayerModeration.  # noqa: E501
        :type source_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and source_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `source_user_id`, must not be `None`")  # noqa: E501

        self._source_user_id = source_user_id

    @property
    def target_display_name(self):
        """Gets the target_display_name of this PlayerModeration.  # noqa: E501


        :return: The target_display_name of this PlayerModeration.  # noqa: E501
        :rtype: str
        """
        return self._target_display_name

    @target_display_name.setter
    def target_display_name(self, target_display_name):
        """Sets the target_display_name of this PlayerModeration.


        :param target_display_name: The target_display_name of this PlayerModeration.  # noqa: E501
        :type target_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and target_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `target_display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                target_display_name is not None and len(target_display_name) < 1):
            raise ValueError("Invalid value for `target_display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._target_display_name = target_display_name

    @property
    def target_user_id(self):
        """Gets the target_user_id of this PlayerModeration.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The target_user_id of this PlayerModeration.  # noqa: E501
        :rtype: str
        """
        return self._target_user_id

    @target_user_id.setter
    def target_user_id(self, target_user_id):
        """Sets the target_user_id of this PlayerModeration.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param target_user_id: The target_user_id of this PlayerModeration.  # noqa: E501
        :type target_user_id: str
        """
        if self.local_vars_configuration.client_side_validation and target_user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_user_id`, must not be `None`")  # noqa: E501

        self._target_user_id = target_user_id

    @property
    def type(self):
        """Gets the type of this PlayerModeration.  # noqa: E501


        :return: The type of this PlayerModeration.  # noqa: E501
        :rtype: PlayerModerationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PlayerModeration.


        :param type: The type of this PlayerModeration.  # noqa: E501
        :type type: PlayerModerationType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, PlayerModeration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerModeration):
            return True

        return self.to_dict() != other.to_dict()
