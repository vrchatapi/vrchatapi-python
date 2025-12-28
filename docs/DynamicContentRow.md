# DynamicContentRow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**name** | **str** |  | 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**sort_heading** | **str** |  | 
**sort_order** | **str** |  | 
**sort_ownership** | **str** |  | 
**tag** | **str** | Tags are a way to grant various access, assign restrictions or other kinds of metadata to various to objects such as worlds, users and avatars.  System tags starting with &#x60;system_&#x60; are granted automatically by the system, while admin tags with &#x60;admin_&#x60; are granted manually. More prefixes such as &#x60;language_ &#x60; (to indicate that a player can speak the tagged language), and &#x60;author_tag_&#x60; (provided by a world author for search and sorting) exist as well. | [optional] 
**type** | **str** | Type is not present if it is a world. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


