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


class CurrentUserPresence(object):
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
        'avatar_thumbnail': 'str',
        'current_avatar_tags': 'str',
        'display_name': 'str',
        'groups': 'list[str]',
        'id': 'str',
        'instance': 'str',
        'instance_type': 'str',
        'is_rejoining': 'str',
        'platform': 'str',
        'profile_pic_override': 'str',
        'status': 'str',
        'traveling_to_instance': 'str',
        'traveling_to_world': 'str',
        'user_icon': 'str',
        'world': 'str'
    }

    attribute_map = {
        'avatar_thumbnail': 'avatarThumbnail',
        'current_avatar_tags': 'currentAvatarTags',
        'display_name': 'displayName',
        'groups': 'groups',
        'id': 'id',
        'instance': 'instance',
        'instance_type': 'instanceType',
        'is_rejoining': 'isRejoining',
        'platform': 'platform',
        'profile_pic_override': 'profilePicOverride',
        'status': 'status',
        'traveling_to_instance': 'travelingToInstance',
        'traveling_to_world': 'travelingToWorld',
        'user_icon': 'userIcon',
        'world': 'world'
    }

    def __init__(self, avatar_thumbnail=None, current_avatar_tags=None, display_name=None, groups=None, id=None, instance=None, instance_type=None, is_rejoining=None, platform=None, profile_pic_override=None, status=None, traveling_to_instance=None, traveling_to_world=None, user_icon=None, world=None, local_vars_configuration=None):  # noqa: E501
        """CurrentUserPresence - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._avatar_thumbnail = None
        self._current_avatar_tags = None
        self._display_name = None
        self._groups = None
        self._id = None
        self._instance = None
        self._instance_type = None
        self._is_rejoining = None
        self._platform = None
        self._profile_pic_override = None
        self._status = None
        self._traveling_to_instance = None
        self._traveling_to_world = None
        self._user_icon = None
        self._world = None
        self.discriminator = None

        self.avatar_thumbnail = avatar_thumbnail
        if current_avatar_tags is not None:
            self.current_avatar_tags = current_avatar_tags
        if display_name is not None:
            self.display_name = display_name
        self.groups = groups
        if id is not None:
            self.id = id
        self.instance = instance
        self.instance_type = instance_type
        self.is_rejoining = is_rejoining
        self.platform = platform
        self.profile_pic_override = profile_pic_override
        self.status = status
        self.traveling_to_instance = traveling_to_instance
        if traveling_to_world is not None:
            self.traveling_to_world = traveling_to_world
        self.user_icon = user_icon
        if world is not None:
            self.world = world

    @property
    def avatar_thumbnail(self):
        """Gets the avatar_thumbnail of this CurrentUserPresence.  # noqa: E501


        :return: The avatar_thumbnail of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._avatar_thumbnail

    @avatar_thumbnail.setter
    def avatar_thumbnail(self, avatar_thumbnail):
        """Sets the avatar_thumbnail of this CurrentUserPresence.


        :param avatar_thumbnail: The avatar_thumbnail of this CurrentUserPresence.  # noqa: E501
        :type avatar_thumbnail: str
        """

        self._avatar_thumbnail = avatar_thumbnail

    @property
    def current_avatar_tags(self):
        """Gets the current_avatar_tags of this CurrentUserPresence.  # noqa: E501


        :return: The current_avatar_tags of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_tags

    @current_avatar_tags.setter
    def current_avatar_tags(self, current_avatar_tags):
        """Sets the current_avatar_tags of this CurrentUserPresence.


        :param current_avatar_tags: The current_avatar_tags of this CurrentUserPresence.  # noqa: E501
        :type current_avatar_tags: str
        """

        self._current_avatar_tags = current_avatar_tags

    @property
    def display_name(self):
        """Gets the display_name of this CurrentUserPresence.  # noqa: E501


        :return: The display_name of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CurrentUserPresence.


        :param display_name: The display_name of this CurrentUserPresence.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def groups(self):
        """Gets the groups of this CurrentUserPresence.  # noqa: E501


        :return: The groups of this CurrentUserPresence.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this CurrentUserPresence.


        :param groups: The groups of this CurrentUserPresence.  # noqa: E501
        :type groups: list[str]
        """

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this CurrentUserPresence.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The id of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrentUserPresence.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param id: The id of this CurrentUserPresence.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def instance(self):
        """Gets the instance of this CurrentUserPresence.  # noqa: E501


        :return: The instance of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this CurrentUserPresence.


        :param instance: The instance of this CurrentUserPresence.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def instance_type(self):
        """Gets the instance_type of this CurrentUserPresence.  # noqa: E501

        either an InstanceType or an empty string  # noqa: E501

        :return: The instance_type of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this CurrentUserPresence.

        either an InstanceType or an empty string  # noqa: E501

        :param instance_type: The instance_type of this CurrentUserPresence.  # noqa: E501
        :type instance_type: str
        """

        self._instance_type = instance_type

    @property
    def is_rejoining(self):
        """Gets the is_rejoining of this CurrentUserPresence.  # noqa: E501


        :return: The is_rejoining of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._is_rejoining

    @is_rejoining.setter
    def is_rejoining(self, is_rejoining):
        """Sets the is_rejoining of this CurrentUserPresence.


        :param is_rejoining: The is_rejoining of this CurrentUserPresence.  # noqa: E501
        :type is_rejoining: str
        """

        self._is_rejoining = is_rejoining

    @property
    def platform(self):
        """Gets the platform of this CurrentUserPresence.  # noqa: E501

        either a Platform or an empty string  # noqa: E501

        :return: The platform of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this CurrentUserPresence.

        either a Platform or an empty string  # noqa: E501

        :param platform: The platform of this CurrentUserPresence.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def profile_pic_override(self):
        """Gets the profile_pic_override of this CurrentUserPresence.  # noqa: E501


        :return: The profile_pic_override of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override

    @profile_pic_override.setter
    def profile_pic_override(self, profile_pic_override):
        """Sets the profile_pic_override of this CurrentUserPresence.


        :param profile_pic_override: The profile_pic_override of this CurrentUserPresence.  # noqa: E501
        :type profile_pic_override: str
        """

        self._profile_pic_override = profile_pic_override

    @property
    def status(self):
        """Gets the status of this CurrentUserPresence.  # noqa: E501

        either a UserStatus or empty string  # noqa: E501

        :return: The status of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CurrentUserPresence.

        either a UserStatus or empty string  # noqa: E501

        :param status: The status of this CurrentUserPresence.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def traveling_to_instance(self):
        """Gets the traveling_to_instance of this CurrentUserPresence.  # noqa: E501


        :return: The traveling_to_instance of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._traveling_to_instance

    @traveling_to_instance.setter
    def traveling_to_instance(self, traveling_to_instance):
        """Sets the traveling_to_instance of this CurrentUserPresence.


        :param traveling_to_instance: The traveling_to_instance of this CurrentUserPresence.  # noqa: E501
        :type traveling_to_instance: str
        """

        self._traveling_to_instance = traveling_to_instance

    @property
    def traveling_to_world(self):
        """Gets the traveling_to_world of this CurrentUserPresence.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The traveling_to_world of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._traveling_to_world

    @traveling_to_world.setter
    def traveling_to_world(self, traveling_to_world):
        """Sets the traveling_to_world of this CurrentUserPresence.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param traveling_to_world: The traveling_to_world of this CurrentUserPresence.  # noqa: E501
        :type traveling_to_world: str
        """

        self._traveling_to_world = traveling_to_world

    @property
    def user_icon(self):
        """Gets the user_icon of this CurrentUserPresence.  # noqa: E501


        :return: The user_icon of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._user_icon

    @user_icon.setter
    def user_icon(self, user_icon):
        """Sets the user_icon of this CurrentUserPresence.


        :param user_icon: The user_icon of this CurrentUserPresence.  # noqa: E501
        :type user_icon: str
        """

        self._user_icon = user_icon

    @property
    def world(self):
        """Gets the world of this CurrentUserPresence.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The world of this CurrentUserPresence.  # noqa: E501
        :rtype: str
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this CurrentUserPresence.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param world: The world of this CurrentUserPresence.  # noqa: E501
        :type world: str
        """

        self._world = world

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
        if not isinstance(other, CurrentUserPresence):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurrentUserPresence):
            return True

        return self.to_dict() != other.to_dict()
