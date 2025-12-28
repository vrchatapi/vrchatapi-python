# NotificationV2



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_delete** | **bool** |  | 
**category** | **str** |  | 
**created_at** | **datetime** |  | 
**data** | **dict(str, str)** |  | 
**details** | [**NotificationV2DetailsBoop**](NotificationV2DetailsBoop.md) |  | [optional] 
**expires_at** | **datetime** |  | 
**expiry_after_seen** | **int** |  | 
**id** | **str** |  | 
**ignore_dnd** | **bool** |  | 
**image_url** | **str** |  | 
**is_system** | **bool** |  | 
**link** | **str** |  | 
**link_text** | **str** |  | 
**link_text_key** | **str** |  | 
**message** | **str** |  | 
**message_key** | **str** |  | [optional] 
**receiver_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**related_notifications_id** | **str** |  | 
**require_seen** | **bool** |  | 
**responses** | [**list[NotificationV2Response]**](NotificationV2Response.md) |  | 
**seen** | **bool** |  | 
**sender_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**sender_username** | **str** |  | 
**title** | **str** |  | 
**title_key** | **str** |  | 
**type** | [**NotificationV2Type**](NotificationV2Type.md) |  | 
**updated_at** | **datetime** |  | 
**version** | **int** |  | [default to 2]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


