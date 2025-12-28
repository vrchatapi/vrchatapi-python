# ModerationReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Valid values are the keys of the object &#x60;$.reportOptions[type]&#x60; from &#x60;GET /config&#x60;. Descriptions of these are found at &#x60;$.reportCategories[type]&#x60;. | 
**content_id** | **str** |  | 
**content_name** | **str** |  | 
**content_thumbnail_image_url** | **str** |  | 
**description** | **str** | The subjective reason for the report | 
**evidence_required** | **bool** |  | 
**id** | **str** |  | 
**reason** | **str** | Valid values are the strings in the array &#x60;$.reportOptions[type][category]&#x60; from &#x60;GET /config&#x60;. Descriptions of these are found at &#x60;$.reportReasons[type]&#x60;. | 
**support_required** | **bool** |  | 
**type** | **str** | Valid values are the keys of the object &#x60;$.reportOptions&#x60; from &#x60;GET /config&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


