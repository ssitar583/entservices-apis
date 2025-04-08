import json
import re

# Templates
HEADER_TOC_TEMPLATE = """<!-- Generated automatically, DO NOT EDIT! -->
<a id="head.{classname}_Plugin"></a>
# {classname} Plugin

**Version: [{version}](https://github.com/rdkcentral/rdkservices/blob/main/{classname}/CHANGELOG.md)**

A {classname} plugin for Thunder framework.

### Table of Contents

- [Abbreviation, Acronyms and Terms](#head.Abbreviation,_Acronyms_and_Terms)
- [Description](#head.Description)
- [Configuration](#head.Configuration)
"""

HEADER_DESCRIPTION_TEMPLATE = """
<a id="head.Abbreviation,_Acronyms_and_Terms"></a>
# Abbreviation, Acronyms and Terms

[[Refer to this link](userguide/aat.md)]

<a id="head.Description"></a>
# Description

The `{classname}` plugin provides an interface for {classname}.

The plugin is designed to be loaded and executed within the Thunder framework. For more information about the framework refer to [[Thunder](#ref.Thunder)].

<a id="head.Configuration"></a>
# Configuration

The table below lists configuration options of the plugin.

| Name | Type | Description |
| :-------- | :-------- | :-------- |
| callsign | string | Plugin instance name (default: *{classname}*) |
| classname | string | Class name: *{classname}* |
| locator | string | Library name: *libWPEFramework{classname}.so* |
| autostart | boolean | Determines if the plugin shall be started automatically along with the framework |
"""

METHODS_TOC_TEMPLATE = """
<a id="head.Methods"></a>
# Methods

The following methods are provided by the {classname} plugin:

{classname} interface methods:

| Method | Description |
| :-------- | :-------- |
"""

METHOD_MARKDOWN_TEMPLATE = """
<a id="method.{method_name}"></a>
## *{method_name} [<sup>method</sup>](#head.Methods)*

{method_description}

"""

PROPERTIES_TOC_TEMPLATE = """
<a id="head.Properties"></a>
# Properties
The following properties are provided by the {classname} plugin:

{classname} interface properties:

| Method | Description |
| :-------- | :-------- |
"""

PROPERTY_MARKDOWN_TEMPLATE = """
<a id="property.{property_name}"></a>
## *{property_name} [<sup>property</sup>](#head.Properties)*

{property_description}

"""

EVENTS_TOC_TEMPLATE = """
<a id="head.Notifications"></a>
# Notifications

Notifications are autonomous events, triggered by the internals of the implementation, and broadcasted via JSON-RPC to all registered observers. Refer to [[Thunder](#ref.Thunder)] for information on how to register for a notification.

The following events are provided by the {classname} plugin:

{classname} interface events:

| Method | Description |
| :-------- | :-------- |
"""

EVENT_MARKDOWN_TEMPLATE = """
<a id="event.{event_name}"></a>
## *{event_name} [<sup>event</sup>](#head.Notifications)*

{event_description}

"""

EXAMPLE_REQUEST_TEMPLATE = """

#### {method_type}Request

```json
{request_json}
"""

EXAMPLE_RESPONSE_TEMPLATE = """

#### {method_type}Response

```json
{response_json}
"""

def generate_header_toc(classname, document_object, version="1.0.0"):
    toc = HEADER_TOC_TEMPLATE.format(classname=classname, version=version)
    if len(document_object.methods.values()) > 0:
        toc += "- [Methods](#head.Methods)\n"
    if len(document_object.properties.values()) > 0:
        toc += "- [Properties](#head.Properties)\n"
    if len(document_object.events.values()) > 0:
        toc += "- [Notifications](#head.Notifications)\n"
    return toc

def generate_header_description_markdown(classname): 
    return HEADER_DESCRIPTION_TEMPLATE.format(classname=classname)

def generate_methods_toc(methods, classname): 
    toc = METHODS_TOC_TEMPLATE.format(classname=classname) 
    for method in methods:
        method_body = methods[method]
        toc += f"| [{method}](#method.{method}) | {method_body['brief'] or method_body['details']} |\n" 
    return toc

def generate_method_markdown(method_name, method_info, symbol_registry): 
    markdown = METHOD_MARKDOWN_TEMPLATE.format(method_name=method_name, method_description=method_info['brief'] or method_info['details']) 
    markdown += generate_events_section(method_info['events'])
    markdown += generate_parameters_section(method_info['params'], symbol_registry)
    markdown += generate_results_section(method_info['results'], symbol_registry)
    markdown += "\n### Examples\n"
    markdown += generate_request_section(method_info['request'], '')
    markdown += generate_response_section(method_info['response'], '')
    return markdown

def generate_events_section(events):
    markdown = "### Events\n"
    if events:
        markdown += """| Event | Description |\n| :-------- | :-------- |\n"""
        for event in events:
            markdown += f"| [{event}](#event.{event}) | {events[event]} |\n"
    else:
        markdown += "No events are associated with this method.\n"
    return markdown

def generate_parameters_section(params, symbol_registry):
    markdown = "### Parameters\n"
    if params:
        markdown += """| Name | Type | Description |\n| :-------- | :-------- | :-------- |\n"""
        for param in params:
            flattened_params = symbol_registry[f"{param['name']}-{param['type']}"]['flattened_description']
            for param_name, param_data in flattened_params.items():
                markdown += f"| params{param_name} | {param_data['type']} | {re.sub(r'e\.g\.\s*".*?(?<!\\)"|ex\:\s*.*?(?=\.|$)', '', param_data['description'])} |\n"
    else:
        markdown += "This method takes no parameters.\n"
    return markdown

def generate_results_section(results, symbol_registry):
    markdown = "### Results\n"
    if results:
        markdown += """| Name | Type | Description |\n| :-------- | :-------- | :-------- |\n"""
        for result in results:
            flattened_results = symbol_registry[f"{result['name']}-{result['type']}"]['flattened_description']
            for result_name, result_data in flattened_results.items():
                markdown += f"| result{result_name} | {result_data['type']} | {re.sub(r'e\.g\.\s*".*?(?<!\\)"|ex\:\s*.*?(?=\.|$)', '', result_data['description'])} |\n"
    else:
        markdown += "This method returns no results.\n"
    return markdown

def generate_values_section(values, symbol_registry):
    markdown = "### Values\n"
    if values:
        markdown += """| Name | Type | Description |\n| :-------- | :-------- | :-------- |\n"""
        for value in values:
            flattened_values = symbol_registry[f"{value['name']}-{value['type']}"]['flattened_description']
            for value_name, value_data in flattened_values.items():
                markdown += f"| (property){value_name} | {value_data['type']} | {re.sub(r'e\.g\.\s*".*?(?<!\\)"|ex\:\s*.*?(?=\.|$)', '', value_data['description'])} |\n"
    else:
        markdown += "This property has no values.\n"
    return markdown

def generate_request_section(request, method_type):
    request_json = json.dumps(request, indent=4)
    markdown = EXAMPLE_REQUEST_TEMPLATE.format(request_json=request_json, method_type=method_type)
    markdown += "````"
    return markdown

def generate_response_section(response, method_type):
    response_json = json.dumps(response, indent=4)
    markdown = EXAMPLE_RESPONSE_TEMPLATE.format(response_json=response_json, method_type=method_type)
    markdown += "````"
    return markdown

def generate_properties_toc(properties, classname):
    toc = PROPERTIES_TOC_TEMPLATE.format(classname=classname)
    for prop in properties:
        property_body = properties[prop]
        super_script = ""
        if property_body['property'] == 'read':
            super_script = "<sup>RO</sup>"
        elif property_body['property'] == 'write':
            super_script = "<sup>WO</sup>"
        toc += f"| [{prop}](#property.{prop}){super_script} | {property_body['brief'] or property_body['details']} |\n"
    return toc

def generate_property_markdown(property_name, property_info, symbol_registry):
    markdown = PROPERTY_MARKDOWN_TEMPLATE.format(property_name=property_name, property_description=property_info['brief'] or property_info['details'])
    if property_info['property'] == 'read':
        markdown += "> This property is read-only.\n"
    elif property_info['property'] == 'write':
        markdown += "> This property is write-only.\n"
    markdown += generate_events_section(property_info['events'])
    markdown += generate_values_section((property_info['results'] + property_info['params']), symbol_registry)
    markdown += "\n### Examples\n"
    if 'read' in property_info['property']:
        markdown += generate_request_section(property_info['get_request'], 'Get ')
        markdown += generate_response_section(property_info['get_response'], 'Get ')
    if 'write' in property_info['property']:
        markdown += generate_request_section(property_info['set_request'], 'Set ')
        markdown += generate_response_section(property_info['set_response'], 'Set ')
    return markdown

def generate_notifications_toc(events, classname): 
    toc = EVENTS_TOC_TEMPLATE.format(classname=classname) 
    for event in events:
        event_body = events[event]
        toc += f"| [{event}](#event.{event}) | {event_body['brief'] or event_body['details']} |\n"
    return toc

def generate_notification_markdown(event_name, event_info, symbol_registry): 
    markdown = EVENT_MARKDOWN_TEMPLATE.format(event_name=event_name, event_description=event_info['brief'] or event_info['details']) 
    markdown += generate_parameters_section(event_info['params'], symbol_registry)
    markdown += "\n### Examples\n"
    markdown += generate_request_section(event_info['request'], '')
    return markdown