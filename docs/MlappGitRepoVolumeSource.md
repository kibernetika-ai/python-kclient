# MlappGitRepoVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** |  | [optional] 
**repository** | **str** | Repository URL | 
**access_token** | **str** |  | [optional] 
**directory** | **str** | Target directory name. Must not contain or start with &#39;..&#39;.  If &#39;.&#39; is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name. | [optional] 
**account_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**revision** | **str** | Commit hash for the specified revision. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


