# APIConfig



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_enable_degradation** | **bool** | Unknown, probably voice optimization testing | [default to False]
**voice_enable_receiver_limiting** | **bool** | Unknown, probably voice optimization testing | [default to True]
**address** | **str** | VRChat&#39;s office address | 
**announcements** | [**list[APIConfigAnnouncement]**](APIConfigAnnouncement.md) | Public Announcements | 
**analytics_segment_new_ui_pct_of_users** | **int** | Unknown | 
**analytics_segment_new_ui_salt** | **str** | Unknown | 
**app_name** | **str** | Game name | [default to 'VrChat']
**available_language_codes** | **list[str]** | List of supported Languages | 
**available_languages** | **list[str]** | List of supported Languages | 
**build_version_tag** | **str** | Build tag of the API server | 
**chatbox_log_buffer_seconds** | **int** | Unknown | [default to 40]
**client_api_key** | **str** | apiKey to be used for all other requests | 
**client_bps_ceiling** | **int** | Unknown | [default to 18432]
**client_disconnect_timeout** | **int** | Unknown | [default to 30000]
**client_net_dispatch_thread** | **bool** | Unknown | [optional] [default to False]
**client_net_dispatch_thread_mobile** | **bool** | Unknown | [default to True]
**client_net_in_thread** | **bool** | Unknown | [optional] [default to False]
**client_net_in_thread2** | **bool** | Unknown | [optional] [default to False]
**client_net_in_thread_mobile** | **bool** | Unknown | [optional] [default to False]
**client_net_in_thread_mobile2** | **bool** | Unknown | [optional] [default to False]
**client_net_out_thread** | **bool** | Unknown | [optional] [default to False]
**client_net_out_thread2** | **bool** | Unknown | [optional] [default to False]
**client_net_out_thread_mobile** | **bool** | Unknown | [optional] [default to False]
**client_net_out_thread_mobile2** | **bool** | Unknown | [optional] [default to False]
**client_qr** | **int** | Unknown | [optional] [default to 1]
**client_reserved_player_bps** | **int** | Unknown | [default to 7168]
**client_sent_count_allowance** | **int** | Unknown | [default to 15]
**constants** | [**APIConfigConstants**](APIConfigConstants.md) |  | 
**contact_email** | **str** | VRChat&#39;s contact email | 
**copyright_email** | **str** | VRChat&#39;s copyright-issues-related email | 
**current_privacy_version** | **int** | Current version number of the Privacy Agreement | [optional] [default to 1]
**current_tos_version** | **int** | Current version number of the Terms of Service | 
**default_avatar** | **str** |  | 
**deployment_group** | [**DeploymentGroup**](DeploymentGroup.md) |  | 
**dev_language_codes** | **list[str]** | Unknown | [optional] 
**dev_sdk_url** | **str** | Link to download the development SDK, use downloadUrls instead | 
**dev_sdk_version** | **str** | Version of the development SDK | 
**dis_countdown** | **datetime** | Unknown, \&quot;dis\&quot; maybe for disconnect? | 
**disable_av_pro_in_proton** | **bool** | Unknown | [optional] [default to False]
**disable_avatar_copying** | **bool** | Toggles if copying avatars should be disabled | [default to False]
**disable_avatar_gating** | **bool** | Toggles if avatar gating should be disabled. Avatar gating restricts uploading of avatars to people with the &#x60;system_avatar_access&#x60; Tag or &#x60;admin_avatar_access&#x60; Tag | [default to False]
**disable_community_labs** | **bool** | Toggles if the Community Labs should be disabled | [default to False]
**disable_community_labs_promotion** | **bool** | Toggles if promotion out of Community Labs should be disabled | [default to False]
**disable_email** | **bool** | Unknown | [default to False]
**disable_captcha** | **bool** | Unknown | [optional] [default to True]
**disable_event_stream** | **bool** | Toggles if Analytics should be disabled. | [default to False]
**disable_feedback_gating** | **bool** | Toggles if feedback gating should be disabled. Feedback gating restricts submission of feedback (reporting a World or User) to people with the &#x60;system_feedback_access&#x60; Tag. | [default to False]
**disable_frontend_builds** | **bool** | Unknown, probably toggles compilation of frontend web builds? So internal flag? | [default to False]
**disable_hello** | **bool** | Unknown | [default to False]
**disable_oculus_subs** | **bool** | Toggles if signing up for Subscriptions in Oculus is disabled or not. | [default to False]
**disable_registration** | **bool** | Toggles if new user account registration should be disabled. | [default to False]
**disable_steam_networking** | **bool** | Toggles if Steam Networking should be disabled. VRChat these days uses Photon Unity Networking (PUN) instead. | [default to True]
**disable_two_factor_auth** | **bool** | Toggles if 2FA should be disabled. | [default to False]
**disable_udon** | **bool** | Toggles if Udon should be universally disabled in-game. | [default to False]
**disable_upgrade_account** | **bool** | Toggles if account upgrading \&quot;linking with Steam/Oculus\&quot; should be disabled. | [default to False]
**download_link_windows** | **str** | Download link for game on the Oculus Rift website. | 
**download_urls** | [**APIConfigDownloadURLList**](APIConfigDownloadURLList.md) |  | 
**dynamic_world_rows** | [**list[DynamicContentRow]**](DynamicContentRow.md) | Array of DynamicWorldRow objects, used by the game to display the list of world rows | 
**economy_pause_end** | **str** | Unknown | [optional] 
**economy_pause_start** | **str** | Unknown | [optional] 
**economy_state** | **int** | Unknown | [optional] [default to 1]
**events** | [**APIConfigEvents**](APIConfigEvents.md) |  | 
**force_use_latest_world** | **bool** | Unknown | [default to True]
**google_api_client_id** | **str** | Unknown | [default to '827942544393-r2ouvckvouldn9dg9uruseje575e878f.apps.googleusercontent.com']
**home_world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**homepage_redirect_target** | **str** | Redirect target if you try to open the base API domain in your browser | [default to 'https://hello.vrchat.com']
**hub_world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**image_host_url_list** | **list[str]** | A list of explicitly allowed origins that worlds can request images from via the Udon&#39;s [VRCImageDownloader#DownloadImage](https://creators.vrchat.com/worlds/udon/image-loading/#downloadimage). | 
**jobs_email** | **str** | VRChat&#39;s job application email | 
**min_supported_client_build_number** | [**APIConfigMinSupportedClientBuildNumber**](APIConfigMinSupportedClientBuildNumber.md) |  | 
**minimum_unity_version_for_uploads** | **str** | Minimum Unity version required for uploading assets | [default to '2019.0.0f1']
**moderation_email** | **str** | VRChat&#39;s moderation related email | 
**not_allowed_to_select_avatar_in_private_world_message** | **str** | Used in-game to notify a user they aren&#39;t allowed to select avatars in private worlds | 
**offline_analysis** | [**APIConfigOfflineAnalysis**](APIConfigOfflineAnalysis.md) |  | 
**photon_nameserver_overrides** | **list[str]** | Unknown | 
**photon_public_keys** | **list[str]** | Unknown | 
**report_categories** | [**APIConfigReportCategories**](APIConfigReportCategories.md) |  | 
**report_form_url** | **str** | URL to the report form | [default to 'https://help.vrchat.com/hc/en-us/requests/new?ticket_form_id=1500000182242&tf_360056455174=user_report&tf_360057451993={userId}&tf_1500001445142={reportedId}&tf_subject={reason} {category} By {contentType} {reportedName}&tf_description={description}']
**report_options** | **object** | Options for reporting content | 
**report_reasons** | [**APIConfigReportReasons**](APIConfigReportReasons.md) |  | 
**sdk_developer_faq_url** | **str** | Link to the developer FAQ | 
**sdk_discord_url** | **str** | Link to the official VRChat Discord | 
**sdk_not_allowed_to_publish_message** | **str** | Used in the SDK to notify a user they aren&#39;t allowed to upload avatars/worlds yet | 
**sdk_unity_version** | **str** | Unity version supported by the SDK | 
**server_name** | **str** | Server name of the API server currently responding | 
**string_host_url_list** | **list[str]** | A list of explicitly allowed origins that worlds can request strings from via the Udon&#39;s [VRCStringDownloader.LoadUrl](https://creators.vrchat.com/worlds/udon/string-loading/#ivrcstringdownload). | 
**support_email** | **str** | VRChat&#39;s support email | 
**timekeeping** | **bool** | Unknown | [default to True]
**time_out_world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**tutorial_world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**update_rate_ms_maximum** | **int** | Unknown | 
**update_rate_ms_minimum** | **int** | Unknown | 
**update_rate_ms_normal** | **int** | Unknown | 
**update_rate_ms_udon_manual** | **int** | Unknown | 
**upload_analysis_percent** | **int** | Unknown | 
**url_list** | **list[str]** | List of allowed URLs that bypass the \&quot;Allow untrusted URL&#39;s\&quot; setting in-game | 
**use_reliable_udp_for_voice** | **bool** | Unknown | [default to False]
**vive_windows_url** | **str** | Download link for game on the Steam website. | 
**white_listed_asset_urls** | **list[str]** | List of allowed URLs that are allowed to host avatar assets | 
**player_url_resolver_version** | **str** | Currently used youtube-dl.exe version | 
**player_url_resolver_sha1** | **str** | Currently used youtube-dl.exe hash in SHA1-delimited format | 
**websocket_max_friends_refresh_delay** | **int** | Unknown | [default to 900]
**websocket_quick_reconnect_time** | **int** | Unknown | [default to 2]
**websocket_reconnect_max_delay** | **int** | Unknown | [default to 2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


