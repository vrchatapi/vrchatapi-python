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


class Feedback(object):
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
        'commenter_id': 'str',
        'commenter_name': 'str',
        'content_author_id': 'str',
        'content_author_name': 'str',
        'content_id': 'str',
        'content_name': 'str',
        'content_type': 'str',
        'content_version': 'int',
        'description': 'str',
        'id': 'str',
        'reason': 'str',
        'tags': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'commenter_id': 'commenterId',
        'commenter_name': 'commenterName',
        'content_author_id': 'contentAuthorId',
        'content_author_name': 'contentAuthorName',
        'content_id': 'contentId',
        'content_name': 'contentName',
        'content_type': 'contentType',
        'content_version': 'contentVersion',
        'description': 'description',
        'id': 'id',
        'reason': 'reason',
        'tags': 'tags',
        'type': 'type'
    }

    def __init__(self, commenter_id=None, commenter_name=None, content_author_id=None, content_author_name=None, content_id=None, content_name=None, content_type=None, content_version=None, description=None, id=None, reason=None, tags=None, type=None, local_vars_configuration=None):  # noqa: E501
        """Feedback - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._commenter_id = None
        self._commenter_name = None
        self._content_author_id = None
        self._content_author_name = None
        self._content_id = None
        self._content_name = None
        self._content_type = None
        self._content_version = None
        self._description = None
        self._id = None
        self._reason = None
        self._tags = None
        self._type = None
        self.discriminator = None

        self.commenter_id = commenter_id
        self.commenter_name = commenter_name
        self.content_author_id = content_author_id
        self.content_author_name = content_author_name
        self.content_id = content_id
        if content_name is not None:
            self.content_name = content_name
        self.content_type = content_type
        self.content_version = content_version
        self.description = description
        self.id = id
        self.reason = reason
        self.tags = tags
        self.type = type

    @property
    def commenter_id(self):
        """Gets the commenter_id of this Feedback.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The commenter_id of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._commenter_id

    @commenter_id.setter
    def commenter_id(self, commenter_id):
        """Sets the commenter_id of this Feedback.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param commenter_id: The commenter_id of this Feedback.  # noqa: E501
        :type commenter_id: str
        """
        if self.local_vars_configuration.client_side_validation and commenter_id is None:  # noqa: E501
            raise ValueError("Invalid value for `commenter_id`, must not be `None`")  # noqa: E501

        self._commenter_id = commenter_id

    @property
    def commenter_name(self):
        """Gets the commenter_name of this Feedback.  # noqa: E501


        :return: The commenter_name of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._commenter_name

    @commenter_name.setter
    def commenter_name(self, commenter_name):
        """Sets the commenter_name of this Feedback.


        :param commenter_name: The commenter_name of this Feedback.  # noqa: E501
        :type commenter_name: str
        """
        if self.local_vars_configuration.client_side_validation and commenter_name is None:  # noqa: E501
            raise ValueError("Invalid value for `commenter_name`, must not be `None`")  # noqa: E501

        self._commenter_name = commenter_name

    @property
    def content_author_id(self):
        """Gets the content_author_id of this Feedback.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The content_author_id of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._content_author_id

    @content_author_id.setter
    def content_author_id(self, content_author_id):
        """Sets the content_author_id of this Feedback.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param content_author_id: The content_author_id of this Feedback.  # noqa: E501
        :type content_author_id: str
        """
        if self.local_vars_configuration.client_side_validation and content_author_id is None:  # noqa: E501
            raise ValueError("Invalid value for `content_author_id`, must not be `None`")  # noqa: E501

        self._content_author_id = content_author_id

    @property
    def content_author_name(self):
        """Gets the content_author_name of this Feedback.  # noqa: E501


        :return: The content_author_name of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._content_author_name

    @content_author_name.setter
    def content_author_name(self, content_author_name):
        """Sets the content_author_name of this Feedback.


        :param content_author_name: The content_author_name of this Feedback.  # noqa: E501
        :type content_author_name: str
        """

        self._content_author_name = content_author_name

    @property
    def content_id(self):
        """Gets the content_id of this Feedback.  # noqa: E501


        :return: The content_id of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this Feedback.


        :param content_id: The content_id of this Feedback.  # noqa: E501
        :type content_id: str
        """
        if self.local_vars_configuration.client_side_validation and content_id is None:  # noqa: E501
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501

        self._content_id = content_id

    @property
    def content_name(self):
        """Gets the content_name of this Feedback.  # noqa: E501


        :return: The content_name of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._content_name

    @content_name.setter
    def content_name(self, content_name):
        """Sets the content_name of this Feedback.


        :param content_name: The content_name of this Feedback.  # noqa: E501
        :type content_name: str
        """

        self._content_name = content_name

    @property
    def content_type(self):
        """Gets the content_type of this Feedback.  # noqa: E501


        :return: The content_type of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Feedback.


        :param content_type: The content_type of this Feedback.  # noqa: E501
        :type content_type: str
        """
        if self.local_vars_configuration.client_side_validation and content_type is None:  # noqa: E501
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def content_version(self):
        """Gets the content_version of this Feedback.  # noqa: E501


        :return: The content_version of this Feedback.  # noqa: E501
        :rtype: int
        """
        return self._content_version

    @content_version.setter
    def content_version(self, content_version):
        """Sets the content_version of this Feedback.


        :param content_version: The content_version of this Feedback.  # noqa: E501
        :type content_version: int
        """

        self._content_version = content_version

    @property
    def description(self):
        """Gets the description of this Feedback.  # noqa: E501


        :return: The description of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Feedback.


        :param description: The description of this Feedback.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Feedback.  # noqa: E501


        :return: The id of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Feedback.


        :param id: The id of this Feedback.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this Feedback.  # noqa: E501


        :return: The reason of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Feedback.


        :param reason: The reason of this Feedback.  # noqa: E501
        :type reason: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def tags(self):
        """Gets the tags of this Feedback.  # noqa: E501


        :return: The tags of this Feedback.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Feedback.


        :param tags: The tags of this Feedback.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this Feedback.  # noqa: E501


        :return: The type of this Feedback.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Feedback.


        :param type: The type of this Feedback.  # noqa: E501
        :type type: str
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
        if not isinstance(other, Feedback):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Feedback):
            return True

        return self.to_dict() != other.to_dict()
