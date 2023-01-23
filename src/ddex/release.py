"""
Author: iamu985
Github: https://github.com/iamu985
DateCompleted: Tuesday, January 10, 2023, 11:56 AM IST

TODO
- Test to be written
- Removing redundant reference functions to automatically create one instead of manual insertions
- Require to proper documentation
- Refactor code to properly make xml file
"""
from lxml import etree as et
from enum import Enum
from utils import add_subelement_with_text
from resource import SoundRecording
from config import ReleaseTypeSet, ReleaseRelationshipTypeSet
from exceptions import InvalidReleaseType, NoNamespaceError, InvalidReleaseRelationshipTypeSet


class ReleaseIdType(Enum):
    """List of allowed Id types"""
    proprietary_id = "ProprietaryId"
    grid = "GRid"
    icpn = "ICPN"


class Tags(Enum):
    """List of Tags used in XML"""
    release_list = "ReleaseList"
    release = "Release"
    release_reference = "ReleaseReference"
    release_type = "ReleaseType"
    release_id = "ReleaseId"
    display_title_text = "DisplayTitleText"
    display_title = "DisplayTitle"
    title_text = "TitleText"
    additional_title = "AdditionalTitle"
    display_artist_name = "DisplayArtistName"
    display_artist = "DisplayArtist"
    artist_party_reference = "ArtistPartyReference"
    display_artist_role = "DisplayArtistRole"
    release_label_reference = "ReleaseLabelReference"
    genre = "Genre"
    genre_text = "GenreText"
    sub_genre = "SubGenre"
    parental_warning = "ParentalWarningType"
    related_release = "RelatedRelease"
    release_relationship_type = "ReleaseRelationshipType"
    resource_group = "ResourceGroup"
    sequence_number = "SequenceNumber"
    resource_group_content = "ResourceGroupContentItem"
    release_resource_reference = "ReleaseResourceReference"
    linked_release_resource_reference = "LinkedReleaseResourceReference"
    cline = "CLine"
    cline_year = "Year"
    cline_company = "CLineCompany"
    cline_text = "CLineText"


class ReleaseList:
    def __init__(self, releases=[]):
        self.releases = releases

    def write(self):
        tag = et.Element(Tags.release_list.value)
        for release in self.releases:
            tag.append(release.write())
        return tag


class Release:
    """Class to create Release"""

    def __init__(self,
                 reference,
                 id_,
                 display_title_text,
                 title_text,
                 territory,
                 artist_name,
                 artist_role,
                 cline_year,
                 cline_company,
                 cline_text,
                 release_label_reference,
                 genre,
                 release_type,
                 release_id_type=ReleaseIdType.icpn.value, # default value is ICPN for every releases if provided otherwise
                 sub_genre=None,
                 additional_title=None,
                 parental_warning="Unknown",
                 related_release=[],
                 resource_group=[],
                 *args,
                 **namespaces,
                 ):
        self.reference = reference
        self.id = id_
        self.display_title_text = display_title_text
        self.title_text = title_text
        self.territory = territory
        self.artist_name = artist_name
        self.artist_role = artist_role
        self.cline_year = cline_year
        self.cline_company = cline_company
        self.cline_text = cline_text
        self.release_label_reference = release_label_reference
        self.genre = genre
        self.sub_genre = sub_genre
        self.additional_title = additional_title
        self.parental_warning = parental_warning

        if release_type in ReleaseTypeSet: # Checks if release_type is in ReleaseTypeSet
            self.release_type = release_type # If yes then assigns the value
        else:
            raise InvalidReleaseType(release_type) # If not then raises InvalidReleaseType Exception

        self.release_id_type = release_id_type

        self.related_release = related_release
        self.resource_group = resource_group

    def build_display_title(self):
        tag = et.Element(Tags.display_title.value)
        add_subelement_with_text(tag, Tags.title_text.value, self.title_text)
        return tag

    def build_additional_title(self):
        tag = et.Element(Tags.additional_title.value)
        add_subelement_with_text(tag, Tags.title_text.value, self.additional_title)
        return tag

    def build_cline(self):
        tag = et.Element(Tags.cline.value)
        add_subelement_with_text(tag, Tags.cline_year.value, self.cline_year)
        add_subelement_with_text(tag, Tags.cline_company.value, self.cline_company)
        add_subelement_with_text(tag, Tags.cline_text.value, self.cline_text)
        return tag

    def build_genre(self):
        tag = et.Element(Tags.genre.value)
        add_subelement_with_text(tag, Tags.genre_text.value, self.genre)
        if self.sub_genre:
            add_subelement_with_text(tag, Tags.sub_genre.value, self.sub_genre)
        return tag

    def build_release_id(self):
        tag = et.Element(Tags.release_id.value)
        # ReleaseId by default is ISRC
        # If releaseId is chosen to be Proprietary then check if senders_dpid is 
        # given to build the Id
        # If not then raise ProprietaryIdNamespace error
        if self.release_id_type == ReleaseIdType.proprietary_id.value:
            if 'NameSpace' in namespaces:
                add_subelement_with_text(tag, self.release_id_type, self.id, **namespaces)
            else:
                raise NoNamespaceError() # If no Namespace argument is provided then raise NoNamespaceError
        add_subelement_with_text(tag, self.release_id_type, self.id)
        return tag

    def get_reference(self):
        return f"P{self.artist_name.replace(' ', '')}"

    def build_display_artist(self):
        tag = et.Element(Tags.display_artist.value)
        add_subelement_with_text(tag, Tags.artist_party_reference.value, self.get_reference()) # ArtistPartyReference
        add_subelement_with_text(tag, Tags.display_artist_role.value, self.artist_role)
        return tag

    def write(self):
        tag = et.Element(Tags.release.value)
        add_subelement_with_text(tag, Tags.release_reference.value, self.reference)
        # release_type should belong to the ReleaseTypeSet
        # check config file to see what types of release_type values are allowed
        add_subelement_with_text(tag, Tags.release_type.value, self.release_type)
        tag.append(self.build_release_id())

        if self.display_title_text:
            add_subelement_with_text(tag, Tags.display_title_text.value, self.display_title_text)
        else:
            add_subelement_with_text(tag, Tags.display_title_text.value, self.title_text)
        tag.append(self.build_display_title())
        if self.additional_title:
            tag.append(self.build_additional_title())
        add_subelement_with_text(
            tag,
            Tags.display_artist_name.value,
            self.artist_name,
            ApplicableTerritoryCode=self.territory
        )
        tag.append(self.build_display_artist())
        add_subelement_with_text(tag, Tags.release_label_reference.value, self.release_label_reference.replace(' ', ''))
        tag.append(self.build_cline())
        tag.append(self.build_genre())
        add_subelement_with_text(tag, Tags.parental_warning.value, self.parental_warning)

        for release in self.related_release:
            tag.append(release.write())

        for resource in self.resource_group:
            tag.append(resource.write())
        return tag


class RelatedRelease:
    """
    Builds RelatedRelease tag
    It has ReleaseId, ReleaseRelationshipType as child elements
    """
    def __init__(
            self,
            relationship_type,
            id_,
            id_type,
            **namespaces,
            ):
        self.relationship_type = relationship_type
        self.id = id_
        self.id_type = id_type
        self.namespaces = namespaces # Namespace keyword argument for when id_type is proprietary

    def build_release_id(self):
        tag = et.Element(Tags.release_id.value)
        if self.id_type == ReleaseIdType.proprietary_id.value:
            if 'Namespace' in self.namespaces:
                add_subelement_with_text(tag, self.id_type, self.id, **self.namespaces)
            else:
                raise NoNamespaceError()
        add_subelement_with_text(tag, self.id_type, self.id) # Adds default ICPN id_type to the build
        return tag

    def write(self):
        tag = et.Element(Tags.related_release.value)
        if self.relationship_type in ReleaseRelationshipTypeSet:
            add_subelement_with_text(tag, Tags.release_relationship_type.value, self.relationship_type)
        else:
            raise InvalidReleaseRelationshipTypeSet(self.relationship_type)
        tag.append(self.build_release_id())
        return tag


class ResourceGroup:
    def __init__(
            self,
            sequence_number,
            resource_reference,
            linked_resource_reference):
        self.sequence_number = sequence_number
        self.resource_reference = resource_reference
        self.linked_resource_reference = linked_resource_reference

    def build_resource_group_items(self):
        tag = et.Element(Tags.resource_group_content.value)
        add_subelement_with_text(tag, Tags.sequence_number.value, self.sequence_number)
        add_subelement_with_text(tag, Tags.release_resource_reference.value, self.resource_reference)
        add_subelement_with_text(tag, Tags.linked_release_resource_reference.value, self.linked_resource_reference)
        return tag

    def write(self):
        tag = et.Element(Tags.resource_group.value)
        add_subelement_with_text(tag, Tags.sequence_number.value, self.sequence_number)
        tag.append(self.build_resource_group_items())
        return tag
