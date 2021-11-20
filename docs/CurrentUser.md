# CurrentUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_tos_version** | **int** |  | 
**allow_avatar_copying** | **bool** |  | 
**bio** | **str** |  | 
**bio_links** | **[str]** |  | 
**current_avatar** | [**AvatarID**](AvatarID.md) |  | 
**current_avatar_asset_url** | **str** |  | 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**date_joined** | **date** |  | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**display_name** | **str** |  | 
**email_verified** | **bool** |  | 
**friend_group_names** | **[str]** | Always empty array. | 
**friend_key** | **str** |  | 
**friends** | **[str]** |  | 
**has_birthday** | **bool** |  | 
**has_email** | **bool** |  | 
**has_logged_in_from_client** | **bool** |  | 
**has_pending_email** | **bool** |  | 
**home_location** | [**WorldID**](WorldID.md) |  | 
**id** | **str** |  | 
**last_login** | **datetime** |  | 
**last_platform** | **str** | This can be &#x60;standalonewindows&#x60; or &#x60;android&#x60;, but can also pretty much be any random Unity verison such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**obfuscated_email** | **str** |  | 
**obfuscated_pending_email** | **str** |  | 
**oculus_id** | **str** |  | 
**past_display_names** | [**[PastDisplayName]**](PastDisplayName.md) |  | 
**profile_pic_override** | **str** |  | 
**state** | [**UserState**](UserState.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**status_description** | **str** |  | 
**status_first_time** | **bool** |  | 
**status_history** | **[str]** |  | 
**steam_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**steam_id** | **str** |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**two_factor_auth_enabled** | **bool** |  | 
**unsubscribe** | **bool** |  | 
**user_icon** | **str** |  | 
**username** | **str** |  | 
**is_friend** | **bool** |  | defaults to False
**account_deletion_date** | **date, none_type** |  | [optional] 
**active_friends** | **[str]** |  | [optional] 
**fallback_avatar** | [**AvatarID**](AvatarID.md) |  | [optional] 
**offline_friends** | **[str]** |  | [optional] 
**online_friends** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


