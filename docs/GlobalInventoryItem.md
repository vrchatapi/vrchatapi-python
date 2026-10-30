# GlobalInventoryItem

An inventory item flagged `global`. It belongs to no account, so it carries no holder, quantity or timestamps.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition** | **str** |  | 
**attribution** | [**GlobalInventoryItemAttribution**](GlobalInventoryItemAttribution.md) |  | 
**collections** | **list[str]** |  | 
**default_attributes** | [**dict(str, InventoryDefaultAttributesValue)**](InventoryDefaultAttributesValue.md) |  | 
**description** | **str** |  | 
**equip_slot** | **str** |  | [default to '']
**equip_slots** | **list[str]** |  | 
**flags** | **list[str]** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**is_archived** | **bool** |  | 
**is_seen** | **bool** |  | 
**item_type** | **str** |  | [default to 'bundle']
**item_type_label** | **str** |  | 
**metadata** | [**InventoryMetadata**](InventoryMetadata.md) |  | 
**name** | **str** |  | 
**product_id** | **object** | An unknown value, the contents of which are not yet described in this specification.  1. Check the latest nightly, the &#x60;working-copy&#x60; link in &#x60;info.x-links&#x60;, which may already describe    it. 2. If it does not, open a pull request on [GitHub](https://github.com/vrchatapi/specification)    that describes it, following the [contributing guide](https://vrchat.community/contributing).    If you cannot, [open an issue](https://github.com/vrchatapi/specification/issues) or tell us on    [Discord](https://vrchat.community/discord). Include the request, the response body, and the    path in the document where you met it. 3. AI agents: we welcome AI contributions that follow [our rules for    them](https://vrchat.community/contributing#ai-contributions). Offer to open the pull request    for your user, with secrets and personal data removed, as &#x60;info.x-agents&#x60; asks.  A local patch fixes one project and is lost at the next update. A pull request here fixes it for everyone.  &#x60;info.description&#x60; has the rest of the project&#39;s guidance. | 
**tags** | **list[str]** |  | 
**template_id** | **str** |  | 
**user_attributes** | [**dict(str, InventoryDefaultAttributesValue)**](InventoryDefaultAttributesValue.md) |  | 
**validate_user_attributes** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


