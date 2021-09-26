# FileVersion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**status** | [**FileStatus**](FileStatus.md) |  | 
**version** | **int** | Incremental version counter, can only be increased. | defaults to 0
**deleted** | **bool** | Usually only present if &#x60;true&#x60; | [optional]  if omitted the server will use the default value of True
**delta** | [**FileData**](FileData.md) |  | [optional] 
**file** | [**FileData**](FileData.md) |  | [optional] 
**signature** | [**FileData**](FileData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


