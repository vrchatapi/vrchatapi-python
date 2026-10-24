# LimitedInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | &#x60;type&#x60;, &#x60;groupAccessType&#x60; and &#x60;canRequestInvite&#x60; folded into one value.  | &#x60;type&#x60; | &#x60;groupAccessType&#x60; | &#x60;canRequestInvite&#x60; | &#x60;accessType&#x60; | | --- | --- | --- | --- | | &#x60;public&#x60; | | | &#x60;public&#x60; | | &#x60;friends&#x60; | | | &#x60;friends&#x60; | | &#x60;hidden&#x60; | | | &#x60;friendsPlus&#x60; | | &#x60;private&#x60; | | &#x60;false&#x60; | &#x60;invite&#x60; | | &#x60;private&#x60; | | &#x60;true&#x60; | &#x60;invitePlus&#x60; | | &#x60;group&#x60; | &#x60;public&#x60; | | &#x60;groupPublic&#x60; | | &#x60;group&#x60; | &#x60;plus&#x60; | | &#x60;groupPlus&#x60; | | &#x60;group&#x60; | &#x60;members&#x60; | | &#x60;group&#x60; | | 
**active** | **bool** |  | [default to True]
**capacity** | **int** |  | 
**category_id** | **str** |  | 
**creation_languages** | **list[object]** |  | 
**description** | **str** |  | 
**disabled_prop_abilities** | **list[str]** |  | 
**display_name** | **str** |  | 
**display_vibe_id** | **str** |  | 
**dominant_language** | **str** |  | 
**full** | **bool** |  | [default to False]
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] 
**id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**language_ratio** | **dict(str, object)** |  | 
**languages** | **list[str]** | The keys of languageRatio, ordered by their share of the instance. | 
**languages_iso639** | **list[str]** |  | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**minimum_avatar_performance** | **str** |  | 
**n_users** | **int** |  | 
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | 
**permanent** | **bool** |  | [default to False]
**photon_region** | [**Region**](Region.md) |  | 
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**queue_enabled** | **bool** |  | 
**queue_size** | **int** |  | 
**recommended_capacity** | **int** |  | 
**region** | [**InstanceRegion**](InstanceRegion.md) |  | 
**role_restricted** | **bool** |  | [optional] 
**short_name** | **str** |  | 
**tags** | **list[str]** | The tags array on Instances usually contain the language tags of the people in the instance.  | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**user_count** | **int** |  | 
**user_icons** | **list[str]** |  | 
**vibe_ids** | **list[str]** |  | 
**world** | [**World**](World.md) |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


