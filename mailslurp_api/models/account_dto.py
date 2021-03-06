# coding: utf-8

"""
    MailSlurp API Documentation

    [MailSlurp](https://www.mailslurp.com) is an end-to-end email testing service. It has a [web-app](https://www.mailslurp.com/dashboard) for managing your account and a [REST API](https://api.mailslurp.com) for sending and receiving emails from randomly generated email addresses.  ## Why? MailSlurp was built to test the integration of email services within an app. If your application relies on the sending or receiving of emails, then MailSlurp will let you test that functionality. This is a more common need than you might think: if your app has a sign up process that requires email verification, how do you currently test that?  ## Getting started - [API Docs](https://www.mailslurp.com/documentation) - [Code Examples](https://www.mailslurp.com/documentation/examples) - [Swagger Definition](https://api.mailslurp.com/v2/api-docs)  Every API request requires a valid API Key appended as a query parameter. [To obtain an API Key visit your account dashboard](https://www.mailslurp.com/dashboard).    The general flow is as follows:  - Create a new inbox during a test. The email address will be returned in the response.  - Send an email to that address or trigger an action in your test that does so. - Fetch the email for your new inbox and check if its content is what you expected, or use the content in another action.  ## SDK - There is an official [Javascript SDK](https://www.npmjs.com/package/mailslurp-client) available on npm. - You can also use the [swagger JSON definition](https://api.mailslurp.com/v2/api-docs) and [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to generate a swagger client in a language of your choice.  ## Legal The Mailslurp API code is owned by [PettmanUG](http://pettmanug.site) and uses a proprietary [software licence](http://www.binpress.com/license/view/l/c8376a01eca7465027a978d3fde5a1e2). The SDKs are free to use in any project and have an ISC licence.  ## Bugs, features, support To report bugs or request features please see the [contact page](https://www.mailslurp.com/contact). For help see [support](https://www.mailslurp.com/support).  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_type': 'str',
        'limit': 'str',
        'price_cents': 'int',
        'price_string': 'str',
        'stripe_product': 'str'
    }

    attribute_map = {
        'account_type': 'accountType',
        'limit': 'limit',
        'price_cents': 'priceCents',
        'price_string': 'priceString',
        'stripe_product': 'stripeProduct'
    }

    def __init__(self, account_type=None, limit=None, price_cents=None, price_string=None, stripe_product=None):  # noqa: E501
        """AccountDto - a model defined in Swagger"""  # noqa: E501

        self._account_type = None
        self._limit = None
        self._price_cents = None
        self._price_string = None
        self._stripe_product = None
        self.discriminator = None

        if account_type is not None:
            self.account_type = account_type
        if limit is not None:
            self.limit = limit
        if price_cents is not None:
            self.price_cents = price_cents
        if price_string is not None:
            self.price_string = price_string
        if stripe_product is not None:
            self.stripe_product = stripe_product

    @property
    def account_type(self):
        """Gets the account_type of this AccountDto.  # noqa: E501


        :return: The account_type of this AccountDto.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this AccountDto.


        :param account_type: The account_type of this AccountDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["FREE", "PAID"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def limit(self):
        """Gets the limit of this AccountDto.  # noqa: E501


        :return: The limit of this AccountDto.  # noqa: E501
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this AccountDto.


        :param limit: The limit of this AccountDto.  # noqa: E501
        :type: str
        """

        self._limit = limit

    @property
    def price_cents(self):
        """Gets the price_cents of this AccountDto.  # noqa: E501


        :return: The price_cents of this AccountDto.  # noqa: E501
        :rtype: int
        """
        return self._price_cents

    @price_cents.setter
    def price_cents(self, price_cents):
        """Sets the price_cents of this AccountDto.


        :param price_cents: The price_cents of this AccountDto.  # noqa: E501
        :type: int
        """

        self._price_cents = price_cents

    @property
    def price_string(self):
        """Gets the price_string of this AccountDto.  # noqa: E501


        :return: The price_string of this AccountDto.  # noqa: E501
        :rtype: str
        """
        return self._price_string

    @price_string.setter
    def price_string(self, price_string):
        """Sets the price_string of this AccountDto.


        :param price_string: The price_string of this AccountDto.  # noqa: E501
        :type: str
        """

        self._price_string = price_string

    @property
    def stripe_product(self):
        """Gets the stripe_product of this AccountDto.  # noqa: E501


        :return: The stripe_product of this AccountDto.  # noqa: E501
        :rtype: str
        """
        return self._stripe_product

    @stripe_product.setter
    def stripe_product(self, stripe_product):
        """Sets the stripe_product of this AccountDto.


        :param stripe_product: The stripe_product of this AccountDto.  # noqa: E501
        :type: str
        """

        self._stripe_product = stripe_product

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
