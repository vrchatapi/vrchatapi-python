# GroupLimitedMember

May be null when attempting to retrieve group membership for a user who is not part of the group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banned_at** | **datetime** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**created_at** | **datetime** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**group_id** | **str** |  | [optional] 
**has_joined_from_purchase** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**is_representing** | **bool** | Whether the user is representing the group. This makes the group show up above the name tag in-game. | [optional] [default to False]
**is_subscribed_to_announcements** | **bool** |  | [optional] [default to False]
**is_subscribed_to_event_announcements** | **bool** |  | [optional] 
**joined_at** | **datetime** |  | [optional] 
**last_post_read_at** | **datetime** |  | [optional] 
**m_role_ids** | **list[str]** |  | [optional] 
**manager_notes** | **str** | Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user. | [optional] 
**membership_status** | [**GroupMemberStatus**](GroupMemberStatus.md) |  | [optional] 
**role_ids** | **list[str]** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**visibility** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


