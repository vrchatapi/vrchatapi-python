# AccountDeletionLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **datetime** | Date and time of the deletion request. | [optional] 
**deletion_scheduled** | **datetime** | When the deletion is scheduled to happen, standard is 14 days after the request. | [optional] 
**message** | **str** | Typically \&quot;Deletion requested\&quot; or \&quot;Deletion canceled\&quot;. Other messages like \&quot;Deletion completed\&quot; may exist, but are these are not possible to see as a regular user. | [optional] [default to 'Deletion requested']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


