# APIConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | VRChat&#39;s office address | 
**announcements** | [**[PublicAnnouncement]**](PublicAnnouncement.md) | Public Announcements | 
**api_key** | **str** | apiKey to be used for all other requests | 
**build_version_tag** | **str** | Build tag of the API server | 
**client_api_key** | **str** | apiKey to be used for all other requests | 
**contact_email** | **str** | VRChat&#39;s contact email | 
**copyright_email** | **str** | VRChat&#39;s copyright-issues-related email | 
**current_tos_version** | **int** | Current version number of the Terms of Service | 
**default_avatar** | [**AvatarID**](AvatarID.md) |  | 
**deployment_group** | [**DeploymentGroup**](DeploymentGroup.md) |  | 
**dev_app_version_standalone** | **str** | Version number for game development build | 
**dev_download_link_windows** | **str** | Developer Download link | 
**dev_sdk_url** | **str** | Link to download the development SDK, use downloadUrls instead | 
**dev_sdk_version** | **str** | Version of the development SDK | 
**dev_server_version_standalone** | **str** | Version number for server development build | 
**dis_countdown** | **datetime** | Unknown, \&quot;dis\&quot; maybe for disconnect? | 
**download_link_windows** | **str** | Download link for game on the Oculus Rift website. | 
**download_urls** | [**DownloadURLList**](DownloadURLList.md) |  | 
**dynamic_world_rows** | [**[DynamicContentRow]**](DynamicContentRow.md) | Array of DynamicWorldRow objects, used by the game to display the list of world rows | 
**events** | [**APIEventConfig**](APIEventConfig.md) |  | 
**gear_demo_room_id** | **str** | Unknown | 
**home_world_id** | [**WorldID**](WorldID.md) |  | 
**hub_world_id** | [**WorldID**](WorldID.md) |  | 
**jobs_email** | **str** | VRChat&#39;s job application email | 
**message_of_the_day** | **str** | MOTD | 
**moderation_email** | **str** | VRChat&#39;s moderation related email | 
**moderation_query_period** | **int** | Unknown | 
**not_allowed_to_select_avatar_in_private_world_message** | **str** | Used in-game to notify a user they aren&#39;t allowed to select avatars in private worlds | 
**plugin** | **str** | Extra [plugin](https://doc.photonengine.com/en-us/server/current/plugins/manual) to run in each instance | 
**release_app_version_standalone** | **str** | Version number for game release build | 
**release_sdk_url** | **str** | Link to download the release SDK | 
**release_sdk_version** | **str** | Version of the release SDK | 
**release_server_version_standalone** | **str** | Version number for server release build | 
**sdk_developer_faq_url** | **str** | Link to the developer FAQ | 
**sdk_discord_url** | **str** | Link to the official VRChat Discord | 
**sdk_not_allowed_to_publish_message** | **str** | Used in the SDK to notify a user they aren&#39;t allowed to upload avatars/worlds yet | 
**sdk_unity_version** | **str** | Unity version supported by the SDK | 
**server_name** | **str** | Server name of the API server currently responding | 
**support_email** | **str** | VRChat&#39;s support email | 
**time_out_world_id** | [**WorldID**](WorldID.md) |  | 
**tutorial_world_id** | [**WorldID**](WorldID.md) |  | 
**update_rate_ms_maximum** | **int** | Unknown | 
**update_rate_ms_minimum** | **int** | Unknown | 
**update_rate_ms_normal** | **int** | Unknown | 
**update_rate_ms_udon_manual** | **int** | Unknown | 
**upload_analysis_percent** | **int** | Unknown | 
**url_list** | **[str]** | List of allowed URLs that bypass the \&quot;Allow untrusted URL&#39;s\&quot; setting in-game | 
**user_update_period** | **int** | Unknown | 
**user_verification_delay** | **int** | Unknown | 
**user_verification_retry** | **int** | Unknown | 
**user_verification_timeout** | **int** | Unknown | 
**vive_windows_url** | **str** | Download link for game on the Steam website. | 
**white_listed_asset_urls** | **[str]** | List of allowed URLs that are allowed to host avatar assets | 
**world_update_period** | **int** | Unknown | 
**player_url_resolver_hash** | **str** | Currently used youtube-dl.exe hash in SHA-256-delimited format | 
**player_url_resolver_version** | **str** | Currently used youtube-dl.exe version | 
**voice_enable_degradation** | **bool** | Unknown, probably voice optimization testing | defaults to False
**voice_enable_receiver_limiting** | **bool** | Unknown, probably voice optimization testing | defaults to True
**app_name** | **str** | Game name | defaults to "VrChat"
**client_bps_ceiling** | **int** | Unknown | defaults to 18432
**client_disconnect_timeout** | **int** | Unknown | defaults to 30000
**client_reserved_player_bps** | **int** | Unknown | defaults to 7168
**client_sent_count_allowance** | **int** | Unknown | defaults to 15
**disable_avatar_copying** | **bool** | Toggles if copying avatars should be disabled | defaults to False
**disable_avatar_gating** | **bool** | Toggles if avatar gating should be disabled. Avatar gating restricts uploading of avatars to people with the &#x60;system_avatar_access&#x60; Tag or &#x60;admin_avatar_access&#x60; Tag | defaults to False
**disable_community_labs** | **bool** | Toggles if the Community Labs should be disabled | defaults to False
**disable_community_labs_promotion** | **bool** | Toggles if promotion out of Community Labs should be disabled | defaults to False
**disable_email** | **bool** | Unknown | defaults to False
**disable_event_stream** | **bool** | Toggles if Analytics should be disabled. | defaults to False
**disable_feedback_gating** | **bool** | Toggles if feedback gating should be disabled. Feedback gating restricts submission of feedback (reporting a World or User) to people with the &#x60;system_feedback_access&#x60; Tag. | defaults to False
**disable_frontend_builds** | **bool** | Unknown, probably toggles compilation of frontend web builds? So internal flag? | defaults to False
**disable_hello** | **bool** | Unknown | defaults to False
**disable_oculus_subs** | **bool** | Toggles if signing up for Subscriptions in Oculus is disabled or not. | defaults to False
**disable_registration** | **bool** | Toggles if new user account registration should be disabled. | defaults to False
**disable_steam_networking** | **bool** | Toggles if Steam Networking should be disabled. VRChat these days uses Photon Unity Networking (PUN) instead. | defaults to True
**disable_two_factor_auth** | **bool** | Toggles if 2FA should be disabled. | defaults to False
**disable_udon** | **bool** | Toggles if Udon should be universally disabled in-game. | defaults to False
**disable_upgrade_account** | **bool** | Toggles if account upgrading \&quot;linking with Steam/Oculus\&quot; should be disabled. | defaults to False
**homepage_redirect_target** | **str** | Redirect target if you try to open the base API domain in your browser | defaults to "https://hello.vrchat.com"
**use_reliable_udp_for_voice** | **bool** | Unknown | defaults to False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


