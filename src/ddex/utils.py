from xml.etree import ElementTree as et
from xml.dom import minidom
from pprint import pprint
from typing import Tuple
 
def add_subelement_with_text(root, tagname, tagtext, **attribs):
    subelement = et.SubElement(root, tagname, **attribs)
    subelement.text = tagtext

def reparse_xml(element):
    rough_string = et.tostring(element, 'utf-8')
    return minidom.parseString(rough_string)

def prettyprint(parsed_string):
    pprint(parsed_string.toprettyxml(indent="    "))

def getstring_from_element(element):
    return et.tostring(element)

def getstring_from_file(file):
    tree = et.parse(file)
    root = tree.getroot()
    return getstring_from_element(root)

def build_duration(duration: Tuple[str, str, str]) -> str:
    return f'PT{duration[0]}H{duration[1]}M{duration[2]}S'

