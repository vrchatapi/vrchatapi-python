# UserExists

Status object representing if a queried user by username or userId exists or not. This model is primarily used by the `/auth/exists` endpoint, which in turn is used during registration. Please see the documentation on that endpoint for more information on usage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_exists** | **bool** | Status if a user exist with that username or userId. | [default to False]
**name_ok** | **bool** | Is the username valid? | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


