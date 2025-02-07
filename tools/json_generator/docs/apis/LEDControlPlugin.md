<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.LEDControl_Plugin"></a>
# LEDControl Plugin

**Version: [1.0.0]()**

A org.rdk.LEDControl plugin for Thunder framework.

### Table of Contents

- [Abbreviation, Acronyms and Terms](#head.Abbreviation,_Acronyms_and_Terms)
- [Description](#head.Description)
- [Configuration](#head.Configuration)
- [Methods](#head.Methods)

<a name="head.Abbreviation,_Acronyms_and_Terms"></a>
# Abbreviation, Acronyms and Terms

[[Refer to this link](overview/aat.md)]

<a name="head.Description"></a>
# Description

The `LEDControl` plugin allows you to control brightness and power state for LEDs on a device.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.LEDControl*) |
| classname | string | Class name: *org.rdk.LEDControl* |
| locator | string | Library name: *libWPEFrameworkLEDControl.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.LEDControl plugin:

LEDControl interface methods:

| Method | Description |
| :-------- | :-------- |
| [getSupportedLEDStates](#method.getSupportedLEDStates) | Returns all the LED states supported by the platform |
| [getLEDState](#method.getLEDState) | Returns current LED state |
| [setLEDState](#method.setLEDState) | Change the device LED state to one mentioned in the input argument |


<a name="method.getSupportedLEDStates"></a>
## *getSupportedLEDStates [<sup>method</sup>](#head.Methods)*

Returns all the LED states supported by the platform.

### Events

No Events

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
    "method": "org.rdk.LEDControl.getSupportedLEDStates"
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

<a name="method.getLEDState"></a>
## *getLEDState [<sup>method</sup>](#head.Methods)*

Returns current LED state.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.state | string | Indicates a platform supported LED state |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.LEDControl.getLEDState"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "state": "ACTIVE",
        "success": true
    }
}
```

<a name="method.setLEDState"></a>
## *setLEDState [<sup>method</sup>](#head.Methods)*

Change the device LED state to one mentioned in the input argument.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.state | string | Indicates a platform supported LED state |

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
    "method": "org.rdk.LEDControl.setLEDState",
    "params": {
        "state": "ACTIVE"
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

