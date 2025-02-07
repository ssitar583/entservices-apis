<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.Telemetry_Plugin"></a>
# Telemetry Plugin

**Version: [1.0.0]()**

A org.rdk.Telemetry plugin for Thunder framework.

### Table of Contents

- [Abbreviation, Acronyms and Terms](#head.Abbreviation,_Acronyms_and_Terms)
- [Description](#head.Description)
- [Configuration](#head.Configuration)
- [Methods](#head.Methods)
- [Notifications](#head.Notifications)

<a name="head.Abbreviation,_Acronyms_and_Terms"></a>
# Abbreviation, Acronyms and Terms

[[Refer to this link](overview/aat.md)]

<a name="head.Description"></a>
# Description

The `Telemetry` plugin allows you to persist event data for monitoring applications.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.Telemetry*) |
| classname | string | Class name: *org.rdk.Telemetry* |
| locator | string | Library name: *libWPEFrameworkTelemetry.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.Telemetry plugin:

Telemtry interface methods:

| Method | Description |
| :-------- | :-------- |
| [setReportProfileStatus](#method.setReportProfileStatus) | Sets the status of telemetry reporting |
| [logApplicationEvent](#method.logApplicationEvent) | Logs an application event |
| [uploadReport](#method.uploadReport) | Triggers processing and uploading of telemetry report for legacy Xconf based configuration |
| [abortReport](#method.abortReport) | Makes request to Telemetry service to abort report upload |


<a name="method.setReportProfileStatus"></a>
## *setReportProfileStatus [<sup>method</sup>](#head.Methods)*

Sets the status of telemetry reporting.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.status | string | The report status (must be one of the following: *STARTED*, *COMPLETE*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.Telemetry.setReportProfileStatus",
    "params": {
        "status": "STARTED"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "success": true
    }
}
```

<a name="method.logApplicationEvent"></a>
## *logApplicationEvent [<sup>method</sup>](#head.Methods)*

Logs an application event.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.eventName | string | The event name |
| params.eventValue | string | The event value |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.Telemetry.logApplicationEvent",
    "params": {
        "eventName": "...",
        "eventValue": "..."
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "success": true
    }
}
```

<a name="method.uploadReport"></a>
## *uploadReport [<sup>method</sup>](#head.Methods)*

Triggers processing and uploading of telemetry report for legacy Xconf based configuration.

### Events

| Event | Description |
| :-------- | :-------- |
| [onReportUpload](#event.onReportUpload) | Triggered by callback from Telemetry after report uploading |
### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 25 | ```ERROR_RPC_CALL_FAILED``` | RBus call report uploading failed |
| 6 | ```ERROR_OPENING_FAILED``` | Failed to open RBus handle |
| 43 | ```ERROR_NOT_EXIST``` | Built with no support for RBus |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.Telemetry.uploadReport"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": null
}
```

<a name="method.abortReport"></a>
## *abortReport [<sup>method</sup>](#head.Methods)*

Makes request to Telemetry service to abort report upload.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 25 | ```ERROR_RPC_CALL_FAILED``` | RBus call report uploading failed |
| 6 | ```ERROR_OPENING_FAILED``` | Failed to open RBus handle |
| 43 | ```ERROR_NOT_EXIST``` | Built with no support for RBus |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.Telemetry.abortReport"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": null
}
```

<a name="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.Telemetry plugin:

Telemtry interface events:

| Event | Description |
| :-------- | :-------- |
| [onReportUpload](#event.onReportUpload) | Triggered by callback from Telemetry after report uploading |


<a name="event.onReportUpload"></a>
## *onReportUpload [<sup>event</sup>](#head.Notifications)*

Triggered by callback from Telemetry after report uploading.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.telemetryUploadStatus | string | Indicates if the upload was successful |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onReportUpload",
    "params": {
        "telemetryUploadStatus": "UPLOAD_SUCCESS"
    }
}
```

