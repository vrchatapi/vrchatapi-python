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


class GroupGalleryImage(object):
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
        'id': 'str',
        'group_id': 'str',
        'gallery_id': 'str',
        'file_id': 'str',
        'image_url': 'str',
        'created_at': 'datetime',
        'submitted_by_user_id': 'str',
        'approved': 'bool',
        'approved_by_user_id': 'str',
        'approved_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'gallery_id': 'galleryId',
        'file_id': 'fileId',
        'image_url': 'imageUrl',
        'created_at': 'createdAt',
        'submitted_by_user_id': 'submittedByUserId',
        'approved': 'approved',
        'approved_by_user_id': 'approvedByUserId',
        'approved_at': 'approvedAt'
    }

    def __init__(self, id=None, group_id=None, gallery_id=None, file_id=None, image_url=None, created_at=None, submitted_by_user_id=None, approved=False, approved_by_user_id=None, approved_at=None, local_vars_configuration=None):  # noqa: E501
        """GroupGalleryImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._gallery_id = None
        self._file_id = None
        self._image_url = None
        self._created_at = None
        self._submitted_by_user_id = None
        self._approved = None
        self._approved_by_user_id = None
        self._approved_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if gallery_id is not None:
            self.gallery_id = gallery_id
        if file_id is not None:
            self.file_id = file_id
        if image_url is not None:
            self.image_url = image_url
        if created_at is not None:
            self.created_at = created_at
        if submitted_by_user_id is not None:
            self.submitted_by_user_id = submitted_by_user_id
        if approved is not None:
            self.approved = approved
        if approved_by_user_id is not None:
            self.approved_by_user_id = approved_by_user_id
        if approved_at is not None:
            self.approved_at = approved_at

    @property
    def id(self):
        """Gets the id of this GroupGalleryImage.  # noqa: E501


        :return: The id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupGalleryImage.


        :param id: The id of this GroupGalleryImage.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupGalleryImage.  # noqa: E501


        :return: The group_id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupGalleryImage.


        :param group_id: The group_id of this GroupGalleryImage.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def gallery_id(self):
        """Gets the gallery_id of this GroupGalleryImage.  # noqa: E501


        :return: The gallery_id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._gallery_id

    @gallery_id.setter
    def gallery_id(self, gallery_id):
        """Sets the gallery_id of this GroupGalleryImage.


        :param gallery_id: The gallery_id of this GroupGalleryImage.  # noqa: E501
        :type gallery_id: str
        """

        self._gallery_id = gallery_id

    @property
    def file_id(self):
        """Gets the file_id of this GroupGalleryImage.  # noqa: E501


        :return: The file_id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this GroupGalleryImage.


        :param file_id: The file_id of this GroupGalleryImage.  # noqa: E501
        :type file_id: str
        """

        self._file_id = file_id

    @property
    def image_url(self):
        """Gets the image_url of this GroupGalleryImage.  # noqa: E501


        :return: The image_url of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this GroupGalleryImage.


        :param image_url: The image_url of this GroupGalleryImage.  # noqa: E501
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def created_at(self):
        """Gets the created_at of this GroupGalleryImage.  # noqa: E501


        :return: The created_at of this GroupGalleryImage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupGalleryImage.


        :param created_at: The created_at of this GroupGalleryImage.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def submitted_by_user_id(self):
        """Gets the submitted_by_user_id of this GroupGalleryImage.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The submitted_by_user_id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by_user_id

    @submitted_by_user_id.setter
    def submitted_by_user_id(self, submitted_by_user_id):
        """Sets the submitted_by_user_id of this GroupGalleryImage.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param submitted_by_user_id: The submitted_by_user_id of this GroupGalleryImage.  # noqa: E501
        :type submitted_by_user_id: str
        """

        self._submitted_by_user_id = submitted_by_user_id

    @property
    def approved(self):
        """Gets the approved of this GroupGalleryImage.  # noqa: E501


        :return: The approved of this GroupGalleryImage.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this GroupGalleryImage.


        :param approved: The approved of this GroupGalleryImage.  # noqa: E501
        :type approved: bool
        """

        self._approved = approved

    @property
    def approved_by_user_id(self):
        """Gets the approved_by_user_id of this GroupGalleryImage.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The approved_by_user_id of this GroupGalleryImage.  # noqa: E501
        :rtype: str
        """
        return self._approved_by_user_id

    @approved_by_user_id.setter
    def approved_by_user_id(self, approved_by_user_id):
        """Sets the approved_by_user_id of this GroupGalleryImage.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param approved_by_user_id: The approved_by_user_id of this GroupGalleryImage.  # noqa: E501
        :type approved_by_user_id: str
        """

        self._approved_by_user_id = approved_by_user_id

    @property
    def approved_at(self):
        """Gets the approved_at of this GroupGalleryImage.  # noqa: E501


        :return: The approved_at of this GroupGalleryImage.  # noqa: E501
        :rtype: datetime
        """
        return self._approved_at

    @approved_at.setter
    def approved_at(self, approved_at):
        """Sets the approved_at of this GroupGalleryImage.


        :param approved_at: The approved_at of this GroupGalleryImage.  # noqa: E501
        :type approved_at: datetime
        """

        self._approved_at = approved_at

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
        if not isinstance(other, GroupGalleryImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupGalleryImage):
            return True

        return self.to_dict() != other.to_dict()
