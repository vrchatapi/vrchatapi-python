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


class TransactionSteamWalletInfo(object):
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
        'state': 'str',
        'country': 'str',
        'currency': 'str',
        'status': 'str'
    }

    attribute_map = {
        'state': 'state',
        'country': 'country',
        'currency': 'currency',
        'status': 'status'
    }

    def __init__(self, state=None, country='US', currency='USD', status=None, local_vars_configuration=None):  # noqa: E501
        """TransactionSteamWalletInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._state = None
        self._country = None
        self._currency = None
        self._status = None
        self.discriminator = None

        self.state = state
        self.country = country
        self.currency = currency
        self.status = status

    @property
    def state(self):
        """Gets the state of this TransactionSteamWalletInfo.  # noqa: E501


        :return: The state of this TransactionSteamWalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionSteamWalletInfo.


        :param state: The state of this TransactionSteamWalletInfo.  # noqa: E501
        :type state: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def country(self):
        """Gets the country of this TransactionSteamWalletInfo.  # noqa: E501


        :return: The country of this TransactionSteamWalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this TransactionSteamWalletInfo.


        :param country: The country of this TransactionSteamWalletInfo.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country is not None and len(country) < 2):
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")  # noqa: E501

        self._country = country

    @property
    def currency(self):
        """Gets the currency of this TransactionSteamWalletInfo.  # noqa: E501


        :return: The currency of this TransactionSteamWalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this TransactionSteamWalletInfo.


        :param currency: The currency of this TransactionSteamWalletInfo.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) < 3):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this TransactionSteamWalletInfo.  # noqa: E501


        :return: The status of this TransactionSteamWalletInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransactionSteamWalletInfo.


        :param status: The status of this TransactionSteamWalletInfo.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, TransactionSteamWalletInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionSteamWalletInfo):
            return True

        return self.to_dict() != other.to_dict()