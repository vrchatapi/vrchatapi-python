# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.0
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


class CreateGroupPostRequest(object):
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
        'title': 'str',
        'text': 'str',
        'image_id': 'str',
        'send_notification': 'bool',
        'role_ids': 'list[str]',
        'visibility': 'GroupPostVisibility'
    }

    attribute_map = {
        'title': 'title',
        'text': 'text',
        'image_id': 'imageId',
        'send_notification': 'sendNotification',
        'role_ids': 'roleIds',
        'visibility': 'visibility'
    }

    def __init__(self, title=None, text=None, image_id=None, send_notification=False, role_ids=None, visibility=None, local_vars_configuration=None):  # noqa: E501
        """CreateGroupPostRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._text = None
        self._image_id = None
        self._send_notification = None
        self._role_ids = None
        self._visibility = None
        self.discriminator = None

        self.title = title
        self.text = text
        if image_id is not None:
            self.image_id = image_id
        self.send_notification = send_notification
        if role_ids is not None:
            self.role_ids = role_ids
        self.visibility = visibility

    @property
    def title(self):
        """Gets the title of this CreateGroupPostRequest.  # noqa: E501

        Post title  # noqa: E501

        :return: The title of this CreateGroupPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateGroupPostRequest.

        Post title  # noqa: E501

        :param title: The title of this CreateGroupPostRequest.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def text(self):
        """Gets the text of this CreateGroupPostRequest.  # noqa: E501

        Post text  # noqa: E501

        :return: The text of this CreateGroupPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateGroupPostRequest.

        Post text  # noqa: E501

        :param text: The text of this CreateGroupPostRequest.  # noqa: E501
        :type text: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def image_id(self):
        """Gets the image_id of this CreateGroupPostRequest.  # noqa: E501


        :return: The image_id of this CreateGroupPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateGroupPostRequest.


        :param image_id: The image_id of this CreateGroupPostRequest.  # noqa: E501
        :type image_id: str
        """

        self._image_id = image_id

    @property
    def send_notification(self):
        """Gets the send_notification of this CreateGroupPostRequest.  # noqa: E501

        Send notification to group members.  # noqa: E501

        :return: The send_notification of this CreateGroupPostRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this CreateGroupPostRequest.

        Send notification to group members.  # noqa: E501

        :param send_notification: The send_notification of this CreateGroupPostRequest.  # noqa: E501
        :type send_notification: bool
        """
        if self.local_vars_configuration.client_side_validation and send_notification is None:  # noqa: E501
            raise ValueError("Invalid value for `send_notification`, must not be `None`")  # noqa: E501

        self._send_notification = send_notification

    @property
    def role_ids(self):
        """Gets the role_ids of this CreateGroupPostRequest.  # noqa: E501

           # noqa: E501

        :return: The role_ids of this CreateGroupPostRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this CreateGroupPostRequest.

           # noqa: E501

        :param role_ids: The role_ids of this CreateGroupPostRequest.  # noqa: E501
        :type role_ids: list[str]
        """

        self._role_ids = role_ids

    @property
    def visibility(self):
        """Gets the visibility of this CreateGroupPostRequest.  # noqa: E501


        :return: The visibility of this CreateGroupPostRequest.  # noqa: E501
        :rtype: GroupPostVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this CreateGroupPostRequest.


        :param visibility: The visibility of this CreateGroupPostRequest.  # noqa: E501
        :type visibility: GroupPostVisibility
        """
        if self.local_vars_configuration.client_side_validation and visibility is None:  # noqa: E501
            raise ValueError("Invalid value for `visibility`, must not be `None`")  # noqa: E501

        self._visibility = visibility

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
        if not isinstance(other, CreateGroupPostRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGroupPostRequest):
            return True

        return self.to_dict() != other.to_dict()