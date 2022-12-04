# Group


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 
**discriminator** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**privacy** | [**GroupPrivacy**](GroupPrivacy.md) |  | [optional] 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**rules** | **str** |  | [optional] 
**links** | **list[str]** |  | [optional] 
**languages** | **list[str]** |  | [optional] 
**icon_id** | **str** |  | [optional] 
**banner_id** | **str** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_count_synced_at** | **datetime** |  | [optional] 
**is_verified** | **bool** |  | [optional] [default to False]
**join_state** | [**GroupJoinState**](GroupJoinState.md) |  | [optional] 
**tags** | **list[str]** |   | [optional] 
**galleries** | [**list[GroupGallery]**](GroupGallery.md) |   | [optional] 
**created_at** | **datetime** |  | [optional] 
**online_member_count** | **int** |  | [optional] 
**membership_status** | [**GroupMemberStatus**](GroupMemberStatus.md) |  | [optional] 
**my_member** | [**GroupMyMember**](GroupMyMember.md) |  | [optional] 
**roles** | [**list[GroupRole]**](GroupRole.md) | Only returned if ?includeRoles&#x3D;true is specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


