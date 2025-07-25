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


class APIConfigEvents(object):
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
        'distance_close': 'int',
        'distance_factor': 'int',
        'distance_far': 'int',
        'group_distance': 'int',
        'maximum_bunch_size': 'int',
        'not_visible_factor': 'int',
        'player_order_bucket_size': 'int',
        'player_order_factor': 'int',
        'slow_update_factor_threshold': 'int',
        'view_segment_length': 'int'
    }

    attribute_map = {
        'distance_close': 'distanceClose',
        'distance_factor': 'distanceFactor',
        'distance_far': 'distanceFar',
        'group_distance': 'groupDistance',
        'maximum_bunch_size': 'maximumBunchSize',
        'not_visible_factor': 'notVisibleFactor',
        'player_order_bucket_size': 'playerOrderBucketSize',
        'player_order_factor': 'playerOrderFactor',
        'slow_update_factor_threshold': 'slowUpdateFactorThreshold',
        'view_segment_length': 'viewSegmentLength'
    }

    def __init__(self, distance_close=None, distance_factor=None, distance_far=None, group_distance=None, maximum_bunch_size=None, not_visible_factor=None, player_order_bucket_size=None, player_order_factor=None, slow_update_factor_threshold=None, view_segment_length=None, local_vars_configuration=None):  # noqa: E501
        """APIConfigEvents - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._distance_close = None
        self._distance_factor = None
        self._distance_far = None
        self._group_distance = None
        self._maximum_bunch_size = None
        self._not_visible_factor = None
        self._player_order_bucket_size = None
        self._player_order_factor = None
        self._slow_update_factor_threshold = None
        self._view_segment_length = None
        self.discriminator = None

        self.distance_close = distance_close
        self.distance_factor = distance_factor
        self.distance_far = distance_far
        self.group_distance = group_distance
        self.maximum_bunch_size = maximum_bunch_size
        self.not_visible_factor = not_visible_factor
        self.player_order_bucket_size = player_order_bucket_size
        self.player_order_factor = player_order_factor
        self.slow_update_factor_threshold = slow_update_factor_threshold
        self.view_segment_length = view_segment_length

    @property
    def distance_close(self):
        """Gets the distance_close of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The distance_close of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._distance_close

    @distance_close.setter
    def distance_close(self, distance_close):
        """Sets the distance_close of this APIConfigEvents.

        Unknown  # noqa: E501

        :param distance_close: The distance_close of this APIConfigEvents.  # noqa: E501
        :type distance_close: int
        """
        if self.local_vars_configuration.client_side_validation and distance_close is None:  # noqa: E501
            raise ValueError("Invalid value for `distance_close`, must not be `None`")  # noqa: E501

        self._distance_close = distance_close

    @property
    def distance_factor(self):
        """Gets the distance_factor of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The distance_factor of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._distance_factor

    @distance_factor.setter
    def distance_factor(self, distance_factor):
        """Sets the distance_factor of this APIConfigEvents.

        Unknown  # noqa: E501

        :param distance_factor: The distance_factor of this APIConfigEvents.  # noqa: E501
        :type distance_factor: int
        """
        if self.local_vars_configuration.client_side_validation and distance_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `distance_factor`, must not be `None`")  # noqa: E501

        self._distance_factor = distance_factor

    @property
    def distance_far(self):
        """Gets the distance_far of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The distance_far of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._distance_far

    @distance_far.setter
    def distance_far(self, distance_far):
        """Sets the distance_far of this APIConfigEvents.

        Unknown  # noqa: E501

        :param distance_far: The distance_far of this APIConfigEvents.  # noqa: E501
        :type distance_far: int
        """
        if self.local_vars_configuration.client_side_validation and distance_far is None:  # noqa: E501
            raise ValueError("Invalid value for `distance_far`, must not be `None`")  # noqa: E501

        self._distance_far = distance_far

    @property
    def group_distance(self):
        """Gets the group_distance of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The group_distance of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._group_distance

    @group_distance.setter
    def group_distance(self, group_distance):
        """Sets the group_distance of this APIConfigEvents.

        Unknown  # noqa: E501

        :param group_distance: The group_distance of this APIConfigEvents.  # noqa: E501
        :type group_distance: int
        """
        if self.local_vars_configuration.client_side_validation and group_distance is None:  # noqa: E501
            raise ValueError("Invalid value for `group_distance`, must not be `None`")  # noqa: E501

        self._group_distance = group_distance

    @property
    def maximum_bunch_size(self):
        """Gets the maximum_bunch_size of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The maximum_bunch_size of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._maximum_bunch_size

    @maximum_bunch_size.setter
    def maximum_bunch_size(self, maximum_bunch_size):
        """Sets the maximum_bunch_size of this APIConfigEvents.

        Unknown  # noqa: E501

        :param maximum_bunch_size: The maximum_bunch_size of this APIConfigEvents.  # noqa: E501
        :type maximum_bunch_size: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_bunch_size is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_bunch_size`, must not be `None`")  # noqa: E501

        self._maximum_bunch_size = maximum_bunch_size

    @property
    def not_visible_factor(self):
        """Gets the not_visible_factor of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The not_visible_factor of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._not_visible_factor

    @not_visible_factor.setter
    def not_visible_factor(self, not_visible_factor):
        """Sets the not_visible_factor of this APIConfigEvents.

        Unknown  # noqa: E501

        :param not_visible_factor: The not_visible_factor of this APIConfigEvents.  # noqa: E501
        :type not_visible_factor: int
        """
        if self.local_vars_configuration.client_side_validation and not_visible_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `not_visible_factor`, must not be `None`")  # noqa: E501

        self._not_visible_factor = not_visible_factor

    @property
    def player_order_bucket_size(self):
        """Gets the player_order_bucket_size of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The player_order_bucket_size of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._player_order_bucket_size

    @player_order_bucket_size.setter
    def player_order_bucket_size(self, player_order_bucket_size):
        """Sets the player_order_bucket_size of this APIConfigEvents.

        Unknown  # noqa: E501

        :param player_order_bucket_size: The player_order_bucket_size of this APIConfigEvents.  # noqa: E501
        :type player_order_bucket_size: int
        """
        if self.local_vars_configuration.client_side_validation and player_order_bucket_size is None:  # noqa: E501
            raise ValueError("Invalid value for `player_order_bucket_size`, must not be `None`")  # noqa: E501

        self._player_order_bucket_size = player_order_bucket_size

    @property
    def player_order_factor(self):
        """Gets the player_order_factor of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The player_order_factor of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._player_order_factor

    @player_order_factor.setter
    def player_order_factor(self, player_order_factor):
        """Sets the player_order_factor of this APIConfigEvents.

        Unknown  # noqa: E501

        :param player_order_factor: The player_order_factor of this APIConfigEvents.  # noqa: E501
        :type player_order_factor: int
        """
        if self.local_vars_configuration.client_side_validation and player_order_factor is None:  # noqa: E501
            raise ValueError("Invalid value for `player_order_factor`, must not be `None`")  # noqa: E501

        self._player_order_factor = player_order_factor

    @property
    def slow_update_factor_threshold(self):
        """Gets the slow_update_factor_threshold of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The slow_update_factor_threshold of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._slow_update_factor_threshold

    @slow_update_factor_threshold.setter
    def slow_update_factor_threshold(self, slow_update_factor_threshold):
        """Sets the slow_update_factor_threshold of this APIConfigEvents.

        Unknown  # noqa: E501

        :param slow_update_factor_threshold: The slow_update_factor_threshold of this APIConfigEvents.  # noqa: E501
        :type slow_update_factor_threshold: int
        """
        if self.local_vars_configuration.client_side_validation and slow_update_factor_threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `slow_update_factor_threshold`, must not be `None`")  # noqa: E501

        self._slow_update_factor_threshold = slow_update_factor_threshold

    @property
    def view_segment_length(self):
        """Gets the view_segment_length of this APIConfigEvents.  # noqa: E501

        Unknown  # noqa: E501

        :return: The view_segment_length of this APIConfigEvents.  # noqa: E501
        :rtype: int
        """
        return self._view_segment_length

    @view_segment_length.setter
    def view_segment_length(self, view_segment_length):
        """Sets the view_segment_length of this APIConfigEvents.

        Unknown  # noqa: E501

        :param view_segment_length: The view_segment_length of this APIConfigEvents.  # noqa: E501
        :type view_segment_length: int
        """
        if self.local_vars_configuration.client_side_validation and view_segment_length is None:  # noqa: E501
            raise ValueError("Invalid value for `view_segment_length`, must not be `None`")  # noqa: E501

        self._view_segment_length = view_segment_length

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
        if not isinstance(other, APIConfigEvents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIConfigEvents):
            return True

        return self.to_dict() != other.to_dict()
