from hashlib import sha1
from ddex.utils import assertData
from ddex.resourcelist import (
        DeliveryFile, 
        ClipDetails, 
        TechnicalDetails, 
        SoundRecordingEdition, 
        Artist,
        SoundRecording
        )

from ddex.fixtures import (
        Fixtures, 
        ClipDetailFixture, 
        TechnicalDetailsFixtures, 
        SoundRecordingEditionFixture, 
        DeliveryFixture, 
        ArtistFixture, 
        SoundRecordingFixture
        )

class TestResourceList:
    fix = Fixtures()

    def test_delivery_file(self):
        dfix = DeliveryFixture()
        compare_file = "deliveryFile.xml"
        df = DeliveryFile(
                dfix.type, 
                dfix.codectype, 
                dfix.bitrate, 
                dfix.channels, 
                dfix.sampling_rate, 
                dfix.duration, 
                dfix.uri, 
                dfix.hashsum_algorithm, 
                dfix.hashsum
                )

        tag = df()
        assertData(tag, compare_file)

    def test_clip_details(self):
        compare_file = "clipDetails.xml"
        df = self.fix.create_delivery_file()
        cf = ClipDetailFixture()
        clipdetail = ClipDetails(
                reference=cf.reference,
                type=cf.type,
                start_time=cf.start_time,
                duration=cf.duration,
                expression_type=cf.expression_type,
                delivery_file=df
                )
        tag = clipdetail()
        assertData(tag, compare_file)

    def test_technical_details(self):
        compare_file = "technicalDetails.xml"
        df = self.fix.create_delivery_file()
        cf = self.fix.create_clip_details()
        td = TechnicalDetailsFixtures()
        element = TechnicalDetails(
                reference=td.reference,
                delivery_file=df,
                is_clip=td.is_clip,
                clip_details=cf
                )

        tag = element()
        assertData(tag, compare_file)

    def test_sound_recording_edition(self):
        compare_file = "soundRecordingEdition.xml"
        td = self.fix.create_technical_details()
        sre = SoundRecordingEditionFixture()
        element = SoundRecordingEdition(
                isrc=sre.isrc,
                pline_year=sre.pline_year,
                pline_text=sre.pline_text,
                technical_details=td
                )

        tag = element()
        assertData(tag, compare_file)

    def test_artists(self):
        compare_file = "displayArtist.xml"
        af = ArtistFixture()
        element = Artist(
                reference=af.reference,
                role=af.artist_role,
                sequence_number=af.sequence_number,
                artist_type=af.artist_type[0]
                )

        tag = element()
        assertData(tag, compare_file)

    def test_contributors(self):
        compare_file = "contributors.xml"
        af = ArtistFixture()
        element = Artist(
                reference=af.reference,
                role=af.contributor_role,
                sequence_number=af.sequence_number,
                artist_type=af.artist_type[1]
                )
        tag = element()
        assertData(tag, compare_file)

    def test_sound_recording(self):
        compare_file = "soundRecording.xml"
        artist = self.fix.create_artist('artist')
        contributor = self.fix.create_artist('contributor')
        sound_record_edition = self.fix.create_sound_recording_edition()
        srf = SoundRecordingFixture()

        element = SoundRecording(
                reference=srf.reference,
                type=srf.type,
                sound_recording_edition=sound_record_edition,
                title_text=srf.title_text,
                artist_name=srf.artist_name,
                duration=srf.duration,
                creation_date=srf.creation_date,
                parental_warning_type=srf.parental_waring_type,
                is_instrumental=srf.is_instrumental,
                language=srf.language,
                applicable_territory_code=srf.applicable_territory_code,
                artists={'a1':artist},
                contributors={'c1':contributor}
                )
        tag = element()
        assertData(tag, compare_file)
        








