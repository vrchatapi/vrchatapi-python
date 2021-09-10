# World


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | 
**asset_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**author_id** | **str** |  | 
**author_name** | **str** |  | [readonly] 
**capacity** | **float** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**description** | **str** |  | 
**id** | [**WorldID**](WorldID.md) |  | 
**image_url** | **str** |  | 
**labs_publication_date** | **str** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**plugin_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**publication_date** | **datetime** |  | 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**unity_packages** | [**[UnityPackage]**](UnityPackage.md) |  | 
**updated_at** | **datetime** |  | 
**featured** | **bool** |  | defaults to False
**heat** | **float** |  | [readonly] defaults to 0
**organization** | **str** |  | defaults to "vrchat"
**popularity** | **float** |  | [readonly] defaults to 0
**version** | **float** |  | defaults to 0
**visits** | **float** |  | [readonly] defaults to 0
**favorites** | **float** |  | [optional] [readonly]  if omitted the server will use the default value of 0
**instances** | **[[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]]** |  | [optional] 
**occupants** | **float** |  | [optional] [readonly]  if omitted the server will use the default value of 0
**preview_youtube_id** | **str** |  | [optional] 
**private_occupants** | **float** |  | [optional] [readonly]  if omitted the server will use the default value of 0
**public_occupants** | **float** |  | [optional] [readonly]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


