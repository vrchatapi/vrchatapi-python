# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.17.1
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


class UpdateGroupRequest(object):
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
        'name': 'str',
        'short_code': 'str',
        'description': 'str',
        'join_state': 'GroupJoinState',
        'icon_id': 'str',
        'banner_id': 'str',
        'languages': 'list[str]',
        'links': 'list[str]',
        'rules': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'short_code': 'shortCode',
        'description': 'description',
        'join_state': 'joinState',
        'icon_id': 'iconId',
        'banner_id': 'bannerId',
        'languages': 'languages',
        'links': 'links',
        'rules': 'rules',
        'tags': 'tags'
    }

    def __init__(self, name=None, short_code=None, description=None, join_state=None, icon_id=None, banner_id=None, languages=None, links=None, rules=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """UpdateGroupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._short_code = None
        self._description = None
        self._join_state = None
        self._icon_id = None
        self._banner_id = None
        self._languages = None
        self._links = None
        self._rules = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if short_code is not None:
            self.short_code = short_code
        if description is not None:
            self.description = description
        if join_state is not None:
            self.join_state = join_state
        self.icon_id = icon_id
        self.banner_id = banner_id
        if languages is not None:
            self.languages = languages
        if links is not None:
            self.links = links
        if rules is not None:
            self.rules = rules
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this UpdateGroupRequest.  # noqa: E501


        :return: The name of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateGroupRequest.


        :param name: The name of this UpdateGroupRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 3):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def short_code(self):
        """Gets the short_code of this UpdateGroupRequest.  # noqa: E501


        :return: The short_code of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this UpdateGroupRequest.


        :param short_code: The short_code of this UpdateGroupRequest.  # noqa: E501
        :type short_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                short_code is not None and len(short_code) > 6):
            raise ValueError("Invalid value for `short_code`, length must be less than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                short_code is not None and len(short_code) < 3):
            raise ValueError("Invalid value for `short_code`, length must be greater than or equal to `3`")  # noqa: E501

        self._short_code = short_code

    @property
    def description(self):
        """Gets the description of this UpdateGroupRequest.  # noqa: E501


        :return: The description of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateGroupRequest.


        :param description: The description of this UpdateGroupRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 250):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `250`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def join_state(self):
        """Gets the join_state of this UpdateGroupRequest.  # noqa: E501


        :return: The join_state of this UpdateGroupRequest.  # noqa: E501
        :rtype: GroupJoinState
        """
        return self._join_state

    @join_state.setter
    def join_state(self, join_state):
        """Sets the join_state of this UpdateGroupRequest.


        :param join_state: The join_state of this UpdateGroupRequest.  # noqa: E501
        :type join_state: GroupJoinState
        """

        self._join_state = join_state

    @property
    def icon_id(self):
        """Gets the icon_id of this UpdateGroupRequest.  # noqa: E501


        :return: The icon_id of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._icon_id

    @icon_id.setter
    def icon_id(self, icon_id):
        """Sets the icon_id of this UpdateGroupRequest.


        :param icon_id: The icon_id of this UpdateGroupRequest.  # noqa: E501
        :type icon_id: str
        """

        self._icon_id = icon_id

    @property
    def banner_id(self):
        """Gets the banner_id of this UpdateGroupRequest.  # noqa: E501


        :return: The banner_id of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._banner_id

    @banner_id.setter
    def banner_id(self, banner_id):
        """Sets the banner_id of this UpdateGroupRequest.


        :param banner_id: The banner_id of this UpdateGroupRequest.  # noqa: E501
        :type banner_id: str
        """

        self._banner_id = banner_id

    @property
    def languages(self):
        """Gets the languages of this UpdateGroupRequest.  # noqa: E501

        3 letter language code  # noqa: E501

        :return: The languages of this UpdateGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this UpdateGroupRequest.

        3 letter language code  # noqa: E501

        :param languages: The languages of this UpdateGroupRequest.  # noqa: E501
        :type languages: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                languages is not None and len(languages) > 3):
            raise ValueError("Invalid value for `languages`, number of items must be less than or equal to `3`")  # noqa: E501

        self._languages = languages

    @property
    def links(self):
        """Gets the links of this UpdateGroupRequest.  # noqa: E501


        :return: The links of this UpdateGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UpdateGroupRequest.


        :param links: The links of this UpdateGroupRequest.  # noqa: E501
        :type links: list[str]
        """
        if (self.local_vars_configuration.client_side_validation and
                links is not None and len(links) > 3):
            raise ValueError("Invalid value for `links`, number of items must be less than or equal to `3`")  # noqa: E501

        self._links = links

    @property
    def rules(self):
        """Gets the rules of this UpdateGroupRequest.  # noqa: E501


        :return: The rules of this UpdateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this UpdateGroupRequest.


        :param rules: The rules of this UpdateGroupRequest.  # noqa: E501
        :type rules: str
        """

        self._rules = rules

    @property
    def tags(self):
        """Gets the tags of this UpdateGroupRequest.  # noqa: E501

           # noqa: E501

        :return: The tags of this UpdateGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateGroupRequest.

           # noqa: E501

        :param tags: The tags of this UpdateGroupRequest.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, UpdateGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
