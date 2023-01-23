"""
Author: iamu985
Github: https://github.com/iamu985
DateCompleted: Saturday, January 07, 2023 IST 12:37AM

TODO
- No tests are written
- Removing redundant reference argument and automatically assigning the reference
- Need to write proper documentation

--------------
Documentation
--------------
All required tags or parts of ResourceList such as SoundRecording, SoundRecordingEdition, etc.
"""

from enum import Enum
from lxml import etree as et
from utils import add_subelement_with_text, format_duration


class Tags(Enum):
    resource_list = "ResourceList"
    sound_recording = "SoundRecording"
    reference = "ResourceReference"
    type = "Type"
    sound_recording_edition = "SoundRecordingEdition"
    resource_id = "ResourceId"
    pline = "PLine"
    pline_year = "Year"
    pline_company = "PLineCompany"
    pline_text = "PLineText"
    technical_details = "TechnicalDetails"
    tech_resource_ref = "TechnicalResourceDetailsReference"
    delivery_file = "DeliveryFile"
    type_ = "Type"
    codec_type = "AudioCodecType"
    bitrate = "BitRate"
    channels = "NumberOfChannels"
    sampling_rate = "SamplingRate"
    duration = "Duration"
    file = "File"
    uri = "URI"
    hashsum = "HashSum"
    algo = "Algorithm"
    hashsum_value = "HashSumValue"
    display_title_text = "DisplayTitleText"
    display_title = "DisplayTitle"
    title_text = "TitleText"
    display_artist_name = "DisplayArtistName"
    display_artist = "DisplayArtist"
    artist_party_reference = "ArtistPartyReference"
    display_artist_role = "DisplayArtistRole"
    artist_role = "ArtistRole"
    contributor = "Contributor"
    contributor_party_reference = "ContributorPartyReference"
    role = "Role"
    parental_warning = "ParentalWarningType"
    isrc = "ISRC"
    image = "Image"
    proprietary_id = "ProprietaryId"


class SoundRecordingType(Enum):
    audio_stem = "AudioStem"
    clip = "Clip"
    musical_work_readalong_sound_rec = "MusicalWorkReadAlongSoundRecording"
    musical_work_sound_recording = "MusicalWorkSoundRecording"
    non_musical_work_readalong_sound_rec = "NonMusicalWorkReadAlongSoundRecording"
    non_musical_work_sound_recording = "NonMusicalWorkSoundRecording"
    spoken_work_sound_recording = "SpokenWorkSoundRecording"
    unknown = "Unknown"
    user_defined = "UserDefined"


class ImageIdType(Enum):
    proprietary_id = "ProprietaryId"


class ResourceList:
    def __init__(self, sound_recording, image):
        self.sound_recording = sound_recording
        self.image = image

    def write(self):
        tag = et.Element(Tags.resource_list.value)
        tag.append(self.sound_recording.write())
        tag.append(self.image.write())
        return tag


class SoundRecording:
    def __init__(self,
                 reference,
                 sound_recording_edition,
                 title_text,
                 artist_name,
                 artist_role,
                 duration,
                 parental_warning,
                 contributors=[],
                 type_=SoundRecordingType.musical_work_sound_recording.value):
        self.reference = reference
        self.sound_recording_edition = sound_recording_edition
        self.title_text = title_text
        self.artist_name = artist_name
        self.artist_role = artist_role
        self.duration = duration
        self.parental_warning = parental_warning
        self.contributors = contributors
        self.type = type_

    def get_reference(self):
        return f"P{self.artist_name.replace(' ', '')}" # Returns a string of artist name with prefix P and no spaces

    def build_display_artist(self):
        """Builds DisplayArtist tag"""
        tag = et.Element(Tags.display_artist.value)
        add_subelement_with_text(tag, Tags.artist_party_reference.value, self.get_reference()) # ArtistPartyReference
        add_subelement_with_text(tag, Tags.display_artist_role.value, self.artist_role) # DisplayArtistRole
        return tag

    def build_display_title(self):
        """
        Builds DisplayTitle tag.

        Xml:
        <DisplayTitle>
            <TitleText>Title</TitleText>
        </DisplayTitle>
        """
        tag = et.Element(Tags.display_title.value)
        add_subelement_with_text(tag, Tags.title_text.value, self.title_text)
        return tag

    def write(self):
        tag = et.Element(Tags.sound_recording.value)
        add_subelement_with_text(tag, Tags.reference.value, self.reference)
        add_subelement_with_text(tag, Tags.type.value, self.type)
        tag.append(self.sound_recording_edition.write())

        #  This only builds the display title text tag by using 
        #  artist_name and title_text provided to the object
        #  TODO: Optional display_title_text needs to be an attribute
        #  To provide an option to use other titles of display
        #  Except the ones provided
        add_subelement_with_text(tag, Tags.display_title_text.value, f"{self.artist_name}: {self.title_text}")
        tag.append(self.build_display_title())
        add_subelement_with_text(tag, Tags.display_artist_name.value, self.artist_name)
        tag.append(self.build_display_artist())

        #  This builds Contributor section
        #  Though I find it unclear on a proper implementation of
        #  the contributor section
        for i, contributor in enumerate(self.contributors):
            tag.append(contributor.write(SequenceNumber=str(i)))
        add_subelement_with_text(tag, Tags.duration.value, self.duration)
        add_subelement_with_text(tag, Tags.parental_warning.value, self.parental_warning)
        return tag


class SoundRecordingEdition:
    def __init__(self,
                 resource_id,
                 pline_text,
                 technical_details,
                 pline_company=None,
                 pline_year=None,
                 ):
        self.resource_id = resource_id
        self.technical_details = technical_details
        self.pline_text = pline_text
        self.pline_company = pline_company
        self.pline_year = pline_year

    def build_resource_id(self):
        tag = et.Element(Tags.resource_id.value)
        add_subelement_with_text(tag, Tags.isrc.value, self.resource_id)
        return tag

    def build_pline(self):
        """
        It returns the PLine tag.
        PLineCompany is not None and can have the name of the party if provided.
        PlineText is optional and is to be used when there is an actual text for pline. Eg: @2020 Sony Music Entertainment
        PLineYear is not necessary for new releases if the input is not provided.
        """
        tag = et.Element(Tags.pline.value)  # PLine
        if self.pline_year:
            add_subelement_with_text(tag, Tags.pline_year.value, self.pline_year)  # PLineYear

        add_subelement_with_text(tag, Tags.pline_text.value, self.pline_text)  # PLineText

        if self.pline_company:
            add_subelement_with_text(tag, Tags.pline_company.value, self.pline_company)  # PLineCompany
        return tag

    def write(self):
        tag = et.Element(Tags.sound_recording_edition.value)
        tag.append(self.build_resource_id())
        tag.append(self.build_pline())
        tag.append(self.technical_details.write())
        return tag


class Image:
    """
    Image class is used to create the Image tag. It gets included inside ResourceList.
    """
    def __init__(self, reference, type_, id_, party_id):
        self.reference = reference  # a unique reference for the image resource over the whole document
        self.type = type_  # the type of the image resource
        self.id = id_  # the identifier of the image resource, proprietary id is currently used.
        self.party_id = party_id # party_id is used as a value for namespace in ProprietaryId

    def build_resource_id(self):
        """
        This function builds resource id with proprietary id.
        """
        tag = et.Element(Tags.resource_id.value)
        add_subelement_with_text(tag, Tags.proprietary_id.value, self.id, Namespace=self.party_id)
        return tag

    def write(self):
        """
        It returns lxml tag for Image
        """
        tag = et.Element(Tags.image.value)
        add_subelement_with_text(tag, Tags.reference.value, self.reference)
        add_subelement_with_text(tag, Tags.type_.value, self.type)
        tag.append(self.build_resource_id())
        return tag
