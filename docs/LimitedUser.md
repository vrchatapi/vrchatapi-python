# LimitedUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**display_name** | **str** |  | 
**fallback_avatar** | [**AvatarID**](AvatarID.md) |  | 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**is_friend** | **bool** |  | 
**last_platform** | **str** | This can be &#x60;standalonewindows&#x60; or &#x60;android&#x60;, but can also pretty much be any random Unity verison such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**profile_pic_override** | **str** |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**status_description** | **str** |  | 
**tags** | [**[Tag]**](Tag.md) | &lt;- Always empty. | 
**user_icon** | **str** |  | 
**username** | **str** |  | 
**bio** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**friend_key** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


