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
from src.ddex.utils import add_subelement_with_text


class Tags(Enum):
    resource_list = "ResourceList"
    sound_recording = "SoundRecording"
    reference = "ResourceReference"
    type = "Type"
    sound_recording_edition = "SoundRecordingEdition"
    resource_id = "ResourceId"
    pline = "Pline"
    pline_year = "Year"
    pline_company = "PlineCompany"
    pline_text = "PlineText"
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
    display_artist = "DisplayArtist"
    artist_party_reference = "ArtistPartyReference"
    display_artist_role = "DislplayArtistRole"
    artist_role = "ArtistRole"
    contributor = "Contributor"
    contributor_party_reference = "ContributorPartyReference"
    role = "Role"
    parental_warning = "ParentalWarning"
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
                 artist_reference,
                 artist_role,
                 duration,
                 parental_warning,
                 contributors=[],
                 type_=SoundRecordingType.musical_work_sound_recording.value):
        self.reference = reference
        self.sound_recording_edition = sound_recording_edition
        self.title_text = title_text
        self.artist_reference = artist_reference
        self.artist_role = artist_role
        self.duration = duration
        self.parental_warning = parental_warning
        self.contributors = contributors
        self.type = type_

    def build_display_artist(self):
        tag = et.Element(Tags.display_artist.value)
        add_subelement_with_text(tag, Tags.artist_party_reference.value, self.artist_reference)
        add_subelement_with_text(tag, Tags.display_artist_role.value, self.artist_role)
        return tag

    def write(self):
        tag = et.Element(Tags.sound_recording.value)
        add_subelement_with_text(tag, Tags.reference.value, self.reference)
        add_subelement_with_text(tag, Tags.type.value, self.type)
        tag.append(self.sound_recording_edition.write())
        add_subelement_with_text(tag, Tags.display_title_text.value, self.title_text)
        for i, contributor in enumerate(self.contributors):
            tag.append(contributor.write(SequenceNumber=str(i)))
        return tag


class SoundRecordingEdition:
    def __init__(self,
                 resource_id,
                 pline_year,
                 pline_company,
                 pline_text,
                 technical_details):
        self.resource_id = resource_id
        self.pline_year = pline_year
        self.pline_company = pline_company
        self.pline_text = pline_text
        self.technical_details = technical_details

    def build_resource_id(self):
        tag = et.Element(Tags.resource_id.value)
        add_subelement_with_text(tag, Tags.isrc.value, self.resource_id)
        return tag

    def build_pline(self):
        tag = et.Element(Tags.pline.value)
        add_subelement_with_text(tag, Tags.pline_year.value, self.pline_year)
        add_subelement_with_text(tag, Tags.pline_company.value, self.pline_company)
        add_subelement_with_text(tag, Tags.pline_text.value, self.pline_text)
        return tag

    def write(self):
        tag = et.Element(Tags.sound_recording_edition.value)
        tag.append(self.build_resource_id())
        tag.append(self.build_pline())
        tag.append(self.technical_details.write())
        return tag


class TechnicalDetails:
    def __init__(self,
                 id_,
                 type_,
                 codec,
                 bitrate,
                 channels,
                 sampling,
                 duration,
                 uri,
                 hash_algorithm,
                 hash_value,
                 ):
        self.id = id_
        self.type = type_
        self.codec = codec
        self.bitrate = bitrate
        self.channels = channels
        self.sampling = sampling
        self.duration = duration
        self.uri = uri
        self.hash_algorithm = hash_algorithm
        self.hash_value = hash_value

    def get_reference(self):
        return f'T{self.id}'

    def build_file(self):
        tag = et.Element(Tags.file.value)
        add_subelement_with_text(tag, Tags.uri.value, self.uri)
        tag.append(self.build_hashsum())
        return tag

    def build_hashsum(self):
        tag = et.Element(Tags.hashsum.value)
        add_subelement_with_text(tag, Tags.algo.value, self.hash_algorithm)
        add_subelement_with_text(tag, Tags.hashsum_value.value, self.hash_value)
        return tag

    def build_delivery_file(self):
        tag = et.Element(Tags.delivery_file.value)
        add_subelement_with_text(tag, Tags.type.value, self.type)  # Type
        add_subelement_with_text(tag, Tags.codec_type.value, self.codec)  # AudioCodecType
        add_subelement_with_text(tag, Tags.bitrate.value, self.bitrate)  # BitRate
        add_subelement_with_text(tag, Tags.channels.value, self.channels)  # NumberOfChannels
        add_subelement_with_text(tag, Tags.sampling_rate.value, self.sampling)  # SamplingRate
        add_subelement_with_text(tag, Tags.duration.value, self.duration)  # Duration
        tag.append(self.build_file())
        return tag

    def write(self):
        tag = et.Element(Tags.technical_details.value)
        add_subelement_with_text(tag, Tags.tech_resource_ref.value, self.get_reference())
        tag.append(self.build_delivery_file())
        return tag


class Image:
    def __init__(self, reference, type_, id_, id_type=ImageIdType.proprietary_id.value):
        self.reference = reference
        self.type = type_
        self.id = id_
        self.id_type = id_type

    def build_resource_id(self):
        tag = et.Element(Tags.resource_id.value)
        if self.id_type == ImageIdType.proprietary_id.value:
            add_subelement_with_text(tag, Tags.proprietary_id.value, self.id)
            return tag
        else:
            add_subelement_with_text(tag, self.id_type, self.id)
            return tag

    def write(self):
        tag = et.Element(Tags.image.value)
        add_subelement_with_text(tag, Tags.reference.value, self.reference)
        print(f"{self.type=}")
        add_subelement_with_text(tag, Tags.type_.value, self.type)
        tag.append(self.build_resource_id())
        return tag
