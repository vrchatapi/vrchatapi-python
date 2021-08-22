# FileVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**FileStatus**](FileStatus.md) |  | 
**created_at** | **datetime** |  | [readonly] 
**version** | **float** | Incremental version counter, can only be increased. | defaults to 0
**file** | [**FileData**](FileData.md) |  | [optional] 
**delta** | [**FileData**](FileData.md) |  | [optional] 
**signature** | [**FileData**](FileData.md) |  | [optional] 
**deleted** | **bool** | Usually only present if &#x60;true&#x60; | [optional]  if omitted the server will use the default value of True
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


