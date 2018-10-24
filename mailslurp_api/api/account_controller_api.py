# coding: utf-8

"""
    MailSlurp API Documentation

    [MailSlurp](https://www.mailslurp.com) is an end-to-end email testing service. It has a [web-app](https://www.mailslurp.com/dashboard) for managing your account and a [REST API](https://api.mailslurp.com) for sending and receiving emails from randomly generated email addresses.  ## Why? MailSlurp was built to test the integration of email services within an app. If your application relies on the sending or receiving of emails, then MailSlurp will let you test that functionality. This is a more common need than you might think: if your app has a sign up process that requires email verification, how do you currently test that?  ## Getting started - [API Docs](https://www.mailslurp.com/documentation) - [Code Examples](https://www.mailslurp.com/documentation/examples) - [Swagger Definition](https://api.mailslurp.com/v2/api-docs)  Every API request requires a valid API Key appended as a query parameter. [To obtain an API Key visit your account dashboard](https://www.mailslurp.com/dashboard).    The general flow is as follows:  - Create a new inbox during a test. The email address will be returned in the response.  - Send an email to that address or trigger an action in your test that does so. - Fetch the email for your new inbox and check if its content is what you expected, or use the content in another action.  ## SDK - There is an official [Javascript SDK](https://www.npmjs.com/package/mailslurp-client) available on npm. - You can also use the [swagger JSON definition](https://api.mailslurp.com/v2/api-docs) and [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to generate a swagger client in a language of your choice.  ## Legal The Mailslurp API code is owned by [PettmanUG](http://pettmanug.site) and uses a proprietary [software licence](http://www.binpress.com/license/view/l/c8376a01eca7465027a978d3fde5a1e2). The SDKs are free to use in any project and have an ISC licence.  ## Bugs, features, support To report bugs or request features please see the [contact page](https://www.mailslurp.com/contact). For help see [support](https://www.mailslurp.com/support).  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailslurp_api.api_client import ApiClient


class AccountControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_subscription_using_post(self, jwt_token, stripe_token, **kwargs):  # noqa: E501
        """Upgrade a user to paid  # noqa: E501

        For use in dashboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subscription_using_post(jwt_token, stripe_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str jwt_token: Cognito ID obtained during login (required)
        :param str stripe_token: Stripe user payment confirmation token (required)
        :return: UserDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_subscription_using_post_with_http_info(jwt_token, stripe_token, **kwargs)  # noqa: E501
        else:
            (data) = self.create_subscription_using_post_with_http_info(jwt_token, stripe_token, **kwargs)  # noqa: E501
            return data

    def create_subscription_using_post_with_http_info(self, jwt_token, stripe_token, **kwargs):  # noqa: E501
        """Upgrade a user to paid  # noqa: E501

        For use in dashboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_subscription_using_post_with_http_info(jwt_token, stripe_token, async=True)
        >>> result = thread.get()

        :param async bool
        :param str jwt_token: Cognito ID obtained during login (required)
        :param str stripe_token: Stripe user payment confirmation token (required)
        :return: UserDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['jwt_token', 'stripe_token']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'jwt_token' is set
        if ('jwt_token' not in params or
                params['jwt_token'] is None):
            raise ValueError("Missing the required parameter `jwt_token` when calling `create_subscription_using_post`")  # noqa: E501
        # verify the required parameter 'stripe_token' is set
        if ('stripe_token' not in params or
                params['stripe_token'] is None):
            raise ValueError("Missing the required parameter `stripe_token` when calling `create_subscription_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'jwt_token' in params:
            query_params.append(('jwtToken', params['jwt_token']))  # noqa: E501
        if 'stripe_token' in params:
            query_params.append(('stripeToken', params['stripe_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subscription', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_accounts_using_get(self, **kwargs):  # noqa: E501
        """List available account types  # noqa: E501

        For use in dashboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_accounts_using_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: AccountsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_accounts_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_accounts_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_accounts_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """List available account types  # noqa: E501

        For use in dashboard  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_accounts_using_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: AccountsDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_accounts_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AccountsDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
