# CreateCalendarEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**CalendarEventAccess**](CalendarEventAccess.md) |  | 
**category** | [**CalendarEventCategory**](CalendarEventCategory.md) |  | 
**close_instance_after_end_minutes** | **int** |  | [optional] 
**description** | **str** |  | 
**ends_at** | **datetime** | Time the event ends at | 
**featured** | **bool** |  | [optional] 
**guest_early_join_minutes** | **int** |  | [optional] 
**host_early_join_minutes** | **int** |  | [optional] 
**image_id** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**languages** | **list[str]** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**platforms** | [**list[CalendarEventPlatform]**](CalendarEventPlatform.md) |  | [optional] 
**role_ids** | **list[str]** |  | [optional] 
**send_creation_notification** | **bool** | Send notification to group members. | 
**starts_at** | **datetime** | Time the event starts at | 
**tags** | **list[str]** |  | [optional] 
**title** | **str** | Event title | 
**uses_instance_overflow** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


