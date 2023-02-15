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
    Image,
    SoundRecordingEdition,
    Tags,
)
from technical_details import TechnicalDetails


class ResourceBuilder:
    """
    Builds ResourceList part of the DDEX for new release single.
    technical_detail_type: the type of technical detail i.e. either 'Audio', 'Video' or 'Image'
    filename: the name or path of the resource file
    resource_id: the id of the resource, currently ISRC is used
    pline_company: the name of the company if only the name of the company is given
    pline_year: the year of the release, can be none if not mentioned or given
    pline_text: the text of the release, can be none if not mentioned or given
    sound_recording_reference: the reference of the sound recording, currently ISRC is used, in future this will be
    obsolete and redundant
    title_text: the title of the song
    artist_reference: the reference of the artist, currently ISRC is used, in future this will be obsolete and redundant
    artist_role: the role of the artist, can be none if not mentioned or given
    parental_warning: the parental warning of the song, the default value is Unknown
    image_reference: the reference of the image, currently ISRC is used, in future this will be obsolete and redundant
    image_type: the type of the image, can be either FrontCoverImage or VideoStillImage
    image_id_type: the type of the image id, currently proprietary is used and is constructed as such "ISRC_IMG.ext"
    image_id: the id of the image,
    type_: the type of the sound recording, can be either MusicalWorkSoundRecording or MusicalWorkSoundRecording
    contributors: the list of contributors, this cannot be none and must be provided.
    """
    def __init__(self,
                 audio_technical_detail_type,
                 image_technical_details_type,
                 audio_filename,
                 image_filename,
                 resource_id,
                 pline_text,
                 sound_recording_reference,
                 title_text,
                 artist_name,
                 artist_role,
                 parental_warning,
                 id_type,
                 image_reference,
                 image_type,
                 party_id,
                 type_=SoundRecordingType.musical_work_sound_recording.value,
                 pline_company=None,
                 pline_year=None,
                 contributors=[]):
        self.audio_td_type = audio_technical_detail_type
        self.image_td_type = image_technical_details_type
        self.audio_filename = audio_filename
        self.resource_id = resource_id
        self.pline_text = pline_text
        self.pline_company = pline_company # None Attribute
        self.pline_year = pline_year # None Attribute
        self.sound_recording_reference = sound_recording_reference
        self.title_text = title_text
        self.artist_name = artist_name
        self.artist_role = artist_role
        self.parental_warning = parental_warning
        self.type = type_
        self.image_reference = image_reference
        self.image_type = image_type
        self.image_filename = image_filename
        self.id_type = id_type
        self.party_id = party_id
        self.contributors = contributors

    def build(self):
        audio_technical_detail_tag = TechnicalDetails(
            id_=self.resource_id,
            type=self.audio_td_type,
            file=self.audio_filename,
        )

        image_technical_detail_tag = TechnicalDetails(
                id_= self.resource_id,
                type=self.image_td_type,
                file=self.image_filename,
                )

        sound_recording_edition_tag = SoundRecordingEdition(
            resource_id=self.resource_id,
            pline_company=self.pline_company,
            technical_details=audio_technical_detail_tag,
            id_type=self.id_type,
            pline_text=self.pline_text,
            pline_year=self.pline_year,
        )

        sound_recording_tag = SoundRecording(
            reference=self.sound_recording_reference,
            sound_recording_edition=sound_recording_edition_tag,
            title_text=self.title_text,
            artist_name=self.artist_name,
            artist_role=self.artist_role,
            duration=audio_technical_detail_tag.build_duration(),
            parental_warning=self.parental_warning,
            contributors=self.contributors,
            type_=self.type
        )

        image_tag = Image(
            reference=self.image_reference,
            type_=self.image_type,
            # Image id is redundant
            id_=self.resource_id,
            party_id=self.party_id,
            technical_details=image_technical_detail_tag,
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
    import os
    from party import Contributor
    from utils import save
    from config import ROOT_DIR

    test_file_name = os.path.join(ROOT_DIR, 'docs/assets/resources/test_file.wav')
    image_file_name = os.path.join(ROOT_DIR, 'docs/assets/resources/INF232200812IMG.jpg')

    c1 = Contributor('1', 'Orchestra')
    c2 = Contributor('2', 'Vocals')
    c3 = Contributor('3', 'Guitar')

    builder = ResourceBuilder(
        audio_technical_detail_type='AudioType',
        image_technical_details_type="ImageType",
        resource_id='1',
        audio_filename=test_file_name,
        pline_company='ForevisionDigital',
        pline_year='2023',
        pline_text='Belongs to Forevision Digital',
        sound_recording_reference='A1',
        title_text='Tumi Din Dhale',
        artist_name="Subrata Kr Dutta",
        artist_role='MainArtist',
        parental_warning='NoExplicit',
        image_reference='R1',
        image_filename=image_file_name,
        image_type='FrontCoverImage',
        party_id="PAPI10393002",
        contributors=[c1, c2, c3]
    )
    root = builder.build()
    save(root, 'resource_list.xml')
    print("Saved XML file")

