import os
import sys
from utils import validate
from config import ROOT_DIR, RELEASE_NOTIFICATION_SCHEMA

def run_validator():
    """
    The validator is for testing purposes only and should be removed during production.
    TODO: Remove the validator before production
    It looks for xml files in the tests directory and lists it in the terminal.
    The developer can then choose on which file to validate on.
    Returns True if the xml file is valid, False otherwise.
    """
    test_files = {}
    ddex_dir = os.path.join(ROOT_DIR, 'src/ddex')
    for root, dirs, files in os.walk(ddex_dir):
        if 'tests' in root:
            for ind, file in enumerate(files):
                if file.endswith('.xml'):
                    test_files[ind] = os.path.join(root, file)
                    print(ind, file)

    file_choice = int(input("Enter the number of the file you want to validate: "))
    xml_file = test_files[file_choice]
    print(f"Validating for {xml_file}\n")
    print(f"Result: {validate(xml_file)}")

if __name__ == "__main__":
    run_validator()