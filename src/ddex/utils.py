from lxml import etree as et
import os


def add_subelement_with_text(root, tagname, text, **attribs):
    tag = et.SubElement(root, tagname, **attribs)
    tag.text = text


def save(root, output_file):
    curr_dir = os.getcwd()
    output_dir = os.path.join(curr_dir, 'tests')
    filepath = os.path.join(output_dir, output_file)
    tree = et.ElementTree(root)
    tree.write(filepath, pretty_print=True)
