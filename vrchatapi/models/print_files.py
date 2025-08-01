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


class PrintFiles(object):
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
        'file_id': 'str',
        'image': 'str'
    }

    attribute_map = {
        'file_id': 'fileId',
        'image': 'image'
    }

    def __init__(self, file_id=None, image=None, local_vars_configuration=None):  # noqa: E501
        """PrintFiles - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._image = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if image is not None:
            self.image = image

    @property
    def file_id(self):
        """Gets the file_id of this PrintFiles.  # noqa: E501


        :return: The file_id of this PrintFiles.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this PrintFiles.


        :param file_id: The file_id of this PrintFiles.  # noqa: E501
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def image(self):
        """Gets the image of this PrintFiles.  # noqa: E501

        Link to file, e.g. https://api.vrchat.cloud/api/1/file/file_66fe782d-f2bd-4462-9761-1d766d7b2b26/1/file  # noqa: E501

        :return: The image of this PrintFiles.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PrintFiles.

        Link to file, e.g. https://api.vrchat.cloud/api/1/file/file_66fe782d-f2bd-4462-9761-1d766d7b2b26/1/file  # noqa: E501

        :param image: The image of this PrintFiles.  # noqa: E501
        :type image: str
        """

        self._image = image

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
        if not isinstance(other, PrintFiles):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintFiles):
            return True

        return self.to_dict() != other.to_dict()
