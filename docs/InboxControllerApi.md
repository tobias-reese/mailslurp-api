# mailslurp_api.InboxControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_random_inbox_using_post**](InboxControllerApi.md#create_random_inbox_using_post) | **POST** /inboxes | Create an inbox
[**delete_inbox_using_delete**](InboxControllerApi.md#delete_inbox_using_delete) | **DELETE** /inboxes/{uuid} | Delete an inbox
[**get_emails_for_inbox_using_get**](InboxControllerApi.md#get_emails_for_inbox_using_get) | **GET** /inboxes/{uuid} | Fetch emails for a given inbox
[**get_list_of_inboxes_using_get**](InboxControllerApi.md#get_list_of_inboxes_using_get) | **GET** /inboxes | List your inboxes
[**send_email_from_user_using_post**](InboxControllerApi.md#send_email_from_user_using_post) | **POST** /inboxes/{uuid} | Send an email


# **create_random_inbox_using_post**
> ResponseInboxDto create_random_inbox_using_post(api_key)

Create an inbox

Create a new random inbox and return the id and email address for it. Send emails to this address and they will be stored for this inbox.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.InboxControllerApi()
api_key = 'test' # str | Your API Key. Sign up and find it in your dashboard. (default to test)

try:
    # Create an inbox
    api_response = api_instance.create_random_inbox_using_post(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxControllerApi->create_random_inbox_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Your API Key. Sign up and find it in your dashboard. | [default to test]

### Return type

[**ResponseInboxDto**](ResponseInboxDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbox_using_delete**
> Response delete_inbox_using_delete(api_key, uuid)

Delete an inbox

Delete an inbox and all the emails associated with it.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.InboxControllerApi()
api_key = 'test' # str | Your API Key. Sign up and find it in your dashboard. (default to test)
uuid = 'uuid_example' # str | The inbox's id.

try:
    # Delete an inbox
    api_response = api_instance.delete_inbox_using_delete(api_key, uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxControllerApi->delete_inbox_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Your API Key. Sign up and find it in your dashboard. | [default to test]
 **uuid** | **str**| The inbox&#39;s id. | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emails_for_inbox_using_get**
> ResponseListEmailDto get_emails_for_inbox_using_get(api_key, uuid, min_count=min_count, max_wait=max_wait, since=since)

Fetch emails for a given inbox

Return a list of emails stored in a given inbox. Each email contains various properties including the email body (in eml format), subject, and sender. The `since` parameter is a ISO8601 LocalDateTime that will filter for emails received on or after the given DateTime. Note that because an inbox may take 5 to 10 seconds to receive an email, you can use the `waitFor` parameter to hold a request open until the desired number of emails is present. If this number is not met after 100 seconds, an error will be returned.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.InboxControllerApi()
api_key = 'test' # str | Your API Key. Sign up and find it in your dashboard. (default to test)
uuid = 'uuid_example' # str | The inbox's id.
min_count = 56 # int | Wait a maximum of 100 seconds for atleast this many emails in an inbox before returning a result. (optional)
max_wait = 789 # int | Maximum seconds API should spend retrying your inbox until the minCount is satisfied (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Filter for emails received on or after this ISO8601 LocalDateTime. (optional)

try:
    # Fetch emails for a given inbox
    api_response = api_instance.get_emails_for_inbox_using_get(api_key, uuid, min_count=min_count, max_wait=max_wait, since=since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxControllerApi->get_emails_for_inbox_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Your API Key. Sign up and find it in your dashboard. | [default to test]
 **uuid** | **str**| The inbox&#39;s id. | 
 **min_count** | **int**| Wait a maximum of 100 seconds for atleast this many emails in an inbox before returning a result. | [optional] 
 **max_wait** | **int**| Maximum seconds API should spend retrying your inbox until the minCount is satisfied | [optional] 
 **since** | **datetime**| Filter for emails received on or after this ISO8601 LocalDateTime. | [optional] 

### Return type

[**ResponseListEmailDto**](ResponseListEmailDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_inboxes_using_get**
> ResponseListInboxDto get_list_of_inboxes_using_get(api_key)

List your inboxes

Return a list of your inboxes. Each inbox has a uuid and an email address. Emails sent to the email address are stored in the inbox and can be fetched via `/inboxes/{uuid}`.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.InboxControllerApi()
api_key = 'test' # str | Your API Key. Sign up and find it in your dashboard. (default to test)

try:
    # List your inboxes
    api_response = api_instance.get_list_of_inboxes_using_get(api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxControllerApi->get_list_of_inboxes_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Your API Key. Sign up and find it in your dashboard. | [default to test]

### Return type

[**ResponseListInboxDto**](ResponseListInboxDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_from_user_using_post**
> Response send_email_from_user_using_post(api_key, uuid, send_email_dto)

Send an email

Send an email from the given inbox's email address. Useful if you need to test a user contacting you, for instance.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.InboxControllerApi()
api_key = 'test' # str | Your API Key. Sign up and find it in your dashboard. (default to test)
uuid = 'uuid_example' # str | The inbox's id.
send_email_dto = mailslurp_api.SendEmailDto() # SendEmailDto | The email to send.

try:
    # Send an email
    api_response = api_instance.send_email_from_user_using_post(api_key, uuid, send_email_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InboxControllerApi->send_email_from_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| Your API Key. Sign up and find it in your dashboard. | [default to test]
 **uuid** | **str**| The inbox&#39;s id. | 
 **send_email_dto** | [**SendEmailDto**](SendEmailDto.md)| The email to send. | 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

