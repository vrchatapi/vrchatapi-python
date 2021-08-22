# UserState

* \"online\" User is online in VRChat * \"active\" User is online, but not in VRChat * \"offline\" User is offline  Always offline when returned through `getCurrentUser` (/auth/user).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | * \&quot;online\&quot; User is online in VRChat * \&quot;active\&quot; User is online, but not in VRChat * \&quot;offline\&quot; User is offline  Always offline when returned through &#x60;getCurrentUser&#x60; (/auth/user). | defaults to "offline",  must be one of ["offline", "active", "online", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


