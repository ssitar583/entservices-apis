import os
import json
import argparse
from header_file_parser import HeaderFileParser
from logger import Logger
from markdown_templates import generate_header_description_markdown, generate_header_toc, generate_methods_toc, generate_method_markdown, generate_notifications_toc, generate_notification_markdown, generate_properties_toc, generate_property_markdown

def generate_md_from_header(header_file, json_file=None):
    filename = os.path.basename(header_file)
    classname, _ = os.path.splitext(filename)

    output_file_path = 'bash_batch_docs/' + classname + '.md'

    log_file_path = 'logs/' + classname + '.txt'
    logger = Logger(log_file_path)

    header_structure = HeaderFileParser(header_file, logger)
    
    # print("Methods: ")
    # print(json.dumps(header_structure.methods, indent=4))
    # print("Properties: ")
    # print(json.dumps(header_structure.properties, indent=4))
    # print("Events: ")
    # print(json.dumps(header_structure.events, indent=4))
    # print("Structs: ")
    # print(json.dumps(header_structure.structs_registry, indent=4))
    # print("Iterators: ")
    # print(json.dumps(header_structure.iterators_registry, indent=4))
    # print("Enums: ")
    # print(json.dumps(header_structure.enums_registry, indent=4))
    # print("Symbols: ")
    # print(json.dumps(header_structure.symbols_registry, indent=4))

    with open(output_file_path, 'w') as file:
        file.write(generate_header_toc(classname, header_structure))
        file.write(generate_header_description_markdown(classname))
        if len(header_structure.methods.values()) > 0:   
            file.write(generate_methods_toc(header_structure.methods, classname))
            for method in header_structure.methods:
                file.write(generate_method_markdown(method, header_structure.methods[method], header_structure.symbols_registry))
        file.write("\n")
        if len(header_structure.properties.values()) > 0:
            file.write(generate_properties_toc(header_structure.properties, classname))
            for prop in header_structure.properties:
                file.write(generate_property_markdown(prop, header_structure.properties[prop], header_structure.symbols_registry))
        file.write("\n")
        if len(header_structure.events.values()) > 0:
            file.write(generate_notifications_toc(header_structure.events, classname))
            for event in header_structure.events:
                file.write(generate_notification_markdown(event, header_structure.events[event], header_structure.symbols_registry))
    logger.write_log()
    logger.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process header file and optional JSON file.')
    parser.add_argument('header_file', type=str, help='Path to header file')
    
    args = parser.parse_args()
    generate_md_from_header(args.header_file)