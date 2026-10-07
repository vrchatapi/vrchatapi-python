# GroupAuditLogEntryDataGroupCalendarEventDelete


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category of the event. | 
**close_instance_after_end_minutes** | **int** | Minutes after the event ends to close the instance. | 
**created_at** | **datetime** | The creation timestamp. | 
**deleted_at** | **datetime** | The deletion timestamp. | 
**duration_in_ms** | **int** | The duration of the event in milliseconds. | 
**ends_at** | **datetime** | The end timestamp. | 
**featured** | **bool** | Whether the event is featured. | 
**guest_early_join_minutes** | **int** | Minutes before the start that guests can join. | 
**host_early_join_minutes** | **int** | Minutes before the start that hosts can join. | 
**interested_user_count** | **int** | The number of interested users. | 
**is_draft** | **bool** | Whether the event is a draft. | 
**languages** | **list[str]** | The languages for the event. | 
**occurrence_kind** | [**CalendarEventOccurrenceKind**](CalendarEventOccurrenceKind.md) |  | 
**occurrence_modified** | **str** |  | 
**owner_id** | **str** |  | 
**platforms** | **list[str]** | The supported platforms. | 
**recurrence** | [**CalendarEventRecurrence**](CalendarEventRecurrence.md) |  | 
**role_ids** | **list[str]** | Group roles that may join this event. | 
**series_id** | **str** | The ID of the recurring series the event belongs to. | 
**short_code** | **str** | The short code. | 
**starts_at** | **datetime** | The start timestamp. | 
**tags** | **list[str]** | The event tags. | 
**updated_at** | **datetime** | The last update timestamp. | 
**uses_instance_overflow** | **bool** | Whether the event uses instance overflow. | 
**access_type** | [**CalendarEventAccess**](CalendarEventAccess.md) |  | 
**description** | **str** | The description of the calendar event. | 
**image_id** | **str** |  | 
**title** | **str** | The title of the calendar event. | 
**type** | **str** | The type of calendar entry. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


