# Instance

* `hidden` field is only present if InstanceType is `hidden` aka \"Friends+\", and is instance creator. * `friends` field is only present if InstanceType is `friends` aka \"Friends\", and is instance creator. * `private` field is only present if InstanceType is `private` aka \"Invite\" or \"Invite+\", and is instance creator.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [default to True]
**can_request_invite** | **bool** |  | [default to True]
**capacity** | **int** |  | 
**client_number** | **str** | Always returns \&quot;unknown\&quot;. | 
**full** | **bool** |  | [default to False]
**id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**instance_id** | **str** |  | 
**location** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**n_users** | **int** |  | 
**name** | **str** |  | 
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | [optional] 
**permanent** | **bool** |  | [default to False]
**photon_region** | [**Region**](Region.md) |  | 
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**region** | [**Region**](Region.md) |  | 
**secure_name** | **str** |  | 
**short_name** | **str** |  | [optional] 
**tags** | **list[str]** | The tags array on Instances usually contain the language tags of the people in the instance.  | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**hidden** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**friends** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**private** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**queue_enabled** | **bool** |  | 
**queue_size** | **int** |  | 
**recommended_capacity** | **int** |  | 
**role_restricted** | **bool** |  | [optional] 
**strict** | **bool** |  | 
**user_count** | **int** |  | 
**world** | [**World**](World.md) |  | 
**users** | [**list[LimitedUser]**](LimitedUser.md) | The users field is present on instances created by the requesting user. | [optional] 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] 
**has_capacity_for_you** | **bool** |  | [optional] 
**nonce** | **str** |  | [optional] 
**closed_at** | **datetime** |  | [optional] 
**hard_close** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


