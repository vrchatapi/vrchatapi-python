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


class File(object):
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
        'extension': 'str',
        'id': 'str',
        'mime_type': 'MIMEType',
        'name': 'str',
        'owner_id': 'str',
        'tags': 'list[str]',
        'versions': 'list[FileVersion]'
    }

    attribute_map = {
        'extension': 'extension',
        'id': 'id',
        'mime_type': 'mimeType',
        'name': 'name',
        'owner_id': 'ownerId',
        'tags': 'tags',
        'versions': 'versions'
    }

    def __init__(self, extension=None, id=None, mime_type=None, name=None, owner_id=None, tags=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extension = None
        self._id = None
        self._mime_type = None
        self._name = None
        self._owner_id = None
        self._tags = None
        self._versions = None
        self.discriminator = None

        self.extension = extension
        self.id = id
        self.mime_type = mime_type
        self.name = name
        self.owner_id = owner_id
        self.tags = tags
        self.versions = versions

    @property
    def extension(self):
        """Gets the extension of this File.  # noqa: E501


        :return: The extension of this File.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this File.


        :param extension: The extension of this File.  # noqa: E501
        :type extension: str
        """
        if self.local_vars_configuration.client_side_validation and extension is None:  # noqa: E501
            raise ValueError("Invalid value for `extension`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                extension is not None and len(extension) < 1):
            raise ValueError("Invalid value for `extension`, length must be greater than or equal to `1`")  # noqa: E501

        self._extension = extension

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501


        :return: The id of this File.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.


        :param id: The id of this File.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def mime_type(self):
        """Gets the mime_type of this File.  # noqa: E501


        :return: The mime_type of this File.  # noqa: E501
        :rtype: MIMEType
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this File.


        :param mime_type: The mime_type of this File.  # noqa: E501
        :type mime_type: MIMEType
        """
        if self.local_vars_configuration.client_side_validation and mime_type is None:  # noqa: E501
            raise ValueError("Invalid value for `mime_type`, must not be `None`")  # noqa: E501

        self._mime_type = mime_type

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501

          # noqa: E501

        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.

          # noqa: E501

        :param name: The name of this File.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this File.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this File.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this File.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this File.  # noqa: E501
        :type owner_id: str
        """
        if self.local_vars_configuration.client_side_validation and owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def tags(self):
        """Gets the tags of this File.  # noqa: E501

           # noqa: E501

        :return: The tags of this File.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this File.

           # noqa: E501

        :param tags: The tags of this File.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def versions(self):
        """Gets the versions of this File.  # noqa: E501

           # noqa: E501

        :return: The versions of this File.  # noqa: E501
        :rtype: list[FileVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this File.

           # noqa: E501

        :param versions: The versions of this File.  # noqa: E501
        :type versions: list[FileVersion]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                versions is not None and len(versions) < 1):
            raise ValueError("Invalid value for `versions`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()