"""
Author: iamu985
Github: https://github.com/iamu985

TODO
- add tests for all the utility functions
- provide neat and clean documentation for each functions
"""
import os
from lxml import etree as et
from config import ROOT_DIR


RELEASE_NOTIFICATION_SCHEMA = 'docs/assets/ern/release-notification.xsd'


def add_subelement_with_text(root, tagname, text, **attribs):
    """Utility function to add a tag with a text in it"""
    tag = et.SubElement(root, tagname, **attribs)
    tag.text = text


def save(root, output_file):
    """Saves the element root tag in the given output file"""
    curr_dir = os.getcwd()
    output_dir = os.path.join(curr_dir, 'tests')
    filepath = os.path.join(output_dir, output_file)
    tree = et.ElementTree(root)
    tree.write(filepath, pretty_print=True)


def validate(xml_file):
    """Validates the generated xml file with the standard schema of ddex"""
    schema_file = os.path.join(ROOT_DIR, RELEASE_NOTIFICATION_SCHEMA)
    xml = et.parse(xml_file)
    schema_doc = et.parse(schema_file)
    schema = et.XMLSchema(schema_doc)
    return schema.validate(xml)

