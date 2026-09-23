# TutorialStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** |  | 
**completed_any_tutorial** | **bool** |  | 
**completed_tutorials** | **list[str]** |  | 
**tutorial_key** | **str** | The ID of a tutorial. A platform tutorial is &#x60;{platform}:{store}:v1&#x60;, taken from the &#x60;X-Platform&#x60; and &#x60;X-Store&#x60; headers, with &#x60;undefined&#x60; for a header the request left out. Other tutorials take a longer form, such as &#x60;platform-agnostic:custom:onboarding-tutorial-world:v1&#x60;. | [default to 'undefined:undefined:v1']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


