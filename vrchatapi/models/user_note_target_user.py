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


class UserNoteTargetUser(object):
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
        'current_avatar_tags': 'list[str]',
        'current_avatar_thumbnail_image_url': 'str',
        'display_name': 'str',
        'id': 'str',
        'profile_pic_override': 'str',
        'user_icon': 'str'
    }

    attribute_map = {
        'current_avatar_tags': 'currentAvatarTags',
        'current_avatar_thumbnail_image_url': 'currentAvatarThumbnailImageUrl',
        'display_name': 'displayName',
        'id': 'id',
        'profile_pic_override': 'profilePicOverride',
        'user_icon': 'userIcon'
    }

    def __init__(self, current_avatar_tags=None, current_avatar_thumbnail_image_url=None, display_name=None, id=None, profile_pic_override=None, user_icon=None, local_vars_configuration=None):  # noqa: E501
        """UserNoteTargetUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._current_avatar_tags = None
        self._current_avatar_thumbnail_image_url = None
        self._display_name = None
        self._id = None
        self._profile_pic_override = None
        self._user_icon = None
        self.discriminator = None

        if current_avatar_tags is not None:
            self.current_avatar_tags = current_avatar_tags
        if current_avatar_thumbnail_image_url is not None:
            self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        self.profile_pic_override = profile_pic_override
        if user_icon is not None:
            self.user_icon = user_icon

    @property
    def current_avatar_tags(self):
        """Gets the current_avatar_tags of this UserNoteTargetUser.  # noqa: E501


        :return: The current_avatar_tags of this UserNoteTargetUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._current_avatar_tags

    @current_avatar_tags.setter
    def current_avatar_tags(self, current_avatar_tags):
        """Sets the current_avatar_tags of this UserNoteTargetUser.


        :param current_avatar_tags: The current_avatar_tags of this UserNoteTargetUser.  # noqa: E501
        :type current_avatar_tags: list[str]
        """

        self._current_avatar_tags = current_avatar_tags

    @property
    def current_avatar_thumbnail_image_url(self):
        """Gets the current_avatar_thumbnail_image_url of this UserNoteTargetUser.  # noqa: E501

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :return: The current_avatar_thumbnail_image_url of this UserNoteTargetUser.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_thumbnail_image_url

    @current_avatar_thumbnail_image_url.setter
    def current_avatar_thumbnail_image_url(self, current_avatar_thumbnail_image_url):
        """Sets the current_avatar_thumbnail_image_url of this UserNoteTargetUser.

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :param current_avatar_thumbnail_image_url: The current_avatar_thumbnail_image_url of this UserNoteTargetUser.  # noqa: E501
        :type current_avatar_thumbnail_image_url: str
        """

        self._current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url

    @property
    def display_name(self):
        """Gets the display_name of this UserNoteTargetUser.  # noqa: E501


        :return: The display_name of this UserNoteTargetUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserNoteTargetUser.


        :param display_name: The display_name of this UserNoteTargetUser.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this UserNoteTargetUser.  # noqa: E501


        :return: The id of this UserNoteTargetUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserNoteTargetUser.


        :param id: The id of this UserNoteTargetUser.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def profile_pic_override(self):
        """Gets the profile_pic_override of this UserNoteTargetUser.  # noqa: E501


        :return: The profile_pic_override of this UserNoteTargetUser.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override

    @profile_pic_override.setter
    def profile_pic_override(self, profile_pic_override):
        """Sets the profile_pic_override of this UserNoteTargetUser.


        :param profile_pic_override: The profile_pic_override of this UserNoteTargetUser.  # noqa: E501
        :type profile_pic_override: str
        """

        self._profile_pic_override = profile_pic_override

    @property
    def user_icon(self):
        """Gets the user_icon of this UserNoteTargetUser.  # noqa: E501


        :return: The user_icon of this UserNoteTargetUser.  # noqa: E501
        :rtype: str
        """
        return self._user_icon

    @user_icon.setter
    def user_icon(self, user_icon):
        """Sets the user_icon of this UserNoteTargetUser.


        :param user_icon: The user_icon of this UserNoteTargetUser.  # noqa: E501
        :type user_icon: str
        """

        self._user_icon = user_icon

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
        if not isinstance(other, UserNoteTargetUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserNoteTargetUser):
            return True

        return self.to_dict() != other.to_dict()
