<!-- Generated automatically, DO NOT EDIT! -->
<a name="PowerManager_Plugin"></a>
# PowerManager Plugin

**Version: [1.0.0]()**

A org.rdk.PowerManager plugin for Thunder framework.

### Table of Contents

- [Abbreviation, Acronyms and Terms](#Abbreviation,_Acronyms_and_Terms)
- [Description](#Description)
- [Configuration](#Configuration)
- [Methods](#Methods)
- [Notifications](#Notifications)

<a name="Abbreviation,_Acronyms_and_Terms"></a>
# Abbreviation, Acronyms and Terms

[[Refer to this link](overview/aat.md)]

<a name="Description"></a>
# Description

The `PowerManager` that is responsible for persisting and notifying listeners of any change of these settings.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#Thunder)].

<a name="Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.PowerManager*) |
| classname | string | Class name: *org.rdk.PowerManager* |
| locator | string | Library name: *libWPEFrameworkPowerManager.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="Methods"></a>
# Methods

The following methods are provided by the org.rdk.PowerManager plugin:

PowerManager interface methods:

| Method | Description |
| :-------- | :-------- |
| [getOvertempGraceInterval](#getOvertempGraceInterval) | Returns the over-temperature grace interval value |
| [getPowerState](#getPowerState) | Returns the current power state of the device |
| [getThermalState](#getThermalState) | Returns temperature threshold values |
| [getTemperatureThresholds](#getTemperatureThresholds) | Returns temperature threshold values |
| [setOvertempGraceInterval](#setOvertempGraceInterval) | Sets the over-temperature grace interval value |
| [setPowerState](#setPowerState) | Sets the power state of the device |
| [setDeepSleepTimer](#setDeepSleepTimer) | Sets the deep sleep timeout period |
| [getWakeupReason](#getWakeupReason) | Returns the reason for the device coming out of deep sleep |
| [getLastWakeupKeyCode](#getLastWakeupKeyCode) | Returns the last wakeup keycode |
| [reboot](#reboot) | Requests that the system performs a reboot of the set-top box |
| [getNetworkStandbyMode](#getNetworkStandbyMode) | Returns the network standby mode of the device |
| [setNetworkStandbyMode](#setNetworkStandbyMode) | This API will be deprecated in the future |
| [setWakeupSrcConfig](#setWakeupSrcConfig) | Sets the wakeup source configuration for the input powerState |
| [getWakeupSrcConfig](#getWakeupSrcConfig) | Returns all the supported wakeup configurations and powerState |
| [setSystemMode](#setSystemMode) | Sets the mode of the set-top box for a specific duration before returning to normal mode |
| [getPowerStateBeforeReboot](#getPowerStateBeforeReboot) | Returns the power state before reboot |
| [setTemperatureThresholds](#setTemperatureThresholds) | Sets the temperature threshold values |


<a name="getOvertempGraceInterval"></a>
## *getOvertempGraceInterval*

Returns the over-temperature grace interval value. Not supported on all devices.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.graceInterval | integer |  |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getOvertempGraceInterval"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "graceInterval": 60
    }
}
```

<a name="getPowerState"></a>
## *getPowerState*

Returns the current power state of the device.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getPowerState"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "powerState": 2
    }
}
```

<a name="getThermalState"></a>
## *getThermalState*

Returns temperature threshold values. Not supported on all devices.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.temperature | float | The temperature |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getThermalState"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "temperature": 48.0
    }
}
```

<a name="getTemperatureThresholds"></a>
## *getTemperatureThresholds*

Returns temperature threshold values. Not supported on all devices.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.high | float | The warning threshold |
| result.critical | float | The max temperature threshold |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getTemperatureThresholds"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "high": 100.0,
        "critical": 110.0
    }
}
```

<a name="setOvertempGraceInterval"></a>
## *setOvertempGraceInterval*

Sets the over-temperature grace interval value. Not supported on all devices.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.graceInterval | integer |  |

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
    "method": "org.rdk.PowerManager.setOvertempGraceInterval",
    "params": {
        "graceInterval": 60
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

<a name="setPowerState"></a>
## *setPowerState*

Sets the power state of the device.

### Events

| Event | Description |
| :-------- | :-------- |
| [onPowerModeChanged](#onPowerModeChanged) | Triggers when the system power state changes |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| params.standbyReason | string | The reason for a standby state |

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
    "method": "org.rdk.PowerManager.setPowerState",
    "params": {
        "powerState": 2,
        "standbyReason": "APIUnitTest"
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

<a name="setDeepSleepTimer"></a>
## *setDeepSleepTimer*

Sets the deep sleep timeout period.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.deep_sleep_timeout | integer | The deep sleep timeout in seconds |

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
    "method": "org.rdk.PowerManager.setDeepSleepTimer",
    "params": {
        "deep_sleep_timeout": 3
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

<a name="getWakeupReason"></a>
## *getWakeupReason*

Returns the reason for the device coming out of deep sleep.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.wakeupReason | integer | The reason (must be one of the following: *WAKEUP_REASON_IR*, *WAKEUP_REASON_RCU_BT*, *WAKEUP_REASON_RCU_RF4CE*, *WAKEUP_REASON_GPIO*, *WAKEUP_REASON_LAN*, *WAKEUP_REASON_WLAN*, *WAKEUP_REASON_TIMER*, *WAKEUP_REASON_FRONT_PANEL*, *WAKEUP_REASON_WATCHDOG*, *WAKEUP_REASON_SOFTWARE_RESET*, *WAKEUP_REASON_THERMAL_RESET*, *WAKEUP_REASON_WARM_RESET*, *WAKEUP_REASON_COLDBOOT*, *WAKEUP_REASON_STR_AUTH_FAILURE*, *WAKEUP_REASON_CEC*, *WAKEUP_REASON_PRESENCE*, *WAKEUP_REASON_VOICE*, *WAKEUP_REASON_UNKNOWN*) |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getWakeupReason"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "wakeupReason": 7,
        "success": true
    }
}
```

<a name="getLastWakeupKeyCode"></a>
## *getLastWakeupKeyCode*

Returns the last wakeup keycode.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.wakeupKeyCode | integer | The last wakeup keycode |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getLastWakeupKeyCode"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "wakeupKeyCode": 59,
        "success": true
    }
}
```

<a name="reboot"></a>
## *reboot*

Requests that the system performs a reboot of the set-top box.

### Events

| Event | Description |
| :-------- | :-------- |
| [onRebootBegin](#onRebootBegin) | Triggers when a device reboot request is made |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.rebootReason | string | The reboot reason |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.IARM_Bus_Call_STATUS | integer | IARM BUS status |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.reboot",
    "params": {
        "rebootReason": "FIRMWARE_FAILURE"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "IARM_Bus_Call_STATUS": 0,
        "success": true
    }
}
```

<a name="getNetworkStandbyMode"></a>
## *getNetworkStandbyMode*

Returns the network standby mode of the device. If network standby is `true`, the device supports `WakeOnLAN` and `WakeOnWLAN` actions in STR mode.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.nwStandby | boolean | Whether `WakeOnLAN` and `WakeOnWLAN` is enabled (`true`); otherwise, `false` |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getNetworkStandbyMode"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "nwStandby": false,
        "success": true
    }
}
```

<a name="setNetworkStandbyMode"></a>
## *setNetworkStandbyMode*

This API will be deprecated in the future. Please refer setWakeupSrcConfiguration to Migrate. This API Enables or disables the network standby mode of the device. If network standby is enabled, the device supports `WakeOnLAN` and `WakeOnWLAN` actions in STR mode.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.nwStandby | boolean | Whether `WakeOnLAN` and `WakeOnWLAN` is enabled (`true`); otherwise, `false` |

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
    "method": "org.rdk.PowerManager.setNetworkStandbyMode",
    "params": {
        "nwStandby": false
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

<a name="setWakeupSrcConfig"></a>
## *setWakeupSrcConfig*

Sets the wakeup source configuration for the input powerState. if you are using setNetworkStandbyMode API, Please do not use this API to set LAN and WIFI wakeup. Please migrate to setWakeupSrcConfiguration API to control all wakeup source settings. This API does not persist. Please call this API on Every bootup to set the values.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.powerState | integer | <sup>*(optional)*</sup> The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| params.wakeupSources | array | Array of Key value pair with wake up sources and its configurations |
| params.wakeupSources[#] | object |  |
| params.wakeupSources[#]?.WAKEUPSRC_VOICE | boolean | <sup>*(optional)*</sup> Voice Wake up |
| params.wakeupSources[#]?.WAKEUPSRC_PRESENCE_DETECTION | boolean | <sup>*(optional)*</sup> Presense detection wake up |
| params.wakeupSources[#]?.WAKEUPSRC_BLUETOOTH | boolean | <sup>*(optional)*</sup> Bluetooth Wakeup |
| params.wakeupSources[#]?.WAKEUPSRC_WIFI | boolean | <sup>*(optional)*</sup> WiFi Wake up |
| params.wakeupSources[#]?.WAKEUPSRC_IR | boolean | <sup>*(optional)*</sup> IR Remote Wake up |
| params.wakeupSources[#]?.WAKEUPSRC_POWER_KEY | boolean | <sup>*(optional)*</sup> Power Button Wake up - GPIO |
| params.wakeupSources[#]?.WAKEUPSRC_CEC | boolean | <sup>*(optional)*</sup> HDMI CEC commadn Wake up |
| params.wakeupSources[#]?.WAKEUPSRC_LAN | boolean | <sup>*(optional)*</sup> LAN wake up |
| params.wakeupSources[#]?.WAKEUPSRC_TIMER | boolean | <sup>*(optional)*</sup> TImer Wake up |

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
    "method": "org.rdk.PowerManager.setWakeupSrcConfig",
    "params": {
        "powerState": 2,
        "wakeupSources": [
            {
                "WAKEUPSRC_VOICE": true,
                "WAKEUPSRC_PRESENCE_DETECTION": true,
                "WAKEUPSRC_BLUETOOTH": true,
                "WAKEUPSRC_WIFI": true,
                "WAKEUPSRC_IR": true,
                "WAKEUPSRC_POWER_KEY": true,
                "WAKEUPSRC_CEC": true,
                "WAKEUPSRC_LAN": true,
                "WAKEUPSRC_TIMER": true
            }
        ]
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

<a name="getWakeupSrcConfig"></a>
## *getWakeupSrcConfig*

Returns all the supported wakeup configurations and powerState.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| result.wakeupSources | array | Array of Key value pair with wake up sources and its configurations |
| result.wakeupSources[#] | object |  |
| result.wakeupSources[#]?.WAKEUPSRC_VOICE | boolean | <sup>*(optional)*</sup> Voice Wake up |
| result.wakeupSources[#]?.WAKEUPSRC_PRESENCE_DETECTION | boolean | <sup>*(optional)*</sup> Presense detection wake up |
| result.wakeupSources[#]?.WAKEUPSRC_BLUETOOTH | boolean | <sup>*(optional)*</sup> Bluetooth Wakeup |
| result.wakeupSources[#]?.WAKEUPSRC_WIFI | boolean | <sup>*(optional)*</sup> WiFi Wake up |
| result.wakeupSources[#]?.WAKEUPSRC_IR | boolean | <sup>*(optional)*</sup> IR Remote Wake up |
| result.wakeupSources[#]?.WAKEUPSRC_POWER_KEY | boolean | <sup>*(optional)*</sup> Power Button Wake up - GPIO |
| result.wakeupSources[#]?.WAKEUPSRC_CEC | boolean | <sup>*(optional)*</sup> HDMI CEC commadn Wake up |
| result.wakeupSources[#]?.WAKEUPSRC_LAN | boolean | <sup>*(optional)*</sup> LAN wake up |
| result.wakeupSources[#]?.WAKEUPSRC_TIMER | boolean | <sup>*(optional)*</sup> TImer Wake up |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getWakeupSrcConfig"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "powerState": 2,
        "wakeupSources": [
            {
                "WAKEUPSRC_VOICE": true,
                "WAKEUPSRC_PRESENCE_DETECTION": true,
                "WAKEUPSRC_BLUETOOTH": true,
                "WAKEUPSRC_WIFI": true,
                "WAKEUPSRC_IR": true,
                "WAKEUPSRC_POWER_KEY": true,
                "WAKEUPSRC_CEC": true,
                "WAKEUPSRC_LAN": true,
                "WAKEUPSRC_TIMER": true
            }
        ],
        "success": true
    }
}
```

<a name="setSystemMode"></a>
## *setSystemMode*

Sets the mode of the set-top box for a specific duration before returning to normal mode. Valid modes are:  
* `NORMAL` - The set-top box is operating in normal mode.  
* `EAS` - The set-top box is operating in Emergency Alert System (EAS) mode. This mode is set when the device needs to perform certain tasks when entering EAS mode, such as setting the clock display or preventing the user from using the diagnostics menu.  
* `WAREHOUSE` - The set-top box is operating in warehouse mode.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.currentMode | integer | Indicates the current operating mode of the STB (must be one of the following: *NORMAL*, *EAS*, *WAREHOUSE*) |
| params.newMode | integer | Sets the desired operating mode for the STB (must be one of the following: *NORMAL*, *EAS*, *WAREHOUSE*) |

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
    "method": "org.rdk.PowerManager.setSystemMode",
    "params": {
        "currentMode": 2,
        "newMode": 1
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

<a name="getPowerStateBeforeReboot"></a>
## *getPowerStateBeforeReboot*

Returns the power state before reboot.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.state | integer | The power state |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PowerManager.getPowerStateBeforeReboot"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "state": 2,
        "success": true
    }
}
```

<a name="setTemperatureThresholds"></a>
## *setTemperatureThresholds*

Sets the temperature threshold values. Not supported on all devices.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.high | float | The warning threshold |
| params.critical | float | The max temperature threshold |

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
    "method": "org.rdk.PowerManager.setTemperatureThresholds",
    "params": {
        "high": 100.0,
        "critical": 110.0
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

<a name="Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.PowerManager plugin:

PowerManager interface events:

| Event | Description |
| :-------- | :-------- |
| [onRebootBegin](#onRebootBegin) | Triggered when an application invokes the reboot method |
| [onPowerModeChanged](#onPowerModeChanged) | Triggered when the power manager detects a device power state change |
| [onPowerModePreChange](#onPowerModePreChange) | Triggered before change then device power state |
| [onDeepSleepTimeout](#onDeepSleepTimeout) | Triggered when the power manager detects a device power state change to light sleep from deep sleep |
| [onNetworkStandbyModeChanged](#onNetworkStandbyModeChanged) | Triggered when the network standby mode setting changes |
| [onThermalModeChanged](#onThermalModeChanged) | Triggered when the device temperature changes beyond the `WARN` or `MAX` limits (see `setTemperatureThresholds`) |


<a name="onRebootBegin"></a>
## *onRebootBegin*

Triggered when an application invokes the reboot 

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.requestedApp | string | The source of the reboot |
| params.rebootReason | string | The reboot reason |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onRebootBegin",
    "params": {
        "requestedApp": "SystemPlugin",
        "rebootReason": "FIRMWARE_FAILURE"
    }
}
```

<a name="onPowerModeChanged"></a>
## *onPowerModeChanged*

Triggered when the power manager detects a device power state change.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| params.currentPowerState | integer | The current power state |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onPowerModeChanged",
    "params": {
        "powerState": 2,
        "currentPowerState": 2
    }
}
```

<a name="onPowerModePreChange"></a>
## *onPowerModePreChange*

Triggered before change then device power state.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| params.currentPowerState | integer | The current power state |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onPowerModePreChange",
    "params": {
        "powerState": 2,
        "currentPowerState": 2
    }
}
```

<a name="onDeepSleepTimeout"></a>
## *onDeepSleepTimeout*

Triggered when the power manager detects a device power state change to light sleep from deep sleep.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.powerState | integer | The power state (must be one of the following: *STANDBY*, *DEEP_SLEEP*, *LIGHT_SLEEP*, *ON*) |
| params.currentPowerState | integer | The current power state |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onDeepSleepTimeout",
    "params": {
        "powerState": 2,
        "currentPowerState": 30
    }
}
```

<a name="onNetworkStandbyModeChanged"></a>
## *onNetworkStandbyModeChanged*

Triggered when the network standby mode setting changes.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.nwStandby | boolean | Network standby mode |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onNetworkStandbyModeChanged",
    "params": {
        "nwStandby": true
    }
}
```

<a name="onThermalModeChanged"></a>
## *onThermalModeChanged*

Triggered when the device temperature changes beyond the `WARN` or `MAX` limits (see `setTemperatureThresholds`). Not supported on all devices.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.thresholdType | integer | The exceeded threshold (must be one of the following: *MAX*, *MIN*) |
| params.exceeded | boolean | Whether the threshold exceeded the configured value |
| params.temperature | float | The temperature |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onThermalModeChanged",
    "params": {
        "thresholdType": 1,
        "exceeded": true,
        "temperature": 48.0
    }
}
```

