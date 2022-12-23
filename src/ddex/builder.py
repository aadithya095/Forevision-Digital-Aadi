from xml.etree import ElementTree as et
from xml.etree.ElementTree import ElementTree
from ddex.messageheader import MessageHeader
from ddex.party import Party

class Builder:
    '''Build Ddex Xml file'''
    def __init__(self, sender, receiver, release_profile='Audio'):
        self.sender = sender
        self.receiver = receiver
        self.release_profile = release_profile

    def build(self):
        root_attrib = {
                'xmlns:ern': 'http://ddex.net/xml/ern/43',
                'xmlns:xsi': 'http://w3.org/2001/XMLSchema-instance',
                'xsi:schemaLocation': 'http://ddex.net/xml/ern/43 http://ddex.net/xml/ern/43/release-notification.xsd',
                'ReleaseProfileVersionId': self.release_profile,
                'LanguageAndScriptCode': 'en',
                'AvsVersionId':'3',
                }

        root_name = "ern:NewReleaseMessage"

        root = et.Element(root_name, root_attrib)
        messageHeader = self._build_message_header()
        root.append(messageHeader)
        return root

    def save(self, root, output="./test.xml"):
        stream = et.tostring(root, 'utf-8')
        with open(output, 'wb') as writeFile:
            writeFile.write(stream)

    def _build_message_header(self):
        return MessageHeader(self.sender, self.receiver).create()


