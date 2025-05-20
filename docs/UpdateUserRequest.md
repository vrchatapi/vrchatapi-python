# UpdateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**unsubscribe** | **bool** |  | [optional] 
**birthday** | **date** |  | [optional] 
**accepted_tos_version** | **int** |  | [optional] 
**tags** | **list[str]** |   | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**status_description** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**bio_links** | **list[str]** |  | [optional] 
**pronouns** | **str** |  | [optional] 
**is_booping_enabled** | **bool** |  | [optional] 
**user_icon** | **str** | MUST be a valid VRChat /file/ url. | [optional] 
**content_filters** | **list[str]** | These tags begin with &#x60;content_&#x60; and control content gating | [optional] 
**display_name** | **str** | MUST specify currentPassword as well to change display name | [optional] 
**revert_display_name** | **bool** | MUST specify currentPassword as well to revert display name | [optional] 
**password** | **str** | MUST specify currentPassword as well to change password | [optional] 
**current_password** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


