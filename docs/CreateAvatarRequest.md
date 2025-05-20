# CreateAvatarRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | [optional] 
**asset_version** | **str** |  | [optional] 
**platform** | **str** | This can be &#x60;standalonewindows&#x60; or &#x60;android&#x60;, but can also pretty much be any random Unity verison such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**created_at** | **str** | A date and time of the pattern &#x60;M/d/yyyy h:mm:ss tt&#x60; (see C Sharp &#x60;System.DateTime&#x60;) | [optional] 
**updated_at** | **str** | A date and time of the pattern &#x60;M/d/yyyy h:mm:ss tt&#x60; (see C Sharp &#x60;System.DateTime&#x60;) | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**tags** | **list[str]** |   | [optional] 
**image_url** | **str** |  | 
**thumbnail_image_url** | **str** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] 
**version** | **int** |  | [optional] [default to 1]
**unity_package_url** | **str** |  | [optional] 
**unity_version** | **str** |  | [optional] [default to '5.3.4p1']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


