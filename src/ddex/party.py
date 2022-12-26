from xml.etree import ElementTree as et
from ddex.utils import add_subelement_with_text

class Party:
    def __init__(self, fullname, reference_id=None, party_id=None, party_role=None):
        self.reference_id = reference_id
        self.party_id = party_id
        self.fullname = fullname
        self.party_role = party_role

    def __call__(self):
        party_tag = et.Element('Party')
        if self.party_role:
            add_subelement_with_text(party_tag, 'PartyId', self.party_id)
        else:
            add_subelement_with_text(party_tag, 'PartyReference', self.reference_id)
        party_name_tag = et.SubElement(party_tag, 'PartyName')
        add_subelement_with_text(party_name_tag, 'FullName', self.fullname)
        return party_tag
