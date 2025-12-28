# CalendarEventDiscovery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | Base64-encoded JSON:   type: object   properties:     dataSource:       type: string       enum:         - featured         - personalized     dataIndex:       type: integer       format: int32     phase:       type: string       enum:         - all         - live         - upcoming       description: see CalendarEventDiscoveryScope     asOf:       type: integer       format: int64       description: milliseconds since Unix epoch     paramHash:       type: string       format: string       description: Base64-encoded 256-bit hash of the original query parameters | 
**results** | [**list[CalendarEvent]**](CalendarEvent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


