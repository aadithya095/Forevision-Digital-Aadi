"""
Author: iamu985
Github: https://github.com/iamu985
DateCompleted: Sunday, January 08, IST 10:06PM

TODO
- No tests are written
- Removing redundant reference argument and automatically assigning the reference
- Need to write proper documentation

--------------
Documentation
--------------

Builds ResourceList part of the DDEX for new release single.
"""
from resource import (
    ResourceList,
    SoundRecordingType,
    SoundRecording,
    TechnicalDetails,
    Image,
    SoundRecordingEdition
)


class ResourceBuilder:
    def __init__(self,
                 td_id,
                 td_type,
                 audio_codec,
                 bitrate,
                 channels,
                 sampling,
                 duration,
                 uri,
                 hash_algorithm,
                 hash_value,
                 resource_id,
                 pline_company,
                 pline_year,
                 pline_text,
                 sound_recording_reference,
                 title_text,
                 artist_reference,
                 artist_role,
                 parental_warning,
                 image_reference,
                 image_type,
                 image_id_type,
                 image_id,
                 type_=SoundRecordingType.musical_work_sound_recording.value,
                 contributors=[]):
        self.td_id = td_id
        self.td_type = td_type
        self.audio_codec = audio_codec
        self.bitrate = bitrate
        self.channels = channels
        self.sampling = sampling
        self.duration = duration
        self.uri = uri
        self.hash_algorithm = hash_algorithm
        self.hash_value = hash_value
        self.resource_id = resource_id
        self.pline_company = pline_company
        self.pline_year = pline_year
        self.pline_text = pline_text
        self.sound_recording_reference = sound_recording_reference
        self.title_text = title_text
        self.artist_reference = artist_reference
        self.artist_role = artist_role
        self.parental_warning = parental_warning
        self.type = type_
        self.image_reference = image_reference
        self.image_id_type = image_id_type
        self.image_type = image_type
        self.image_id = image_id
        self.contributors = contributors

    def build(self):
        technical_detail_tag = TechnicalDetails(
            id_=self.td_id,
            type_=self.td_type,
            codec=self.audio_codec,
            bitrate=self.bitrate,
            channels=self.channels,
            sampling=self.sampling,
            duration=self.duration,
            uri=self.uri,
            hash_algorithm=self.hash_algorithm,
            hash_value=self.hash_value
        )

        sound_recording_edition_tag = SoundRecordingEdition(
            resource_id=self.resource_id,
            pline_year=self.pline_year,
            pline_text=self.pline_text,
            pline_company=self.pline_company,
            technical_details=technical_detail_tag
        )

        sound_recording_tag = SoundRecording(
            reference=self.sound_recording_reference,
            sound_recording_edition=sound_recording_edition_tag,
            title_text=self.title_text,
            artist_reference=self.artist_reference,
            artist_role=self.artist_role,
            duration=self.duration,
            parental_warning=self.parental_warning,
            contributors=self.contributors,
            type_=self.type
        )
        image_tag = Image(
            reference=self.image_reference,
            type_=self.image_type,
            id_=self.image_id,
            id_type=self.image_id_type
        )
        resource_list_tag = ResourceList(
            sound_recording=sound_recording_tag,
            image=image_tag
        )
        root = resource_list_tag.write()
        return root


if __name__ == "__main__":
    """
    This File should only run as a module for testing purposes.
    Need to be removed once done properly with the tests and documentation.
    """
    from party import Contributor
    from utils import save

    c1 = Contributor('1', 'Orchestra')
    c2 = Contributor('2', 'Vocals')
    c3 = Contributor('3', 'Guitar')

    builder = ResourceBuilder(
        td_id='1',
        td_type='AudioFile',
        audio_codec='Mp3',
        bitrate='16',
        channels='2',
        sampling='44.1',
        duration='PT0H3M20S',
        uri='resources/tests.mp3',
        hash_algorithm='md5',
        hash_value='dad345add3324ewa4',
        resource_id='1',
        pline_company='ForevisionDigital',
        pline_year='2023',
        pline_text='Belongs to Forevision Digital',
        sound_recording_reference='A1',
        title_text='Tumi Din Dhale',
        artist_reference='P1',
        artist_role='MainArtist',
        parental_warning='NoExplicit',
        image_reference='R1',
        image_type='FrontCoverImage',
        image_id_type='ProprietaryId',
        image_id='PAPI1034003',
        contributors=[c1, c2, c3]
    )
    root = builder.build()
    save(root, 'resource_list.xml')
    print("Saved XML file")

