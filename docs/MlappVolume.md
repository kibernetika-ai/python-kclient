# MlappVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_fs** | [**MlappDatasetFSSource**](MlappDatasetFSSource.md) |  | [optional] 
**is_train_log_dir** | **bool** |  | [optional] 
**cluster_storage** | **str** |  | [optional] 
**name** | **str** |  | 
**mount_path** | **str** |  | [optional] 
**is_workspace_local** | **bool** |  | [optional] 
**is_lib_dir** | **bool** |  | [optional] 
**sub_path** | **str** |  | [optional] 
**dataset** | [**MlappDatasetSource**](MlappDatasetSource.md) |  | [optional] 
**s3bucket** | [**MlappS3BucketSource**](MlappS3BucketSource.md) |  | [optional] 
**read_only** | **bool** |  | [optional] 
**git_repo** | [**MlappGitRepoVolumeSource**](MlappGitRepoVolumeSource.md) |  | [optional] 
**nfs** | [**V1NFSVolumeSource**](V1NFSVolumeSource.md) |  | [optional] 
**host_path** | [**V1HostPathVolumeSource**](V1HostPathVolumeSource.md) |  | [optional] 
**empty_dir** | [**V1EmptyDirVolumeSource**](V1EmptyDirVolumeSource.md) |  | [optional] 
**flex_volume** | [**V1FlexVolumeSource**](V1FlexVolumeSource.md) |  | [optional] 
**model** | [**MlappModelSource**](MlappModelSource.md) |  | [optional] 
**persistent_storage** | [**MlappPersistentStorage**](MlappPersistentStorage.md) |  | [optional] 
**persistent_volume_claim** | [**V1PersistentVolumeClaimVolumeSource**](V1PersistentVolumeClaimVolumeSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


