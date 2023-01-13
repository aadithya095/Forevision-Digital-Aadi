from lxml import etree as et
from datetime import datetime
from enum import Enum
from uuid import uuid4 as uuid
from utils import add_subelement_with_text


class Tags(Enum):
    # Message Header
    root = "MessageHeader"
    message_id = "MessageId"
    thread_id = "MessageThreadId"
    created_date = "MessageCreateDateTime"
    control = "MessageControlType"

    # Message Party
    sender = "MessageSender"
    receiver = "MessageRecipient"
    party_id = "PartyId"
    party_name = "PartyName"
    full_name = "FullName"


class MessageControlType(Enum):
    live_message = "LiveMessage"
    test_message = "TestMessage"


class MessagePartyType(Enum):
    Sender = "Sender"
    Receiver = "Recipient"


class MessageHeader:
    def __init__(self, sender, recipient, message_control=MessageControlType.live_message.value, message_id=None,
                 thread_id=None):
        self.sender = sender
        self.recipient = recipient
        if message_id:
            self.message_id = message_id
        self.message_id = str(uuid())
        if thread_id:
            self.thread_id = thread_id
        self.thread_id = str(uuid())
        self.created_date_time = str(datetime.now())
        self.message_control = message_control

    def write(self):
        tag = et.Element(Tags.root.value)  # MessageHeader
        add_subelement_with_text(tag, Tags.thread_id.value, self.thread_id)
        add_subelement_with_text(tag, Tags.message_id.value, self.message_id)
        tag.append(self.sender.write())
        tag.append(self.recipient.write())
        add_subelement_with_text(tag, Tags.created_date.value, self.created_date_time)
        add_subelement_with_text(tag, Tags.control.value, self.message_control)
        return tag


class MessageParty:
    def __init__(self, name, id_, role=MessagePartyType.Sender.value):
        self.name = name
        self.id_ = id_
        self.role = role

    def build_party_name(self):
        tag = et.Element(Tags.party_name.value)
        add_subelement_with_text(tag, Tags.full_name.value, self.name)  # FullName
        return tag

    def get_reference(self):
        return f"P{self.id_}"

    def make_sender(self):
        tag = et.Element(Tags.sender.value)  # MessageSender
        add_subelement_with_text(tag, Tags.party_id.value, self.id_)  # PartyId
        tag.append(self.build_party_name())  # PartyName
        return tag

    def make_recipient(self):
        tag = et.Element(Tags.receiver.value)  # MessageSender
        add_subelement_with_text(tag, Tags.party_id.value, self.id_)  # PartyId
        tag.append(self.build_party_name())  # PartyName
        return tag

    def write(self):
        if self.role == MessagePartyType.Sender.value:
            return self.make_sender()  # Sender
        if self.role == MessagePartyType.Receiver.value:
            return self.make_recipient()  # Receiver
