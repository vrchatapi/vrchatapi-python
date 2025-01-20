# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.9
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


class GroupInstance(object):
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
        'instance_id': 'str',
        'location': 'str',
        'world': 'World',
        'member_count': 'int'
    }

    attribute_map = {
        'instance_id': 'instanceId',
        'location': 'location',
        'world': 'world',
        'member_count': 'memberCount'
    }

    def __init__(self, instance_id=None, location=None, world=None, member_count=None, local_vars_configuration=None):  # noqa: E501
        """GroupInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._instance_id = None
        self._location = None
        self._world = None
        self._member_count = None
        self.discriminator = None

        self.instance_id = instance_id
        self.location = location
        self.world = world
        self.member_count = member_count

    @property
    def instance_id(self):
        """Gets the instance_id of this GroupInstance.  # noqa: E501


        :return: The instance_id of this GroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this GroupInstance.


        :param instance_id: The instance_id of this GroupInstance.  # noqa: E501
        :type instance_id: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) < 1):
            raise ValueError("Invalid value for `instance_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def location(self):
        """Gets the location of this GroupInstance.  # noqa: E501

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :return: The location of this GroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GroupInstance.

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :param location: The location of this GroupInstance.  # noqa: E501
        :type location: str
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def world(self):
        """Gets the world of this GroupInstance.  # noqa: E501


        :return: The world of this GroupInstance.  # noqa: E501
        :rtype: World
        """
        return self._world

    @world.setter
    def world(self, world):
        """Sets the world of this GroupInstance.


        :param world: The world of this GroupInstance.  # noqa: E501
        :type world: World
        """
        if self.local_vars_configuration.client_side_validation and world is None:  # noqa: E501
            raise ValueError("Invalid value for `world`, must not be `None`")  # noqa: E501

        self._world = world

    @property
    def member_count(self):
        """Gets the member_count of this GroupInstance.  # noqa: E501


        :return: The member_count of this GroupInstance.  # noqa: E501
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        """Sets the member_count of this GroupInstance.


        :param member_count: The member_count of this GroupInstance.  # noqa: E501
        :type member_count: int
        """
        if self.local_vars_configuration.client_side_validation and member_count is None:  # noqa: E501
            raise ValueError("Invalid value for `member_count`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                member_count is not None and member_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `member_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._member_count = member_count

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
        if not isinstance(other, GroupInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupInstance):
            return True

        return self.to_dict() != other.to_dict()
