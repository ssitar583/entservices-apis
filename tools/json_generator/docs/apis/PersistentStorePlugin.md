<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.PersistentStore_Plugin"></a>
# PersistentStore Plugin

**Version: [1.0.0]()**

A org.rdk.PersistentStore plugin for Thunder framework.

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

The `PersistentStore` plugin allows you to persist key/value pairs by namespace.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.PersistentStore*) |
| classname | string | Class name: *org.rdk.PersistentStore* |
| locator | string | Library name: *libWPEFrameworkPersistentStore.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.PersistentStore plugin:

PersistentStore interface methods:

| Method | Description |
| :-------- | :-------- |
| [deleteKey](#method.deleteKey) | Deletes a key from the specified namespace |
| [deleteNamespace](#method.deleteNamespace) | Deletes the specified namespace |
| [flushCache](#method.flushCache) | Flushes the device cache |
| [getKeys](#method.getKeys) | Returns the keys that are stored in the specified namespace |
| [getNamespaces](#method.getNamespaces) | Returns the namespaces |
| [getStorageSizes](#method.getStorageSizes) | Returns the size occupied by each namespace |
| [getValue](#method.getValue) | Returns the value of a key from the specified namespace |
| [setValue](#method.setValue) | Sets the value of a key in the the specified namespace |
| [setNamespaceStorageLimit](#method.setNamespaceStorageLimit) | Sets the storage limit for a given namespace |
| [getNamespaceStorageLimit](#method.getNamespaceStorageLimit) | Returns the storage limit for a given namespace |


<a name="method.deleteKey"></a>
## *deleteKey [<sup>method</sup>](#head.Methods)*

Deletes a key from the specified namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params.key | string | Key |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.deleteKey",
    "params": {
        "namespace": "ns1",
        "key": "key1",
        "scope": "device"
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

<a name="method.deleteNamespace"></a>
## *deleteNamespace [<sup>method</sup>](#head.Methods)*

Deletes the specified namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.deleteNamespace",
    "params": {
        "namespace": "ns1",
        "scope": "device"
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

<a name="method.flushCache"></a>
## *flushCache [<sup>method</sup>](#head.Methods)*

Flushes the device cache.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.flushCache"
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

<a name="method.getKeys"></a>
## *getKeys [<sup>method</sup>](#head.Methods)*

Returns the keys that are stored in the specified namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.keys | array |  |
| result.keys[#] | string | Key |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.getKeys",
    "params": {
        "namespace": "ns1",
        "scope": "device"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "keys": [
            "key1"
        ],
        "success": true
    }
}
```

<a name="method.getNamespaces"></a>
## *getNamespaces [<sup>method</sup>](#head.Methods)*

Returns the namespaces.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.namespaces | array |  |
| result.namespaces[#] | string | Namespace |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.getNamespaces",
    "params": {
        "scope": "device"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "namespaces": [
            "ns1"
        ],
        "success": true
    }
}
```

<a name="method.getStorageSizes"></a>
## *getStorageSizes [<sup>method</sup>](#head.Methods)*

Returns the size occupied by each namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.storageList | array |  |
| result.storageList[#] | object |  |
| result.storageList[#].namespace | string | Namespace |
| result.storageList[#].size | number | Size in bytes |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.getStorageSizes",
    "params": {
        "scope": "device"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "storageList": [
            {
                "namespace": "ns1",
                "size": 100
            }
        ]
    }
}
```

<a name="method.getValue"></a>
## *getValue [<sup>method</sup>](#head.Methods)*

Returns the value of a key from the specified namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params.key | string | Key |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.value | string | Value |
| result.success | boolean | Legacy parameter (always true) |
| result?.ttl | number | <sup>*(optional)*</sup> Time in seconds |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 31 | ```ERROR_PENDING_CONDITIONS``` | Time is not synced |
| 43 | ```ERROR_NOT_EXIST``` | Unknown namespace |
| 22 | ```ERROR_UNKNOWN_KEY``` | Unknown key |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.getValue",
    "params": {
        "namespace": "ns1",
        "key": "key1",
        "scope": "device"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "value": "value1",
        "success": true,
        "ttl": 100
    }
}
```

<a name="method.setValue"></a>
## *setValue [<sup>method</sup>](#head.Methods)*

Sets the value of a key in the the specified namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params.key | string | Key |
| params.value | string | Value |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |
| params?.ttl | number | <sup>*(optional)*</sup> Time in seconds |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Legacy parameter (always true) |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 31 | ```ERROR_PENDING_CONDITIONS``` | Time is not synced |
| 16 | ```ERROR_INVALID_INPUT_LENGTH``` | Empty/too large namespace or key, or the storage doesn't have enough space |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.setValue",
    "params": {
        "namespace": "ns1",
        "key": "key1",
        "value": "value1",
        "scope": "device",
        "ttl": 100
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

<a name="method.setNamespaceStorageLimit"></a>
## *setNamespaceStorageLimit [<sup>method</sup>](#head.Methods)*

Sets the storage limit for a given namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params.storageLimit | number | Size in bytes |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | null | Always null |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 16 | ```ERROR_INVALID_INPUT_LENGTH``` | Empty/too large namespace, or the storage doesn't have enough space |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.setNamespaceStorageLimit",
    "params": {
        "namespace": "ns1",
        "storageLimit": 100,
        "scope": "device"
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

<a name="method.getNamespaceStorageLimit"></a>
## *getNamespaceStorageLimit [<sup>method</sup>](#head.Methods)*

Returns the storage limit for a given namespace.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params?.scope | string | <sup>*(optional)*</sup> Scope (must be one of the following: *device*, *account*) |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.storageLimit | number | Size in bytes |

### Errors

| Code | Message | Description |
| :-------- | :-------- | :-------- |
| 43 | ```ERROR_NOT_EXIST``` | Unknown namespace |
| 1 | ```ERROR_GENERAL``` | Unknown error |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.PersistentStore.getNamespaceStorageLimit",
    "params": {
        "namespace": "ns1",
        "scope": "device"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "storageLimit": 100
    }
}
```

<a name="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the org.rdk.PersistentStore plugin:

PersistentStore interface events:

| Event | Description |
| :-------- | :-------- |
| [onValueChanged](#event.onValueChanged) | Triggered whenever any of the values stored are changed using setValue |


<a name="event.onValueChanged"></a>
## *onValueChanged [<sup>event</sup>](#head.Notifications)*

Triggered whenever any of the values stored are changed using setValue.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.namespace | string | Namespace |
| params.key | string | Key |
| params.value | string | Value |
| params.scope | string | Scope (must be one of the following: *device*, *account*) |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onValueChanged",
    "params": {
        "namespace": "ns1",
        "key": "key1",
        "value": "value1",
        "scope": "device"
    }
}
```

