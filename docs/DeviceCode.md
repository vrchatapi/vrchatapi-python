# DeviceCode

A code that logs the device that created it in, once a logged-in user approves it with `approveDeviceAuth`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Identifies this login attempt to &#x60;checkDeviceCode&#x60;. | 
**expires_in** | **int** |  | 
**interval** | **int** |  | 
**user_code** | **str** | Identifies this login attempt to &#x60;getDeviceAuthInfo&#x60; and &#x60;approveDeviceAuth&#x60;. | 
**verification_url** | **str** |  | 
**verification_url_complete** | **str** | &#x60;verificationUrl&#x60; with the code already filled in. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


