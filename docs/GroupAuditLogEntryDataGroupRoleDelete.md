# GroupAuditLogEntryDataGroupRoleDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The creation timestamp of the role. | 
**default_role** | **bool** | Whether the role is the group&#39;s default role. | 
**is_management_role** | **bool** | Whether the role is a management role. | 
**description** | **str** | The role description. | 
**is_added_on_join** | **bool** | Whether the role is automatically assigned on join. | 
**is_self_assignable** | **bool** | Whether users can self-assign this role. | 
**name** | **str** | The role name. | 
**order** | **int** | The display order of the role. | 
**permissions** | [**list[GroupPermissions]**](GroupPermissions.md) | The permissions assigned to this role. | 
**requires_purchase** | **bool** | Whether the role requires a purchase. | 
**requires_two_factor** | **bool** | Whether the role requires two-factor authentication. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


