# DeviceCode

A code that logs this device in once someone approves it at `verificationUrl`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_code** | **str** | Identifies this login attempt to &#x60;checkDeviceCode&#x60;. | 
**expires_in** | **int** | Seconds until the code expires. | 
**interval** | **int** | Seconds to wait between calls to &#x60;checkDeviceCode&#x60;. | 
**user_code** | **str** | The code a person enters at &#x60;verificationUrl&#x60; to approve the login. | 
**verification_url** | **str** |  | 
**verification_url_complete** | **str** | &#x60;verificationUrl&#x60; with the code already filled in. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


