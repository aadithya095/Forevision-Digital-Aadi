from xml.etree import ElementTree as et
from xml.etree.ElementTree import Element
from typing import Tuple
from ddex.utils import add_subelement_with_text, build_duration

SAMPLING_RATE_UNIT = 'kHz'
BIT_RATE_UNIT = 'kbps'

class Resource:
    def __init__(self, reference, type, id_, pline):
        self.reference = reference
        self.type = type
        self.id_ = id_
        self.pline = pline

class TechnicalDetails:
    def __init__(self, reference, delivery_file, is_clip, clip_details):
        self.reference = reference
        self.delivery_file = delivery_file
        self.is_clip = is_clip
        self.clip_details = clip_details

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
