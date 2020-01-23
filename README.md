# kclient
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = kclient.InferenceApi(kclient.ApiClient(configuration))
workspace = 'workspace_example' # str | Workspace's name
inference = 'inference_example' # str | Item's name (Inference)
version = 'version_example' # str | Inference's version

try:
    # Delete inference's version
    api_instance.inference_inference_version_delete(workspace, inference, version)
except ApiException as e:
    print("Exception when calling InferenceApi->inference_inference_version_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dev.kibernetika.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InferenceApi* | [**inference_inference_version_delete**](docs/InferenceApi.md#inference_inference_version_delete) | **DELETE** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Delete inference&#39;s version
*InferenceApi* | [**inference_inference_version_info**](docs/InferenceApi.md#inference_inference_version_info) | **GET** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Return inference&#39;s info for specified version
*InferenceApi* | [**inference_inference_version_start**](docs/InferenceApi.md#inference_inference_version_start) | **POST** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version}/start | Starts serving
*InferenceApi* | [**inference_inference_version_update**](docs/InferenceApi.md#inference_inference_version_update) | **PUT** /api/v0.2/workspace/{workspace}/inference/{inference}/versions/{version} | Update inference&#39;s info for specified version
*ServingApi* | [**serving_delete**](docs/ServingApi.md#serving_delete) | **DELETE** /api/v0.2/workspace/{workspace}/serving/{serving} | Delete serving
*ServingApi* | [**serving_disable**](docs/ServingApi.md#serving_disable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/disable | Disable serving
*ServingApi* | [**serving_enable**](docs/ServingApi.md#serving_enable) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/enable | Enable serving
*ServingApi* | [**serving_info**](docs/ServingApi.md#serving_info) | **GET** /api/v0.2/workspace/{workspace}/serving/{serving} | Return serving&#39;s info
*ServingApi* | [**serving_proxy**](docs/ServingApi.md#serving_proxy) | **POST** /api/v0.2/workspace/{workspace}/serving/{serving}/proxy | Proxy to serving (json data)
*ServingApi* | [**update_serving**](docs/ServingApi.md#update_serving) | **PUT** /api/v0.2/workspace/{workspace}/serving/{serving} | Update serving


## Documentation For Models

 - [DealerclientResourceLimit](docs/DealerclientResourceLimit.md)
 - [InferenceRunServingRequest](docs/InferenceRunServingRequest.md)
 - [MlappAutoscale](docs/MlappAutoscale.md)
 - [MlappDatasetFSSource](docs/MlappDatasetFSSource.md)
 - [MlappDatasetSource](docs/MlappDatasetSource.md)
 - [MlappEnv](docs/MlappEnv.md)
 - [MlappGitRepoVolumeSource](docs/MlappGitRepoVolumeSource.md)
 - [MlappImages](docs/MlappImages.md)
 - [MlappModelSource](docs/MlappModelSource.md)
 - [MlappPersistentStorage](docs/MlappPersistentStorage.md)
 - [MlappPort](docs/MlappPort.md)
 - [MlappResourceAccelerators](docs/MlappResourceAccelerators.md)
 - [MlappResourceRequest](docs/MlappResourceRequest.md)
 - [MlappS3BucketSource](docs/MlappS3BucketSource.md)
 - [MlappServing](docs/MlappServing.md)
 - [MlappServingResponseParam](docs/MlappServingResponseParam.md)
 - [MlappServingSpec](docs/MlappServingSpec.md)
 - [MlappServingSpecOptions](docs/MlappServingSpecOptions.md)
 - [MlappServingSpecParam](docs/MlappServingSpecParam.md)
 - [MlappServingSpecParamValue](docs/MlappServingSpecParamValue.md)
 - [MlappUniversalServing](docs/MlappUniversalServing.md)
 - [MlappVolume](docs/MlappVolume.md)
 - [MlappVolumeMount](docs/MlappVolumeMount.md)
 - [ModelsArbitrary](docs/ModelsArbitrary.md)
 - [ModelsInferenceVersion](docs/ModelsInferenceVersion.md)
 - [ModelsServing](docs/ModelsServing.md)
 - [ModelsTaskFormElement](docs/ModelsTaskFormElement.md)
 - [ModelsTaskFormElementStreamExtended](docs/ModelsTaskFormElementStreamExtended.md)
 - [ModelsTaskFormElementValue](docs/ModelsTaskFormElementValue.md)
 - [V1EmptyDirVolumeSource](docs/V1EmptyDirVolumeSource.md)
 - [V1FlexVolumeSource](docs/V1FlexVolumeSource.md)
 - [V1HostPathType](docs/V1HostPathType.md)
 - [V1HostPathVolumeSource](docs/V1HostPathVolumeSource.md)
 - [V1LocalObjectReference](docs/V1LocalObjectReference.md)
 - [V1NFSVolumeSource](docs/V1NFSVolumeSource.md)
 - [V1PersistentVolumeClaimVolumeSource](docs/V1PersistentVolumeClaimVolumeSource.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



