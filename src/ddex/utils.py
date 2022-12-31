from xml.etree import ElementTree as et
from xml.etree.ElementTree import Element
from xml.dom import minidom
from pprint import pprint
from typing import Tuple
import xmltodict
import os

from src.settings import BASE_DIR

def add_subelement_with_text(root, tagname, tagtext, **attribs):
    subelement = et.SubElement(root, tagname, **attribs)
    subelement.text = tagtext

def reparse_xml(element):
    rough_string = et.tostring(element, 'utf-8')
    return minidom.parseString(rough_string)

def prettyprint(parsed_string):
    pprint(parsed_string.toprettyxml(indent="    "))

def getstring_from_element(element):
    return et.tostring(element, encoding='utf-8')

def getstring_from_file(file):
    tree = et.parse(file)
    root = tree.getroot()
    return getstring_from_element(root)

def build_duration(duration: Tuple[str, str, str]) -> str:
    return f'PT{duration[0]}H{duration[1]}M{duration[2]}S'

def assertData(tag: Element, compare_file: str) -> None:
    file_path = compare_file_discover(compare_file)
    xml_data = getstring_from_element(tag)
    xml_dict = xmltodict.parse(xml_data)

    original_data = getstring_from_file(file_path)
    expected_dict = xmltodict.parse(original_data)

    assert xml_dict == expected_dict

def compare_file_discover(filename: str) -> str:
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file == filename:
                return os.path.join(root, file)

def save_to_file(root, output):
    stream = et.tostring(root, 'utf-8')
    with open(output, 'wb') as xml_file:
        xml_file.write(stream)







    

