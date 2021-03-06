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


class InboxControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_random_inbox_using_post(self, api_key, **kwargs):  # noqa: E501
        """Create an inbox  # noqa: E501

        Create a new random inbox and return the id and email address for it. Send emails to this address and they will be stored for this inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_random_inbox_using_post(api_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :return: ResponseInboxDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_random_inbox_using_post_with_http_info(api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.create_random_inbox_using_post_with_http_info(api_key, **kwargs)  # noqa: E501
            return data

    def create_random_inbox_using_post_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """Create an inbox  # noqa: E501

        Create a new random inbox and return the id and email address for it. Send emails to this address and they will be stored for this inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_random_inbox_using_post_with_http_info(api_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :return: ResponseInboxDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_random_inbox_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `create_random_inbox_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in params:
            query_params.append(('apiKey', params['api_key']))  # noqa: E501

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
            '/inboxes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseInboxDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_inbox_using_delete(self, api_key, uuid, **kwargs):  # noqa: E501
        """Delete an inbox  # noqa: E501

        Delete an inbox and all the emails associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_inbox_using_delete(api_key, uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_inbox_using_delete_with_http_info(api_key, uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_inbox_using_delete_with_http_info(api_key, uuid, **kwargs)  # noqa: E501
            return data

    def delete_inbox_using_delete_with_http_info(self, api_key, uuid, **kwargs):  # noqa: E501
        """Delete an inbox  # noqa: E501

        Delete an inbox and all the emails associated with it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_inbox_using_delete_with_http_info(api_key, uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'uuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_inbox_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `delete_inbox_using_delete`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `delete_inbox_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('apiKey', params['api_key']))  # noqa: E501

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
            '/inboxes/{uuid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_emails_for_inbox_using_get(self, api_key, uuid, **kwargs):  # noqa: E501
        """Fetch emails for a given inbox  # noqa: E501

        Return a list of emails stored in a given inbox. Each email contains various properties including the email body (in eml format), subject, and sender. The `since` parameter is a ISO8601 LocalDateTime that will filter for emails received on or after the given DateTime. Note that because an inbox may take 5 to 10 seconds to receive an email, you can use the `waitFor` parameter to hold a request open until the desired number of emails is present. If this number is not met after 100 seconds, an error will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_emails_for_inbox_using_get(api_key, uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :param int min_count: Wait a maximum of 100 seconds for atleast this many emails in an inbox before returning a result.
        :param int max_wait: Maximum seconds API should spend retrying your inbox until the minCount is satisfied
        :param datetime since: Filter for emails received on or after this ISO8601 LocalDateTime.
        :return: ResponseListEmailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_emails_for_inbox_using_get_with_http_info(api_key, uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_emails_for_inbox_using_get_with_http_info(api_key, uuid, **kwargs)  # noqa: E501
            return data

    def get_emails_for_inbox_using_get_with_http_info(self, api_key, uuid, **kwargs):  # noqa: E501
        """Fetch emails for a given inbox  # noqa: E501

        Return a list of emails stored in a given inbox. Each email contains various properties including the email body (in eml format), subject, and sender. The `since` parameter is a ISO8601 LocalDateTime that will filter for emails received on or after the given DateTime. Note that because an inbox may take 5 to 10 seconds to receive an email, you can use the `waitFor` parameter to hold a request open until the desired number of emails is present. If this number is not met after 100 seconds, an error will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_emails_for_inbox_using_get_with_http_info(api_key, uuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :param int min_count: Wait a maximum of 100 seconds for atleast this many emails in an inbox before returning a result.
        :param int max_wait: Maximum seconds API should spend retrying your inbox until the minCount is satisfied
        :param datetime since: Filter for emails received on or after this ISO8601 LocalDateTime.
        :return: ResponseListEmailDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'uuid', 'min_count', 'max_wait', 'since']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_emails_for_inbox_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_emails_for_inbox_using_get`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `get_emails_for_inbox_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('apiKey', params['api_key']))  # noqa: E501
        if 'min_count' in params:
            query_params.append(('minCount', params['min_count']))  # noqa: E501
        if 'max_wait' in params:
            query_params.append(('maxWait', params['max_wait']))  # noqa: E501
        if 'since' in params:
            query_params.append(('since', params['since']))  # noqa: E501

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
            '/inboxes/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseListEmailDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_list_of_inboxes_using_get(self, api_key, **kwargs):  # noqa: E501
        """List your inboxes  # noqa: E501

        Return a list of your inboxes. Each inbox has a uuid and an email address. Emails sent to the email address are stored in the inbox and can be fetched via `/inboxes/{uuid}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_list_of_inboxes_using_get(api_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :return: ResponseListInboxDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_list_of_inboxes_using_get_with_http_info(api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_list_of_inboxes_using_get_with_http_info(api_key, **kwargs)  # noqa: E501
            return data

    def get_list_of_inboxes_using_get_with_http_info(self, api_key, **kwargs):  # noqa: E501
        """List your inboxes  # noqa: E501

        Return a list of your inboxes. Each inbox has a uuid and an email address. Emails sent to the email address are stored in the inbox and can be fetched via `/inboxes/{uuid}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_list_of_inboxes_using_get_with_http_info(api_key, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :return: ResponseListInboxDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_list_of_inboxes_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_list_of_inboxes_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_key' in params:
            query_params.append(('apiKey', params['api_key']))  # noqa: E501

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
            '/inboxes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseListInboxDto',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_email_from_user_using_post(self, api_key, uuid, send_email_dto, **kwargs):  # noqa: E501
        """Send an email  # noqa: E501

        Send an email from the given inbox's email address. Useful if you need to test a user contacting you, for instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_email_from_user_using_post(api_key, uuid, send_email_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :param SendEmailDto send_email_dto: The email to send. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_email_from_user_using_post_with_http_info(api_key, uuid, send_email_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.send_email_from_user_using_post_with_http_info(api_key, uuid, send_email_dto, **kwargs)  # noqa: E501
            return data

    def send_email_from_user_using_post_with_http_info(self, api_key, uuid, send_email_dto, **kwargs):  # noqa: E501
        """Send an email  # noqa: E501

        Send an email from the given inbox's email address. Useful if you need to test a user contacting you, for instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_email_from_user_using_post_with_http_info(api_key, uuid, send_email_dto, async=True)
        >>> result = thread.get()

        :param async bool
        :param str api_key: Your API Key. Sign up and find it in your dashboard. (required)
        :param str uuid: The inbox's id. (required)
        :param SendEmailDto send_email_dto: The email to send. (required)
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_key', 'uuid', 'send_email_dto']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_email_from_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `send_email_from_user_using_post`")  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `send_email_from_user_using_post`")  # noqa: E501
        # verify the required parameter 'send_email_dto' is set
        if ('send_email_dto' not in params or
                params['send_email_dto'] is None):
            raise ValueError("Missing the required parameter `send_email_dto` when calling `send_email_from_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []
        if 'api_key' in params:
            query_params.append(('apiKey', params['api_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'send_email_dto' in params:
            body_params = params['send_email_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/inboxes/{uuid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
