# Instance

* `hidden` field is only present if InstanceType is `hidden` aka \"Friends+\", and is instance creator. * `friends` field is only present if InstanceType is `friends` aka \"Friends\", and is instance creator. * `private` field is only present if InstanceType is `private` aka \"Invite\" or \"Invite+\", and is instance creator.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] [default to True]
**age_gate** | **bool** |  | [optional] 
**calendar_entry_id** | **str** |  | [optional] 
**can_request_invite** | **bool** |  | [optional] [default to True]
**capacity** | **int** |  | [optional] 
**client_number** | **str** | Always returns \&quot;unknown\&quot;. | 
**closed_at** | **datetime** |  | [optional] 
**content_settings** | [**InstanceContentSettings**](InstanceContentSettings.md) |  | [optional] 
**creator_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**display_name** | **str** |  | [optional] 
**friends** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**full** | **bool** |  | [default to False]
**game_server_version** | **int** |  | [optional] 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] 
**hard_close** | **bool** |  | [optional] 
**has_capacity_for_you** | **bool** |  | [optional] 
**hidden** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**instance_persistence_enabled** | **bool** |  | [optional] 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**n_users** | **int** |  | 
**name** | **str** |  | 
**nonce** | **str** |  | [optional] 
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | [optional] 
**permanent** | **bool** |  | [default to False]
**photon_region** | [**Region**](Region.md) |  | 
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**player_persistence_enabled** | **bool** |  | [optional] 
**private** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**queue_enabled** | **bool** |  | 
**queue_size** | **int** |  | 
**recommended_capacity** | **int** |  | 
**region** | [**InstanceRegion**](InstanceRegion.md) |  | 
**role_restricted** | **bool** |  | [optional] 
**secure_name** | **str** |  | 
**short_name** | **str** |  | [optional] 
**strict** | **bool** |  | 
**tags** | **list[str]** | The tags array on Instances usually contain the language tags of the people in the instance.  | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**user_count** | **int** |  | 
**users** | [**list[LimitedUserInstance]**](LimitedUserInstance.md) | The users field is present on instances created by the requesting user. | [optional] 
**world** | [**World**](World.md) |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


