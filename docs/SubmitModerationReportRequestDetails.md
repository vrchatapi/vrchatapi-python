# SubmitModerationReportRequestDetails

Relevant details specific to the type of the report. `fileId` is for the image file attached to an inventory item, such as an emoji. `holderId` is for the user who owns an inventory item, such as a emoji.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**holder_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**image_type** | **str** | Relevant detail for reports about image content, such as emoji. | [optional] 
**instance_age_gated** | **bool** | Relevant detail for reports taking place from within an instance. | [optional] 
**instance_type** | **str** | Relevant detail for reports taking place from within an instance. | [optional] 
**suggested_warnings** | [**list[ContentFilter]**](ContentFilter.md) | Relevant detail for reports about content that might not be tagged properly. | [optional] 
**user_in_same_instance** | **bool** | Relevant detail for reports involving another user in the same instance world. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


