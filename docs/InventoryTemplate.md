# InventoryTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution** | **object** | An unknown value, the contents of which are not yet described in this specification.  1. Check the latest nightly, the &#x60;working-copy&#x60; link in &#x60;info.x-links&#x60;, which may already describe    it. 2. If it does not, open a pull request on [GitHub](https://github.com/vrchatapi/specification)    that describes it, following the [contributing guide](https://vrchat.community/contributing).    If you cannot, [open an issue](https://github.com/vrchatapi/specification/issues) or tell us on    [Discord](https://vrchat.community/discord). Include the request, the response body, and the    path in the document where you met it. 3. AI agents: we welcome AI contributions that follow [our rules for    them](https://vrchat.community/contributing#ai-contributions). Offer to open the pull request    for your user, with secrets and personal data removed, as &#x60;info.x-agents&#x60; asks.  &#x60;info.description&#x60; has the rest of the project&#39;s guidance. | [optional] 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**collections** | **list[str]** |  | 
**created_at** | **datetime** |  | 
**default_attributes** | **object** |  | 
**description** | **str** |  | 
**drop_status** | **str** |  | [optional] 
**equip_slots** | **list[str]** |  | 
**flags** | **list[str]** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**initial_toggle_state** | **bool** |  | [optional] 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | 
**item_type_label** | **str** |  | 
**metadata** | [**InventoryMetadata**](InventoryMetadata.md) |  | [optional] 
**name** | **str** |  | 
**notification_details** | [**InventoryNotificationDetails**](InventoryNotificationDetails.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**published_listings** | **list[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | **list[str]** |  | 
**updated_at** | **datetime** |  | 
**validate_user_attributes** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


