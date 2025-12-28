# InventoryItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | **list[str]** |  | 
**created_at** | **datetime** |  | 
**default_attributes** | [**dict(str, InventoryDefaultAttributes1)**](InventoryDefaultAttributes1.md) |  | 
**description** | **str** |  | 
**equip_slot** | [**InventoryEquipSlot**](InventoryEquipSlot.md) |  | [optional] 
**equip_slots** | [**list[InventoryEquipSlot]**](InventoryEquipSlot.md) |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**flags** | **list[str]** |  | 
**holder_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**is_archived** | **bool** |  | 
**is_seen** | **bool** |  | 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | 
**item_type_label** | **str** |  | 
**metadata** | [**InventoryMetadata**](InventoryMetadata.md) |  | 
**name** | **str** |  | 
**quantifiable** | **bool** |  | 
**tags** | **list[str]** |  | 
**template_id** | **str** |  | 
**template_created_at** | **datetime** |  | 
**template_updated_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_attributes** | [**InventoryUserAttributes**](InventoryUserAttributes.md) |  | 
**validate_user_attributes** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


