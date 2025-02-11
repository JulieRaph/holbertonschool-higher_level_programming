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

        dictionary = {child.tag: child.text for child in root}

        return dictionary

    except FileNotFoundError:
        print("Error: The file {} was not found".format(filename))
        return None
    except ET.ParseError as e:
        print("Error: {} can't parsing to XML".format(e))
        return None
