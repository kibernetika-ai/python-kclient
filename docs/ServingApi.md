# kclient.ServingApi

All URIs are relative to *https://dev.kibernetika.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serving_delete**](ServingApi.md#serving_delete) | **DELETE** /api/v0.2/workspace/{workspace}/serving/{serving} | Delete serving
[**serving_disable**](ServingApi.md#serving_disable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/disable | Disable serving
[**serving_enable**](ServingApi.md#serving_enable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/enable | Enable serving
[**serving_info**](ServingApi.md#serving_info) | **GET** /api/v0.2/workspace/{workspace}/serving/{serving} | Return serving&#39;s info
[**serving_tf_proxy_model**](ServingApi.md#serving_tf_proxy_model) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/tfproxy/{port}/{model} | TF proxy to serving (model)
[**serving_tf_proxy_model_signature**](ServingApi.md#serving_tf_proxy_model_signature) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/tfproxy/{port}/{model}/{signature} | TF proxy to serving (model, signature)
[**serving_tf_proxy_model_signature_version**](ServingApi.md#serving_tf_proxy_model_signature_version) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/tfproxy/{port}/{model}/{signature}/{version} | TF proxy to serving (model, signature, version)
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

# **serving_tf_proxy_model**
> str serving_tf_proxy_model(model, body, workspace, serving, port)

TF proxy to serving (model)

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
model = 'model_example' # str | Serving model
body = 'body_example' # str | 
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID
port = 'port_example' # str | Serving port

try:
    # TF proxy to serving (model)
    api_response = api_instance.serving_tf_proxy_model(model, body, workspace, serving, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_tf_proxy_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Serving model | 
 **body** | [**str**](str.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 
 **port** | **str**| Serving port | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_tf_proxy_model_signature**
> str serving_tf_proxy_model_signature(model, signature, body, workspace, serving, port)

TF proxy to serving (model, signature)

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
model = 'model_example' # str | Serving model
signature = 'signature_example' # str | Serving signature
body = 'body_example' # str | 
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID
port = 'port_example' # str | Serving port

try:
    # TF proxy to serving (model, signature)
    api_response = api_instance.serving_tf_proxy_model_signature(model, signature, body, workspace, serving, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_tf_proxy_model_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Serving model | 
 **signature** | **str**| Serving signature | 
 **body** | [**str**](str.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 
 **port** | **str**| Serving port | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serving_tf_proxy_model_signature_version**
> str serving_tf_proxy_model_signature_version(model, signature, version, body, workspace, serving, port)

TF proxy to serving (model, signature, version)

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
model = 'model_example' # str | Serving model
signature = 'signature_example' # str | Serving signature
version = 'version_example' # str | Serving version
body = 'body_example' # str | 
workspace = 'workspace_example' # str | Workspace's name
serving = 'serving_example' # str | Serving's Name or ID
port = 'port_example' # str | Serving port

try:
    # TF proxy to serving (model, signature, version)
    api_response = api_instance.serving_tf_proxy_model_signature_version(model, signature, version, body, workspace, serving, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServingApi->serving_tf_proxy_model_signature_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Serving model | 
 **signature** | **str**| Serving signature | 
 **version** | **str**| Serving version | 
 **body** | [**str**](str.md)|  | 
 **workspace** | **str**| Workspace&#39;s name | 
 **serving** | **str**| Serving&#39;s Name or ID | 
 **port** | **str**| Serving port | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
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

