# mailslurp-api
[MailSlurp](https://www.mailslurp.com) is an end-to-end email testing service. It has a [web-app](https://www.mailslurp.com/dashboard) for managing your account and a [REST API](https://api.mailslurp.com) for sending and receiving emails from randomly generated email addresses.  ## Why? MailSlurp was built to test the integration of email services within an app. If your application relies on the sending or receiving of emails, then MailSlurp will let you test that functionality. This is a more common need than you might think: if your app has a sign up process that requires email verification, how do you currently test that?  ## Getting started - [API Docs](https://www.mailslurp.com/documentation) - [Code Examples](https://www.mailslurp.com/documentation/examples) - [Swagger Definition](https://api.mailslurp.com/v2/api-docs)  Every API request requires a valid API Key appended as a query parameter. [To obtain an API Key visit your account dashboard](https://www.mailslurp.com/dashboard).    The general flow is as follows:  - Create a new inbox during a test. The email address will be returned in the response.  - Send an email to that address or trigger an action in your test that does so. - Fetch the email for your new inbox and check if its content is what you expected, or use the content in another action.  ## SDK - There is an official [Javascript SDK](https://www.npmjs.com/package/mailslurp-client) available on npm. - You can also use the [swagger JSON definition](https://api.mailslurp.com/v2/api-docs) and [swagger-codegen](https://github.com/swagger-api/swagger-codegen) to generate a swagger client in a language of your choice.  ## Legal The Mailslurp API code is owned by [PettmanUG](http://pettmanug.site) and uses a proprietary [software licence](http://www.binpress.com/license/view/l/c8376a01eca7465027a978d3fde5a1e2). The SDKs are free to use in any project and have an ISC licence.  ## Bugs, features, support To report bugs or request features please see the [contact page](https://www.mailslurp.com/contact). For help see [support](https://www.mailslurp.com/support).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/tobias-reese/mailslurp-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tobias-reese/mailslurp-api.git`)

Then import the package:
```python
import mailslurp_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mailslurp_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = mailslurp_api.AccountControllerApi()
jwt_token = 'jwt_token_example' # str | Cognito ID obtained during login
stripe_token = 'stripe_token_example' # str | Stripe user payment confirmation token

try:
    # Upgrade a user to paid
    api_response = api_instance.create_subscription_using_post(jwt_token, stripe_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->create_subscription_using_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mailslurp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountControllerApi* | [**create_subscription_using_post**](docs/AccountControllerApi.md#create_subscription_using_post) | **POST** /subscription | Upgrade a user to paid
*AccountControllerApi* | [**get_accounts_using_get**](docs/AccountControllerApi.md#get_accounts_using_get) | **GET** /accounts | List available account types
*InboxControllerApi* | [**create_random_inbox_using_post**](docs/InboxControllerApi.md#create_random_inbox_using_post) | **POST** /inboxes | Create an inbox
*InboxControllerApi* | [**delete_inbox_using_delete**](docs/InboxControllerApi.md#delete_inbox_using_delete) | **DELETE** /inboxes/{uuid} | Delete an inbox
*InboxControllerApi* | [**get_emails_for_inbox_using_get**](docs/InboxControllerApi.md#get_emails_for_inbox_using_get) | **GET** /inboxes/{uuid} | Fetch emails for a given inbox
*InboxControllerApi* | [**get_list_of_inboxes_using_get**](docs/InboxControllerApi.md#get_list_of_inboxes_using_get) | **GET** /inboxes | List your inboxes
*InboxControllerApi* | [**send_email_from_user_using_post**](docs/InboxControllerApi.md#send_email_from_user_using_post) | **POST** /inboxes/{uuid} | Send an email
*UserControllerApi* | [**get_user_using_get**](docs/UserControllerApi.md#get_user_using_get) | **GET** /user | Fetch a user


## Documentation For Models

 - [AccountDto](docs/AccountDto.md)
 - [AccountsDto](docs/AccountsDto.md)
 - [EmailDto](docs/EmailDto.md)
 - [InboxDto](docs/InboxDto.md)
 - [Response](docs/Response.md)
 - [ResponseInboxDto](docs/ResponseInboxDto.md)
 - [ResponseListEmailDto](docs/ResponseListEmailDto.md)
 - [ResponseListInboxDto](docs/ResponseListInboxDto.md)
 - [SendEmailDto](docs/SendEmailDto.md)
 - [UserDto](docs/UserDto.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



