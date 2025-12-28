# CurrentUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_privacy_version** | **int** |  | [optional] 
**accepted_tos_version** | **int** |  | 
**account_deletion_date** | **date** |  | [optional] 
**account_deletion_log** | [**list[AccountDeletionLog]**](AccountDeletionLog.md) |   | [optional] 
**active_friends** | **list[str]** |   | [optional] 
**age_verification_status** | [**AgeVerificationStatus**](AgeVerificationStatus.md) |  | 
**age_verified** | **bool** | &#x60;true&#x60; if, user is age verified (not 18+). | 
**allow_avatar_copying** | **bool** |  | 
**auth_token** | **str** | The auth token for NEWLY REGISTERED ACCOUNTS ONLY (/auth/register) | [optional] 
**badges** | [**list[Badge]**](Badge.md) |   | [optional] 
**bio** | **str** |  | 
**bio_links** | **list[str]** |   | 
**content_filters** | **list[str]** | These tags begin with &#x60;content_&#x60; and control content gating | [optional] 
**current_avatar** | **str** |  | 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_tags** | **list[str]** |  | 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**date_joined** | **date** |  | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**discord_details** | [**DiscordDetails**](DiscordDetails.md) |  | [optional] 
**discord_id** | **str** | https://discord.com/developers/docs/reference#snowflakes | [optional] 
**display_name** | **str** |  | 
**email_verified** | **bool** |  | 
**fallback_avatar** | **str** |  | [optional] 
**friend_group_names** | **list[str]** | Always empty array. | 
**friend_key** | **str** |  | 
**friends** | **list[str]** |  | 
**google_details** | **object** |  | [optional] 
**google_id** | **str** |  | [optional] 
**has_birthday** | **bool** |  | 
**has_email** | **bool** |  | 
**has_logged_in_from_client** | **bool** |  | 
**has_pending_email** | **bool** |  | 
**hide_content_filter_settings** | **bool** |  | [optional] 
**home_location** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**is_adult** | **bool** |  | 
**is_booping_enabled** | **bool** |  | [optional] [default to True]
**is_friend** | **bool** |  | [default to False]
**last_activity** | **datetime** |  | [optional] 
**last_login** | **datetime** |  | 
**last_mobile** | **datetime** |  | 
**last_platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**obfuscated_email** | **str** |  | 
**obfuscated_pending_email** | **str** |  | 
**oculus_id** | **str** |  | 
**offline_friends** | **list[str]** |  | [optional] 
**online_friends** | **list[str]** |  | [optional] 
**past_display_names** | [**list[PastDisplayName]**](PastDisplayName.md) |   | 
**pico_id** | **str** |  | [optional] 
**platform_history** | [**list[CurrentUserPlatformHistoryInner]**](CurrentUserPlatformHistoryInner.md) |  | [optional] 
**presence** | [**CurrentUserPresence**](CurrentUserPresence.md) |  | [optional] 
**profile_pic_override** | **str** |  | 
**profile_pic_override_thumbnail** | **str** |  | 
**pronouns** | **str** |  | 
**pronouns_history** | **list[str]** |  | 
**queued_instance** | **str** |  | [optional] 
**receive_mobile_invitations** | **bool** |  | [optional] 
**state** | [**UserState**](UserState.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**status_description** | **str** |  | 
**status_first_time** | **bool** |  | 
**status_history** | **list[str]** |  | 
**steam_details** | **object** |  | 
**steam_id** | **str** |  | 
**tags** | **list[str]** |  | 
**two_factor_auth_enabled** | **bool** |  | 
**two_factor_auth_enabled_date** | **datetime** |  | [optional] 
**unsubscribe** | **bool** |  | 
**updated_at** | **datetime** |  | [optional] 
**user_icon** | **str** |  | 
**user_language** | **str** |  | [optional] 
**user_language_code** | **str** |  | [optional] 
**username** | **str** | -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429). | [optional] 
**uses_generated_password** | **bool** |  | 
**vive_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


