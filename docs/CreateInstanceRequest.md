# CreateInstanceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**region** | [**Region**](Region.md) |  | 
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | [optional] 
**role_ids** | **list[str]** | Group roleIds that are allowed to join if the type is \&quot;group\&quot; and groupAccessType is \&quot;member\&quot; | [optional] 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] 
**queue_enabled** | **bool** |  | [optional] [default to False]
**closed_at** | **datetime** | The time after which users won&#39;t be allowed to join the instance | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


