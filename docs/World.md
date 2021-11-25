# World


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | 
**asset_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**capacity** | **int** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | [**WorldID**](WorldID.md) |  | 
**image_url** | **str** |  | 
**labs_publication_date** | **str** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**plugin_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**publication_date** | **str** |  | 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**unity_packages** | [**[UnityPackage]**](UnityPackage.md) |  | 
**updated_at** | **datetime** |  | 
**featured** | **bool** |  | defaults to False
**heat** | **int** |  | defaults to 0
**organization** | **str** |  | defaults to "vrchat"
**popularity** | **int** |  | defaults to 0
**version** | **int** |  | defaults to 0
**visits** | **int** |  | defaults to 0
**favorites** | **int** |  | [optional]  if omitted the server will use the default value of 0
**instances** | **[[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]]** |  | [optional] 
**occupants** | **int** |  | [optional]  if omitted the server will use the default value of 0
**preview_youtube_id** | **str** |  | [optional] 
**private_occupants** | **int** |  | [optional]  if omitted the server will use the default value of 0
**public_occupants** | **int** |  | [optional]  if omitted the server will use the default value of 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


