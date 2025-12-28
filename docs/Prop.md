# Prop



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**description** | **str** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**max_count_per_user** | **int** |  | [default to 1]
**name** | **str** |  | 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**spawn_type** | **int** | How a prop is summoned and interacted with. 0: the prop fixed to some surface in the world 1: the prop is a pickup and may be held by users 2: ??? | [default to 1]
**tags** | **list[str]** |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url** | **str** |  | 
**unity_packages** | [**list[PropUnityPackage]**](PropUnityPackage.md) |  | 
**world_placement_mask** | **int** | Bitmask for restrictions on what world surfaces a prop may be summoned. 0: no restrictions 1: floors 2: walls 4: ceilings | [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


