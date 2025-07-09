<!-- Generated automatically, DO NOT EDIT! -->
<a id="head.PowerManager_Plugin"></a>
# PowerManager Plugin

**Version: [1.0.0](https://github.com/rdkcentral/rdkservices/blob/main/PowerManager/CHANGELOG.md)**

A PowerManager plugin for Thunder framework.

### Table of Contents

- [Abbreviation, Acronyms and Terms](#head.Abbreviation,_Acronyms_and_Terms)
- [Description](#head.Description)
- [Configuration](#head.Configuration)
- [Methods](#head.Methods)
- [Properties](#head.Properties)

<a id="head.Abbreviation,_Acronyms_and_Terms"></a>
# Abbreviation, Acronyms and Terms

[[Refer to this link](userguide/aat.md)]

<a id="head.Description"></a>
# Description

The `PowerManager` plugin provides an interface for PowerManager.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a id="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: org.rdk.PowerManager) |
| classname | string | Class name: *PowerManager* |
| locator | string | Library name: *libWPEFrameworkPowerManager.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a id="head.Methods"></a>
# Methods

The following methods are provided by the PowerManager plugin:

PowerManager interface methods:

| Method | Description |
| :-------- | :-------- |
| [addPowerModePreChangeClient](#method.addPowerModePreChangeClient) | Register a client to engage in power mode state changes. Added client should call either - `PowerModePreChangeComplete` API to inform power manager that this client has completed its pre-change operation. - Or `DelayPowerModeChangeBy` API to delay the power mode change. If the client does not call `PowerModePreChangeComplete` API, the power mode change will complete after the maximum delay `stateChangeAfter` seconds (as received in `OnPowerModePreChange` event).  IMPORTANT: ** IT'S A BUG IF CLIENT `Unregister` FROM `IModePreChangeNotification` BEFORE DISENGAGING ITSELF ** always make sure to call `RemovePowerModePreChangeClient` before calling `Unregister` from `IModePreChangeNotification`.  |
| [delayPowerModeChangeBy](#method.delayPowerModeChangeBy) | Delay Powermode change by given time. If different clients provide different values of delay, then the maximum of these values is used. |
| [getNetworkStandbyMode](#method.getNetworkStandbyMode) | Get the standby mode for Network |
| [getPowerState](#method.getPowerState) | Get Power State |
| [getPowerStateBeforeReboot](#method.getPowerStateBeforeReboot) | Get Power state before reboot |
| [getTemperatureThresholds](#method.getTemperatureThresholds) | Get Temperature Thresholds |
| [getThermalState](#method.getThermalState) | Get Current Thermal State (temperature) |
| [getWakeupSrcConfig](#method.getWakeupSrcConfig) | Get the source configuration for device wakeup |
| [onDeepSleepTimeout](#method.onDeepSleepTimeout) | Deep sleep timeout event |
| [onNetworkStandbyModeChanged](#method.onNetworkStandbyModeChanged) | Network Standby Mode changed event - only on XIone |
| [onPowerModeChanged](#method.onPowerModeChanged) | Power mode changed |
| [onPowerModePreChange](#method.onPowerModePreChange) | Power mode Pre-change event |
| [onRebootBegin](#method.onRebootBegin) | Reboot begin event |
| [onThermalModeChanged](#method.onThermalModeChanged) | Thermal Mode changed event |
| [powerModePreChangeComplete](#method.powerModePreChangeComplete) | Pre power mode handling complete for given client and transation id |
| [reboot](#method.reboot) | Reboot device |
| [removePowerModePreChangeClient](#method.removePowerModePreChangeClient) | Removes a registered client from participating in power mode pre-change operations. NOTE client will still continue to receive pre-change notifications. |
| [setPowerState](#method.setPowerState) | Set Power State |
| [setSystemMode](#method.setSystemMode) | System mode change |
| [setTemperatureThresholds](#method.setTemperatureThresholds) | Set Temperature Thresholds |
| [setWakeupSrcConfig](#method.setWakeupSrcConfig) | Set the source configuration for device wakeup |

<a id="method.addPowerModePreChangeClient"></a>
## *addPowerModePreChangeClient [<sup>method</sup>](#head.Methods)*

Register a client to engage in power mode state changes. Added client should call either - `PowerModePreChangeComplete` API to inform power manager that this client has completed its pre-change operation. - Or `DelayPowerModeChangeBy` API to delay the power mode change. If the client does not call `PowerModePreChangeComplete` API, the power mode change will complete after the maximum delay `stateChangeAfter` seconds (as received in `OnPowerModePreChange` event).  IMPORTANT: ** IT'S A BUG IF CLIENT `Unregister` FROM `IModePreChangeNotification` BEFORE DISENGAGING ITSELF ** always make sure to call `RemovePowerModePreChangeClient` before calling `Unregister` from `IModePreChangeNotification`. 

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.clientName | string | Name of the client |
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.clientId | uint32_t | Unique identifier for the client to be used while acknowledging the pre-change operation (`PowerModePreChangeComplete`) or to delay the power mode change (`DelayPowerModeChangeBy`) |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 0,
    "method": "org.rdk.PowerManager.addPowerModePreChangeClient",
    "params": {
        "clientName": ""
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 0,
    "result": 0
}
```

<a id="method.delayPowerModeChangeBy"></a>
## *delayPowerModeChangeBy [<sup>method</sup>](#head.Methods)*

Delay Powermode change by given time. If different clients provide different values of delay, then the maximum of these values is used.

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.clientId | uint32_t | Unique identifier for the client to be used while acknowledging the pre-change operation (`PowerModePreChangeComplete`) or to delay the power mode change (`DelayPowerModeChangeBy`) |
| params.transactionId | int | transactionId to be used when invoking prePowerChangeComplete() / delayPowerModeChangeBy API |
| params.delayPeriod | int | delay in seconds |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 1,
    "method": "org.rdk.PowerManager.delayPowerModeChangeBy",
    "params": {
        "clientId": 0,
        "transactionId": 0,
        "delayPeriod": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 1,
    "result": null
}
```

<a id="method.getNetworkStandbyMode"></a>
## *getNetworkStandbyMode [<sup>method</sup>](#head.Methods)*

Get the standby mode for Network

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.standbyMode | bool | Network standby mode |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 2,
    "method": "org.rdk.PowerManager.getNetworkStandbyMode"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 2,
    "result": true
}
```

<a id="method.getPowerState"></a>
## *getPowerState [<sup>method</sup>](#head.Methods)*

Get Power State

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.currentState | PowerState | Current Power State |
| result.previousState | PowerState | - |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 3,
    "method": "org.rdk.PowerManager.getPowerState"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 3,
    "result": {
        "currentState": "POWER_STATE_UNKNOWN",
        "previousState": "POWER_STATE_UNKNOWN"
    }
}
```

<a id="method.getPowerStateBeforeReboot"></a>
## *getPowerStateBeforeReboot [<sup>method</sup>](#head.Methods)*

Get Power state before reboot

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.powerStateBeforeReboot | PowerState | power state |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 4,
    "method": "org.rdk.PowerManager.getPowerStateBeforeReboot"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 4,
    "result": "POWER_STATE_UNKNOWN"
}
```

<a id="method.getTemperatureThresholds"></a>
## *getTemperatureThresholds [<sup>method</sup>](#head.Methods)*

Get Temperature Thresholds

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.high | float | high threshold |
| result.critical | float | critical threshold |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 5,
    "method": "org.rdk.PowerManager.getTemperatureThresholds"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 5,
    "result": {
        "high": 0.0,
        "critical": 0.0
    }
}
```

<a id="method.getThermalState"></a>
## *getThermalState [<sup>method</sup>](#head.Methods)*

Get Current Thermal State (temperature)

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.currentTemperature | float | current temperature |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 6,
    "method": "org.rdk.PowerManager.getThermalState"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 6,
    "result": 0.0
}
```

<a id="method.getWakeupSrcConfig"></a>
## *getWakeupSrcConfig [<sup>method</sup>](#head.Methods)*

Get the source configuration for device wakeup

### Events
No events are associated with this method.
### Parameters
This method takes no parameters.
### Results
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result.powerMode | int | power mode |
| result.srcType | int | source type |
| result.config | int | config |

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 7,
    "method": "org.rdk.PowerManager.getWakeupSrcConfig"
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 7,
    "result": {
        "powerMode": 0,
        "srcType": 0,
        "config": 0
    }
}
```

<a id="method.onDeepSleepTimeout"></a>
## *onDeepSleepTimeout [<sup>method</sup>](#head.Methods)*

Deep sleep timeout event

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.wakeupTimeout | int | Deep sleep wakeup timeout in seconds |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 8,
    "method": "org.rdk.PowerManager.onDeepSleepTimeout",
    "params": {
        "wakeupTimeout": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 8,
    "result": null
}
```

<a id="method.onNetworkStandbyModeChanged"></a>
## *onNetworkStandbyModeChanged [<sup>method</sup>](#head.Methods)*

Network Standby Mode changed event - only on XIone

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.enabled | bool | network standby enabled or disabled |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 9,
    "method": "org.rdk.PowerManager.onNetworkStandbyModeChanged",
    "params": {
        "enabled": true
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 9,
    "result": null
}
```

<a id="method.onPowerModeChanged"></a>
## *onPowerModeChanged [<sup>method</sup>](#head.Methods)*

Power mode changed

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.currentState | PowerState | Current Power State |
| params.newState | PowerState | Changing power state to this New Power State |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 10,
    "method": "org.rdk.PowerManager.onPowerModeChanged",
    "params": {
        "currentState": "POWER_STATE_UNKNOWN",
        "newState": "POWER_STATE_UNKNOWN"
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 10,
    "result": null
}
```

<a id="method.onPowerModePreChange"></a>
## *onPowerModePreChange [<sup>method</sup>](#head.Methods)*

Power mode Pre-change event

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.currentState | PowerState | Current Power State |
| params.newState | PowerState | Changing power state to this New Power State |
| params.transactionId | int | transactionId to be used when invoking prePowerChangeComplete() / delayPowerModeChangeBy API |
| params.stateChangeAfter | int | seconds after which the actual power mode will be applied. |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 11,
    "method": "org.rdk.PowerManager.onPowerModePreChange",
    "params": {
        "currentState": "POWER_STATE_UNKNOWN",
        "newState": "POWER_STATE_UNKNOWN",
        "transactionId": 0,
        "stateChangeAfter": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 11,
    "result": null
}
```

<a id="method.onRebootBegin"></a>
## *onRebootBegin [<sup>method</sup>](#head.Methods)*

Reboot begin event

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.rebootReasonCustom | string | Reboot reason custom |
| params.rebootReasonOther | string | Reboot reason other |
| params.rebootRequestor | string | Reboot requested by |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 12,
    "method": "org.rdk.PowerManager.onRebootBegin",
    "params": {
        "rebootReasonCustom": "",
        "rebootReasonOther": "",
        "rebootRequestor": ""
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 12,
    "result": null
}
```

<a id="method.onThermalModeChanged"></a>
## *onThermalModeChanged [<sup>method</sup>](#head.Methods)*

Thermal Mode changed event

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.currentThermalLevel | ThermalTemperature | current thermal level |
| params.newThermalLevel | ThermalTemperature | new thermal level |
| params.currentTemperature | float | current temperature |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 13,
    "method": "org.rdk.PowerManager.onThermalModeChanged",
    "params": {
        "currentThermalLevel": "THERMAL_TEMPERATURE_UNKNOWN",
        "newThermalLevel": "THERMAL_TEMPERATURE_UNKNOWN",
        "currentTemperature": 0.0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 13,
    "result": null
}
```

<a id="method.powerModePreChangeComplete"></a>
## *powerModePreChangeComplete [<sup>method</sup>](#head.Methods)*

Pre power mode handling complete for given client and transation id

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.clientId | uint32_t | Unique identifier for the client to be used while acknowledging the pre-change operation (`PowerModePreChangeComplete`) or to delay the power mode change (`DelayPowerModeChangeBy`) |
| params.transactionId | int | transactionId to be used when invoking prePowerChangeComplete() / delayPowerModeChangeBy API |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 14,
    "method": "org.rdk.PowerManager.powerModePreChangeComplete",
    "params": {
        "clientId": 0,
        "transactionId": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 14,
    "result": null
}
```

<a id="method.reboot"></a>
## *reboot [<sup>method</sup>](#head.Methods)*

Reboot device

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.rebootRequestor | string | Reboot requested by |
| params.rebootReasonCustom | string | Reboot reason custom |
| params.rebootReasonOther | string | Reboot reason other |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 15,
    "method": "org.rdk.PowerManager.reboot",
    "params": {
        "rebootRequestor": "",
        "rebootReasonCustom": "",
        "rebootReasonOther": ""
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 15,
    "result": null
}
```

<a id="method.removePowerModePreChangeClient"></a>
## *removePowerModePreChangeClient [<sup>method</sup>](#head.Methods)*

Removes a registered client from participating in power mode pre-change operations. NOTE client will still continue to receive pre-change notifications.

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.clientId | uint32_t | Unique identifier for the client to be used while acknowledging the pre-change operation (`PowerModePreChangeComplete`) or to delay the power mode change (`DelayPowerModeChangeBy`) |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 16,
    "method": "org.rdk.PowerManager.removePowerModePreChangeClient",
    "params": {
        "clientId": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 16,
    "result": null
}
```

<a id="method.setPowerState"></a>
## *setPowerState [<sup>method</sup>](#head.Methods)*

Set Power State

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.keyCode | int | - |
| params.powerState | PowerState | Set power to this state |
| params.reason | string | Reason for moving to the power state |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 17,
    "method": "org.rdk.PowerManager.setPowerState",
    "params": {
        "keyCode": 0,
        "powerState": "POWER_STATE_UNKNOWN",
        "reason": ""
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 17,
    "result": null
}
```

<a id="method.setSystemMode"></a>
## *setSystemMode [<sup>method</sup>](#head.Methods)*

System mode change

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.currentMode | SystemMode | - |
| params.newMode | SystemMode | new mode |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 18,
    "method": "org.rdk.PowerManager.setSystemMode",
    "params": {
        "currentMode": "SYSTEM_MODE_UNKNOWN",
        "newMode": "SYSTEM_MODE_UNKNOWN"
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 18,
    "result": null
}
```

<a id="method.setTemperatureThresholds"></a>
## *setTemperatureThresholds [<sup>method</sup>](#head.Methods)*

Set Temperature Thresholds

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.high | float | high threshold |
| params.critical | float | critical threshold |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 19,
    "method": "org.rdk.PowerManager.setTemperatureThresholds",
    "params": {
        "high": 0.0,
        "critical": 0.0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 19,
    "result": null
}
```

<a id="method.setWakeupSrcConfig"></a>
## *setWakeupSrcConfig [<sup>method</sup>](#head.Methods)*

Set the source configuration for device wakeup

### Events
No events are associated with this method.
### Parameters
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.powerMode | int | power mode |
| params.wakeSrcType | int | source type |
| params.config | int | config |
### Results
This method returns no results.

### Examples


#### Request

```json
{
    "jsonrpc": 2.0,
    "id": 20,
    "method": "org.rdk.PowerManager.setWakeupSrcConfig",
    "params": {
        "powerMode": 0,
        "wakeSrcType": 0,
        "config": 0
    }
}
```


#### Response

```json
{
    "jsonrpc": 2.0,
    "id": 20,
    "result": null
}
```


<a id="head.Properties"></a>
# Properties
The following properties are provided by the PowerManager plugin:

PowerManager interface properties:

| Method | Description |
| :-------- | :-------- |
| [GetLastWakeupKeyCode](#property.GetLastWakeupKeyCode)<sup>RO</sup> | Get the key code that can be used for wakeup |
| [GetLastWakeupReason](#property.GetLastWakeupReason)<sup>RO</sup> | Get Last Wake up reason |
| [GetOvertempGraceInterval](#property.GetOvertempGraceInterval)<sup>RO</sup> | Get Temperature Grace interval |
| [SetDeepSleepTimer](#property.SetDeepSleepTimer)<sup>WO</sup> | Set Deep sleep timer for timeOut period |
| [SetNetworkStandbyMode](#property.SetNetworkStandbyMode)<sup>WO</sup> | Set the standby mode for Network |
| [SetOvertempGraceInterval](#property.SetOvertempGraceInterval)<sup>WO</sup> | Set Temperature Thresholds |

<a id="property.GetLastWakeupKeyCode"></a>
## *GetLastWakeupKeyCode [<sup>property</sup>](#head.Properties)*

Get the key code that can be used for wakeup

> This property is read-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).keycode | int | Key code for wakeup |

### Examples


#### Get Request

```json
{
    "jsonrpc": 2.0,
    "id": 21,
    "method": "org.rdk.PowerManager.getLastWakeupKeyCode"
}
```


#### Get Response

```json
{
    "jsonrpc": 2.0,
    "id": 21,
    "result": 0
}
```

<a id="property.GetLastWakeupReason"></a>
## *GetLastWakeupReason [<sup>property</sup>](#head.Properties)*

Get Last Wake up reason

> This property is read-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).wakeupReason | WakeupReason | wake up reason |

### Examples


#### Get Request

```json
{
    "jsonrpc": 2.0,
    "id": 22,
    "method": "org.rdk.PowerManager.getLastWakeupReason"
}
```


#### Get Response

```json
{
    "jsonrpc": 2.0,
    "id": 22,
    "result": "WAKEUP_REASON_UNKNOWN"
}
```

<a id="property.GetOvertempGraceInterval"></a>
## *GetOvertempGraceInterval [<sup>property</sup>](#head.Properties)*

Get Temperature Grace interval

> This property is read-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).graceInterval | int | interval in secs? |

### Examples


#### Get Request

```json
{
    "jsonrpc": 2.0,
    "id": 23,
    "method": "org.rdk.PowerManager.getOvertempGraceInterval"
}
```


#### Get Response

```json
{
    "jsonrpc": 2.0,
    "id": 23,
    "result": 0
}
```

<a id="property.SetDeepSleepTimer"></a>
## *SetDeepSleepTimer [<sup>property</sup>](#head.Properties)*

Set Deep sleep timer for timeOut period

> This property is write-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).timeOut | int | deep sleep timeout |

### Examples


#### Set Request

```json
{
    "jsonrpc": 2.0,
    "id": 24,
    "method": "org.rdk.PowerManager.setDeepSleepTimer",
    "params": {
        "timeOut": 0
    }
}
```


#### Set Response

```json
{
    "jsonrpc": 2.0,
    "id": 24,
    "result": null
}
```

<a id="property.SetNetworkStandbyMode"></a>
## *SetNetworkStandbyMode [<sup>property</sup>](#head.Properties)*

Set the standby mode for Network

> This property is write-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).standbyMode | bool | Network standby mode |

### Examples


#### Set Request

```json
{
    "jsonrpc": 2.0,
    "id": 25,
    "method": "org.rdk.PowerManager.setNetworkStandbyMode",
    "params": {
        "standbyMode": true
    }
}
```


#### Set Response

```json
{
    "jsonrpc": 2.0,
    "id": 25,
    "result": null
}
```

<a id="property.SetOvertempGraceInterval"></a>
## *SetOvertempGraceInterval [<sup>property</sup>](#head.Properties)*

Set Temperature Thresholds

> This property is write-only.
### Events
No events are associated with this method.
### Values
| Name | Type | Description |
| :-------- | :-------- | :-------- |
| (property).graceInterval | int | interval in secs? |

### Examples


#### Set Request

```json
{
    "jsonrpc": 2.0,
    "id": 26,
    "method": "org.rdk.PowerManager.setOvertempGraceInterval",
    "params": {
        "graceInterval": 0
    }
}
```


#### Set Response

```json
{
    "jsonrpc": 2.0,
    "id": 26,
    "result": null
}
```

