# Transaction



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**user_display_name** | **str** |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**subscription** | [**Subscription**](Subscription.md) |  | 
**sandbox** | **bool** |  | [default to False]
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**steam** | [**TransactionSteamInfo**](TransactionSteamInfo.md) |  | [optional] 
**agreement** | [**TransactionAgreement**](TransactionAgreement.md) |  | [optional] 
**error** | **str** |  | 
**is_gift** | **bool** |  | [optional] [default to False]
**is_tokens** | **bool** |  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


