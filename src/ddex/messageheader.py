import typing
from uuid import uuid4 as uuid
from xml.etree import ElementTree as et
from ddex.utils import add_subelement_with_text

class MessageHeader:
    '''Build MessageHeader'''

    def __init__(self, sender, recipient, thread_id=None, message_id=None):
        if thread_id:
            self.thread_id = thread_id
        else:
            self.thread_id = str(uuid())

        if message_id:
            self.message_id = message_id
        else:
            self.message_id = str(uuid())

        self.sender = sender
        self.recipient = recipient

    def __call__(self):
        message_header_tag = et.Element("MessageHeader")
        add_subelement_with_text(message_header_tag, "MessageThreadId", self.thread_id)
        add_subelement_with_text(message_header_tag, "MessageId", self.message_id)
        sender_tag = et.SubElement(message_header_tag, "MessageSender")
        sender_tag.append(self.sender)
        recipient_tag= et.SubElement(message_header_tag, "MessageRecepient")
        recipient_tag.append(self.recipient)
        return message_header_tag




