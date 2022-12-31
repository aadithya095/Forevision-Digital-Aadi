from ddex.party import Party
from uuid import uuid4 as uuid
from hashlib import sha1

from ddex.resourcelist import (
        DeliveryFile, 
        ClipDetails, 
        TechnicalDetails, 
        Artist, 
        SoundRecordingEdition
        )

class DeliveryFixture:
    type = 'AudioFile'
    codectype = 'MP3'
    bitrate = '320'
    channels = '2'
    sampling_rate = '44.1'
    duration = ('0', '7', '4')
    uri = 'test.mp3'
    hashsum = sha1('test'.encode('utf-8')).hexdigest()
    hashsum_algorithm = 'sha1'
    compare_file = "./compare_fixtures/deliveryFile.xml"

class ClipDetailFixture:
    reference = 'T3'
    type = 'Preview'
    start_time = '48'
    duration = (0, 0, 30)
    expression_type = 'Informative'

class TechnicalDetailsFixtures:
    reference = 'T2'
    is_clip = 'false'
    
class SoundRecordingEditionFixture:
    isrc = 'JPTO09405080'
    pline_year = '1994'
    pline_text = "RandomText"

class SoundRecordingFixture:
    reference = 'A20'
    type = 'MusicalWorkSoundRecording'
    title_text = 'song'
    artist_name = 'artist'
    duration = ('0', '3', '42')
    creation_date = '1993-12-01'
    parental_waring_type = 'NoAdviceAvailable'
    is_instrumental = 'false'
    language = 'ja'
    applicable_territory_code='WorldWide'

class SenderPartyFixture:
    party_role_sender = "Sender"
    fullname = "Shu Shae Jim"
    party_id = "PADPIDA2013042401U"

class ReceipientPartyFixture:
    party_name = "UniversalMusicStudio"
    party_role_recipient = "Recipient"
    party_id = "PADPIDA2013042401U"

class PartyFixture:
    reference_id = "Shu Shae"
    fullname = "Shu Shae Jim"

class ArtistFixture:
    reference = 'PSaekoShu'
    artist_role = 'MainArtist'
    contributor_role = 'Artist'
    sequence_number = '1'
    artist_type = ('artist', 'contributor')

class Fixtures:
    pf = PartyFixture()
    spf = SenderPartyFixture()
    rpf = ReceipientPartyFixture()
    df = DeliveryFixture()
    cf = ClipDetailFixture()
    af = ArtistFixture()

    def create_party(self) -> Party:
        return Party(
                reference_id=self.pf.reference_id,
                fullname=self.pf.fullname,
                )

    def create_sender(self) -> Party:
        return Party(
                party_id=self.spf.party_id,
                fullname=self.spf.fullname,
                party_role=self.spf.party_role_sender,
                )

    def create_recipient(self) -> Party:
        return Party(
               party_id=self.rpf.party_id,
                fullname=self.rpf.party_name,
                party_role=self.rpf.party_role_recipient,
                )

    def create_thread_id(self) -> str:
        return str(uuid())

    def create_delivery_file(self) -> DeliveryFile:
        element = DeliveryFile(
                self.df.type, 
                self.df.codectype, 
                self.df.bitrate, 
                self.df.channels, 
                self.df.sampling_rate, 
                self.df.duration, 
                self.df.uri, 
                self.df.hashsum_algorithm, 
                self.df.hashsum
                )
        return element() 

    def create_clip_details(self) :
        df = self.create_delivery_file()
        element = ClipDetails(
                reference=self.cf.reference,
                type=self.cf.type,
                start_time=self.cf.start_time,
                duration=self.cf.duration,
                expression_type=self.cf.expression_type,
                delivery_file=df
                )

        return element()

    def create_technical_details(self):
        df = self.create_delivery_file()
        cf = self.create_clip_details()
        td = TechnicalDetailsFixtures()

        element = TechnicalDetails(
                reference=td.reference,
                delivery_file=df,
                is_clip=td.is_clip,
                clip_details=cf
                )

        return element()
    
    def create_sound_recording_edition(self):
        td = self.create_technical_details()
        sre = SoundRecordingEditionFixture()
        element = SoundRecordingEdition(
                isrc=sre.isrc,
                pline_year=sre.pline_year,
                pline_text=sre.pline_text,
                technical_details=td
                )
        return element()
    
    def create_artist(self, type):
        if type == 'artist':
            element = Artist(
                    reference=self.af.reference,
                    role=self.af.artist_role,
                    sequence_number=self.af.sequence_number,
                    artist_type=type
                    )

            return element()

        if type == 'contributor':
            element = Artist(
                    reference=self.af.reference,
                    role=self.af.contributor_role,
                    sequence_number=self.af.sequence_number,
                    artist_type=type
                    )
            return element()
