# DynamicContentRow

A row of content. The fields depend on `type`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** |  | 
**platform** | **str** | Usually \&quot;ThisPlatformSupported\&quot;, but can also be other values such as \&quot;all\&quot; or platform specific identifiers. | 
**any_style** | **list[str]** |  | [optional] 
**any_tag** | **list[str]** |  | [optional] 
**marketplace** | **str** |  | [optional] 
**max_price** | **int** |  | [optional] 
**min_price** | **int** |  | [optional] 
**notag** | **list[str]** |  | [optional] 
**params** | **dict(str, object)** |  | [optional] 
**sort_heading** | **str** |  | [optional] 
**sort_order** | [**OrderOption**](OrderOption.md) |  | [optional] 
**sort_ownership** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**tag** | **str** | Tag to filter content for this row. Not a &#x60;Tag&#x60;: that type forbids the empty string, which this field uses for a row that is not tag-filtered. | [optional] 
**type** | **str** |  | [optional] 
**categories** | **list[str]** |  | [optional] 
**featured_results** | **str** |  | [optional] 
**minimum_interest_count** | **int** |  | [optional] 
**minimum_remaining_minutes** | **int** |  | [optional] 
**non_featured_results** | **str** |  | [optional] 
**personalized_results** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**upcoming_offset_minutes** | **int** |  | [optional] 
**group_pool** | **str** |  | [optional] 
**min_occupants** | **int** |  | [optional] 
**mode** | [**InstanceDiscoveryMode**](InstanceDiscoveryMode.md) |  | [optional] 
**n** | **int** |  | [optional] 
**region** | [**InstanceRegion**](InstanceRegion.md) |  | [optional] 
**world_pool** | [**InstanceDiscoveryWorldPool**](InstanceDiscoveryWorldPool.md) |  | [optional] 
**avatar_specific** | **bool** |  | [optional] 
**banners_tag** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**short_name** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


