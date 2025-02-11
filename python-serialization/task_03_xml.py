#!/usr/bin/python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize a Python dictionnary to XML and save it to a file"""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Error: {e}")

def deserialize_from_xml(filename):
    """deserialize XMl to a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}

        for child in root:
            key = child.tag
            value = child.text

            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)

                except ValueError:
                    if value.lower() == "true":
                        value = True
                    elif value.lower() == "false":
                        value = False

            data[key] = value

        return data

    except(FileNotFoundError, ET.ParseError, Exception) as e:
        print(f"Error: {e, filename}")
        return None
