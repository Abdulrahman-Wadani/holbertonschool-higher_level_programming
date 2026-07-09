#!/usr/bin/python3
"""
Docstring for python-serialization.task_03_xml
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        Docstring for serialize_to_xml

        :param dictionary: Description
        :param filename: Description
        """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    if hasattr(ET, 'indent'):
        ET.indent(tree, space="    ", level=0)

    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):

    tree = ET.parse(filename)

    root = tree.getroot()

    result = {}
    for child in root:

        result[child.tag] = child.text

    return result
