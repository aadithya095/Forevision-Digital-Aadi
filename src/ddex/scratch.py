"""
Author: iamu985
Github: https://github.com/iamu985

TODO
- add tests for all the functions
- patch the code to make it work with ddex module
- provide neat and clean documentation for each functions
- refactor other parts of the ddex module to make it work with this

Documentation It is a scratch file to possible automate the process of making Technical Details section without any
inputs from the user. In future it might be patched with the main resource.py file.

Future Work
- Perhaps the file argument might change depending on how the user wants to provide the resource
Maybe the we can directly access the audio file from the media resource provided by django and process it without
saving it in the database.
"""

import audio_metadata
from resource import Tags
from utils import add_subelement_with_text, parse_file_path
from mp3hash import mp3hash
from lxml import etree as et


# id_ is used to create a reference id with T as a prefix. Example: T1, T2, T3
# as required by the ddex standard

# type is the type of the file received. It can be of the following types
# - Audio
# - Video
# - Image

# file is the full path of the resource file to be uploaded to the sftp server
class TechnicalDetails:
    def __init__(self, id_, type, file):
        self.id_ = id_
        self.type = type
        self.file = file

        # the metadata for the audio file
        # TODO: add support for other types of files (Images, Videos)
        self.metadata = audio_metadata.load(file)['streaminfo']  # holds all the metadata of the audio file
        self.bitrate = str(self.metadata.bitrate / 1000)  # converting to kbps from bytes
        self.channels = str(self.metadata.channels)
        self.sample_rate = str(self.metadata.sample_rate / 1000)  # converting to kbps from bytes

        self.duration = self.metadata.duration  # duration is in seconds need to convert it to PT0M00S format
        self.hash_value = mp3hash(file)

    def get_reference(self):
        # The reference id can be used to refer to the technical details
        # in the other parts of the ddex file
        # I have used the resource's id as the reference id
        # with T as a prefix as required by the ddex standard
        return f'T{self.id_}'

    def build_hashsum(self):
        # builds hashsum using mp3hash library
        # currently takes md5 as the hash algorithm
        tag = et.Element(Tags.hashsum.value)
        add_subelement_with_text(tag, Tags.algo.value, 'MD5')
        add_subelement_with_text(tag, Tags.hashsum_value.value, self.hash_value)
        return tag

    def build_file(self):
        """Returns the File element"""
        tag = et.Element(Tags.file.value)
        # URI must be resources directory as it is the standard directory name to upload the resources
        # on sftp server
        filename = parse_file_path(self.file)
        add_subelement_with_text(tag, Tags.uri.value, f"resources/{filename}")  # URI
        tag.append(self.build_hashsum())
        return tag

    def build_duration(self):
        """Returns a string in PT0M00S format"""
        minutes = int(self.duration // 60)
        seconds = int(self.duration % 60)
        return f'PT{minutes}M{seconds}S'

    def build_delivery_file(self):
        """Returns the DeliveryFile element"""
        tag = et.Element(Tags.delivery_file.value)  # DeliveryTag
        add_subelement_with_text(tag, Tags.type.value, self.type)

        # Making codec tag for all supported types of files
        if 'mp3' in str(type(self.metadata)):
            add_subelement_with_text(tag, Tags.codec_type.value, 'MP3')
        if 'flac' in str(type(self.metadata)):
            add_subelement_with_text(tag, Tags.codec_type.value, 'FLAC')
        if 'wav' in str(type(self.metadata)):
            add_subelement_with_text(tag, Tags.codec_type.value, 'WAV')
        if 'ogg' in str(type(self.metadata)):
            add_subelement_with_text(tag, Tags.codec_type.value, 'OGG')
        if 'aac' in str(type(self.metadata)):
            add_subelement_with_text(tag, Tags.codec_type.value, 'AAC')

        add_subelement_with_text(tag, Tags.bitrate.value, self.bitrate)  # BitRate
        add_subelement_with_text(tag, Tags.channels.value, self.channels)  # Channels
        add_subelement_with_text(tag, Tags.sampling_rate.value, self.sample_rate)  # SamplingRate
        add_subelement_with_text(tag, Tags.duration.value, self.build_duration())  # Duration
        return tag

    def write(self):
        """Returns the TechnicalDetails element"""
        tag = et.Element(Tags.technical_details.value)  # TechnicalDetails
        add_subelement_with_text(tag, Tags.tech_resource_ref.value, self.get_reference())  # ResourceReference
        tag.append(self.build_file())  # File
        tag.append(self.build_delivery_file())  # DeliveryFile
        return tag


if __name__ == "__main__":
    """This is just a test to see if the code works"""
    import os
    from config import ROOT_DIR
    from utils import save

    resources_dir = os.path.join(ROOT_DIR, 'docs/assets/resources')
    file = os.path.join(resources_dir, 'INF232200812.wav')
    print(file)

    td = TechnicalDetails('INF232200812', 'Audio', file)
    tag = td.write()
    save(tag, 'INF232200812_technical_details.xml')
    print(f"Technical Details for {file} is written to INF232200812_technical_details.xml")



