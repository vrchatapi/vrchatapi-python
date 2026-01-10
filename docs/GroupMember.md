# GroupMember

May be null when attempting to retrieve group membership for a user who is not part of the group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_by_display_name** | **str** | Only missing when explicitly fetching own user. | [optional] 
**accepted_by_id** | **str** | Only missing when explicitly fetching own user. | [optional] 
**banned_at** | **datetime** | Only missing when explicitly fetching own user. | [optional] 
**created_at** | **datetime** | Only missing when explicitly fetching own user. | [optional] 
**group_id** | **str** |  | 
**has_joined_from_purchase** | **bool** | Missing when explicitly fetching own user, or when group isn&#39;t linked to a purchase. | [optional] 
**id** | **str** |  | 
**is_representing** | **bool** | Whether the user is representing the group. This makes the group show up above the name tag in-game. | [default to False]
**is_subscribed_to_announcements** | **bool** |  | [default to False]
**is_subscribed_to_event_announcements** | **bool** | Only missing when explicitly fetching own user. | [optional] 
**joined_at** | **datetime** |  | 
**last_post_read_at** | **datetime** |  | 
**m_role_ids** | **list[str]** |  | 
**manager_notes** | **str** | Only missing when explicitly fetching own user. | [optional] 
**membership_status** | [**GroupMemberStatus**](GroupMemberStatus.md) |  | 
**role_ids** | **list[str]** |  | 
**user** | [**GroupMemberLimitedUser**](GroupMemberLimitedUser.md) |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**visibility** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


