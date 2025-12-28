# Group


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_verification_beta_code** | **str** |  | [optional] 
**age_verification_beta_slots** | **float** |  | [optional] 
**age_verification_slots_available** | **bool** |  | [optional] 
**allow_group_join_prompt** | **bool** |  | [optional] 
**badges** | **list[str]** |  | [optional] 
**banner_id** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**discriminator** | **str** |  | [optional] 
**galleries** | [**list[GroupGallery]**](GroupGallery.md) |  | [optional] 
**icon_id** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_verified** | **bool** |  | [optional] [default to False]
**join_state** | [**GroupJoinState**](GroupJoinState.md) |  | [optional] 
**languages** | **list[str]** |  | [optional] 
**last_post_created_at** | **datetime** |  | [optional] 
**links** | **list[str]** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_count_synced_at** | **datetime** |  | [optional] 
**membership_status** | [**GroupMemberStatus**](GroupMemberStatus.md) |  | [optional] 
**my_member** | [**GroupMyMember**](GroupMyMember.md) |  | [optional] 
**name** | **str** |  | [optional] 
**online_member_count** | **int** |  | [optional] 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**privacy** | [**GroupPrivacy**](GroupPrivacy.md) |  | [optional] 
**roles** | [**list[GroupRole]**](GroupRole.md) | Only returned if ?includeRoles&#x3D;true is specified. | [optional] 
**rules** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**transfer_target_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**updated_at** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


