from xml.etree import ElementTree as et
from xml.dom import minidom
from pprint import pprint
 
def add_subelement_with_text(root, tagname, tagtext):
    subelement = et.SubElement(root, tagname)
    subelement.text = tagtext

def reparse_xml(element):
    rough_string = et.tostring(element, 'utf-8')
    return minidom.parseString(rough_string)

def prettyprint(parsed_string):
    pprint(parsed_string.toprettyxml(indent="    "))







