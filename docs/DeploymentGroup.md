# DeploymentGroup

Used to identify which API deployment cluster is currently responding.  `blue` and `green` are used by Production. `grape`and `cherry` are used during Development.  [Blue Green Deployment by Martin Fowler](https://martinfowler.com/bliki/BlueGreenDeployment.html)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Used to identify which API deployment cluster is currently responding.  &#x60;blue&#x60; and &#x60;green&#x60; are used by Production. &#x60;grape&#x60;and &#x60;cherry&#x60; are used during Development.  [Blue Green Deployment by Martin Fowler](https://martinfowler.com/bliki/BlueGreenDeployment.html) | defaults to "blue",  must be one of ["blue", "green", "grape", "cherry", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


