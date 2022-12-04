# UserSubscription



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**transaction_id** | **str** |  | 
**store** | **str** | Which \&quot;Store\&quot; it came from. Right now only Stores are \&quot;Steam\&quot; and \&quot;Admin\&quot;. | 
**steam_item_id** | **str** |  | [optional] 
**amount** | **float** |  | 
**description** | **str** |  | 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | 
**tier** | **float** |  | 
**active** | **bool** |  | [default to True]
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**expires** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**license_groups** | **list[str]** |  | 
**is_gift** | **bool** |  | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


