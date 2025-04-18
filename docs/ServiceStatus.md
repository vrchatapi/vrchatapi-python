# ServiceStatus

Status information for a service request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** | The id of this service, NOT the id of the thing this service was requested for. | 
**progress** | **list[object]** |  | 
**requester_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**state** | **str** |  | 
**subject_id** | **str** | The id of the thing this service was requested for. | 
**subject_type** | **str** | The kind of the thing this service was requested for. | 
**type** | **str** | The kind of service that was requested. | 
**updated_at** | **datetime** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


