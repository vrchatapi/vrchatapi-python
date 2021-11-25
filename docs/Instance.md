# Instance

* `hidden` field is only present if InstanceType is `hidden` aka \"Friends+\", and is instance creator. * `friends` field is only present if InstanceType is `friends` aka \"Friends\", and is instance creator. * `private` field is only present if InstanceType is `private` aka \"Invite\" or \"Invite+\", and is instance creator.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** |  | 
**client_number** | **str** | Always returns \&quot;unknown\&quot;. | 
**id** | [**InstanceID**](InstanceID.md) |  | 
**instance_id** | **str** |  | 
**location** | [**InstanceID**](InstanceID.md) |  | 
**n_users** | **int** |  | 
**name** | **str** |  | 
**photon_region** | [**Region**](Region.md) |  | 
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**region** | [**Region**](Region.md) |  | 
**short_name** | **str** |  | 
**tags** | [**[Tag]**](Tag.md) | The tags array on Instances usually contain the language tags of the people in the instance.  | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**world_id** | [**WorldID**](WorldID.md) |  | 
**active** | **bool** |  | defaults to True
**can_request_invite** | **bool** |  | defaults to True
**full** | **bool** |  | defaults to False
**permanent** | **bool** |  | defaults to False
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**hidden** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**friends** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**private** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


