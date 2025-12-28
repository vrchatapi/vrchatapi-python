# UpdatePropRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | [optional] 
**asset_version** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**prop_signature** | **str** |  | [optional] 
**spawn_type** | **int** | How a prop is summoned and interacted with. 0: the prop fixed to some surface in the world 1: the prop is a pickup and may be held by users 2: ??? | [optional] [default to 1]
**tags** | **list[str]** |  | [optional] 
**unity_version** | **str** |  | [optional] 
**world_placement_mask** | **int** | Bitmask for restrictions on what world surfaces a prop may be summoned. 0: no restrictions 1: floors 2: walls 4: ceilings | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


