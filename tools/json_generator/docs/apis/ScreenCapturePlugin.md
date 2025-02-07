<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.ScreenCapture_Plugin"></a>
# ScreenCapture Plugin

**Version: [1.0.0]()**

A org.rdk.ScreenCapture plugin for Thunder framework.

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

The `ScreenCapture` plugin is used to upload screen captures.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.ScreenCapture*) |
| classname | string | Class name: *org.rdk.ScreenCapture* |
| locator | string | Library name: *libWPEFrameworkScreenCapture.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.ScreenCapture plugin:

ScreenCapture interface methods:

| Method | Description |
| :-------- | :-------- |
| [uploadScreenCapture](#method.uploadScreenCapture) | Takes a screenshot and uploads it to the specified URL |


<a name="method.uploadScreenCapture"></a>
## *uploadScreenCapture [<sup>method</sup>](#head.Methods)*

Takes a screenshot and uploads it to the specified URL. A screenshot is uploaded using raw HTTP POST request as binary image/png data. It's the same as running the following command:  
`wget -d -q -O - --header='Content-Type: application/octet-stream' --post-file=/path/to/screenshot.png http://server/cgi-bin/upload.cgi`  
or,  
`curl -F image=@/path/to/screenshot.png http://server/cgi-bin/upload.cgi`  
For implementation details, see `bool ScreenCapture::uploadDataToUrl(std::vector<unsigned char> &data, const char *url, std::string &error_str)`.

### Events

| Event | Description |
| :-------- | :-------- |
| [uploadComplete](#event.uploadComplete) | Triggered after uploading a screen capture with status and message |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.url | string | The upload destination |
| params?.callGUID | string | <sup>*(optional)*</sup> A unique identifier of a call. The identifier is used to find a corresponding `uploadComplete` event |

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
    "method": "org.rdk.ScreenCapture.uploadScreenCapture",
    "params": {
        "url": "http://server/cgi-bin/upload.cgi",
        "callGUID": "12345"
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

<a name="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.ScreenCapture plugin:

ScreenCapture interface events:

| Event | Description |
| :-------- | :-------- |
| [uploadComplete](#event.uploadComplete) | Triggered after uploading a screen capture |


<a name="event.uploadComplete"></a>
## *uploadComplete [<sup>event</sup>](#head.Notifications)*

Triggered after uploading a screen capture.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.status | boolean | Indicates if the upload was successful |
| params.message | string | A `Success` value indicates that the upload was successful; otherwise, a description of the failure |
| params.call_guid | string | A unique identifier of the call |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.uploadComplete",
    "params": {
        "status": true,
        "message": "Success",
        "call_guid": "12345"
    }
}
```

