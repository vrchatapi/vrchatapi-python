# CreateInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_gate** | **bool** |  | [optional] [default to False]
**calendar_entry_id** | **str** |  | [optional] 
**can_request_invite** | **bool** | Only applies to invite type instances to make them invite+ | [optional] [default to False]
**closed_at** | **datetime** | The time after which users won&#39;t be allowed to join the instance. This doesn&#39;t work for public instances. | [optional] 
**content_settings** | [**InstanceContentSettings**](InstanceContentSettings.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] 
**hard_close** | **bool** | Currently unused, but will eventually be a flag to set if the closing of the instance should kick people. | [optional] [default to False]
**instance_persistence_enabled** | **bool** |  | [optional] 
**invite_only** | **bool** |  | [optional] [default to False]
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | [optional] 
**player_persistence_enabled** | **bool** |  | [optional] 
**queue_enabled** | **bool** |  | [optional] [default to False]
**region** | [**InstanceRegion**](InstanceRegion.md) |  | 
**role_ids** | **list[str]** | Group roleIds that are allowed to join if the type is \&quot;group\&quot; and groupAccessType is \&quot;member\&quot; | [optional] 
**type** | [**InstanceType**](InstanceType.md) |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


