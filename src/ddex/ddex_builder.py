from messageheader import MessageHeader, MessageParty, MessageControlType, MessagePartyType
from party import Party, PartyList, Contributor
from release_builder import ReleaseBuilder
from resource_builder import ResourceBuilder
from utils import save

from lxml import etree as et


class DdexBuilder:
    def __init__(
            self,
            song_name,
            song_id_type,
            song_id,
            territory,

            artist_name,
            artist_role,

            pline_year,
            pline_text,

            cline_year,
            cline_text,

            genre,

            record_label_name,

            codec,
            bitrate,
            channels,
            sampling,
            duration,
            uri,
            hash_algorithm,
            hash_value,
            parental_warning,

            image_id,
            image_id_type,
            image_type,

            sender_name,
            sender_dpid,
            receiver_name,
            receiver_dpid,

            display_title=None,
            alternative_titles=[],
            pline_company=None,
            cline_company=None,
            sub_genre=None,

            message_control_type=MessageControlType.live_message.value,
            parties=[],
            contributors=[],
    ):
        self.song_name = song_name
        self.song_id_type = song_id_type
        self.song_id = song_id
        self.display_title = display_title
        self.alternative_titles = alternative_titles
        self.territory = territory

        self.artist_name = artist_name
        self.artist_role = artist_role

        self.pline_year = pline_year
        self.pline_text = pline_text
        self.pline_company = pline_company

        self.cline_year = cline_year
        self.cline_text = cline_text
        self.cline_company = cline_company

        self.genre = genre
        self.subgenre = sub_genre

        self.record_label_name = record_label_name

        self.codec = codec
        self.bitrate = bitrate
        self.channels = channels
        self.sampling = sampling
        self.duration = duration
        self.uri = uri
        self.hash_algorithm = hash_algorithm
        self.hash_value = hash_value
        self.parental_warning = parental_warning

        self.image_id = image_id
        self.image_id_type = image_id_type
        self.image_type = image_type

        self.sender_name = sender_name
        self.sender_dpid = sender_dpid
        self.receiver_name = receiver_name
        self.receiver_dpid = receiver_dpid

        self.message_control_type = message_control_type
        self.parties = parties
        self.contributors = contributors

    def build_root(self):
        attrs = {
            'release_version_id': 'Audio',
            'language_code': 'en',
            'avs_version_id': '3',
        }
        ern = 'http://ddex.net/xml/ern/43'
        xsi = 'http://w3.org/2001/XMLSchema-instance'
        xsd = 'http://ddex.net/xml/ern/43 http://ddex.net/xml/ern/43/release-notification.xsd'
        root_tag = "NewReleaseMessage"

        mapping = {
            'ern': ern,
            'xsi': xsi,
        }
        tag = et.Element(et.QName(ern, 'NewReleaseMessage'), nsmap=mapping)
        tag.set(et.QName(xsi, 'schemaLocation'), xsd)
        return tag

    def build(self):
        sender = MessageParty(
            self.sender_name,
            self.sender_dpid
        )

        receiver = MessageParty(
            self.receiver_name,
            self.receiver_dpid,
            MessagePartyType.Receiver.value
        )

        message_header = MessageHeader(
            sender=sender,
            recipient=receiver,
            message_control=self.message_control_type,
        )

        party_list = PartyList(self.parties)

        resource_list = ResourceBuilder(
            td_id=self.song_id,
            td_type='AudioFile',
            audio_codec=self.codec,
            bitrate=self.bitrate,
            channels=self.channels,
            sampling=self.sampling,
            duration=self.duration,
            uri=self.uri,
            hash_algorithm=self.hash_algorithm,
            hash_value=self.hash_value,
            resource_id=f"R{self.song_id}",
            pline_company=self.pline_company,
            pline_year=self.pline_year,
            pline_text=self.pline_text,
            sound_recording_reference=f"A{self.song_id}",
            title_text=self.song_name,
            artist_reference=f'P{self.artist_name}',
            artist_role=self.artist_role,
            parental_warning=self.parental_warning,
            image_reference=f"R{self.image_id}",
            image_type=self.image_type,
            image_id_type=self.image_id_type,
            image_id=self.image_id,
            contributors=self.contributors,
        )

        release_list = ReleaseBuilder(
            reference=f'R{self.song_id}',
            display_title_text=self.display_title,
            title_text=self.song_name,
            territory=self.territory,
            artist_name=self.artist_name,
            artist_reference=f"P{self.artist_name}",
            artist_role=self.artist_role,
            cline_year=self.cline_year,
            cline_text=self.cline_text,
            cline_company=self.cline_company,
            release_label_reference=f"P{self.record_label_name}",
            genre=self.genre,
            relationship_type="LinkedRelease",
            release_id=self.song_id,
            sequence_number='1',
            resource_reference=f'R{self.song_id}',
            linked_resource_reference=f'R{self.song_id}'
        )

        root = self.build_root()
        root.append(message_header.write())
        root.append(party_list.write())
        root.append(resource_list.build())
        root.append(release_list.build())
        return root


if __name__ == "__main__":
    builder = DdexBuilder(
        song_name="Chillo Je Tar",
        song_id_type='ISRC',
        song_id='INF232100008',
        territory='Worldwide',
        artist_name='Subrata kr Dutta',
        artist_role='MainArtist',
        pline_year='2022',
        pline_text='Subrata kr Dutta',
        cline_year='2022',
        cline_text='Big Machine Records',
        genre='mellow',
        record_label_name='Big Machine Records',
        codec='WAV',
        bitrate='16',
        channels='2',
        sampling='44.1',
        duration='3.44',
        uri='resource/INF232100008.wav',
        hash_algorithm='md5',
        hash_value='08e6f989841236dc98f2d0eeb4a00636',
        parental_warning='NoExplicit',
        image_id='INF232100008IMG',
        image_id_type='ISRC',
        image_type='FrontCoverImage',
        sender_name='Forevision Digital',
        sender_dpid='PADPIDA2015010310U',
        receiver_name='Universal Studios',
        receiver_dpid='PADPIDA201508920U',
    )

    root = builder.build()
    save(root, 'ddex-demo.xml')
