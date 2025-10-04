# Store


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**display_name** | **str** |  | 
**id** | **str** |  | 
**seller_display_name** | **str** |  | 
**seller_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**store_id** | **str** |  | 
**store_type** | [**StoreType**](StoreType.md) |  | 
**tags** | **list[str]** |  | 
**listing_ids** | **list[str]** | Only for store type world and group | [optional] 
**listings** | [**list[ProductListing]**](ProductListing.md) | Only for store type world and group | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 
**group_id** | **str** |  | [optional] 
**shelf_ids** | **list[str]** | Only for store type house | [optional] 
**shelves** | [**list[StoreShelf]**](StoreShelf.md) | Only for store type house | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


