from xml.etree import ElementTree as et
from xml.etree.ElementTree import Element
from typing import Tuple
from ddex.utils import add_subelement_with_text, build_duration

SAMPLING_RATE_UNIT = 'kHz'
BIT_RATE_UNIT = 'kbps'

class SoundRecording:
    def __init__(
            self,
            reference: str,
            type: str,
            sound_recording_edition: Element,
            title_text: str,
            artist_name: str,
            duration: Tuple[str, str, str],
            creation_date: str,
            parental_warning_type: str,
            is_instrumental: str,
            language: str,
            applicable_territory_code: str,
            **parties,
            ):
        self.reference = reference
        self.type = type
        self.sound_recording_edition = sound_recording_edition
        self.title_text = title_text
        self.artist_name = artist_name
        self.duration = duration
        self.creation_date = creation_date
        self.parental_waring_type = parental_warning_type
        self.is_instrumental = is_instrumental
        self.language = language
        self.applicable_territory_code = applicable_territory_code
        self.artists = parties['artists']
        self.contributors = parties['contributors']

    def __call__(self):
        tag = et.Element('SoundRecording', ApplyClassicalProfileVariant='true')
        add_subelement_with_text(tag, 'ResourceReference', self.reference)
        add_subelement_with_text(tag, 'Type', self.type)
        tag.append(self.sound_recording_edition)
        add_subelement_with_text(tag, 'DisplayTitleText', self.title_text)
        tag.append(self._build_display_title())
        add_subelement_with_text(tag, "DisplayArtistName", self.artist_name, IsDefault='true')

        for artist in self.artists.values():
            tag.append(artist)
        for contributor in self.contributors.values():
            tag.append(contributor)

        add_subelement_with_text(tag, 'Duration', build_duration(self.duration))
        add_subelement_with_text(tag, 'CreationDate', self.creation_date)
        add_subelement_with_text(tag, 'ParentalWarningType', self.parental_waring_type)
        add_subelement_with_text(tag, 'Is Instrumental', self.is_instrumental)
        add_subelement_with_text(tag, 'LanguageOfPerformance', self.language)
        return tag

    def _build_display_title(self):
        tag = et.Element('DisplayTitle', ApplicableTerritoryCode=self.applicable_territory_code)
        add_subelement_with_text(tag, 'TitleText', self.title_text)
        return tag

class Image:
    def __init__(
            self,
            reference: str,
            type: str,
            resource_id: str,
            title_text: str,
            contributor: Element,
            cline_year: str,
            cline_company: str,
            cline_text: str,
            parental_waring_type: str,
            technical_details: Element
            ):
        self.reference = reference
        self.type = type
        self.resource_id = resource_id
        self.title_text = title_text
        self.contributor = contributor
        self.cline_year = cline_year
        self.cline_company = cline_company
        self.cline_text = cline_text
        self.parental_waring_type = parental_waring_type
        self.technical_details = technical_details

class Artist:
    def __init__(
            self,
            reference: str,
            role: str,
            sequence_number: str,
            artist_type: str,
            ):
        self.reference = reference
        self.role = role
        self.sequence_number = sequence_number
        self.artist_type = artist_type

    def __call__(self):
        if self.artist_type == 'artist':
            tag = et.Element('DisplayArtist', SequenceNumber=self.sequence_number)
            add_subelement_with_text(tag, 'ArtistPartyReference', self.reference)
            add_subelement_with_text(tag, 'DisplayArtistRole', self.role)
            return tag
        if self.artist_type == 'contributor':
            tag = et.Element('Contributor', SequenceNumber=self.sequence_number)
            add_subelement_with_text(tag, 'ContributorPartyReference', self.reference)
            add_subelement_with_text(tag, 'Role', self.role)
            return tag

class SoundRecordingEdition:
    def __init__(
            self, 
            isrc: str, 
            pline_year: str, 
            pline_text: str, 
            technical_details: Element
            ):

        self.isrc = isrc
        self.pline_year = pline_year
        self.pline_text = pline_text
        self.technical_details = technical_details

    def __call__(self):
        tag = et.Element('SoundRecordingEdition')
        tag.append(self._build_resource_id())
        tag.append(self._build_pline())
        tag.append(self.technical_details)
        return tag
    
    def _build_resource_id(self):
        tag = et.Element('ResourceId')
        add_subelement_with_text(tag, 'ISRC', self.isrc)
        return tag

    def _build_pline(self):
        tag = et.Element('PLine')
        add_subelement_with_text(tag, 'Year', self.pline_year)
        add_subelement_with_text(tag, 'PLineText', self.pline_text)
        return tag

class TechnicalDetails:
    def __init__(
            self, 
            reference: str, 
            delivery_file: Element, 
            is_clip: str, 
            clip_details: Element
            ) -> None:

        self.reference = reference
        self.delivery_file = delivery_file
        self.is_clip = is_clip
        self.clip_details = clip_details

    def __call__(self):
        tag = et.Element('TechnicalDetails')
        add_subelement_with_text(tag, 'TechnicalResourceDetailsReference', self.reference)
        tag.append(self.delivery_file)
        add_subelement_with_text(tag, 'IsClip', self.is_clip)
        tag.append(self.clip_details)
        return tag

class DeliveryFile:
    def __init__(
            self, 
            type: str, 
            codectype: str, 
            bitrate: str, 
            channels: str, 
            sampling_rate: str, 
            duration: Tuple[str, str, str], 
            uri: str, 
            hashsum_algorithm: str, 
            hashsum_value: str, 
            is_audio: bool=True
            ) -> None:

        self.type = type
        self.codectype = codectype
        self.bitrate = bitrate
        self.channels = channels
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.uri = uri
        self.hashsum_algorithm = hashsum_algorithm
        self.hashsum_value = hashsum_value
        self.is_audio = is_audio

    def __call__(self) -> Element:
        tag = et.Element('DeliveryFile')
        add_subelement_with_text(tag, 'Type', self.type)
        if self.is_audio:
            add_subelement_with_text(tag, 'AudioCodecType', self.codectype)
            add_subelement_with_text(tag, 'BitRate', self.bitrate, UnitOfMeasure=BIT_RATE_UNIT)
            add_subelement_with_text(tag, 'NumberOfChannels', self.channels)
            add_subelement_with_text(tag, 'SamplingRate', self.sampling_rate, UnitOfMeasure=SAMPLING_RATE_UNIT)
            add_subelement_with_text(tag, 'Duration', build_duration(self.duration))
        file_subtag = self._build_file()
        tag.append(file_subtag)
        return tag

    def _build_file(self) -> Element:
        '''This function builds the File section of the xml'''
        tag = et.Element('File')
        add_subelement_with_text(tag, 'URI', self.uri)
        hashsum_subtag = self._build_hashsum()
        tag.append(hashsum_subtag)
        return tag
    
    def _build_hashsum(self) -> Element:
        '''
        This function does not automatically generate hashsums.
        Automated functionality is a possible use case scenario.
        '''
        tag = et.Element('HashSum')
        add_subelement_with_text(tag, 'Algorithm', self.hashsum_algorithm)
        add_subelement_with_text(tag, 'HashSumValue', self.hashsum_value)
        return tag

class ClipDetails:
    def __init__ (
            self, 
            reference: str, 
            type: str, 
            start_time: str, 
            duration: Tuple[str, str, str], 
            expression_type: str, 
            delivery_file: Element
            ) -> None:

        self.reference = reference
        self.type = type
        self.start_time = start_time
        self.duration = duration
        self.expression_type = expression_type
        self.delivery_file = delivery_file

    def __call__(self) -> Element:
        tag = et.Element('ClipDetails')
        add_subelement_with_text(tag, 'TechnicalResourceDetailsReference', self.reference)
        add_subelement_with_text(tag, 'ClipType', self.type)
        tag.append(self._build_timing())
        add_subelement_with_text(tag, 'ExpressionType', self.expression_type)
        tag.append(self.delivery_file)
        return tag


    def _build_timing(self) -> Element:
        tag: Element = et.Element('Timing')
        add_subelement_with_text(tag, 'StartPoint', self.start_time)
        add_subelement_with_text(tag, 'DurationUsed', build_duration(self.duration))
        return tag
