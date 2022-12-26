from ddex.party import Party
from uuid import uuid4 as uuid
from hashlib import sha1

from ddex.resourcelist import DeliveryFile

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

class Fixtures:
    pf = PartyFixture()
    spf = SenderPartyFixture()
    rpf = ReceipientPartyFixture()
    df = DeliveryFixture()
    cf = ClipDetailFixture()

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
        delivery_file = DeliveryFile(
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
        return delivery_file
