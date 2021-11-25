# Avatar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**id** | [**AvatarID**](AvatarID.md) |  | 
**image_url** | **str** |  | 
**name** | **str** |  | 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**tags** | [**[Tag]**](Tag.md) |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url** | **str** |  | 
**unity_package_url_object** | [**AvatarUnityPackageUrlObject**](AvatarUnityPackageUrlObject.md) |  | 
**unity_packages** | [**[UnityPackage]**](UnityPackage.md) |  | 
**updated_at** | **datetime** |  | 
**featured** | **bool** |  | defaults to False
**version** | **int** |  | defaults to 0
**asset_url** | **str** | Not present from general serach &#x60;/avatars&#x60;, only on specific requests &#x60;/avatars/{avatarId}&#x60;. | [optional] 
**asset_url_object** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Not present from general serach &#x60;/avatars&#x60;, only on specific requests &#x60;/avatars/{avatarId}&#x60;. **Deprecation:** &#x60;Object&#x60; has unknown usage/fields, and is always empty. Use normal &#x60;Url&#x60; field instead. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


