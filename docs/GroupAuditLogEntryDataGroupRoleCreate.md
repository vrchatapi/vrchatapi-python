# GroupAuditLogEntryDataGroupRoleCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**last_updated_by_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**description** | **str** | The role description. | 
**is_added_on_join** | **bool** | Whether the role is automatically assigned on join. | 
**is_self_assignable** | **bool** | Whether users can self-assign this role. | 
**name** | **str** | The role name. | 
**order** | **int** | The display order of the role. | [optional] 
**permissions** | [**list[GroupPermissions]**](GroupPermissions.md) | The permissions assigned to this role. | 
**requires_purchase** | **bool** | Whether the role requires a purchase. | 
**requires_two_factor** | **bool** | Whether the role requires two-factor authentication. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


