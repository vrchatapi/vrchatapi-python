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


class InfoPushDataArticleContent(object):
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
        'text': 'str',
        'image_url': 'str',
        'on_pressed': 'InfoPushDataClickable'
    }

    attribute_map = {
        'text': 'text',
        'image_url': 'imageUrl',
        'on_pressed': 'onPressed'
    }

    def __init__(self, text=None, image_url=None, on_pressed=None, local_vars_configuration=None):  # noqa: E501
        """InfoPushDataArticleContent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._image_url = None
        self._on_pressed = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if image_url is not None:
            self.image_url = image_url
        if on_pressed is not None:
            self.on_pressed = on_pressed

    @property
    def text(self):
        """Gets the text of this InfoPushDataArticleContent.  # noqa: E501


        :return: The text of this InfoPushDataArticleContent.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this InfoPushDataArticleContent.


        :param text: The text of this InfoPushDataArticleContent.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def image_url(self):
        """Gets the image_url of this InfoPushDataArticleContent.  # noqa: E501


        :return: The image_url of this InfoPushDataArticleContent.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this InfoPushDataArticleContent.


        :param image_url: The image_url of this InfoPushDataArticleContent.  # noqa: E501
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def on_pressed(self):
        """Gets the on_pressed of this InfoPushDataArticleContent.  # noqa: E501


        :return: The on_pressed of this InfoPushDataArticleContent.  # noqa: E501
        :rtype: InfoPushDataClickable
        """
        return self._on_pressed

    @on_pressed.setter
    def on_pressed(self, on_pressed):
        """Sets the on_pressed of this InfoPushDataArticleContent.


        :param on_pressed: The on_pressed of this InfoPushDataArticleContent.  # noqa: E501
        :type on_pressed: InfoPushDataClickable
        """

        self._on_pressed = on_pressed

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
        if not isinstance(other, InfoPushDataArticleContent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfoPushDataArticleContent):
            return True

        return self.to_dict() != other.to_dict()
