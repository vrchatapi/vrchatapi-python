# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.18.1
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


class Badge(object):
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
        'assigned_at': 'datetime',
        'badge_description': 'str',
        'badge_id': 'str',
        'badge_image_url': 'str',
        'badge_name': 'str',
        'hidden': 'bool',
        'showcased': 'bool',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'assigned_at': 'assignedAt',
        'badge_description': 'badgeDescription',
        'badge_id': 'badgeId',
        'badge_image_url': 'badgeImageUrl',
        'badge_name': 'badgeName',
        'hidden': 'hidden',
        'showcased': 'showcased',
        'updated_at': 'updatedAt'
    }

    def __init__(self, assigned_at=None, badge_description=None, badge_id=None, badge_image_url=None, badge_name=None, hidden=None, showcased=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """Badge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._assigned_at = None
        self._badge_description = None
        self._badge_id = None
        self._badge_image_url = None
        self._badge_name = None
        self._hidden = None
        self._showcased = None
        self._updated_at = None
        self.discriminator = None

        self.assigned_at = assigned_at
        self.badge_description = badge_description
        self.badge_id = badge_id
        self.badge_image_url = badge_image_url
        self.badge_name = badge_name
        self.hidden = hidden
        self.showcased = showcased
        self.updated_at = updated_at

    @property
    def assigned_at(self):
        """Gets the assigned_at of this Badge.  # noqa: E501

        only present in CurrentUser badges  # noqa: E501

        :return: The assigned_at of this Badge.  # noqa: E501
        :rtype: datetime
        """
        return self._assigned_at

    @assigned_at.setter
    def assigned_at(self, assigned_at):
        """Sets the assigned_at of this Badge.

        only present in CurrentUser badges  # noqa: E501

        :param assigned_at: The assigned_at of this Badge.  # noqa: E501
        :type assigned_at: datetime
        """

        self._assigned_at = assigned_at

    @property
    def badge_description(self):
        """Gets the badge_description of this Badge.  # noqa: E501


        :return: The badge_description of this Badge.  # noqa: E501
        :rtype: str
        """
        return self._badge_description

    @badge_description.setter
    def badge_description(self, badge_description):
        """Sets the badge_description of this Badge.


        :param badge_description: The badge_description of this Badge.  # noqa: E501
        :type badge_description: str
        """
        if self.local_vars_configuration.client_side_validation and badge_description is None:  # noqa: E501
            raise ValueError("Invalid value for `badge_description`, must not be `None`")  # noqa: E501

        self._badge_description = badge_description

    @property
    def badge_id(self):
        """Gets the badge_id of this Badge.  # noqa: E501


        :return: The badge_id of this Badge.  # noqa: E501
        :rtype: str
        """
        return self._badge_id

    @badge_id.setter
    def badge_id(self, badge_id):
        """Sets the badge_id of this Badge.


        :param badge_id: The badge_id of this Badge.  # noqa: E501
        :type badge_id: str
        """
        if self.local_vars_configuration.client_side_validation and badge_id is None:  # noqa: E501
            raise ValueError("Invalid value for `badge_id`, must not be `None`")  # noqa: E501

        self._badge_id = badge_id

    @property
    def badge_image_url(self):
        """Gets the badge_image_url of this Badge.  # noqa: E501

        direct url to image  # noqa: E501

        :return: The badge_image_url of this Badge.  # noqa: E501
        :rtype: str
        """
        return self._badge_image_url

    @badge_image_url.setter
    def badge_image_url(self, badge_image_url):
        """Sets the badge_image_url of this Badge.

        direct url to image  # noqa: E501

        :param badge_image_url: The badge_image_url of this Badge.  # noqa: E501
        :type badge_image_url: str
        """
        if self.local_vars_configuration.client_side_validation and badge_image_url is None:  # noqa: E501
            raise ValueError("Invalid value for `badge_image_url`, must not be `None`")  # noqa: E501

        self._badge_image_url = badge_image_url

    @property
    def badge_name(self):
        """Gets the badge_name of this Badge.  # noqa: E501


        :return: The badge_name of this Badge.  # noqa: E501
        :rtype: str
        """
        return self._badge_name

    @badge_name.setter
    def badge_name(self, badge_name):
        """Sets the badge_name of this Badge.


        :param badge_name: The badge_name of this Badge.  # noqa: E501
        :type badge_name: str
        """
        if self.local_vars_configuration.client_side_validation and badge_name is None:  # noqa: E501
            raise ValueError("Invalid value for `badge_name`, must not be `None`")  # noqa: E501

        self._badge_name = badge_name

    @property
    def hidden(self):
        """Gets the hidden of this Badge.  # noqa: E501

        only present in CurrentUser badges  # noqa: E501

        :return: The hidden of this Badge.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Badge.

        only present in CurrentUser badges  # noqa: E501

        :param hidden: The hidden of this Badge.  # noqa: E501
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def showcased(self):
        """Gets the showcased of this Badge.  # noqa: E501


        :return: The showcased of this Badge.  # noqa: E501
        :rtype: bool
        """
        return self._showcased

    @showcased.setter
    def showcased(self, showcased):
        """Sets the showcased of this Badge.


        :param showcased: The showcased of this Badge.  # noqa: E501
        :type showcased: bool
        """
        if self.local_vars_configuration.client_side_validation and showcased is None:  # noqa: E501
            raise ValueError("Invalid value for `showcased`, must not be `None`")  # noqa: E501

        self._showcased = showcased

    @property
    def updated_at(self):
        """Gets the updated_at of this Badge.  # noqa: E501

        only present in CurrentUser badges  # noqa: E501

        :return: The updated_at of this Badge.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Badge.

        only present in CurrentUser badges  # noqa: E501

        :param updated_at: The updated_at of this Badge.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, Badge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Badge):
            return True

        return self.to_dict() != other.to_dict()
