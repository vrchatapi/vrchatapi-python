# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.2
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


class GroupMemberLimitedUser(object):
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
        'id': 'str',
        'display_name': 'str',
        'thumbnail_url': 'str',
        'icon_url': 'str',
        'profile_pic_override': 'str',
        'current_avatar_thumbnail_image_url': 'str',
        'current_avatar_tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'thumbnail_url': 'thumbnailUrl',
        'icon_url': 'iconUrl',
        'profile_pic_override': 'profilePicOverride',
        'current_avatar_thumbnail_image_url': 'currentAvatarThumbnailImageUrl',
        'current_avatar_tags': 'currentAvatarTags'
    }

    def __init__(self, id=None, display_name=None, thumbnail_url=None, icon_url=None, profile_pic_override=None, current_avatar_thumbnail_image_url=None, current_avatar_tags=None, local_vars_configuration=None):  # noqa: E501
        """GroupMemberLimitedUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._thumbnail_url = None
        self._icon_url = None
        self._profile_pic_override = None
        self._current_avatar_thumbnail_image_url = None
        self._current_avatar_tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        self.thumbnail_url = thumbnail_url
        if icon_url is not None:
            self.icon_url = icon_url
        if profile_pic_override is not None:
            self.profile_pic_override = profile_pic_override
        self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        if current_avatar_tags is not None:
            self.current_avatar_tags = current_avatar_tags

    @property
    def id(self):
        """Gets the id of this GroupMemberLimitedUser.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The id of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupMemberLimitedUser.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param id: The id of this GroupMemberLimitedUser.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this GroupMemberLimitedUser.  # noqa: E501


        :return: The display_name of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GroupMemberLimitedUser.


        :param display_name: The display_name of this GroupMemberLimitedUser.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this GroupMemberLimitedUser.  # noqa: E501


        :return: The thumbnail_url of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this GroupMemberLimitedUser.


        :param thumbnail_url: The thumbnail_url of this GroupMemberLimitedUser.  # noqa: E501
        :type thumbnail_url: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def icon_url(self):
        """Gets the icon_url of this GroupMemberLimitedUser.  # noqa: E501


        :return: The icon_url of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this GroupMemberLimitedUser.


        :param icon_url: The icon_url of this GroupMemberLimitedUser.  # noqa: E501
        :type icon_url: str
        """

        self._icon_url = icon_url

    @property
    def profile_pic_override(self):
        """Gets the profile_pic_override of this GroupMemberLimitedUser.  # noqa: E501


        :return: The profile_pic_override of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override

    @profile_pic_override.setter
    def profile_pic_override(self, profile_pic_override):
        """Sets the profile_pic_override of this GroupMemberLimitedUser.


        :param profile_pic_override: The profile_pic_override of this GroupMemberLimitedUser.  # noqa: E501
        :type profile_pic_override: str
        """

        self._profile_pic_override = profile_pic_override

    @property
    def current_avatar_thumbnail_image_url(self):
        """Gets the current_avatar_thumbnail_image_url of this GroupMemberLimitedUser.  # noqa: E501


        :return: The current_avatar_thumbnail_image_url of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_thumbnail_image_url

    @current_avatar_thumbnail_image_url.setter
    def current_avatar_thumbnail_image_url(self, current_avatar_thumbnail_image_url):
        """Sets the current_avatar_thumbnail_image_url of this GroupMemberLimitedUser.


        :param current_avatar_thumbnail_image_url: The current_avatar_thumbnail_image_url of this GroupMemberLimitedUser.  # noqa: E501
        :type current_avatar_thumbnail_image_url: str
        """

        self._current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url

    @property
    def current_avatar_tags(self):
        """Gets the current_avatar_tags of this GroupMemberLimitedUser.  # noqa: E501


        :return: The current_avatar_tags of this GroupMemberLimitedUser.  # noqa: E501
        :rtype: list[str]
        """
        return self._current_avatar_tags

    @current_avatar_tags.setter
    def current_avatar_tags(self, current_avatar_tags):
        """Sets the current_avatar_tags of this GroupMemberLimitedUser.


        :param current_avatar_tags: The current_avatar_tags of this GroupMemberLimitedUser.  # noqa: E501
        :type current_avatar_tags: list[str]
        """

        self._current_avatar_tags = current_avatar_tags

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
        if not isinstance(other, GroupMemberLimitedUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupMemberLimitedUser):
            return True

        return self.to_dict() != other.to_dict()
