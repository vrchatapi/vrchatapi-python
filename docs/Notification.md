# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**sender_user_id** | **str** |  | [readonly] 
**sender_username** | **str** |  | 
**type** | [**NotificationType**](NotificationType.md) |  | 
**message** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**details** | **str** | **NOTICE:** This is not a JSON object, this is a json **encoded** object, meaning you have to json-de-encode to get the NotificationDetail object depending on the NotificationType. | defaults to "{}"
**seen** | **bool** |  | defaults to False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


