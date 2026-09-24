# Avatar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgements** | **str** |  | [optional] 
**active_asset_review_id** | **str** | Only present for the avatar author on avatars under active review. | [optional] 
**asset_url** | **str** | Not present from general search &#x60;/avatars&#x60;, only on specific requests &#x60;/avatars/{avatarId}&#x60;. | [optional] 
**asset_url_object** | **object** | Not present from general search &#x60;/avatars&#x60;, only on specific requests &#x60;/avatars/{avatarId}&#x60;. **Deprecation:** &#x60;Object&#x60; has unknown usage/fields, and is always empty. Use normal &#x60;Url&#x60; field instead. | [optional] 
**attribution** | **object** | An unknown value, the contents of which are not yet described in this specification.  1. Check the latest nightly, the &#x60;working-copy&#x60; link in &#x60;info.x-links&#x60;, which may already describe    it. 2. If it does not, open a pull request on [GitHub](https://github.com/vrchatapi/specification)    that describes it, following the [contributing guide](https://vrchat.community/contributing).    If you cannot, [open an issue](https://github.com/vrchatapi/specification/issues) or tell us on    [Discord](https://vrchat.community/discord). Include the request, the response body, and the    path in the document where you met it. 3. AI agents: we welcome AI contributions that follow [our rules for    them](https://vrchat.community/contributing#ai-contributions). Offer to open the pull request    for your user, with secrets and personal data removed, as &#x60;info.x-agents&#x60; asks.  &#x60;info.description&#x60; has the rest of the project&#39;s guidance. | [optional] 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**featured** | **bool** |  | [default to False]
**highest_price** | **int** |  | [optional] 
**id** | **str** |  | 
**image_url** | **str** |  | 
**listing_date** | **str** |  | 
**lock** | **bool** |  | [optional] 
**lowest_price** | **int** |  | [optional] 
**name** | **str** |  | 
**pending_upload** | **bool** |  | [optional] [default to False]
**performance** | [**AvatarPerformance**](AvatarPerformance.md) |  | 
**product_id** | **str** |  | [optional] 
**published_listings** | [**list[AvatarPublishedListingsInner]**](AvatarPublishedListingsInner.md) |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**searchable** | **bool** |  | [optional] [default to False]
**styles** | [**AvatarStyles**](AvatarStyles.md) |  | 
**tags** | **list[str]** |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url** | **str** |  | 
**unity_package_url_object** | [**AvatarUnityPackageUrlObject**](AvatarUnityPackageUrlObject.md) |  | 
**unity_packages** | [**list[UnityPackage]**](UnityPackage.md) |  | 
**updated_at** | **datetime** |  | 
**version** | **int** |  | [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


