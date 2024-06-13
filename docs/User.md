# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_avatar_copying** | **bool** |  | [default to True]
**badges** | [**list[Badge]**](Badge.md) |   | [optional] 
**bio** | **str** |  | 
**bio_links** | **list[str]** |  | 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_tags** | **list[str]** |  | 
**date_joined** | **date** |  | 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | 
**display_name** | **str** | A users visual display name. This is what shows up in-game, and can different from their &#x60;username&#x60;. Changing display name is restricted to a cooldown period. | 
**friend_key** | **str** |  | 
**friend_request_status** | **str** |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | [optional] 
**is_friend** | **bool** | Either their &#x60;friendKey&#x60;, or empty string if you are not friends. Unknown usage. | 
**last_activity** | **str** | Either a date-time or empty string. | 
**last_login** | **str** | Either a date-time or empty string. | 
**last_platform** | **str** | This can be &#x60;standalonewindows&#x60; or &#x60;android&#x60;, but can also pretty much be any random Unity verison such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**location** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 
**note** | **str** |  | [optional] 
**profile_pic_override** | **str** |  | 
**profile_pic_override_thumbnail** | **str** |  | 
**pronouns** | **str** |  | 
**state** | [**UserState**](UserState.md) |  | 
**status** | [**UserStatus**](UserStatus.md) |  | 
**status_description** | **str** |  | 
**tags** | **list[str]** |   | 
**traveling_to_instance** | **str** |  | [optional] 
**traveling_to_location** | **str** |  | [optional] 
**traveling_to_world** | **str** |  | [optional] 
**user_icon** | **str** |  | 
**username** | **str** | -| A users unique name, used during login. This is different from &#x60;displayName&#x60; which is what shows up in-game. A users &#x60;username&#x60; can never be changed.&#39; **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429). | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


