# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.10.0
    Contact: me@ariesclark.com
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


class InfoPushData(object):
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
        'content_list': 'DynamicContentRow',
        'description': 'str',
        'image_url': 'str',
        'name': 'str',
        'on_pressed': 'InfoPushDataClickable',
        'template': 'str',
        'version': 'str',
        'article': 'InfoPushDataArticle'
    }

    attribute_map = {
        'content_list': 'contentList',
        'description': 'description',
        'image_url': 'imageUrl',
        'name': 'name',
        'on_pressed': 'onPressed',
        'template': 'template',
        'version': 'version',
        'article': 'article'
    }

    def __init__(self, content_list=None, description=None, image_url=None, name=None, on_pressed=None, template=None, version=None, article=None, local_vars_configuration=None):  # noqa: E501
        """InfoPushData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._content_list = None
        self._description = None
        self._image_url = None
        self._name = None
        self._on_pressed = None
        self._template = None
        self._version = None
        self._article = None
        self.discriminator = None

        if content_list is not None:
            self.content_list = content_list
        if description is not None:
            self.description = description
        if image_url is not None:
            self.image_url = image_url
        if name is not None:
            self.name = name
        if on_pressed is not None:
            self.on_pressed = on_pressed
        if template is not None:
            self.template = template
        if version is not None:
            self.version = version
        if article is not None:
            self.article = article

    @property
    def content_list(self):
        """Gets the content_list of this InfoPushData.  # noqa: E501


        :return: The content_list of this InfoPushData.  # noqa: E501
        :rtype: DynamicContentRow
        """
        return self._content_list

    @content_list.setter
    def content_list(self, content_list):
        """Sets the content_list of this InfoPushData.


        :param content_list: The content_list of this InfoPushData.  # noqa: E501
        :type content_list: DynamicContentRow
        """

        self._content_list = content_list

    @property
    def description(self):
        """Gets the description of this InfoPushData.  # noqa: E501


        :return: The description of this InfoPushData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InfoPushData.


        :param description: The description of this InfoPushData.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def image_url(self):
        """Gets the image_url of this InfoPushData.  # noqa: E501


        :return: The image_url of this InfoPushData.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this InfoPushData.


        :param image_url: The image_url of this InfoPushData.  # noqa: E501
        :type image_url: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_url is not None and len(image_url) < 1):
            raise ValueError("Invalid value for `image_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._image_url = image_url

    @property
    def name(self):
        """Gets the name of this InfoPushData.  # noqa: E501


        :return: The name of this InfoPushData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfoPushData.


        :param name: The name of this InfoPushData.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def on_pressed(self):
        """Gets the on_pressed of this InfoPushData.  # noqa: E501


        :return: The on_pressed of this InfoPushData.  # noqa: E501
        :rtype: InfoPushDataClickable
        """
        return self._on_pressed

    @on_pressed.setter
    def on_pressed(self, on_pressed):
        """Sets the on_pressed of this InfoPushData.


        :param on_pressed: The on_pressed of this InfoPushData.  # noqa: E501
        :type on_pressed: InfoPushDataClickable
        """

        self._on_pressed = on_pressed

    @property
    def template(self):
        """Gets the template of this InfoPushData.  # noqa: E501


        :return: The template of this InfoPushData.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this InfoPushData.


        :param template: The template of this InfoPushData.  # noqa: E501
        :type template: str
        """

        self._template = template

    @property
    def version(self):
        """Gets the version of this InfoPushData.  # noqa: E501


        :return: The version of this InfoPushData.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InfoPushData.


        :param version: The version of this InfoPushData.  # noqa: E501
        :type version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def article(self):
        """Gets the article of this InfoPushData.  # noqa: E501


        :return: The article of this InfoPushData.  # noqa: E501
        :rtype: InfoPushDataArticle
        """
        return self._article

    @article.setter
    def article(self, article):
        """Sets the article of this InfoPushData.


        :param article: The article of this InfoPushData.  # noqa: E501
        :type article: InfoPushDataArticle
        """

        self._article = article

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
        if not isinstance(other, InfoPushData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InfoPushData):
            return True

        return self.to_dict() != other.to_dict()