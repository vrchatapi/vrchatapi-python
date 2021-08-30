# CurrentUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**username** | **str** |  | 
**display_name** | **str** |  | 
**user_icon** | **str** |  | 
**bio** | **str** |  | 
**bio_links** | **[str]** |  | 
**profile_pic_override** | **str** |  | 
**status_description** | **str** |  | 
**past_display_names** | [**[PastDisplayName]**](PastDisplayName.md) |  | 
**has_email** | **bool** |  | 
**has_pending_email** | **bool** |  | 
**obfuscated_email** | **str** |  | 
**obfuscated_pending_email** | **str** |  | 
**email_verified** | **bool** |  | 
**has_birthday** | **bool** |  | 
**unsubscribe** | **bool** |  | 
**status_history** | **[str]** |  | 
**status_first_time** | **bool** |  | 
**friends** | **[str]** |  | 
**friend_group_names** | **[str]** | Always empty array. | 
**current_avatar_image_url** | **str** |  | 
**current_avatar_thumbnail_image_url** | **str** |  | 
**fallback_avatar** | [**AvatarID**](AvatarID.md) |  | 
**current_avatar** | [**AvatarID**](AvatarID.md) |  | 
**current_avatar_asset_url** | **str** |  | 
**accepted_tos_version** | **float** |  | 
**steam_id** | **str** |  | 
**steam_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**oculus_id** | **str** |  | 
**has_logged_in_from_client** | **bool** |  | 
**home_location** | [**WorldID**](WorldID.md) |  | 
**two_factor_auth_enabled** | **bool** |  | 
**state** | [**UserState**](UserState.md) |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**last_login** | **datetime** |  | 
**last_platform** | [**Platform**](Platform.md) |  | 
**allow_avatar_copying** | **bool** |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**date_joined** | **date** |  | [readonly] 
**friend_key** | **str** |  | 
**is_friend** | **bool** |  | defaults to False
**account_deletion_date** | **date, none_type** |  | [optional] 
**online_friends** | **[str]** |  | [optional] 
**active_friends** | **[str]** |  | [optional] 
**offline_friends** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


