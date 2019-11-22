# swagger_client.InferenceApi

All URIs are relative to *https://dev.kibernetika.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inference_inference_version_delete**](InferenceApi.md#inference_inference_version_delete) | **DELETE** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Delete inference&#39;s version
[**inference_inference_version_info**](InferenceApi.md#inference_inference_version_info) | **GET** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Return inference&#39;s info for specified version
[**inference_inference_version_start**](InferenceApi.md#inference_inference_version_start) | **POST** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version}/start | Starts serving
[**inference_inference_version_update**](InferenceApi.md#inference_inference_version_update) | **PUT** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Update inference&#39;s info for specified version


# **inference_inference_version_delete**
> inference_inference_version_delete(workspace, inference, version)

Delete inference's version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.InferenceApi(swagger_client.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
inference = 'inference_example' # str | Item's name (Inference)
version = 'version_example' # str | Inference's version

try:
    # Delete inference's version
    api_instance.inference_inference_version_delete(workspace, inference, version)
except ApiException as e:
    print("Exception when calling InferenceApi->inference_inference_version_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **inference** | **str**| Item&#39;s name (Inference) | 
 **version** | **str**| Inference&#39;s version | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_inference_version_info**
> ModelsInferenceVersion inference_inference_version_info(workspace, inference, version)

Return inference's info for specified version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.InferenceApi(swagger_client.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
inference = 'inference_example' # str | Item's name (Inference)
version = 'version_example' # str | Inference's version

try:
    # Return inference's info for specified version
    api_response = api_instance.inference_inference_version_info(workspace, inference, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceApi->inference_inference_version_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **inference** | **str**| Item&#39;s name (Inference) | 
 **version** | **str**| Inference&#39;s version | 

### Return type

[**ModelsInferenceVersion**](ModelsInferenceVersion.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_inference_version_start**
> ModelsServing inference_inference_version_start(body, workspace, inference, version)

Starts serving

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.InferenceApi(swagger_client.ApiClient(configuration))
body = swagger_client.InferenceRunServingRequest() # InferenceRunServingRequest | 
workspace = 'workspace_example' # str | Workspace's name
inference = 'inference_example' # str | Item's name (Inference)
version = 'version_example' # str | Inference's version

try:
    # Starts serving
    api_response = api_instance.inference_inference_version_start(body, workspace, inference, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceApi->inference_inference_version_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InferenceRunServingRequest**](InferenceRunServingRequest.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **inference** | **str**| Item&#39;s name (Inference) | 
 **version** | **str**| Inference&#39;s version | 

### Return type

[**ModelsServing**](ModelsServing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inference_inference_version_update**
> ModelsInferenceVersion inference_inference_version_update(body, workspace, inference, version)

Update inference's info for specified version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.InferenceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ModelsInferenceVersion() # ModelsInferenceVersion | 
workspace = 'workspace_example' # str | Workspace's name
inference = 'inference_example' # str | Item's name (Inference)
version = 'version_example' # str | Inference's version

try:
    # Update inference's info for specified version
    api_response = api_instance.inference_inference_version_update(body, workspace, inference, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InferenceApi->inference_inference_version_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsInferenceVersion**](ModelsInferenceVersion.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **inference** | **str**| Item&#39;s name (Inference) | 
 **version** | **str**| Inference&#39;s version | 

### Return type

[**ModelsInferenceVersion**](ModelsInferenceVersion.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

