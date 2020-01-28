# kclient.ServingApi

All URIs are relative to *https://dev.kibernetika.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serving_delete**](ServingApi.md#serving_delete) | **DELETE** /api/v0.2/workspace/{workspace}/serving/{serving} | Delete serving
[**serving_disable**](ServingApi.md#serving_disable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/disable | Disable serving
[**serving_enable**](ServingApi.md#serving_enable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/enable | Enable serving
[**serving_info**](ServingApi.md#serving_info) | **GET** /api/v0.2/workspace/{workspace}/serving/{serving} | Return serving&#39;s info
[**serving_project_job**](ServingApi.md#serving_project_job) | **GET** /api/v0.2/workspace/{workspace}/serving/{serving}/projresult/job/{job} | Serving result jobs
[**serving_proxy**](ServingApi.md#serving_proxy) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/proxy | Proxy to serving (json data)
[**update_serving**](ServingApi.md#update_serving) | **PUT** /api/v0.2/workspace/{workspace}/serving/{serving} | Update serving


# **serving_delete**
> serving_delete(workspace, serving, dependencies=dependencies, confirm=confirm, force=force)

Delete serving

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID
dependencies = true # bool | Get only dependencies (optional)
confirm = 'confirm_example' # str | String for confirmation (optional)
force = true # bool | Force deletion (optional)

try:
    # Delete serving
    api_instance.serving_delete(workspace, serving, dependencies=dependencies, confirm=confirm, force=force)
except ApiException as e:
    print("Exception when calling ServingApi->serving_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 
 **dependencies** | **bool**| Get only dependencies | [optional] 
 **confirm** | **str**| String for confirmation | [optional] 
 **force** | **bool**| Force deletion | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_disable**
> ModelsServing serving_disable(workspace, serving)

Disable serving

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Disable serving
    api_response = api_instance.serving_disable(workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ModelsServing**](ModelsServing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_enable**
> ModelsServing serving_enable(workspace, serving)

Enable serving

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Enable serving
    api_response = api_instance.serving_enable(workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ModelsServing**](ModelsServing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_info**
> ModelsServing serving_info(workspace, serving)

Return serving's info

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Return serving's info
    api_response = api_instance.serving_info(workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ModelsServing**](ModelsServing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_project_job**
> ApplicationProjectServingJob serving_project_job(job, workspace, serving)

Serving result jobs

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
job = 'job_example' # str | Serving job ID
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Serving result jobs
    api_response = api_instance.serving_project_job(job, workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_project_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | **str**| Serving job ID | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ApplicationProjectServingJob**](ApplicationProjectServingJob.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_proxy**
> ModelsArbitrary serving_proxy(body, workspace, serving)

Proxy to serving (json data)

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
body = kclient.ModelsArbitrary() # ModelsArbitrary | 
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Proxy to serving (json data)
    api_response = api_instance.serving_proxy(body, workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsArbitrary**](ModelsArbitrary.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ModelsArbitrary**](ModelsArbitrary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_serving**
> ModelsServing update_serving(body, workspace, serving)

Update serving

### Example
```python
from __future__ import print_function
import time
import kclient
from kclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = kclient.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kclient.ServingApi(kclient.ApiClient(configuration))
body = kclient.MlappServing() # MlappServing | 
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID

try:
    # Update serving
    api_response = api_instance.update_serving(body, workspace, serving)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->update_serving: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MlappServing**](MlappServing.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 

### Return type

[**ModelsServing**](ModelsServing.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

