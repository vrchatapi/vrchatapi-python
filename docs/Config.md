# Config


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | VRChat&#39;s office address | [readonly] 
**announcements** | [**[ConfigAnnouncements]**](ConfigAnnouncements.md) | Public Announcements | [readonly] 
**api_key** | **str** | apiKey to be used for all other requests | [readonly] 
**build_version_tag** | **str** | Build tag of the API server | [readonly] 
**client_api_key** | **str** | apiKey to be used for all other requests | [readonly] 
**contact_email** | **str** | VRChat&#39;s contact email | [readonly] 
**copyright_email** | **str** | VRChat&#39;s copyright-issues-related email | [readonly] 
**current_tos_version** | **float** | Current version number of the Terms of Service | [readonly] 
**default_avatar** | [**AvatarID**](AvatarID.md) |  | 
**deployment_group** | [**DeploymentGroup**](DeploymentGroup.md) |  | 
**dev_app_version_standalone** | **str** | Version number for game development build | [readonly] 
**dev_download_link_windows** | **str** | Developer Download link | [readonly] 
**dev_sdk_url** | **str** | Link to download the development SDK, use downloadUrls instead | [readonly] 
**dev_sdk_version** | **str** | Version of the development SDK | [readonly] 
**dev_server_version_standalone** | **str** | Version number for server development build | [readonly] 
**download_link_windows** | **str** | Download link for game on the Oculus Rift website. | [readonly] 
**download_urls** | [**ConfigDownloadUrls**](ConfigDownloadUrls.md) |  | 
**dynamic_world_rows** | [**[ConfigDynamicWorldRows]**](ConfigDynamicWorldRows.md) | Array of DynamicWorldRow objects, used by the game to display the list of world rows | [readonly] 
**events** | [**ConfigEvents**](ConfigEvents.md) |  | 
**gear_demo_room_id** | **str** | Unknown | [readonly] 
**home_world_id** | [**WorldID**](WorldID.md) |  | 
**hub_world_id** | [**WorldID**](WorldID.md) |  | 
**jobs_email** | **str** | VRChat&#39;s job application email | [readonly] 
**message_of_the_day** | **str** | MOTD | [readonly] 
**moderation_email** | **str** | VRChat&#39;s moderation related email | [readonly] 
**moderation_query_period** | **float** | Unknown | 
**not_allowed_to_select_avatar_in_private_world_message** | **str** | Used in-game to notify a user they aren&#39;t allowed to select avatars in private worlds | [readonly] 
**plugin** | **str** | Extra [plugin](https://doc.photonengine.com/en-us/server/current/plugins/manual) to run in each instance | [readonly] 
**release_app_version_standalone** | **str** | Version number for game release build | [readonly] 
**release_sdk_url** | **str** | Link to download the release SDK | [readonly] 
**release_sdk_version** | **str** | Version of the release SDK | [readonly] 
**release_server_version_standalone** | **str** | Version number for server release build | [readonly] 
**sdk_developer_faq_url** | **str** | Link to the developer FAQ | [readonly] 
**sdk_discord_url** | **str** | Link to the official VRChat Discord | [readonly] 
**sdk_not_allowed_to_publish_message** | **str** | Used in the SDK to notify a user they aren&#39;t allowed to upload avatars/worlds yet | [readonly] 
**sdk_unity_version** | **str** | Unity version supported by the SDK | [readonly] 
**server_name** | **str** | Server name of the API server currently responding | [readonly] 
**support_email** | **str** | VRChat&#39;s support email | [readonly] 
**time_out_world_id** | [**WorldID**](WorldID.md) |  | 
**tutorial_world_id** | [**WorldID**](WorldID.md) |  | 
**update_rate_ms_maximum** | **float** | Unknown | [readonly] 
**update_rate_ms_minimum** | **float** | Unknown | [readonly] 
**update_rate_ms_normal** | **float** | Unknown | [readonly] 
**update_rate_ms_udon_manual** | **float** | Unknown | [readonly] 
**upload_analysis_percent** | **float** | Unknown | [readonly] 
**url_list** | **[str]** | List of allowed URLs that bypass the \&quot;Allow untrusted URL&#39;s\&quot; setting in-game | [readonly] 
**user_update_period** | **float** | Unknown | [readonly] 
**user_verification_delay** | **float** | Unknown | [readonly] 
**user_verification_retry** | **float** | Unknown | [readonly] 
**user_verification_timeout** | **float** | Unknown | [readonly] 
**vive_windows_url** | **str** | Download link for game on the Steam website. | [readonly] 
**white_listed_asset_urls** | **[str]** | List of allowed URLs that are allowed to host avatar assets | [readonly] 
**world_update_period** | **float** | Unknown | [readonly] 
**youtubedl_hash** | **str** | Currently used youtube-dl.exe hash in SHA-256-delimited format | [readonly] 
**youtubedl_version** | **str** | Currently used youtube-dl.exe version | [readonly] 
**app_name** | **str** | Game name | [readonly] defaults to "VrChat"
**disable_avatar_copying** | **bool** | Toggles if copying avatars should be disabled | defaults to False
**disable_avatar_gating** | **bool** | Toggles if avatar gating should be disabled. Avatar gating restricts uploading of avatars to people with the &#x60;system_avatar_access&#x60; Tag or &#x60;admin_avatar_access&#x60; Tag | defaults to False
**disable_community_labs** | **bool** | Toggles if the Community Labs should be disabled | defaults to False
**disable_community_labs_promotion** | **bool** | Toggles if promotion out of Community Labs should be disabled | defaults to False
**disable_event_stream** | **bool** | Toggles if Analytics should be disabled (this sreportedly not used in the Client) | defaults to False
**disable_feedback_gating** | **bool** | Toggles if feedback gating should be disabled. Feedback gating restricts submission of feedback (reporting a World or User) to people with the &#x60;system_feedback_access&#x60; Tag. | defaults to False
**disable_registration** | **bool** | Toggles if new user account registration should be disabled | defaults to False
**disable_steam_networking** | **bool** | Toggles if Steam Networking should be disabled. VRChat these days uses Photon Unity Networking (PUN) instead. | defaults to True
**disable_two_factor_auth** | **bool** | Toggles if 2FA should be disabled. | defaults to False
**disable_udon** | **bool** | Toggles if Udon should be universally disabled in-game. | defaults to False
**disable_upgrade_account** | **bool** | Toggles if account upgrading \&quot;linking with Steam/Oculus\&quot; should be disabled. | defaults to False
**homepage_redirect_target** | **str** | Redirect target if you try to open the base API domain in your browser | [readonly] defaults to "https://hello.vrchat.com"
**use_reliable_udp_for_voice** | **bool** | Unknown | defaults to False
**client_bps_ceiling** | **float** | Unknown | [optional] 
**client_disconnect_timeout** | **float** | Unknown | [optional] 
**client_reserved_player_bps** | **float** | Unknown | [optional] 
**client_sent_count_allowance** | **float** | Unknown | [optional] 
**disable_email** | **bool** | Unknown | [optional]  if omitted the server will use the default value of False
**disable_hello** | **bool** | Unknown | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


