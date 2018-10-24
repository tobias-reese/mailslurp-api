# mailslurp_api.UserControllerApi

All URIs are relative to *https://api.mailslurp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_using_get**](UserControllerApi.md#get_user_using_get) | **GET** /user | Fetch a user


# **get_user_using_get**
> UserDto get_user_using_get(jwt_token)

Fetch a user

Used by the dashboard to fetch user information.

### Example
```python
from __future__ import print_function
import time
import mailslurp_api
from mailslurp_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mailslurp_api.UserControllerApi()
jwt_token = 'jwt_token_example' # str | Cognito ID obtained during login

try:
    # Fetch a user
    api_response = api_instance.get_user_using_get(jwt_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserControllerApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jwt_token** | **str**| Cognito ID obtained during login | 

### Return type

[**UserDto**](UserDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

