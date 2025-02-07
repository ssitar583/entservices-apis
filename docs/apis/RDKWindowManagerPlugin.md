<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.RDKWindowManager_Plugin"></a>
# RDKWindowManager Plugin

**Version: [1.0.0]()**

A org.rdk.RDKWindowManager plugin for Thunder framework.

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

The `RDKWindowManager`plugin controls the management of composition, layout, Z order, and key handling.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.RDKWindowManager*) |
| classname | string | Class name: *org.rdk.RDKWindowManager* |
| locator | string | Library name: *libWPEFrameworkRDKWindowManager.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.RDKWindowManager plugin:

RDKWindowManager interface methods:

| Method | Description |
| :-------- | :-------- |
| [addKeyIntercept](#method.addKeyIntercept) | Adds a key intercept to the client application specified |
| [addKeyIntercepts](#method.addKeyIntercepts) | Adds the list of key intercepts |
| [addKeyListener](#method.addKeyListener) | Adds a key listener to an application |
| [createDisplay](#method.createDisplay) |  Creates a display for the specified client using the configuration parameters |
| [enableInactivityReporting](#method.enableInactivityReporting) | Enables or disables inactivity reporting and events |
| [enableInputEvents](#method.enableInputEvents) | Enables KeyInputEvents for list of clients specified |
| [enableKeyRepeats](#method.enableKeyRepeats) | Enables or disables key repeats |
| [generateKey](#method.generateKey) | Triggers the key events (key press and release) |
| [getClients](#method.getClients) | Gets a list of clients |
| [getKeyRepeatsEnabled](#method.getKeyRepeatsEnabled) | Returns whether key repeating is enabled or disabled |
| [ignoreKeyInputs](#method.ignoreKeyInputs) | Blocks user key inputs |
| [injectKey](#method.injectKey) | Injects the keys |
| [keyRepeatConfig](#method.keyRepeatConfig) | Configuration for keyrepeat |
| [removeKeyIntercept](#method.removeKeyIntercept) | Removes a key intercept |
| [removeKeyListener](#method.removeKeyListener) | Removes a key listener for an application |
| [resetInactivityTime](#method.resetInactivityTime) | Resets the inactivity notification interval |
| [setInactivityInterval](#method.setInactivityInterval) | Sets the inactivity notification interval |


<a name="method.addKeyIntercept"></a>
## *addKeyIntercept [<sup>method</sup>](#head.Methods)*

Adds a key intercept to the client application specified. The keys are specified by a key code and a set of modifiers. Regardless of the application that has focus, key presses that match the key code and modifiers will be sent to the client application.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.intercept | string | A JSON String containing client, callSign (optional), keyCode and modifiers (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.addKeyIntercept",
    "params": {
        "intercept": "{\"client\":\"org.rdk.Netflix\",\"keyCode\":37,\"modifiers\":[\"shift\"]}"
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

<a name="method.addKeyIntercepts"></a>
## *addKeyIntercepts [<sup>method</sup>](#head.Methods)*

Adds the list of key intercepts.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.intercepts | string | A JSON String containing client, callSign (optional), keyCode and modifiers (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.addKeyIntercepts",
    "params": {
        "intercepts": "{\"intercepts\":[{\"keys\":[{\"keyCode\": 37,\"modifiers\":[\"ctrl\",\"alt\"]},{\"keyCode\": 38,\"modifiers\":[\"shift\"]}],\"client\":\"org.rdk.Netflix\"}]}"
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

<a name="method.addKeyListener"></a>
## *addKeyListener [<sup>method</sup>](#head.Methods)*

Adds a key listener to an application. The keys are bubbled up based on their z-order.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.keyListeners | string | A JSON String containing keys(keyCode, nativekeyCode (optional), modifiers (optional), activate, propagate), client, callSign (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.addKeyListener",
    "params": {
        "keyListeners": "{\"keys\":[{\"keyCode\":37,\"modifiers\":[\"shift\"],\"activate\":false,\"propagate\":true}],\"client\":\"org.rdk.Netflix\"}"
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

<a name="method.createDisplay"></a>
## *createDisplay [<sup>method</sup>](#head.Methods)*

 Creates a display for the specified client using the configuration parameters.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.displayParams | string | A JSON String containing client, callSign (optional), displayName, displayWidth, displayHeight, virtualDisplay, virtualWidth, virtualHeight, topmost (optional), focus (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.createDisplay",
    "params": {
        "displayParams": "{\"client\":\"org.rdk.Netflix\",\"callsign\":\"org.rdk.Netflix\",\"displayName\":\"test\",\"displayWidth\":1920,\"displayHeight\":1080,\"virtualDisplay\":true,\"virtualWidth\":1920,\"virtualHeight\":1080,\"topmost\":false,\"focus\":false}"
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

<a name="method.enableInactivityReporting"></a>
## *enableInactivityReporting [<sup>method</sup>](#head.Methods)*

Enables or disables inactivity reporting and events.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.enable | boolean | Whether to enable (`true`) or disable (`false`) inactivity reporting |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.enableInactivityReporting",
    "params": {
        "enable": true
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

<a name="method.enableInputEvents"></a>
## *enableInputEvents [<sup>method</sup>](#head.Methods)*

Enables KeyInputEvents for list of clients specified.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.clients | string | A JSON String containing one or more clients |
| params.enable | boolean | enable:Flag to enable input events |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.enableInputEvents",
    "params": {
        "clients": "{\"clients\":[\"org.rdk.Netflix\"]}",
        "enable": true
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

<a name="method.enableKeyRepeats"></a>
## *enableKeyRepeats [<sup>method</sup>](#head.Methods)*

Enables or disables key repeats.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.enable | boolean | Whether to enable (`true`) or disable (`false`) key repeats |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.enableKeyRepeats",
    "params": {
        "enable": true
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

<a name="method.generateKey"></a>
## *generateKey [<sup>method</sup>](#head.Methods)*

Triggers the key events (key press and release).

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.keys | string | A JSON String containing keyCode, modifiers (optional), delay |
| params?.client | string | <sup>*(optional)*</sup> The client name |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.generateKey",
    "params": {
        "keys": "{\"keys\": [{\"keyCode\":37,\"modifiers\":[\"shift\"],\"delay\":1}]}",
        "client": "org.rdk.Netflix"
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

<a name="method.getClients"></a>
## *getClients [<sup>method</sup>](#head.Methods)*

Gets a list of clients.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | string | A JSON String containing one or more clients |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.getClients"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": "{\"clients\":[\"org.rdk.Netflix\"]}"
}
```

<a name="method.getKeyRepeatsEnabled"></a>
## *getKeyRepeatsEnabled [<sup>method</sup>](#head.Methods)*

Returns whether key repeating is enabled or disabled.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.keyRepeat | boolean | `true` if enabled, otherwise `false` |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.getKeyRepeatsEnabled"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "keyRepeat": true
    }
}
```

<a name="method.ignoreKeyInputs"></a>
## *ignoreKeyInputs [<sup>method</sup>](#head.Methods)*

Blocks user key inputs.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.ignore | boolean | Whether key inputs are ignored |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.ignoreKeyInputs",
    "params": {
        "ignore": false
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

<a name="method.injectKey"></a>
## *injectKey [<sup>method</sup>](#head.Methods)*

Injects the keys.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.keycode | number | The key code of the key to intercept (only symbol * (string data type) is acceptable) |
| params?.modifiers | string | <sup>*(optional)*</sup> A JSON String containing one or more modifiers (`ctrl`, `alt`, and `shift` are supported) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.injectKey",
    "params": {
        "keycode": 37,
        "modifiers": "{\"modifiers\":[\"ctrl\",\"alt\"]}"
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

<a name="method.keyRepeatConfig"></a>
## *keyRepeatConfig [<sup>method</sup>](#head.Methods)*

Configuration for keyrepeat.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.input | string | Input type (default/keyboard) |
| params.keyConfig | string | A JSON String containing enabled, initialDelay (in milli seconds) and repeatInterval (in milli seconds) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.keyRepeatConfig",
    "params": {
        "input": "default",
        "keyConfig": "{\"enabled\":true,\"initialDelay\":500,\"repeatInterval\":100}"
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

<a name="method.removeKeyIntercept"></a>
## *removeKeyIntercept [<sup>method</sup>](#head.Methods)*

Removes a key intercept.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.intercept | string | A JSON String containing client, callSign (optional), keyCode and modifiers (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.removeKeyIntercept",
    "params": {
        "intercept": "{\"client\":\"org.rdk.Netflix\",\"keyCode\":37,\"modifiers\":[\"shift\"]}"
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

<a name="method.removeKeyListener"></a>
## *removeKeyListener [<sup>method</sup>](#head.Methods)*

Removes a key listener for an application.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.keyListeners | string | A JSON String containing keys(keyCode, nativekeyCode (optional), modifiers (optional), activate, propagate), client, callSign (optional) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.removeKeyListener",
    "params": {
        "keyListeners": "{\"keys\":[{\"keyCode\":37,\"modifiers\":[\"ctrl\",\"alt\"]},{\"keyCode\":38,\"modifiers\":[\"ctrl\",\"alt\"]}],\"client\":\"org.rdk.Netflix\"}"
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

<a name="method.resetInactivityTime"></a>
## *resetInactivityTime [<sup>method</sup>](#head.Methods)*

Resets the inactivity notification interval.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.resetInactivityTime"
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

<a name="method.setInactivityInterval"></a>
## *setInactivityInterval [<sup>method</sup>](#head.Methods)*

Sets the inactivity notification interval.

### Events

| Event | Description |
| :-------- | :-------- |
| [onUserInactivity](#event.onUserInactivity) | Triggers only if the device is inactive for the specified time interval |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.interval | integer | The inactivity event interval in minutes |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | null on success |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.RDKWindowManager.setInactivityInterval",
    "params": {
        "interval": 15
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

<a name="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.RDKWindowManager plugin:

RDKWindowManager interface events:

| Event | Description |
| :-------- | :-------- |
| [onUserInactivity](#event.onUserInactivity) | Triggered when a device has been inactive for a period of time |


<a name="event.onUserInactivity"></a>
## *onUserInactivity [<sup>event</sup>](#head.Notifications)*

Triggered when a device has been inactive for a period of time. This event is broadcasted at the frequency specified by `setInactivityInterval` if the device is not active. The default frequency is 15 minutes.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.minutes | number | The number of minutes that the device has been inactive |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onUserInactivity",
    "params": {
        "minutes": 5
    }
}
```

