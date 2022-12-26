import xmltodict
from hashlib import sha1

from ddex.utils import getstring_from_file, getstring_from_element
from ddex.resourcelist import DeliveryFile, ClipDetails
from ddex.fixtures import Fixtures, ClipDetailFixture

class TestResourceList:
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

    fix = Fixtures()

    def test_delivery_file(self):
        df = DeliveryFile(
                self.type, 
                self.codectype, 
                self.bitrate, 
                self.channels, 
                self.sampling_rate, 
                self.duration, 
                self.uri, 
                self.hashsum_algorithm, 
                self.hashsum
                )

        tag = df()
        xml_data = getstring_from_element(tag)
        xml_dict = xmltodict.parse(xml_data)

        original_data = getstring_from_file(self.compare_file)
        expected_data = xmltodict.parse(original_data)

        assert xml_dict == expected_data

    def test_clip_details(self):
        compare_file = "./compare_fixtures/clipDetails.xml"
        df = self.fix.create_delivery_file()
        cf = ClipDetailFixture()
        clipdetail = ClipDetails(
                reference=cf.reference,
                type=cf.type,
                start_time=cf.start_time,
                duration=cf.duration,
                expression_type=cf.expression_type,
                delivery_file=df()
                )

        tag = clipdetail()
        xml_data = getstring_from_element(tag)
        xml_dict = xmltodict.parse(xml_data)
        
        original_data = getstring_from_file(compare_file)
        expected_data = xmltodict.parse(original_data)

        assert xml_dict == expected_data











