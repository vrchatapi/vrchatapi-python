# InviteMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**InviteMessageID**](InviteMessageID.md) |  | 
**message** | **str** |  | 
**message_type** | [**InviteMessageType**](InviteMessageType.md) |  | 
**slot** | **int** |  | 
**updated_at** | **datetime** |  | 
**can_be_updated** | **bool** |  | defaults to True
**remaining_cooldown_minutes** | **int** | Changes to 60 when updated, although probably server-side configurable. | defaults to 0
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


