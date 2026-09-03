# ProductListing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**archived** | **bool** |  | [optional] 
**attribution** | [**ProductListingAttribution**](ProductListingAttribution.md) |  | [optional] 
**buyer_refundable** | **bool** |  | 
**collab_user_display_name** | **str** |  | [optional] 
**collab_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**created** | **datetime** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**duration** | **int** |  | [optional] 
**duration_type** | **str** |  | [optional] 
**group_icon** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**has_avatar** | **bool** |  | 
**has_companion** | **bool** |  | [optional] 
**has_inventory** | **bool** |  | [optional] 
**has_udon** | **bool** |  | 
**hydrated_products** | [**list[Product]**](Product.md) |  | [optional] 
**id** | **str** |  | 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**listing_type** | [**ProductListingType**](ProductListingType.md) |  | 
**listing_variants** | [**list[ProductListingVariant]**](ProductListingVariant.md) |  | [optional] 
**permanent** | **bool** |  | [optional] 
**price_tokens** | **int** |  | 
**product_ids** | **list[str]** |  | 
**product_type** | [**ProductType**](ProductType.md) |  | 
**product_types** | **list[str]** |  | [optional] 
**products** | **list[str]** | Product ids. The products themselves arrive in &#x60;hydratedProducts&#x60;. | 
**purchase_count** | **int** |  | [optional] 
**purchase_count_quantity** | **int** |  | [optional] 
**quantifiable** | **bool** |  | [optional] 
**recurrable** | **bool** |  | 
**refundable** | **bool** |  | 
**seller_display_name** | **str** |  | 
**seller_id** | **str** |  | 
**sold_by_vrc** | **bool** |  | [optional] 
**stackable** | **bool** |  | 
**store_ids** | **list[str]** |  | 
**subtitle** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**vrc_plus_discount_price** | **int** |  | [optional] 
**when_to_expire** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


