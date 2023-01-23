"""
Author: iamu985
Github: https://github.com/iamu985

TODO
- add tests for all the utility functions
- provide neat and clean documentation for each functions
"""
import os
from lxml import etree as et

ROOT_DIR = os.path.realpath(os.path.join(__file__, '..', '..', '..'))
print(ROOT_DIR)
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
    # Checks if the system is windows or linux
    # if windows then it will run the normal method of validation
    # the normal method won't give any errors to tell why validation failed
    # if linux is found it will try to run xmllint command 
    # if xmllint is not found it will run the normal mode
    
    def normal_method():
        """Returns True if passed and False if failed"""
        xml = et.parse(xml_file)
        schema_doc = et.parse(schema_file)
        schema = et.XMLSchema(schema_doc)
        return schema.validate(xml)
    
    def lint_method():
        cmd = f"xmllint --noout --schema {schema_file} {xml_file}"
        result = os.system(cmd)
        if result != 0:
            return False
        else:
            return True

    if os.name == 'nt':
        return normal_method()

    if os.name == 'posix':
        try:
            return lint_method()
        except:
            print('Maybe xmllint might not be installed in the system.')
            print('Running on normal mode.')
            print('Warning only the result will be displayed on this mode. No errors will be displayed.')
            return normal_method()

def format_duration(duration):
    """
    This function returns the formatted duration
    accepeted by the ddex standard.
    PT00H00M00S is the format for any duration

    The input should be a string seperated by colons, i.e.
    3:44
    1:20:20

    TODO: Write a test for this function.
    """
    split_duration = duration.split(":")
    if len(split_duration) == 2:
        return f"PT{split_duration[0]}M{split_duration[1]}S"
    if len(split_duration) == 3:
        return f"PT{split_duration[0]}H{split_duration[1]}M{split_duration[2]}S"

def parse_file_path(file_path):
    """
    Parses the file path and returns the file name and extension.
    Example:
    >>> parse_file_path('path/to/file.mp3')
    """
    return file_path.split('/')[-1]
