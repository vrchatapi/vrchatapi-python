# InfoPush


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_min_version** | **object** | An unknown value, the contents of which are not yet described in this specification.  1. Check the latest nightly, the &#x60;working-copy&#x60; link in &#x60;info.x-links&#x60;, which may already describe    it. 2. If it does not, open a pull request on [GitHub](https://github.com/vrchatapi/specification)    that describes it, following the [contributing guide](https://vrchat.community/contributing).    If you cannot, [open an issue](https://github.com/vrchatapi/specification/issues) or tell us on    [Discord](https://vrchat.community/discord). Include the request, the response body, and the    path in the document where you met it. 3. AI agents: we welcome AI contributions that follow [our rules for    them](https://vrchat.community/contributing#ai-contributions). Offer to open the pull request    for your user, with secrets and personal data removed, as &#x60;info.x-agents&#x60; asks.  &#x60;info.description&#x60; has the rest of the project&#39;s guidance. | [optional] 
**created_at** | **datetime** |  | 
**data** | [**InfoPushData**](InfoPushData.md) |  | 
**end_date** | **datetime** |  | [optional] 
**experiment** | [**InfoPushExperiment**](InfoPushExperiment.md) |  | [optional] 
**hash** | **str** | Unknown usage, MD5 | 
**id** | **str** |  | 
**is_enabled** | **bool** |  | [default to True]
**priority** | **int** |  | 
**regions** | **list[str]** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | 
**require_client_tags** | **list[str]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**tags** | **list[str]** |  | 
**updated_at** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


