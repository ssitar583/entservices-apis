<!-- Generated automatically, DO NOT EDIT! -->
<a name="head.UsbAccess_Plugin"></a>
# UsbAccess Plugin

**Version: [1.0.0]()**

A org.rdk.UsbAccess plugin for Thunder framework.

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

The `UsbAccess` plugin provides the ability to examine the contents on a USB drive and access the content through HTTP URLs.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a name="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *org.rdk.UsbAccess*) |
| classname | string | Class name: *org.rdk.UsbAccess* |
| locator | string | Library name: *libWPEFrameworkUsbAccess.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |

<a name="head.Methods"></a>
# Methods

The following methods are provided by the org.rdk.UsbAccess plugin:

UsbAccess interface methods:

| Method | Description |
| :-------- | :-------- |
| [clearLink](#method.clearLink) | Clears or removes the symbolic link created by the `createLink` method |
| [createLink](#method.createLink) | Creates a symbolic link to the root folder of the USB drive |
| [getLinks](#method.getLinks) | Returns a list of created links and the associated root folder of the USB drive |
| [getAvailableFirmwareFiles](#method.getAvailableFirmwareFiles) | Gets a list of firmware files on the device |
| [getFileList](#method.getFileList) | Gets a list of files and folders from the specified directory or path |
| [getMounted](#method.getMounted) | Returns a list of mounted USB devices |
| [updateFirmware](#method.updateFirmware) | Updates the firmware using the specified file retrieved from the `getAvailableFirmwareFiles` method |
| [ArchiveLogs](#method.ArchiveLogs) | Compresses and uploads device logs into attached USB drive from /opt/logs with a name comprises of Mac of the device , date and time in a `tgz` format |


<a name="method.clearLink"></a>
## *clearLink [<sup>method</sup>](#head.Methods)*

Clears or removes the symbolic link created by the `createLink` method.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.baseURL | string | <sup>*(optional)*</sup> baseURL refers to the web server URL returned by createLink API that points to the symbolic link. If no parameter is given, then http://localhost:50050/usbdrive will be cleared |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Whether the request succeeded |
| result?.error | string | <sup>*(optional)*</sup> An error message in case of a failure |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.clearLink",
    "params": {
        "baseURL": "http://localhost:50050/usbdrive"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "success": true,
        "error": "could not remove symlink"
    }
}
```

<a name="method.createLink"></a>
## *createLink [<sup>method</sup>](#head.Methods)*

Creates a symbolic link to the root folder of the USB drive. If called, and a link already exists, then it errors out. Symbolic link has read-only access. Use the name `usbdrive`.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.path | string | <sup>*(optional)*</sup> path refers to the root folder of the mounted USB Drive as returned by getMounted API. If no parameter is given, then the first USB drive returned by getMounted API will be used |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.baseURL | string | The URL of the web server that points to this location |
| result.success | boolean | Whether the request succeeded |
| result?.error | string | <sup>*(optional)*</sup> An error message in case of a failure |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.createLink",
    "params": {
        "path": "/run/media/sda1"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "baseURL": "http://localhost/usbdrive",
        "success": true,
        "error": "could not create symlink OR symlink already exists: http://localhost/usbdrive"
    }
}
```

<a name="method.getLinks"></a>
## *getLinks [<sup>method</sup>](#head.Methods)*

Returns a list of created links and the associated root folder of the USB drive.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.links | array | The list of links and associated baseURL paths (empty if there are no results) |
| result.links[#] | object |  |
| result.links[#].path | string | The root folder of the mounted USB Drive as returned by getMounted API |
| result.links[#].baseURL | string | The URL of the web server that points to the path as returned by createLink |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.getLinks"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "links": [
            {
                "path": "/run/media/sda1",
                "baseURL": "http://localhost/usbdrive"
            }
        ],
        "success": true
    }
}
```

<a name="method.getAvailableFirmwareFiles"></a>
## *getAvailableFirmwareFiles [<sup>method</sup>](#head.Methods)*

Gets a list of firmware files on the device. These files should start with the PMI or model number for that device and end with `.bin`. For example `HSTP11MWR_4.11p5s1_VBN_sdy.bin`.  
Firmware files are scanned in the root directories. If multiple USB devices are found, then the available firmware files are checked and listed from each device.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.availableFirmwareFiles | array | The list of firmware files including the full path name |
| result.availableFirmwareFiles[#] | string |  |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.getAvailableFirmwareFiles"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "availableFirmwareFiles": [
            "/tmp/usbmnts/sda1/HSTP11MWR_4.11p5s1_VBN_sdy.bin"
        ],
        "success": true
    }
}
```

<a name="method.getFileList"></a>
## *getFileList [<sup>method</sup>](#head.Methods)*

Gets a list of files and folders from the specified directory or path.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.path | string | <sup>*(optional)*</sup> The directory name for which the contents are listed. It supports relative and absolute paths. Any path names starting with / will be checked to see if starts with any of the root folder mounted paths returned by getMounted API. If it matches, it will be considered absolute path and used to retrieve the list of files. If path starting with / doesn't match any of the root folder mounted paths returned by getMounted API, then it is considered relative path from the root folder of the first USB drive returned by getMounted API. If no value is specified, then the contents of the root folder of the first USB drive returned by getMounted API are listed |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.path | string | Absolute path for which the contents are returned |
| result.contents | array | A list of files and directories (empty if there are no results) |
| result.contents[#] | object |  |
| result.contents[#].name | string | the name of the file or directory |
| result.contents[#].t | string | The type. Either `d` for directory or `f` for file |
| result.success | boolean | Whether the request succeeded |
| result?.error | string | <sup>*(optional)*</sup> An error message in case of a failure |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.getFileList",
    "params": {
        "path": "/run/media/sda1/logs/PreviousLogs"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "path": "/run/media/sda1/logs/PreviousLogs",
        "contents": [
            {
                "name": "img1.jpg",
                "t": "f"
            }
        ],
        "success": true,
        "error": "no disk"
    }
}
```

<a name="method.getMounted"></a>
## *getMounted [<sup>method</sup>](#head.Methods)*

Returns a list of mounted USB devices.

### Events

No Events

### Parameters

This method takes no parameters.

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.mounted | array | The list of file paths where USB devices are mounted |
| result.mounted[#] | string |  |
| result.success | boolean | Whether the request succeeded |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.getMounted"
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "mounted": [
            "/tmp/usbmnts/sda"
        ],
        "success": true
    }
}
```

<a name="method.updateFirmware"></a>
## *updateFirmware [<sup>method</sup>](#head.Methods)*

Updates the firmware using the specified file retrieved from the `getAvailableFirmwareFiles` method.

### Events

No Events

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.fileName | string | <sup>*(optional)*</sup> The firmware file path to use for the update |

### Result

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| result | object |  |
| result.success | boolean | Whether the request succeeded |
| result?.error | string | <sup>*(optional)*</sup> An error message in case of a failure |

### Example

#### Request

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "method": "org.rdk.UsbAccess.updateFirmware",
    "params": {
        "fileName": "/tmp/usbmnts/sda/this_is_test.bin"
    }
}
```

#### Response

```json
{
    "jsonrpc": "2.0",
    "id": 42,
    "result": {
        "success": true,
        "error": "invalid filename"
    }
}
```

<a name="method.ArchiveLogs"></a>
## *ArchiveLogs [<sup>method</sup>](#head.Methods)*

Compresses and uploads device logs into attached USB drive from /opt/logs with a name comprises of Mac of the device , date and time in a `tgz` format. For example `18310C696834_Logs_10-13-21-04-42PM.tgz` `(<MAC address>_Logs_<unix epoch time>.tgz)`.Notifies about new messages in a room.

### Events

| Event | Description |
| :-------- | :-------- |
| [onArchiveLogs](#event.onArchiveLogs) | Triggered to archive the device logs and returns the status of the archive |
### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params?.path | string | <sup>*(optional)*</sup> path refers to the root folder of the mounted USB Drive as returned by getMounted API. If no parameter is given, then the first USB drive returned by getMounted API will be used |

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
    "method": "org.rdk.UsbAccess.ArchiveLogs",
    "params": {
        "path": "/run/media/sda1"
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

The following events are provided by the org.rdk.UsbAccess plugin:

UsbAccess interface events:

| Event | Description |
| :-------- | :-------- |
| [onUSBMountChanged](#event.onUSBMountChanged) | Triggered when a USB drive is mounted or unmounted |
| [onArchiveLogs](#event.onArchiveLogs) | Triggered to archive the device logs and returns the status of the archive |


<a name="event.onUSBMountChanged"></a>
## *onUSBMountChanged [<sup>event</sup>](#head.Notifications)*

Triggered when a USB drive is mounted or unmounted.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.mounted | boolean | `true` when the USB device is mounted or `false` when the USB device is unmounted |
| params.device | string | The location where the device is mounted |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onUSBMountChanged",
    "params": {
        "mounted": true,
        "device": "/dev/sda1"
    }
}
```

<a name="event.onArchiveLogs"></a>
## *onArchiveLogs [<sup>event</sup>](#head.Notifications)*

Triggered to archive the device logs and returns the status of the archive.

### Parameters

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| params | object |  |
| params.error | string | Specifies the status of upload logs (must be one of the following: *script error*, *none*, *Locked*, *No USB*, *Writing Error*) |
| params.success | boolean | Whether the request succeeded |
| params.path | string | Absolute path on the USB drive where the log is archived. On errors, it's set to empty string ("") |

### Example

```json
{
    "jsonrpc": "2.0",
    "method": "client.events.onArchiveLogs",
    "params": {
        "error": "none",
        "success": true,
        "path": "/run/media/sda1/Log/5C3400F15492_Logs_12-05-22-10-41PM.tgz"
    }
}
```

