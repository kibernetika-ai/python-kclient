# MlappVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_storage** | **str** |  | [optional] 
**dataset** | [**MlappDatasetSource**](MlappDatasetSource.md) |  | [optional] 
**dataset_fs** | [**MlappDatasetFSSource**](MlappDatasetFSSource.md) |  | [optional] 
**empty_dir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) |  | [optional] 
**flex_volume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) |  | [optional] 
**git_repo** | [**MlappGitRepoVolumeSource**](MlappGitRepoVolumeSource.md) |  | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) |  | [optional] 
**is_lib_dir** | **bool** |  | [optional] 
**is_train_log_dir** | **bool** |  | [optional] 
**is_workspace_local** | **bool** |  | [optional] 
**model** | [**MlappModelSource**](MlappModelSource.md) |  | [optional] 
**mount_path** | **str** |  | [optional] 
**name** | **str** |  | 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) |  | [optional] 
**persistent_storage** | [**MlappPersistentStorage**](MlappPersistentStorage.md) |  | [optional] 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) |  | [optional] 
**read_only** | **bool** |  | [optional] 
**s3bucket** | [**MlappS3BucketSource**](MlappS3BucketSource.md) |  | [optional] 
**sub_path** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


