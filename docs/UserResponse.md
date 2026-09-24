# UserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_privacy_version** | **int** |  | [optional] 
**accepted_tos_version** | **int** |  | [optional] 
**account_deletion_date** | **str** |  | [optional] 
**account_deletion_log** | **list[object]** |  | [optional] 
**age_verification_status** | [**AgeVerificationStatus**](AgeVerificationStatus.md) |  | 
**age_verified** | **bool** | &#x60;true&#x60; if, user is age verified (not 18+). | 
**allow_avatar_copying** | **bool** |  | 
**apple_details** | **object** | Details of an account on another service linked to this one. | [optional] 
**banner_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**banner_type** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**date_joined** | **date** |  | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**display_name** | **str** |  | 
**friend_key** | **str** |  | 
**friend_request_status** | **str** | State of a friend request between the caller and this user. VRChat sends the string &#x60;\&quot;null\&quot;&#x60;, not JSON &#x60;null&#x60;. | [optional] 
**icon_frame** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | [optional] 
**is_economy_creator** | **bool** |  | [optional] 
**is_friend** | **bool** |  | 
**last_activity** | **str** |  | [optional] 
**last_login** | **str** |  | 
**last_mobile** | **str** |  | [optional] 
**last_platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | [optional] 
**nameplate_effect** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**profile_effect** | **str** |  | [optional] 
**pronouns** | **str** |  | 
**state** | [**UserState**](UserState.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**status_description** | **str** |  | 
**tags** | **list[str]** |  | 
**traveling_to_instance** | **str** |  | [optional] 
**traveling_to_location** | **str** |  | [optional] 
**traveling_to_world** | **str** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 
**active_friends** | **list[str]** |  | [optional] 
**apple_id** | **str** |  | [optional] 
**auth_token** | **str** | The auth token for NEWLY REGISTERED ACCOUNTS ONLY (/auth/register) | [optional] 
**completed_tutorials** | **list[str]** |  | [optional] 
**content_filters** | **list[str]** | These tags begin with &#x60;content_&#x60; and control content gating | [optional] 
**current_avatar** | **str** |  | [optional] 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**current_avatar_tags** | **list[str]** |  | [optional] 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**discord_details** | [**DiscordDetails**](DiscordDetails.md) |  | [optional] 
**discord_id** | **str** | https://discord.com/developers/docs/reference#snowflakes | [optional] 
**email_verified** | **bool** |  | [optional] 
**fallback_avatar** | **str** |  | [optional] 
**friend_group_names** | **list[str]** | Always empty array. | [optional] 
**friends** | **list[str]** |  | [optional] 
**google_details** | **object** | Details of an account on another service linked to this one. | [optional] 
**google_id** | **str** |  | [optional] 
**has_birthday** | **bool** |  | [optional] 
**has_discord_friends_opt_out** | **bool** |  | [optional] 
**has_email** | **bool** |  | [optional] 
**has_logged_in_from_client** | **bool** |  | [optional] 
**has_pending_email** | **bool** |  | [optional] 
**has_shared_connections_opt_out** | **bool** |  | [optional] 
**hide_content_filter_settings** | **bool** |  | [optional] 
**home_location** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 
**is_adult** | **bool** |  | [optional] 
**is_booping_enabled** | **bool** |  | [optional] [default to True]
**is_temporary** | **bool** |  | [optional] [default to False]
**obfuscated_email** | **str** |  | [optional] 
**obfuscated_pending_email** | **str** |  | [optional] 
**oculus_id** | **str** |  | [optional] 
**offline_friends** | **list[str]** |  | [optional] 
**online_friends** | **list[str]** |  | [optional] 
**past_display_names** | [**list[PastDisplayName]**](PastDisplayName.md) |  | [optional] 
**personalization_opt_out** | **bool** |  | [optional] 
**pico_id** | **str** |  | [optional] 
**platform_history** | [**list[PlatformHistoryEntry]**](PlatformHistoryEntry.md) |  | [optional] 
**presence** | [**CurrentUserPresence**](CurrentUserPresence.md) |  | [optional] 
**pronouns_history** | **list[str]** |  | [optional] 
**queued_instance** | **str** |  | [optional] 
**receive_mobile_invitations** | **bool** |  | [optional] 
**status_first_time** | **bool** |  | [optional] 
**status_history** | **list[str]** |  | [optional] 
**steam_details** | **object** | Details of an account on another service linked to this one. | [optional] 
**steam_id** | **str** |  | [optional] 
**temporary_expiry_date** | **object** | An unknown value. Consider [contributing](https://vrchat.community/contributing). | [optional] 
**twitch_details** | **object** | Details of an account on another service linked to this one. | [optional] 
**twitch_id** | **str** |  | [optional] 
**two_factor_auth_enabled** | **bool** |  | [optional] 
**two_factor_auth_enabled_date** | **datetime** |  | [optional] 
**unsubscribe** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_language** | **str** |  | [optional] 
**user_language_code** | **str** |  | [optional] 
**username** | **str** | Your own unique name, used during login. Distinct from &#x60;displayName&#x60;, and never returned for another user. | [optional] 
**uses_generated_password** | **bool** |  | [optional] 
**vive_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


