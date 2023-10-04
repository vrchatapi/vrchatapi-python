# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.15.0
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


class UserSubscription(object):
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
        'transaction_id': 'str',
        'store': 'str',
        'steam_item_id': 'str',
        'amount': 'float',
        'description': 'str',
        'period': 'SubscriptionPeriod',
        'tier': 'float',
        'active': 'bool',
        'status': 'TransactionStatus',
        'expires': 'datetime',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'license_groups': 'list[str]',
        'is_gift': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'transaction_id': 'transactionId',
        'store': 'store',
        'steam_item_id': 'steamItemId',
        'amount': 'amount',
        'description': 'description',
        'period': 'period',
        'tier': 'tier',
        'active': 'active',
        'status': 'status',
        'expires': 'expires',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'license_groups': 'licenseGroups',
        'is_gift': 'isGift'
    }

    def __init__(self, id=None, transaction_id=None, store=None, steam_item_id=None, amount=None, description=None, period=None, tier=None, active=True, status=None, expires=None, created_at=None, updated_at=None, license_groups=None, is_gift=False, local_vars_configuration=None):  # noqa: E501
        """UserSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._transaction_id = None
        self._store = None
        self._steam_item_id = None
        self._amount = None
        self._description = None
        self._period = None
        self._tier = None
        self._active = None
        self._status = None
        self._expires = None
        self._created_at = None
        self._updated_at = None
        self._license_groups = None
        self._is_gift = None
        self.discriminator = None

        self.id = id
        self.transaction_id = transaction_id
        self.store = store
        if steam_item_id is not None:
            self.steam_item_id = steam_item_id
        self.amount = amount
        self.description = description
        self.period = period
        self.tier = tier
        self.active = active
        self.status = status
        self.expires = expires
        self.created_at = created_at
        self.updated_at = updated_at
        self.license_groups = license_groups
        self.is_gift = is_gift

    @property
    def id(self):
        """Gets the id of this UserSubscription.  # noqa: E501


        :return: The id of this UserSubscription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSubscription.


        :param id: The id of this UserSubscription.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this UserSubscription.  # noqa: E501


        :return: The transaction_id of this UserSubscription.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this UserSubscription.


        :param transaction_id: The transaction_id of this UserSubscription.  # noqa: E501
        :type transaction_id: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_id is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_id is not None and not re.search(r'txn_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', transaction_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `transaction_id`, must be a follow pattern or equal to `/txn_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def store(self):
        """Gets the store of this UserSubscription.  # noqa: E501

        Which \"Store\" it came from. Right now only Stores are \"Steam\" and \"Admin\".  # noqa: E501

        :return: The store of this UserSubscription.  # noqa: E501
        :rtype: str
        """
        return self._store

    @store.setter
    def store(self, store):
        """Sets the store of this UserSubscription.

        Which \"Store\" it came from. Right now only Stores are \"Steam\" and \"Admin\".  # noqa: E501

        :param store: The store of this UserSubscription.  # noqa: E501
        :type store: str
        """
        if self.local_vars_configuration.client_side_validation and store is None:  # noqa: E501
            raise ValueError("Invalid value for `store`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                store is not None and len(store) < 1):
            raise ValueError("Invalid value for `store`, length must be greater than or equal to `1`")  # noqa: E501

        self._store = store

    @property
    def steam_item_id(self):
        """Gets the steam_item_id of this UserSubscription.  # noqa: E501


        :return: The steam_item_id of this UserSubscription.  # noqa: E501
        :rtype: str
        """
        return self._steam_item_id

    @steam_item_id.setter
    def steam_item_id(self, steam_item_id):
        """Sets the steam_item_id of this UserSubscription.


        :param steam_item_id: The steam_item_id of this UserSubscription.  # noqa: E501
        :type steam_item_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                steam_item_id is not None and len(steam_item_id) < 1):
            raise ValueError("Invalid value for `steam_item_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._steam_item_id = steam_item_id

    @property
    def amount(self):
        """Gets the amount of this UserSubscription.  # noqa: E501


        :return: The amount of this UserSubscription.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UserSubscription.


        :param amount: The amount of this UserSubscription.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this UserSubscription.  # noqa: E501


        :return: The description of this UserSubscription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserSubscription.


        :param description: The description of this UserSubscription.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def period(self):
        """Gets the period of this UserSubscription.  # noqa: E501


        :return: The period of this UserSubscription.  # noqa: E501
        :rtype: SubscriptionPeriod
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this UserSubscription.


        :param period: The period of this UserSubscription.  # noqa: E501
        :type period: SubscriptionPeriod
        """
        if self.local_vars_configuration.client_side_validation and period is None:  # noqa: E501
            raise ValueError("Invalid value for `period`, must not be `None`")  # noqa: E501

        self._period = period

    @property
    def tier(self):
        """Gets the tier of this UserSubscription.  # noqa: E501


        :return: The tier of this UserSubscription.  # noqa: E501
        :rtype: float
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this UserSubscription.


        :param tier: The tier of this UserSubscription.  # noqa: E501
        :type tier: float
        """
        if self.local_vars_configuration.client_side_validation and tier is None:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must not be `None`")  # noqa: E501

        self._tier = tier

    @property
    def active(self):
        """Gets the active of this UserSubscription.  # noqa: E501


        :return: The active of this UserSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this UserSubscription.


        :param active: The active of this UserSubscription.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def status(self):
        """Gets the status of this UserSubscription.  # noqa: E501


        :return: The status of this UserSubscription.  # noqa: E501
        :rtype: TransactionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserSubscription.


        :param status: The status of this UserSubscription.  # noqa: E501
        :type status: TransactionStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def expires(self):
        """Gets the expires of this UserSubscription.  # noqa: E501


        :return: The expires of this UserSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this UserSubscription.


        :param expires: The expires of this UserSubscription.  # noqa: E501
        :type expires: datetime
        """
        if self.local_vars_configuration.client_side_validation and expires is None:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must not be `None`")  # noqa: E501

        self._expires = expires

    @property
    def created_at(self):
        """Gets the created_at of this UserSubscription.  # noqa: E501


        :return: The created_at of this UserSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserSubscription.


        :param created_at: The created_at of this UserSubscription.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserSubscription.  # noqa: E501


        :return: The updated_at of this UserSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserSubscription.


        :param updated_at: The updated_at of this UserSubscription.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def license_groups(self):
        """Gets the license_groups of this UserSubscription.  # noqa: E501


        :return: The license_groups of this UserSubscription.  # noqa: E501
        :rtype: list[str]
        """
        return self._license_groups

    @license_groups.setter
    def license_groups(self, license_groups):
        """Sets the license_groups of this UserSubscription.


        :param license_groups: The license_groups of this UserSubscription.  # noqa: E501
        :type license_groups: list[str]
        """
        if self.local_vars_configuration.client_side_validation and license_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `license_groups`, must not be `None`")  # noqa: E501

        self._license_groups = license_groups

    @property
    def is_gift(self):
        """Gets the is_gift of this UserSubscription.  # noqa: E501


        :return: The is_gift of this UserSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_gift

    @is_gift.setter
    def is_gift(self, is_gift):
        """Sets the is_gift of this UserSubscription.


        :param is_gift: The is_gift of this UserSubscription.  # noqa: E501
        :type is_gift: bool
        """
        if self.local_vars_configuration.client_side_validation and is_gift is None:  # noqa: E501
            raise ValueError("Invalid value for `is_gift`, must not be `None`")  # noqa: E501

        self._is_gift = is_gift

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
        if not isinstance(other, UserSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSubscription):
            return True

        return self.to_dict() != other.to_dict()
