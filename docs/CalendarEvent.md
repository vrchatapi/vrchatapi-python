# CalendarEvent

An event scheduled on a group's calendar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**CalendarEventAccess**](CalendarEventAccess.md) |  | 
**category** | [**CalendarEventCategory**](CalendarEventCategory.md) |  | 
**close_instance_after_end_minutes** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**description** | **str** |  | 
**duration_in_ms** | **int** |  | [optional] 
**ends_at** | **datetime** |  | 
**featured** | **bool** |  | [optional] 
**guest_early_join_minutes** | **int** |  | [optional] 
**host_early_join_minutes** | **int** |  | [optional] 
**id** | **str** |  | 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**interested_user_count** | **int** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**languages** | **list[str]** | Languages that might be spoken at this event | [optional] 
**owner_id** | **str** |  | [optional] 
**platforms** | [**list[CalendarEventPlatform]**](CalendarEventPlatform.md) |  | [optional] 
**role_ids** | **list[str]** | Group roles that may join this event | [optional] 
**starts_at** | **datetime** |  | 
**tags** | **list[str]** | Custom tags for this event | [optional] 
**title** | **str** |  | 
**type** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_interest** | [**CalendarEventUserInterest**](CalendarEventUserInterest.md) |  | [optional] 
**uses_instance_overflow** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


