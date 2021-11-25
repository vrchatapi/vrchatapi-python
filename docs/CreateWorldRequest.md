# CreateWorldRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | 
**image_url** | **str** |  | 
**name** | **str** |  | 
**asset_version** | **int** |  | [optional] 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**author_name** | **str** |  | [optional] 
**capacity** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | [**WorldID**](WorldID.md) |  | [optional] 
**platform** | **str** | This can be &#x60;standalonewindows&#x60; or &#x60;android&#x60;, but can also pretty much be any random Unity verison such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) |  | [optional] 
**unity_package_url** | **str** |  | [optional] 
**unity_version** | **str** |  | [optional]  if omitted the server will use the default value of "5.3.4p1"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


