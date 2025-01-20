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


class Product(object):
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
        'archived': 'bool',
        'created': 'datetime',
        'description': 'str',
        'display_name': 'str',
        'group_access': 'bool',
        'group_access_remove': 'bool',
        'group_id': 'str',
        'group_role_id': 'str',
        'id': 'str',
        'image_id': 'str',
        'parent_listings': 'list[str]',
        'product_type': 'ProductType',
        'seller_display_name': 'str',
        'seller_id': 'str',
        'tags': 'list[str]',
        'updated': 'datetime',
        'use_for_subscriber_list': 'bool'
    }

    attribute_map = {
        'archived': 'archived',
        'created': 'created',
        'description': 'description',
        'display_name': 'displayName',
        'group_access': 'groupAccess',
        'group_access_remove': 'groupAccessRemove',
        'group_id': 'groupId',
        'group_role_id': 'groupRoleId',
        'id': 'id',
        'image_id': 'imageId',
        'parent_listings': 'parentListings',
        'product_type': 'productType',
        'seller_display_name': 'sellerDisplayName',
        'seller_id': 'sellerId',
        'tags': 'tags',
        'updated': 'updated',
        'use_for_subscriber_list': 'useForSubscriberList'
    }

    def __init__(self, archived=None, created=None, description=None, display_name=None, group_access=False, group_access_remove=False, group_id=None, group_role_id=None, id=None, image_id=None, parent_listings=None, product_type=None, seller_display_name=None, seller_id=None, tags=None, updated=None, use_for_subscriber_list=False, local_vars_configuration=None):  # noqa: E501
        """Product - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._archived = None
        self._created = None
        self._description = None
        self._display_name = None
        self._group_access = None
        self._group_access_remove = None
        self._group_id = None
        self._group_role_id = None
        self._id = None
        self._image_id = None
        self._parent_listings = None
        self._product_type = None
        self._seller_display_name = None
        self._seller_id = None
        self._tags = None
        self._updated = None
        self._use_for_subscriber_list = None
        self.discriminator = None

        self.archived = archived
        self.created = created
        self.description = description
        self.display_name = display_name
        if group_access is not None:
            self.group_access = group_access
        if group_access_remove is not None:
            self.group_access_remove = group_access_remove
        if group_id is not None:
            self.group_id = group_id
        if group_role_id is not None:
            self.group_role_id = group_role_id
        self.id = id
        self.image_id = image_id
        self.parent_listings = parent_listings
        self.product_type = product_type
        self.seller_display_name = seller_display_name
        self.seller_id = seller_id
        self.tags = tags
        self.updated = updated
        if use_for_subscriber_list is not None:
            self.use_for_subscriber_list = use_for_subscriber_list

    @property
    def archived(self):
        """Gets the archived of this Product.  # noqa: E501


        :return: The archived of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Product.


        :param archived: The archived of this Product.  # noqa: E501
        :type archived: bool
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def created(self):
        """Gets the created of this Product.  # noqa: E501


        :return: The created of this Product.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Product.


        :param created: The created of this Product.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def description(self):
        """Gets the description of this Product.  # noqa: E501


        :return: The description of this Product.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Product.


        :param description: The description of this Product.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this Product.  # noqa: E501


        :return: The display_name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Product.


        :param display_name: The display_name of this Product.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def group_access(self):
        """Gets the group_access of this Product.  # noqa: E501


        :return: The group_access of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._group_access

    @group_access.setter
    def group_access(self, group_access):
        """Sets the group_access of this Product.


        :param group_access: The group_access of this Product.  # noqa: E501
        :type group_access: bool
        """

        self._group_access = group_access

    @property
    def group_access_remove(self):
        """Gets the group_access_remove of this Product.  # noqa: E501


        :return: The group_access_remove of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._group_access_remove

    @group_access_remove.setter
    def group_access_remove(self, group_access_remove):
        """Sets the group_access_remove of this Product.


        :param group_access_remove: The group_access_remove of this Product.  # noqa: E501
        :type group_access_remove: bool
        """

        self._group_access_remove = group_access_remove

    @property
    def group_id(self):
        """Gets the group_id of this Product.  # noqa: E501


        :return: The group_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this Product.


        :param group_id: The group_id of this Product.  # noqa: E501
        :type group_id: str
        """

        self._group_id = group_id

    @property
    def group_role_id(self):
        """Gets the group_role_id of this Product.  # noqa: E501


        :return: The group_role_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._group_role_id

    @group_role_id.setter
    def group_role_id(self, group_role_id):
        """Sets the group_role_id of this Product.


        :param group_role_id: The group_role_id of this Product.  # noqa: E501
        :type group_role_id: str
        """

        self._group_role_id = group_role_id

    @property
    def id(self):
        """Gets the id of this Product.  # noqa: E501


        :return: The id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Product.


        :param id: The id of this Product.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def image_id(self):
        """Gets the image_id of this Product.  # noqa: E501


        :return: The image_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this Product.


        :param image_id: The image_id of this Product.  # noqa: E501
        :type image_id: str
        """
        if self.local_vars_configuration.client_side_validation and image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def parent_listings(self):
        """Gets the parent_listings of this Product.  # noqa: E501


        :return: The parent_listings of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._parent_listings

    @parent_listings.setter
    def parent_listings(self, parent_listings):
        """Sets the parent_listings of this Product.


        :param parent_listings: The parent_listings of this Product.  # noqa: E501
        :type parent_listings: list[str]
        """
        if self.local_vars_configuration.client_side_validation and parent_listings is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_listings`, must not be `None`")  # noqa: E501

        self._parent_listings = parent_listings

    @property
    def product_type(self):
        """Gets the product_type of this Product.  # noqa: E501


        :return: The product_type of this Product.  # noqa: E501
        :rtype: ProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this Product.


        :param product_type: The product_type of this Product.  # noqa: E501
        :type product_type: ProductType
        """
        if self.local_vars_configuration.client_side_validation and product_type is None:  # noqa: E501
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def seller_display_name(self):
        """Gets the seller_display_name of this Product.  # noqa: E501


        :return: The seller_display_name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._seller_display_name

    @seller_display_name.setter
    def seller_display_name(self, seller_display_name):
        """Sets the seller_display_name of this Product.


        :param seller_display_name: The seller_display_name of this Product.  # noqa: E501
        :type seller_display_name: str
        """
        if self.local_vars_configuration.client_side_validation and seller_display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `seller_display_name`, must not be `None`")  # noqa: E501

        self._seller_display_name = seller_display_name

    @property
    def seller_id(self):
        """Gets the seller_id of this Product.  # noqa: E501


        :return: The seller_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this Product.


        :param seller_id: The seller_id of this Product.  # noqa: E501
        :type seller_id: str
        """
        if self.local_vars_configuration.client_side_validation and seller_id is None:  # noqa: E501
            raise ValueError("Invalid value for `seller_id`, must not be `None`")  # noqa: E501

        self._seller_id = seller_id

    @property
    def tags(self):
        """Gets the tags of this Product.  # noqa: E501


        :return: The tags of this Product.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Product.


        :param tags: The tags of this Product.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def updated(self):
        """Gets the updated of this Product.  # noqa: E501


        :return: The updated of this Product.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Product.


        :param updated: The updated of this Product.  # noqa: E501
        :type updated: datetime
        """

        self._updated = updated

    @property
    def use_for_subscriber_list(self):
        """Gets the use_for_subscriber_list of this Product.  # noqa: E501


        :return: The use_for_subscriber_list of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._use_for_subscriber_list

    @use_for_subscriber_list.setter
    def use_for_subscriber_list(self, use_for_subscriber_list):
        """Sets the use_for_subscriber_list of this Product.


        :param use_for_subscriber_list: The use_for_subscriber_list of this Product.  # noqa: E501
        :type use_for_subscriber_list: bool
        """

        self._use_for_subscriber_list = use_for_subscriber_list

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
        if not isinstance(other, Product):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Product):
            return True

        return self.to_dict() != other.to_dict()
