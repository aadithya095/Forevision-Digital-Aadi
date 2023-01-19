from src.ddex.ddex_builder import DdexBuilder
from lxml import etree as et
import os
def make_ddex():
    print('Warning! This is only to be run for development purposes and will not be deployed in production.')
    print('Enter the following details:')
    song_name = 'Akash Nila Nila Sopun'
    song_id_type = 'ISRC'
    song_id = 'INF232200812'
    territory = 'Regional'
    artist_name = 'Tanmay Jyoti Pathak'
    artist_role = 'RecordingArtist'
    pline_year = '2023'
    pline_text = 'Banjit Pathak'
    cline_year = '2023'
    cline_text = 'Amit Soukadhara'
    genre = 'Regional'
    record_label_name = 'HRIDOI'
    codec = 'WAV'
    bitrate = '16'
    channels = '2'
    sampling = '44.1'
    duration = 'PT0H3M52S'
    uri = 'resource/Akash Nila Nila Sopun.wav'
    hash_algorithm = 'md5'
    hash_value = 'b99130fb10c5b2a932d448722486a176'
    parental_warning = 'Unknown'
    image_id = 'INF232200812IMG'
    image_id_type = 'ISRC'
    image_type = 'FrontCoverImage'
    sender_name = "Forevision Digital"
    sender_dpid = 'PADPIDA2015010310U'
    receiver_name = 'JAXTA'
    receiver_dpid = 'PADPIDA2015010310U'
    builder = DdexBuilder(
        song_name=song_name,
        song_id_type=song_id_type,
        song_id=song_id,
        territory=territory,
        artist_name=artist_name,
        artist_role=artist_role,
        pline_year=pline_year,
        pline_text=pline_text,
        cline_year=cline_year,
        cline_text=cline_text,
        genre=genre,
        record_label_name=record_label_name,
        codec=codec,
        bitrate=bitrate,
        channels=channels,
        sampling=sampling,
        duration=duration,
        uri=uri,
        hash_algorithm=hash_algorithm,
        hash_value=hash_value,
        parental_warning=parental_warning,
        image_id=image_id,
        image_id_type=image_id_type,
        image_type=image_type,
        sender_name=sender_name,
        sender_dpid=sender_dpid,
        receiver_name=receiver_name,
        receiver_dpid=receiver_dpid
    )
    root = builder.build()
    curr_dir = os.getcwd()
    filename = 'test_single_release.xml'
    filepath = os.path.join(curr_dir, filename)
    tree = et.ElementTree(root)
    tree.write(filepath, pretty_print=True)
    print(f'Saved {filename}')
