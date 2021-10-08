# Instance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** |  | 
**client_number** | **str** |  | 
**id** | [**InstanceID**](InstanceID.md) |  | 
**instance_id** | **str** |  | 
**location** | **str** |  | 
**n_users** | **int** |  | 
**name** | **str** |  | 
**photon_region** | **str** |  | 
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**region** | **str** |  | 
**short_name** | **str** |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**type** | **str** |  | 
**world_id** | [**WorldID**](WorldID.md) |  | 
**active** | **bool** |  | defaults to True
**can_request_invite** | **bool** |  | defaults to True
**full** | **bool** |  | defaults to False
**permanent** | **bool** |  | defaults to False
**nonce** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**users** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** | Always empty on non-existing instances, and non-present on existing instances. | [optional] 
**world** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Only present on non-existing instances, and only contains a very small subject of World object. Use World API instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


