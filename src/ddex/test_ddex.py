import pytest
from ddex.party import Party, PartyType
from ddex.messageheader import MessageHeader, MessageControlType

class TestCases:
    def test_sender(self):
        sender = Party('ForevisionDigital', 'Pfore')
        assert sender.write().tag == 'MessageSender'

    def test_receiver(self):
        receiver = Party('Universal Studios', 'Puniversal', PartyType.Receiver.value)
        assert receiver.write().tag == 'MessageRecipient'

