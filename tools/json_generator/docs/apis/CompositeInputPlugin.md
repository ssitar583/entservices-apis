<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.CompositeInput_Plugin"></a>
# CompositeInput Plugin

**Version: [1.0.0]()**

A org.rdk.CompositeInput plugin for Thunder framework.

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

The `CompositeInput` Plugin allows you to control the composite input source on a device.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

> This Plugin is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new plugin](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin)

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.CompositeInput*) |
| classname | string | Class name: *org.rdk.CompositeInput* |
| locator | string | Library name: *libWPEFrameworkCompositeInput.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.CompositeInput plugin:

CompositeInput interface methods:

| Method | Description |
| :-------- | :-------- |
| [getCompositeInputDevices](#method.getCompositeInputDevices) | returns a list of composite input devices |
| [setVideoRectangle](#method.setVideoRectangle) | Sets the composite input video window |
| [startCompositeInput](#method.startCompositeInput) | Activates the specified composite input as the primary video source |
| [stopCompositeInput](#method.stopCompositeInput) | Deactivates the current composite input source that is the primary video source |


<a name="method.getCompositeInputDevices"></a>
## *getCompositeInputDevices [<sup>method</sup>](#head.Methods)*

returns a list of composite input devices.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=getinputdevices)

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.devices | array | An object array that lists the composite input ports on the device |
| result.devices[#] | object |  |
| result.devices[#].id | number | The ID of the composite input source |
| result.devices[#].locator | string | The location of the input source on the device |
| result.devices[#].connected | boolean | `true` if the input source is connected, otherwise `false` |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.CompositeInput.getCompositeInputDevices"
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
                "locator": "cvbsin://localhost/deviceid/0",
                "connected": true
            }
        ],
        "success": true
    }
}
```

<a name="method.setVideoRectangle"></a>
## *setVideoRectangle [<sup>method</sup>](#head.Methods)*

Sets the composite input video window.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=setvideorectangle)

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
    "method": "org.rdk.CompositeInput.setVideoRectangle",
    "params": {
        "x": 900,
        "y": 500,
        "w": 1920,
        "h": 1080
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

<a name="method.startCompositeInput"></a>
## *startCompositeInput [<sup>method</sup>](#head.Methods)*

Activates the specified composite input as the primary video source.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=startinput)

### Events

| Event | Description |
| :-------- | :-------- |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggers this event when activates composite input source and input status changes to started |
| [onSignalChanged](#event.onSignalChanged) | Triggers this event when composite input signal changes (must be one of the following:noSignal, unstableSignal, notSupportedSignal, stableSignal) |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.portId | number | The id of a composite input source as returned by `getCompositeInputDevices` |

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
    "method": "org.rdk.CompositeInput.startCompositeInput",
    "params": {
        "portId": 0
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

<a name="method.stopCompositeInput"></a>
## *stopCompositeInput [<sup>method</sup>](#head.Methods)*

Deactivates the current composite input source that is the primary video source.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=stopinput)

### Events

| Event | Description |
| :-------- | :-------- |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggers this event when deactivates composite input source and input status changes to stopped |
### Parameters

This method takes no parameters.

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
    "method": "org.rdk.CompositeInput.stopCompositeInput"
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

The following events are provided by the org.rdk.CompositeInput plugin:

CompositeInput interface events:

| Event | Description |
| :-------- | :-------- |
| [onDevicesChanged](#event.onDevicesChanged) | Triggered when the composite input device changes |
| [onInputStatusChanged](#event.onInputStatusChanged) | Triggered when the status of the composite input changes |
| [onSignalChanged](#event.onSignalChanged) | Triggered when the status of the composite input signal changes |


<a name="event.onDevicesChanged"></a>
## *onDevicesChanged [<sup>event</sup>](#head.Notifications)*

Triggered when the composite input device changes.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=ondeviceschanged)

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.devices | array | An object array that lists the composite input ports on the device |
| params.devices[#] | object |  |
| params.devices[#].id | number | The ID of the composite input source |
| params.devices[#].locator | string | The location of the input source on the device |
| params.devices[#].connected | boolean | `true` if the input source is connected, otherwise `false` |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onDevicesChanged",
    "params": {
        "devices": [
            {
                "id": 0,
                "locator": "cvbsin://localhost/deviceid/0",
                "connected": true
            }
        ]
    }
}
```

<a name="event.onInputStatusChanged"></a>
## *onInputStatusChanged [<sup>event</sup>](#head.Notifications)*

Triggered when the status of the composite input changes.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=oninputstatuschanged)

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The ID of the composite input source |
| params.locator | string | The location of the input source on the device |
| params.status | string | The status of the composite input source. (must be one of the following: *started*, *stopped*) |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onInputStatusChanged",
    "params": {
        "id": 0,
        "locator": "cvbsin://localhost/deviceid/0",
        "status": "started"
    }
}
```

<a name="event.onSignalChanged"></a>
## *onSignalChanged [<sup>event</sup>](#head.Notifications)*

Triggered when the status of the composite input signal changes.

> This API is **deprecated** and may be removed in the future. It is no longer recommended for use in new implementations. [Refer this link for the new api](https://rdkcentral.github.io/rdkservices/#/api/AVInputPlugin?id=onsignalchanged)

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.id | number | The ID of the composite input source |
| params.locator | string | The location of the input source on the device |
| params.signalStatus | string | The status of the composite input source signal. (must be one of the following: *noSignal*, *unstableSignal*, *notSupportedSignal*, *stableSignal*, *none*) |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onSignalChanged",
    "params": {
        "id": 0,
        "locator": "cvbsin://localhost/deviceid/0",
        "signalStatus": "noSignal"
    }
}
```

