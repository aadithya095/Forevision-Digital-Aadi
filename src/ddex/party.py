"""
Author: iamu985
Github: https://github.com/iamu985
DateCompleted: Saturday, January 07, IST 4:53PM

TODO
- No tests are written
- Removing redundant reference argument and automatically assigning the reference
- Need to write proper documentation
- Refactor code to properly make xml file

--------------
Documentation
--------------
Builds Party part of the DDEX for new release single.
"""

from lxml import etree as et
from enum import Enum
from utils import add_subelement_with_text


class Tags(Enum):
    party = "Party"
    name = "PartyName"
    fullname = "FullName"
    reference = "PartyReference"
    partylist = "PartyList"

    # contributor
    contributor = "Contributor"
    contributor_party_reference = "ContributorPartyReference"
    role = "Role"


class Party:
    """
    I removed id as it is redundant and the reference can be made by attaching P as a prefix with the name. The id will be optional.
    """
    def __init__(self, name, id_=None, role=None):
        self.name = name
        self.id = id_
        self.role = role

    def build_name(self):
        tag = et.Element(Tags.name.value)
        add_subelement_with_text(tag, Tags.fullname.value, self.name)
        return tag

    def get_reference(self):
        # Gives name reference of the party
        parse_name = self.name.replace(" ", "")
        return f"P{parse_name}"

    def write(self):
        tag = et.Element(Tags.party.value)
        if self.id:
            add_subelement_with_text(tag, Tags.reference.value, f'P{self.id}')
        else:
            add_subelement_with_text(tag, Tags.reference.value, self.get_reference()) # Removes the spaces in the name that is not accepted as per the ddex standard
        tag.append(self.build_name())
        return tag


class PartyList:
    def __init__(self, parties=[]):
        self.parties = parties

    def write(self):
        tag = et.Element(Tags.partylist.value)
        for party in self.parties:
            tag.append(party.write())
        return tag


class Contributor:
    def __init__(self, id_, role):
        self.id = id_
        self.role = role

    def write(self, **attribs):
        tag = et.Element(Tags.contributor.value, **attribs)
        add_subelement_with_text(tag, Tags.contributor_party_reference.value, self.id)  # ContributorPartyReference
        add_subelement_with_text(tag, Tags.role.value, self.role)  # Role
        return tag
