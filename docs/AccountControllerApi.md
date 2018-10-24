# mailslurp_api.AccountControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription_using_post**](AccountControllerApi.md#create_subscription_using_post) | **POST** /subscription | Upgrade a user to paid
[**get_accounts_using_get**](AccountControllerApi.md#get_accounts_using_get) | **GET** /accounts | List available account types


# **create_subscription_using_post**
> UserDto create_subscription_using_post(jwt_token, stripe_token)

Upgrade a user to paid

For use in dashboard

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | **str**| Cognito ID obtained during login | 
 **stripe_token** | **str**| Stripe user payment confirmation token | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_using_get**
> AccountsDto get_accounts_using_get()

List available account types

For use in dashboard

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.AccountControllerApi()

try:
    # List available account types
    api_response = api_instance.get_accounts_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountControllerApi->get_accounts_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountsDto**](AccountsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

