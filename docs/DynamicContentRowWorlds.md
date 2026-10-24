# DynamicContentRowWorlds

A row of worlds, which has no `type`, or a row whose `type` has no schema of its own.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_specific** | **bool** |  | [optional] 
**banners_tag** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**short_name** | **object** |  | [optional] 
**sort_heading** | **str** |  | 
**sort_order** | [**OrderOption**](OrderOption.md) |  | 
**sort_ownership** | **str** |  | 
**tag** | **str** | Tag to filter content for this row. Not a &#x60;Tag&#x60;: that type forbids the empty string, which this field uses for a row that is not tag-filtered. | [optional] 
**type** | **str** |  | [optional] 
**name** | **object** |  | 
**platform** | **str** | Usually \&quot;ThisPlatformSupported\&quot;, but can also be other values such as \&quot;all\&quot; or platform specific identifiers. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


