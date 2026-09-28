# UpdateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_tos_version** | **int** |  | [optional] 
**allow_worlds_to_count_friends_in_instance** | **bool** | The \&quot;Allow Worlds to Count Friends in Instance\&quot; setting, introduced under [Udon Methods for Friend Info](https://ask.vrchat.com/t/developer-update-24-september-2026/48972#p-90922-udon-methods-for-friend-info-13) in the Developer Update of September 24, 2026. | [optional] 
**birthday** | **date** |  | [optional] 
**content_filters** | [**list[ContentFilter]**](ContentFilter.md) | These tags begin with &#x60;content_&#x60; and control content gating | [optional] 
**current_password** | **str** |  | [optional] 
**display_name** | **str** | MUST specify currentPassword as well to change display name | [optional] 
**email** | **str** |  | [optional] 
**has_discord_friends_opt_out** | **bool** | Opt out of the Discord Friend Connections feature | [optional] 
**has_shared_connections_opt_out** | **bool** | Opt out of the Mutuals feature | [optional] 
**is_booping_enabled** | **bool** |  | [optional] 
**password** | **str** | MUST specify currentPassword as well to change password | [optional] 
**pronouns** | **str** |  | [optional] 
**revert_display_name** | **bool** | MUST specify currentPassword as well to revert display name | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**unsubscribe** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


