"""
Author: iamu985
Github: https://github.com/iamu985
DateCompleted: Saturday, January 07, IST 4:53PM

TODO
- No tests are written
- Removing redundant reference argument and automatically assigning the reference
- Need to write proper documentation

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
    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def build_name(self):
        tag = et.Element(Tags.name.value)
        add_subelement_with_text(tag, Tags.fullname.value, self.name)
        return tag

    def write(self):
        tag = et.Element(Tags.party.value)
        add_subelement_with_text(tag, Tags.reference.value, f'P{self.id}')
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
