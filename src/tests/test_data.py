from ddex.party import Party
from ddex.messageheader import MessageHeader
from ddex.utils import prettyprint, add_subelement_with_text, reparse_xml
from uuid import uuid4 as uuid

class Fixtures:
    party_name = "UniversalMusicStudio"
    party_role_sender = "Sender"
    party_role_recipient = "Recipient"
    reference_id = "Shu Shae"
    fullname = "Shu Shae Jim"
    party_id = "PADPIDA2013042401U"

    def create_party(self):
        return Party(
                reference_id=self.reference_id,
                fullname=self.fullname,
                ).create()

    def create_sender(self):
        return Party(
                party_id=self.party_id,
                fullname=self.fullname,
                party_role=self.party_role_sender,
                ).create()

    def create_recipient(self):
        return Party(
                party_id=self.party_id,
                fullname=self.party_name,
                party_role=self.party_role_recipient,
                ).create()

    def create_thread_id(self):
        return str(uuid())


class TestCases:
    def test_prettyprint():
        fix = Fixtures()
        party = fix.create_party()
        rough_string = reparse_xml(party)
        prettyprint(rough_string)

    def test_message_header():
        fix = Fixtures()
        sender = fix.create_sender()
        receiver = fix.create_recipient()
        thread_id = fix.create_thread_id()
        message_id = '1'
        
        messageHeader = MessageHeader(thread_id, message_id, sender, receiver).create()
        return messageHeader



