# GroupLimitedMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**is_representing** | **bool** | Whether the user is representing the group. This makes the group show up above the name tag in-game. | [optional] [default to False]
**role_ids** | **list[str]** |  | [optional] 
**m_role_ids** | **list[str]** |  | [optional] 
**joined_at** | **datetime** |  | [optional] 
**membership_status** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**is_subscribed_to_announcements** | **bool** |  | [optional] [default to False]
**created_at** | **datetime** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**banned_at** | **datetime** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**manager_notes** | **str** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**last_post_read_at** | **datetime** |  | [optional] 
**has_joined_from_purchase** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


