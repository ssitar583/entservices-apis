<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.AVInput_Plugin"></a>
# AVInput Plugin

**Version: [1.0.0]()**

A org.rdk.AVInput plugin for Thunder framework.

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

The `AVInput` plugin allows you to control the Hdmi and Composite input source on a device.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.AVInput*) |
| classname | string | Class name: *org.rdk.AVInput* |
| locator | string | Library name: *libWPEFrameworkAVInput.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.AVInput plugin:

AVInput interface methods:

| Method | Description |
| :-------- | :-------- |
| [contentProtected](#method.contentProtected) | Returns `true` if the content coming in the HDMI input is protected; otherwise, it returns `false` |
| [currentVideoMode](#method.currentVideoMode) | Returns a string encoding the video mode being supplied by the device currently attached to the HDMI input |
| [numberOfInputs](#method.numberOfInputs) | Returns an integer that specifies the number of available inputs |
| [getInputDevices](#method.getInputDevices) | Returns an array of available HDMI/Composite Input ports |
| [getEdid2AllmSupport](#method.getEdid2AllmSupport) | Returns the EDID ALLM bit value |
| [getEdidVersion](#method.getEdidVersion) | Returns the EDID version |
| [getSPD](#method.getSPD) | Returns the Source Data Product Descriptor (SPD) infoFrame packet information for the specified HDMI Input device |
| [getRawSPD](#method.getRawSPD) | Returns the Source Data Product Descriptor (SPD) infoFrame packet information for the specified HDMI Input device as raw bits |
| [readEDID](#method.readEDID) | Returns the current EDID value |
| [startInput](#method.startInput) | Activates the specified HDMI/Composite Input port as the primary video source |
| [stopInput](#method.stopInput) | Deactivates the HDMI/Composite Input port currently selected as the primary video source |
| [setAudioMixerLevels](#method.setAudioMixerLevels) | Sets the audio mixer level for given audio input |
| [setEdid2AllmSupport](#method.setEdid2AllmSupport) | Sets an HDMI ALLM bit in EDID |
| [setEdidVersion](#method.setEdidVersion) | Sets an HDMI EDID version |
| [setVideoRectangle](#method.setVideoRectangle) | Sets an HDMI/Composite Input video window |
| [writeEDID](#method.writeEDID) | Changes a current EDID value |
| [getSupportedGameFeatures](#method.getSupportedGameFeatures) | Returns the list of supported game features |
| [getGameFeatureStatus](#method.getGameFeatureStatus) | Returns the Game Feature Status |


<a name="method.contentProtected"></a>
## *contentProtected [<sup>method</sup>](#head.Methods)*

Returns `true` if the content coming in the HDMI input is protected; otherwise, it returns `false`. If the content is protected, then it is only presented if the component and composite outputs of the box are disabled.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object | An empty parameter object |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.isContentProtected | boolean | Whether the HDMI input is protected |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.contentProtected",
    "params": {}
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "isContentProtected": true,
        "success": true
    }
}
```

<a name="method.currentVideoMode"></a>
## *currentVideoMode [<sup>method</sup>](#head.Methods)*

Returns a string encoding the video mode being supplied by the device currently attached to the HDMI input. The format of the string is the same format used for the `resolutionName` parameter of the XRE `setResolution` messages. HDMI input is presentable if its resolution is less than or equal to the current Parker display resolution.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object | An empty parameter object |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.currentVideoMode | string | The current video mode |
| result.message | string | `Success` if plugin is activated successfully and gets the current Videomode. `org.rdk.HdmiInput plugin is not ready` if plugin is not activated or activation failed |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.currentVideoMode",
    "params": {}
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "currentVideoMode": "Unknown",
        "message": "Success",
        "success": true
    }
}
```

<a name="method.numberOfInputs"></a>
## *numberOfInputs [<sup>method</sup>](#head.Methods)*

Returns an integer that specifies the number of available inputs. For example, a value of `2` indicates that there are two available inputs that can be selected using `avin://input0` and `avin://input1`.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object | An empty parameter object |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.numberOfInputs | number | The number of inputs that are available for selection |
| result.message | string | `Success` if plugin is activated successfully and gets the current Videomode. `org.rdk.HdmiInput plugin is not ready` if plugin is not activated or activation failed |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.numberOfInputs",
    "params": {}
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "numberOfInputs": 1,
        "message": "Success",
        "success": true
    }
}
```

<a name="method.getInputDevices"></a>
## *getInputDevices [<sup>method</sup>](#head.Methods)*

Returns an array of available HDMI/Composite Input ports.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.typeOfInput | string | The type of Input - HDMI/COMPOSITE |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.devices | array | An object [] that describes each HDMI/Composite Input port |
| result.devices[#] | object |  |
| result.devices[#].id | number | The port identifier for the HDMI/Composite Input |
| result.devices[#].locator | string | A URL corresponding to the HDMI/Composite Input port |
| result.devices[#].connected | boolean | Whether a device is currently connected to this HDMI/Composite Input port |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 30 | ```ERROR_BAD_REQUEST``` | Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getInputDevices",
    "params": {
        "typeOfInput": "HDMI"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "devices": [
            {
                "id": 0,
                "locator": "hdmiin://localhost/deviceid/0",
                "connected": true
            }
        ]
    }
}
```

<a name="method.getEdid2AllmSupport"></a>
## *getEdid2AllmSupport [<sup>method</sup>](#head.Methods)*

Returns the EDID ALLM bit value.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.portId | string | <sup>*(optional)*</sup> An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.allmSupport | boolean | The ALLM bit value in edid |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getEdid2AllmSupport",
    "params": {
        "portId": "0"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "allmSupport": true,
        "success": true
    }
}
```

<a name="method.getEdidVersion"></a>
## *getEdidVersion [<sup>method</sup>](#head.Methods)*

Returns the EDID version.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.portId | string | <sup>*(optional)*</sup> An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.edidVersion | string | The EDID version |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getEdidVersion",
    "params": {
        "portId": "0"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "edidVersion": "HDMI2.0"
    }
}
```

<a name="method.getSPD"></a>
## *getSPD [<sup>method</sup>](#head.Methods)*

Returns the Source Data Product Descriptor (SPD) infoFrame packet information for the specified HDMI Input device. The SPD infoFrame packet includes vendor name, product description, and source information.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.portId | string | <sup>*(optional)*</sup> An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.HDMISPD | string | The SPD information |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getSPD",
    "params": {
        "portId": "0"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "HDMISPD": "..."
    }
}
```

<a name="method.getRawSPD"></a>
## *getRawSPD [<sup>method</sup>](#head.Methods)*

Returns the Source Data Product Descriptor (SPD) infoFrame packet information for the specified HDMI Input device as raw bits.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | string | An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.HDMISPD | string | The SPD information as raw bits |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getRawSPD",
    "params": {
        "portId": "0"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "HDMISPD": "..."
    }
}
```

<a name="method.readEDID"></a>
## *readEDID [<sup>method</sup>](#head.Methods)*

Returns the current EDID value.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | string | An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.EDID | string | The EDID Value |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.readEDID",
    "params": {
        "portId": "0"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "EDID": "..."
    }
}
```

<a name="method.startInput"></a>
## *startInput [<sup>method</sup>](#head.Methods)*

Activates the specified HDMI/Composite Input port as the primary video source.

### Events

| Event | Description |
| :-------- | :-------- |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggers the event when HDMI/Composite Input source is activated and Input status changes to `started` |
| [onSignalChanged](#event.onSignalChanged) | Triggers the event when HDMI/Composite Input signal changes (must be one of the following:noSignal, unstableSignal, notSupportedSignal, stableSignal) |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.portId | string | <sup>*(optional)*</sup> An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |
| params.typeOfInput | string | The type of Input - HDMI/COMPOSITE |
| params?.audioMix | boolean | <sup>*(optional)*</sup> Defines whether the Audio mixing is true or false, This is an optional argument |
| params?.planeType | integer | <sup>*(optional)*</sup> Defines whether the video plane type, 0 - Primary video plane, 1 - Secondary Video Plane, Other values - Invalid - This is an optional argument  |
| params?.topMost | boolean | <sup>*(optional)*</sup> Defines whether the Hdmi Input should be over or under the other video plane |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId/Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.startInput",
    "params": {
        "portId": "0",
        "typeOfInput": "HDMI",
        "audioMix": true,
        "planeType": 0,
        "topMost": true
    }
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

<a name="method.stopInput"></a>
## *stopInput [<sup>method</sup>](#head.Methods)*

Deactivates the HDMI/Composite Input port currently selected as the primary video source.

### Events

| Event | Description |
| :-------- | :-------- |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggers the event when HDMI/Composite Input source is deactivated and Input status changes to `stopped` |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.typeOfInput | string | The type of Input - HDMI/COMPOSITE |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.stopInput",
    "params": {
        "typeOfInput": "HDMI"
    }
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

<a name="method.setAudioMixerLevels"></a>
## *setAudioMixerLevels [<sup>method</sup>](#head.Methods)*

Sets the audio mixer level for given audio input.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.primaryVolume | integer | Primary audio input volume |
| params.inputVolume | integer | System audio input volume |

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
    "method": "org.rdk.AVInput.setAudioMixerLevels",
    "params": {
        "primaryVolume": 100,
        "inputVolume": 75
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

<a name="method.setEdid2AllmSupport"></a>
## *setEdid2AllmSupport [<sup>method</sup>](#head.Methods)*

Sets an HDMI ALLM bit in EDID.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | string | An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |
| params.allmSupport | boolean | The ALLM support in EDID |

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
    "method": "org.rdk.AVInput.setEdid2AllmSupport",
    "params": {
        "portId": "0",
        "allmSupport": true
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

<a name="method.setEdidVersion"></a>
## *setEdidVersion [<sup>method</sup>](#head.Methods)*

Sets an HDMI EDID version.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | string | An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |
| params.edidVersion | string | The EDID version |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | portId/edidVersion is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.setEdidVersion",
    "params": {
        "portId": "0",
        "edidVersion": "HDMI2.0"
    }
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

<a name="method.setVideoRectangle"></a>
## *setVideoRectangle [<sup>method</sup>](#head.Methods)*

Sets an HDMI/Composite Input video window.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.x | integer | The x-coordinate of the video rectangle |
| params.y | integer | The y-coordinate of the video rectangle |
| params.w | integer | The width of the video rectangle |
| params.h | integer | The height of the video rectangle |
| params.typeOfInput | string | The type of Input - HDMI/COMPOSITE |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |
| 30 | ```ERROR_BAD_REQUEST``` | Coordinates/Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.setVideoRectangle",
    "params": {
        "x": 0,
        "y": 0,
        "w": 1920,
        "h": 1080,
        "typeOfInput": "HDMI"
    }
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

<a name="method.writeEDID"></a>
## *writeEDID [<sup>method</sup>](#head.Methods)*

Changes a current EDID value.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | string | An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |
| params.message | string | A new EDID value |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 30 | ```ERROR_BAD_REQUEST``` | Coordinates/Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.writeEDID",
    "params": {
        "portId": "0",
        "message": "EDID"
    }
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

<a name="method.getSupportedGameFeatures"></a>
## *getSupportedGameFeatures [<sup>method</sup>](#head.Methods)*

Returns the list of supported game features.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.supportedGameFeatures | array | The supported game Features |
| result.supportedGameFeatures[#] | string |  |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | General error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getSupportedGameFeatures"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "supportedGameFeatures": [
            "ALLM"
        ]
    }
}
```

<a name="method.getGameFeatureStatus"></a>
## *getGameFeatureStatus [<sup>method</sup>](#head.Methods)*

Returns the Game Feature Status. For example: ALLM.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.portId | string | <sup>*(optional)*</sup> An ID of an HDMI/Composite Input port as returned by the `getInputDevices` method |
| params.gameFeature | string | Game Feature to which current status requested |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.mode | boolean | The current game feature status. Mode is required only for ALLM. Need to add support for future game features |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 30 | ```ERROR_BAD_REQUEST``` | Coordinates/Type of Input is invalid |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.AVInput.getGameFeatureStatus",
    "params": {
        "portId": "0",
        "gameFeature": "ALLM"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "mode": true
    }
}
```

<a name="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.AVInput plugin:

AVInput interface events:

| Event | Description |
| :-------- | :-------- |
| [onDevicesChanged](#event.onDevicesChanged) | Triggered whenever a new HDMI/Composite device is connected to an HDMI/Composite Input |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggered whenever the status changes for an HDMI/Composite Input |
| [onSignalChanged](#event.onSignalChanged) | Triggered whenever the signal status changes for an HDMI/Composite Input |
| [videoStreamInfoUpdate](#event.videoStreamInfoUpdate) | Triggered whenever there is an update in HDMI Input video stream info |
| [gameFeatureStatusUpdate](#event.gameFeatureStatusUpdate) | Triggered whenever game feature(ALLM) status changes for an HDMI Input |
| [hdmiContentTypeUpdate](#event.hdmiContentTypeUpdate) | Triggered whenever AV Infoframe content type changes for an HDMI Input |


<a name="event.onDevicesChanged"></a>
## *onDevicesChanged [<sup>event</sup>](#head.Notifications)*

Triggered whenever a new HDMI/Composite device is connected to an HDMI/Composite Input.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.devices | array | An object [] that describes each HDMI/Composite Input port |
| params.devices[#] | object |  |
| params.devices[#].id | number | The port identifier for the HDMI/Composite Input |
| params.devices[#].locator | string | A URL corresponding to the HDMI/Composite Input port |
| params.devices[#].connected | boolean | Whether a device is currently connected to this HDMI/Composite Input port |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onDevicesChanged",
    "params": {
        "devices": [
            {
                "id": 0,
                "locator": "hdmiin://localhost/deviceid/0",
                "connected": true
            }
        ]
    }
}
```

<a name="event.onInputStatusChanged"></a>
## *onInputStatusChanged [<sup>event</sup>](#head.Notifications)*

Triggered whenever the status changes for an HDMI/Composite Input.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The port identifier for the HDMI/Composite Input |
| params.locator | string | A URL corresponding to the HDMI/Composite Input port |
| params.status | string | Status of the HDMI/Composite Input. Valid values are `started` or `stopped` |
| params?.plane | integer | <sup>*(optional)*</sup> Defines whether the video plane type, 0 - Primary video plane, 1 - Secondary Video Plane, Other values - Invalid  |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onInputStatusChanged",
    "params": {
        "id": 0,
        "locator": "hdmiin://localhost/deviceid/0",
        "status": "started",
        "plane": 0
    }
}
```

<a name="event.onSignalChanged"></a>
## *onSignalChanged [<sup>event</sup>](#head.Notifications)*

Triggered whenever the signal status changes for an HDMI/Composite Input.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The port identifier for the HDMI/Composite Input |
| params.locator | string | A URL corresponding to the HDMI/Composite Input port |
| params.signalStatus | string | Signal Status of the HDMI/Composite Input. Valid values are `noSignal`, `unstableSignal`, `notSupportedSignal`, `stableSignal` |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onSignalChanged",
    "params": {
        "id": 0,
        "locator": "hdmiin://localhost/deviceid/0",
        "signalStatus": "stableSignal"
    }
}
```

<a name="event.videoStreamInfoUpdate"></a>
## *videoStreamInfoUpdate [<sup>event</sup>](#head.Notifications)*

Triggered whenever there is an update in HDMI Input video stream info.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The port identifier for the HDMI/Composite Input |
| params.locator | string | A URL corresponding to the HDMI/Composite Input port |
| params.width | integer | Width of the Video Stream |
| params.height | integer | Height of the Video Stream |
| params.progressive | boolean | Whether the streaming video is progressive or not? |
| params.frameRateN | integer | FrameRate Numerator |
| params.frameRateD | integer | FrameRate Denomirator |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.videoStreamInfoUpdate",
    "params": {
        "id": 0,
        "locator": "hdmiin://localhost/deviceid/0",
        "width": 3840,
        "height": 2160,
        "progressive": true,
        "frameRateN": 60000,
        "frameRateD": 1001
    }
}
```

<a name="event.gameFeatureStatusUpdate"></a>
## *gameFeatureStatusUpdate [<sup>event</sup>](#head.Notifications)*

Triggered whenever game feature(ALLM) status changes for an HDMI Input.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The port identifier for the HDMI/Composite Input |
| params.gameFeature | string | Game Feature to which current status requested |
| params.mode | boolean | The current game feature status. Mode is required only for ALLM. Need to add support for future game features |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.gameFeatureStatusUpdate",
    "params": {
        "id": 0,
        "gameFeature": "ALLM",
        "mode": true
    }
}
```

<a name="event.hdmiContentTypeUpdate"></a>
## *hdmiContentTypeUpdate [<sup>event</sup>](#head.Notifications)*

Triggered whenever AV Infoframe content type changes for an HDMI Input.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | integer | Hdmi Input port ID for which content type change event received and possible values are port id 0, 1 and 2 for three Hdmi Input ports |
| params.aviContentType | integer | new Content type received for the active hdmi input port and the possible integer values indicates following accordingly 0 - Graphics, 1 - Photo, 2 - Cinema, 3 - Game, 4 - Invalid data |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.hdmiContentTypeUpdate",
    "params": {
        "id": 1,
        "aviContentType": 1
    }
}
```

