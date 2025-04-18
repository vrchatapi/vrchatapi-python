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


class User(object):
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
        'age_verification_status': 'AgeVerificationStatus',
        'age_verified': 'bool',
        'allow_avatar_copying': 'bool',
        'badges': 'list[Badge]',
        'bio': 'str',
        'bio_links': 'list[str]',
        'current_avatar_image_url': 'str',
        'current_avatar_thumbnail_image_url': 'str',
        'current_avatar_tags': 'list[str]',
        'date_joined': 'date',
        'developer_type': 'DeveloperType',
        'display_name': 'str',
        'friend_key': 'str',
        'friend_request_status': 'str',
        'id': 'str',
        'instance_id': 'str',
        'is_friend': 'bool',
        'last_activity': 'str',
        'last_login': 'str',
        'last_mobile': 'str',
        'last_platform': 'str',
        'location': 'str',
        'note': 'str',
        'platform': 'str',
        'profile_pic_override': 'str',
        'profile_pic_override_thumbnail': 'str',
        'pronouns': 'str',
        'state': 'UserState',
        'status': 'UserStatus',
        'status_description': 'str',
        'tags': 'list[str]',
        'traveling_to_instance': 'str',
        'traveling_to_location': 'str',
        'traveling_to_world': 'str',
        'user_icon': 'str',
        'username': 'str',
        'world_id': 'str'
    }

    attribute_map = {
        'age_verification_status': 'ageVerificationStatus',
        'age_verified': 'ageVerified',
        'allow_avatar_copying': 'allowAvatarCopying',
        'badges': 'badges',
        'bio': 'bio',
        'bio_links': 'bioLinks',
        'current_avatar_image_url': 'currentAvatarImageUrl',
        'current_avatar_thumbnail_image_url': 'currentAvatarThumbnailImageUrl',
        'current_avatar_tags': 'currentAvatarTags',
        'date_joined': 'date_joined',
        'developer_type': 'developerType',
        'display_name': 'displayName',
        'friend_key': 'friendKey',
        'friend_request_status': 'friendRequestStatus',
        'id': 'id',
        'instance_id': 'instanceId',
        'is_friend': 'isFriend',
        'last_activity': 'last_activity',
        'last_login': 'last_login',
        'last_mobile': 'last_mobile',
        'last_platform': 'last_platform',
        'location': 'location',
        'note': 'note',
        'platform': 'platform',
        'profile_pic_override': 'profilePicOverride',
        'profile_pic_override_thumbnail': 'profilePicOverrideThumbnail',
        'pronouns': 'pronouns',
        'state': 'state',
        'status': 'status',
        'status_description': 'statusDescription',
        'tags': 'tags',
        'traveling_to_instance': 'travelingToInstance',
        'traveling_to_location': 'travelingToLocation',
        'traveling_to_world': 'travelingToWorld',
        'user_icon': 'userIcon',
        'username': 'username',
        'world_id': 'worldId'
    }

    def __init__(self, age_verification_status=None, age_verified=None, allow_avatar_copying=True, badges=None, bio=None, bio_links=None, current_avatar_image_url=None, current_avatar_thumbnail_image_url=None, current_avatar_tags=None, date_joined=None, developer_type=None, display_name=None, friend_key=None, friend_request_status=None, id=None, instance_id=None, is_friend=None, last_activity=None, last_login=None, last_mobile=None, last_platform=None, location=None, note=None, platform=None, profile_pic_override=None, profile_pic_override_thumbnail=None, pronouns=None, state=None, status=None, status_description=None, tags=None, traveling_to_instance=None, traveling_to_location=None, traveling_to_world=None, user_icon=None, username=None, world_id=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._age_verification_status = None
        self._age_verified = None
        self._allow_avatar_copying = None
        self._badges = None
        self._bio = None
        self._bio_links = None
        self._current_avatar_image_url = None
        self._current_avatar_thumbnail_image_url = None
        self._current_avatar_tags = None
        self._date_joined = None
        self._developer_type = None
        self._display_name = None
        self._friend_key = None
        self._friend_request_status = None
        self._id = None
        self._instance_id = None
        self._is_friend = None
        self._last_activity = None
        self._last_login = None
        self._last_mobile = None
        self._last_platform = None
        self._location = None
        self._note = None
        self._platform = None
        self._profile_pic_override = None
        self._profile_pic_override_thumbnail = None
        self._pronouns = None
        self._state = None
        self._status = None
        self._status_description = None
        self._tags = None
        self._traveling_to_instance = None
        self._traveling_to_location = None
        self._traveling_to_world = None
        self._user_icon = None
        self._username = None
        self._world_id = None
        self.discriminator = None

        self.age_verification_status = age_verification_status
        self.age_verified = age_verified
        self.allow_avatar_copying = allow_avatar_copying
        if badges is not None:
            self.badges = badges
        self.bio = bio
        self.bio_links = bio_links
        self.current_avatar_image_url = current_avatar_image_url
        self.current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url
        self.current_avatar_tags = current_avatar_tags
        self.date_joined = date_joined
        self.developer_type = developer_type
        self.display_name = display_name
        self.friend_key = friend_key
        if friend_request_status is not None:
            self.friend_request_status = friend_request_status
        self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        self.is_friend = is_friend
        self.last_activity = last_activity
        self.last_login = last_login
        self.last_mobile = last_mobile
        self.last_platform = last_platform
        if location is not None:
            self.location = location
        if note is not None:
            self.note = note
        if platform is not None:
            self.platform = platform
        self.profile_pic_override = profile_pic_override
        self.profile_pic_override_thumbnail = profile_pic_override_thumbnail
        self.pronouns = pronouns
        self.state = state
        self.status = status
        self.status_description = status_description
        self.tags = tags
        if traveling_to_instance is not None:
            self.traveling_to_instance = traveling_to_instance
        if traveling_to_location is not None:
            self.traveling_to_location = traveling_to_location
        if traveling_to_world is not None:
            self.traveling_to_world = traveling_to_world
        self.user_icon = user_icon
        if username is not None:
            self.username = username
        if world_id is not None:
            self.world_id = world_id

    @property
    def age_verification_status(self):
        """Gets the age_verification_status of this User.  # noqa: E501


        :return: The age_verification_status of this User.  # noqa: E501
        :rtype: AgeVerificationStatus
        """
        return self._age_verification_status

    @age_verification_status.setter
    def age_verification_status(self, age_verification_status):
        """Sets the age_verification_status of this User.


        :param age_verification_status: The age_verification_status of this User.  # noqa: E501
        :type age_verification_status: AgeVerificationStatus
        """
        if self.local_vars_configuration.client_side_validation and age_verification_status is None:  # noqa: E501
            raise ValueError("Invalid value for `age_verification_status`, must not be `None`")  # noqa: E501

        self._age_verification_status = age_verification_status

    @property
    def age_verified(self):
        """Gets the age_verified of this User.  # noqa: E501

        `true` if, user is age verified (not 18+).  # noqa: E501

        :return: The age_verified of this User.  # noqa: E501
        :rtype: bool
        """
        return self._age_verified

    @age_verified.setter
    def age_verified(self, age_verified):
        """Sets the age_verified of this User.

        `true` if, user is age verified (not 18+).  # noqa: E501

        :param age_verified: The age_verified of this User.  # noqa: E501
        :type age_verified: bool
        """
        if self.local_vars_configuration.client_side_validation and age_verified is None:  # noqa: E501
            raise ValueError("Invalid value for `age_verified`, must not be `None`")  # noqa: E501

        self._age_verified = age_verified

    @property
    def allow_avatar_copying(self):
        """Gets the allow_avatar_copying of this User.  # noqa: E501


        :return: The allow_avatar_copying of this User.  # noqa: E501
        :rtype: bool
        """
        return self._allow_avatar_copying

    @allow_avatar_copying.setter
    def allow_avatar_copying(self, allow_avatar_copying):
        """Sets the allow_avatar_copying of this User.


        :param allow_avatar_copying: The allow_avatar_copying of this User.  # noqa: E501
        :type allow_avatar_copying: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_avatar_copying is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_avatar_copying`, must not be `None`")  # noqa: E501

        self._allow_avatar_copying = allow_avatar_copying

    @property
    def badges(self):
        """Gets the badges of this User.  # noqa: E501

           # noqa: E501

        :return: The badges of this User.  # noqa: E501
        :rtype: list[Badge]
        """
        return self._badges

    @badges.setter
    def badges(self, badges):
        """Sets the badges of this User.

           # noqa: E501

        :param badges: The badges of this User.  # noqa: E501
        :type badges: list[Badge]
        """

        self._badges = badges

    @property
    def bio(self):
        """Gets the bio of this User.  # noqa: E501


        :return: The bio of this User.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this User.


        :param bio: The bio of this User.  # noqa: E501
        :type bio: str
        """
        if self.local_vars_configuration.client_side_validation and bio is None:  # noqa: E501
            raise ValueError("Invalid value for `bio`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bio is not None and len(bio) > 512):
            raise ValueError("Invalid value for `bio`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bio is not None and len(bio) < 0):
            raise ValueError("Invalid value for `bio`, length must be greater than or equal to `0`")  # noqa: E501

        self._bio = bio

    @property
    def bio_links(self):
        """Gets the bio_links of this User.  # noqa: E501


        :return: The bio_links of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._bio_links

    @bio_links.setter
    def bio_links(self, bio_links):
        """Sets the bio_links of this User.


        :param bio_links: The bio_links of this User.  # noqa: E501
        :type bio_links: list[str]
        """
        if self.local_vars_configuration.client_side_validation and bio_links is None:  # noqa: E501
            raise ValueError("Invalid value for `bio_links`, must not be `None`")  # noqa: E501

        self._bio_links = bio_links

    @property
    def current_avatar_image_url(self):
        """Gets the current_avatar_image_url of this User.  # noqa: E501

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :return: The current_avatar_image_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_image_url

    @current_avatar_image_url.setter
    def current_avatar_image_url(self, current_avatar_image_url):
        """Sets the current_avatar_image_url of this User.

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :param current_avatar_image_url: The current_avatar_image_url of this User.  # noqa: E501
        :type current_avatar_image_url: str
        """
        if self.local_vars_configuration.client_side_validation and current_avatar_image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `current_avatar_image_url`, must not be `None`")  # noqa: E501

        self._current_avatar_image_url = current_avatar_image_url

    @property
    def current_avatar_thumbnail_image_url(self):
        """Gets the current_avatar_thumbnail_image_url of this User.  # noqa: E501

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :return: The current_avatar_thumbnail_image_url of this User.  # noqa: E501
        :rtype: str
        """
        return self._current_avatar_thumbnail_image_url

    @current_avatar_thumbnail_image_url.setter
    def current_avatar_thumbnail_image_url(self, current_avatar_thumbnail_image_url):
        """Sets the current_avatar_thumbnail_image_url of this User.

        When profilePicOverride is not empty, use it instead.  # noqa: E501

        :param current_avatar_thumbnail_image_url: The current_avatar_thumbnail_image_url of this User.  # noqa: E501
        :type current_avatar_thumbnail_image_url: str
        """
        if self.local_vars_configuration.client_side_validation and current_avatar_thumbnail_image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `current_avatar_thumbnail_image_url`, must not be `None`")  # noqa: E501

        self._current_avatar_thumbnail_image_url = current_avatar_thumbnail_image_url

    @property
    def current_avatar_tags(self):
        """Gets the current_avatar_tags of this User.  # noqa: E501


        :return: The current_avatar_tags of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._current_avatar_tags

    @current_avatar_tags.setter
    def current_avatar_tags(self, current_avatar_tags):
        """Sets the current_avatar_tags of this User.


        :param current_avatar_tags: The current_avatar_tags of this User.  # noqa: E501
        :type current_avatar_tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and current_avatar_tags is None:  # noqa: E501
            raise ValueError("Invalid value for `current_avatar_tags`, must not be `None`")  # noqa: E501

        self._current_avatar_tags = current_avatar_tags

    @property
    def date_joined(self):
        """Gets the date_joined of this User.  # noqa: E501


        :return: The date_joined of this User.  # noqa: E501
        :rtype: date
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this User.


        :param date_joined: The date_joined of this User.  # noqa: E501
        :type date_joined: date
        """
        if self.local_vars_configuration.client_side_validation and date_joined is None:  # noqa: E501
            raise ValueError("Invalid value for `date_joined`, must not be `None`")  # noqa: E501

        self._date_joined = date_joined

    @property
    def developer_type(self):
        """Gets the developer_type of this User.  # noqa: E501


        :return: The developer_type of this User.  # noqa: E501
        :rtype: DeveloperType
        """
        return self._developer_type

    @developer_type.setter
    def developer_type(self, developer_type):
        """Sets the developer_type of this User.


        :param developer_type: The developer_type of this User.  # noqa: E501
        :type developer_type: DeveloperType
        """
        if self.local_vars_configuration.client_side_validation and developer_type is None:  # noqa: E501
            raise ValueError("Invalid value for `developer_type`, must not be `None`")  # noqa: E501

        self._developer_type = developer_type

    @property
    def display_name(self):
        """Gets the display_name of this User.  # noqa: E501

        A users visual display name. This is what shows up in-game, and can different from their `username`. Changing display name is restricted to a cooldown period.  # noqa: E501

        :return: The display_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this User.

        A users visual display name. This is what shows up in-game, and can different from their `username`. Changing display name is restricted to a cooldown period.  # noqa: E501

        :param display_name: The display_name of this User.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def friend_key(self):
        """Gets the friend_key of this User.  # noqa: E501


        :return: The friend_key of this User.  # noqa: E501
        :rtype: str
        """
        return self._friend_key

    @friend_key.setter
    def friend_key(self, friend_key):
        """Sets the friend_key of this User.


        :param friend_key: The friend_key of this User.  # noqa: E501
        :type friend_key: str
        """
        if self.local_vars_configuration.client_side_validation and friend_key is None:  # noqa: E501
            raise ValueError("Invalid value for `friend_key`, must not be `None`")  # noqa: E501

        self._friend_key = friend_key

    @property
    def friend_request_status(self):
        """Gets the friend_request_status of this User.  # noqa: E501


        :return: The friend_request_status of this User.  # noqa: E501
        :rtype: str
        """
        return self._friend_request_status

    @friend_request_status.setter
    def friend_request_status(self, friend_request_status):
        """Sets the friend_request_status of this User.


        :param friend_request_status: The friend_request_status of this User.  # noqa: E501
        :type friend_request_status: str
        """

        self._friend_request_status = friend_request_status

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this User.  # noqa: E501

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :return: The instance_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this User.

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :param instance_id: The instance_id of this User.  # noqa: E501
        :type instance_id: str
        """

        self._instance_id = instance_id

    @property
    def is_friend(self):
        """Gets the is_friend of this User.  # noqa: E501

        Either their `friendKey`, or empty string if you are not friends. Unknown usage.  # noqa: E501

        :return: The is_friend of this User.  # noqa: E501
        :rtype: bool
        """
        return self._is_friend

    @is_friend.setter
    def is_friend(self, is_friend):
        """Sets the is_friend of this User.

        Either their `friendKey`, or empty string if you are not friends. Unknown usage.  # noqa: E501

        :param is_friend: The is_friend of this User.  # noqa: E501
        :type is_friend: bool
        """
        if self.local_vars_configuration.client_side_validation and is_friend is None:  # noqa: E501
            raise ValueError("Invalid value for `is_friend`, must not be `None`")  # noqa: E501

        self._is_friend = is_friend

    @property
    def last_activity(self):
        """Gets the last_activity of this User.  # noqa: E501

        Either a date-time or empty string.  # noqa: E501

        :return: The last_activity of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this User.

        Either a date-time or empty string.  # noqa: E501

        :param last_activity: The last_activity of this User.  # noqa: E501
        :type last_activity: str
        """
        if self.local_vars_configuration.client_side_validation and last_activity is None:  # noqa: E501
            raise ValueError("Invalid value for `last_activity`, must not be `None`")  # noqa: E501

        self._last_activity = last_activity

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501

        Either a date-time or empty string.  # noqa: E501

        :return: The last_login of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.

        Either a date-time or empty string.  # noqa: E501

        :param last_login: The last_login of this User.  # noqa: E501
        :type last_login: str
        """
        if self.local_vars_configuration.client_side_validation and last_login is None:  # noqa: E501
            raise ValueError("Invalid value for `last_login`, must not be `None`")  # noqa: E501

        self._last_login = last_login

    @property
    def last_mobile(self):
        """Gets the last_mobile of this User.  # noqa: E501


        :return: The last_mobile of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_mobile

    @last_mobile.setter
    def last_mobile(self, last_mobile):
        """Sets the last_mobile of this User.


        :param last_mobile: The last_mobile of this User.  # noqa: E501
        :type last_mobile: str
        """

        self._last_mobile = last_mobile

    @property
    def last_platform(self):
        """Gets the last_platform of this User.  # noqa: E501

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :return: The last_platform of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_platform

    @last_platform.setter
    def last_platform(self, last_platform):
        """Sets the last_platform of this User.

        This can be `standalonewindows` or `android`, but can also pretty much be any random Unity verison such as `2019.2.4-801-Release` or `2019.2.2-772-Release` or even `unknownplatform`.  # noqa: E501

        :param last_platform: The last_platform of this User.  # noqa: E501
        :type last_platform: str
        """
        if self.local_vars_configuration.client_side_validation and last_platform is None:  # noqa: E501
            raise ValueError("Invalid value for `last_platform`, must not be `None`")  # noqa: E501

        self._last_platform = last_platform

    @property
    def location(self):
        """Gets the location of this User.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The location of this User.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this User.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param location: The location of this User.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def note(self):
        """Gets the note of this User.  # noqa: E501


        :return: The note of this User.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this User.


        :param note: The note of this User.  # noqa: E501
        :type note: str
        """

        self._note = note

    @property
    def platform(self):
        """Gets the platform of this User.  # noqa: E501


        :return: The platform of this User.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this User.


        :param platform: The platform of this User.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def profile_pic_override(self):
        """Gets the profile_pic_override of this User.  # noqa: E501


        :return: The profile_pic_override of this User.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override

    @profile_pic_override.setter
    def profile_pic_override(self, profile_pic_override):
        """Sets the profile_pic_override of this User.


        :param profile_pic_override: The profile_pic_override of this User.  # noqa: E501
        :type profile_pic_override: str
        """
        if self.local_vars_configuration.client_side_validation and profile_pic_override is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_pic_override`, must not be `None`")  # noqa: E501

        self._profile_pic_override = profile_pic_override

    @property
    def profile_pic_override_thumbnail(self):
        """Gets the profile_pic_override_thumbnail of this User.  # noqa: E501


        :return: The profile_pic_override_thumbnail of this User.  # noqa: E501
        :rtype: str
        """
        return self._profile_pic_override_thumbnail

    @profile_pic_override_thumbnail.setter
    def profile_pic_override_thumbnail(self, profile_pic_override_thumbnail):
        """Sets the profile_pic_override_thumbnail of this User.


        :param profile_pic_override_thumbnail: The profile_pic_override_thumbnail of this User.  # noqa: E501
        :type profile_pic_override_thumbnail: str
        """
        if self.local_vars_configuration.client_side_validation and profile_pic_override_thumbnail is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_pic_override_thumbnail`, must not be `None`")  # noqa: E501

        self._profile_pic_override_thumbnail = profile_pic_override_thumbnail

    @property
    def pronouns(self):
        """Gets the pronouns of this User.  # noqa: E501


        :return: The pronouns of this User.  # noqa: E501
        :rtype: str
        """
        return self._pronouns

    @pronouns.setter
    def pronouns(self, pronouns):
        """Sets the pronouns of this User.


        :param pronouns: The pronouns of this User.  # noqa: E501
        :type pronouns: str
        """
        if self.local_vars_configuration.client_side_validation and pronouns is None:  # noqa: E501
            raise ValueError("Invalid value for `pronouns`, must not be `None`")  # noqa: E501

        self._pronouns = pronouns

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501


        :return: The state of this User.  # noqa: E501
        :rtype: UserState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.


        :param state: The state of this User.  # noqa: E501
        :type state: UserState
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def status(self):
        """Gets the status of this User.  # noqa: E501


        :return: The status of this User.  # noqa: E501
        :rtype: UserStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this User.


        :param status: The status of this User.  # noqa: E501
        :type status: UserStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this User.  # noqa: E501


        :return: The status_description of this User.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this User.


        :param status_description: The status_description of this User.  # noqa: E501
        :type status_description: str
        """
        if self.local_vars_configuration.client_side_validation and status_description is None:  # noqa: E501
            raise ValueError("Invalid value for `status_description`, must not be `None`")  # noqa: E501

        self._status_description = status_description

    @property
    def tags(self):
        """Gets the tags of this User.  # noqa: E501

           # noqa: E501

        :return: The tags of this User.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this User.

           # noqa: E501

        :param tags: The tags of this User.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def traveling_to_instance(self):
        """Gets the traveling_to_instance of this User.  # noqa: E501


        :return: The traveling_to_instance of this User.  # noqa: E501
        :rtype: str
        """
        return self._traveling_to_instance

    @traveling_to_instance.setter
    def traveling_to_instance(self, traveling_to_instance):
        """Sets the traveling_to_instance of this User.


        :param traveling_to_instance: The traveling_to_instance of this User.  # noqa: E501
        :type traveling_to_instance: str
        """

        self._traveling_to_instance = traveling_to_instance

    @property
    def traveling_to_location(self):
        """Gets the traveling_to_location of this User.  # noqa: E501


        :return: The traveling_to_location of this User.  # noqa: E501
        :rtype: str
        """
        return self._traveling_to_location

    @traveling_to_location.setter
    def traveling_to_location(self, traveling_to_location):
        """Sets the traveling_to_location of this User.


        :param traveling_to_location: The traveling_to_location of this User.  # noqa: E501
        :type traveling_to_location: str
        """

        self._traveling_to_location = traveling_to_location

    @property
    def traveling_to_world(self):
        """Gets the traveling_to_world of this User.  # noqa: E501


        :return: The traveling_to_world of this User.  # noqa: E501
        :rtype: str
        """
        return self._traveling_to_world

    @traveling_to_world.setter
    def traveling_to_world(self, traveling_to_world):
        """Sets the traveling_to_world of this User.


        :param traveling_to_world: The traveling_to_world of this User.  # noqa: E501
        :type traveling_to_world: str
        """

        self._traveling_to_world = traveling_to_world

    @property
    def user_icon(self):
        """Gets the user_icon of this User.  # noqa: E501


        :return: The user_icon of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_icon

    @user_icon.setter
    def user_icon(self, user_icon):
        """Sets the user_icon of this User.


        :param user_icon: The user_icon of this User.  # noqa: E501
        :type user_icon: str
        """
        if self.local_vars_configuration.client_side_validation and user_icon is None:  # noqa: E501
            raise ValueError("Invalid value for `user_icon`, must not be `None`")  # noqa: E501

        self._user_icon = user_icon

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501

        -| A users unique name, used during login. This is different from `displayName` which is what shows up in-game. A users `username` can never be changed.' **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.

        -| A users unique name, used during login. This is different from `displayName` which is what shows up in-game. A users `username` can never be changed.' **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429).  # noqa: E501

        :param username: The username of this User.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def world_id(self):
        """Gets the world_id of this User.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The world_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._world_id

    @world_id.setter
    def world_id(self, world_id):
        """Sets the world_id of this User.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param world_id: The world_id of this User.  # noqa: E501
        :type world_id: str
        """

        self._world_id = world_id

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
