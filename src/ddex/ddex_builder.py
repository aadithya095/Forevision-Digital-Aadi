from messageheader import MessageHeader, MessageParty, MessageControlType, MessagePartyType
from technical_details import TechnicalDetailsType
from party import Party, PartyList, Contributor
from release_builder import ReleaseBuilder
from resource_builder import ResourceBuilder
from deallist import DealList
from utils import save
from resource import Tags

from lxml import etree as et


class DdexBuilder:
    def __init__(
            self,
            song_name,
            song_id,
            territory,
            release_date, # used for start date in deal list

            artist_name,
            artist_role,

            pline_text,
            cline_text,

            genre,

            record_label_name,

            uri,  # filename or path of the file
            parental_warning,

            image_id,
            image_file,
            image_type,

            sender_name,
            sender_dpid,
            receiver_name,
            receiver_dpid,

            display_title=None,
            alternative_titles=[],
            cline_company=None,
            pline_company=None,
            pline_year=None,
            cline_year=None,
            sub_genre=None,
            audio_technical_detail_type=TechnicalDetailsType.audio.value,
            image_technical_detail_type=TechnicalDetailsType.image.value,
            release_type="Single",
            song_id_type=Tags.isrc.value, # If no id type is provided
            # by default it would be ISRC

            message_control_type=MessageControlType.live_message.value,
            parties=[],
            contributors=[],
    ):
        self.song_name = song_name
        self.song_id_type = song_id_type
        self.song_id = song_id
        self.release_date = release_date
        self.display_title = display_title
        self.alternative_titles = alternative_titles
        self.territory = territory

        self.artist_name = artist_name
        self.artist_role = artist_role

        self.pline_company = pline_company
        self.pline_year = pline_year
        self.pline_text = pline_text

        self.cline_company = cline_company
        self.cline_year = cline_year
        self.cline_text = cline_text

        self.genre = genre
        self.subgenre = sub_genre
        self.audio_technical_detail_type = audio_technical_detail_type

        self.release_type = release_type # ReleaseType the value by default is Unknown

        self.record_label_name = record_label_name

        self.uri = uri
        self.parental_warning = parental_warning

        self.image_id = image_id
        self.image_file = image_file
        self.image_type = image_type
        self.image_technical_detail_type = image_technical_detail_type

        self.sender_name = sender_name
        self.sender_dpid = sender_dpid
        self.receiver_name = receiver_name
        self.receiver_dpid = receiver_dpid

        self.message_control_type = message_control_type
        self.parties = parties
        self.contributors = contributors

    def build_root(self):
        attrs = {
            'ReleaseProfileVariantVersionId': 'Classical',
            'LanguageAndScriptCode': 'en',
            'AvsVersionId': '3',
        }
        ern = 'http://ddex.net/xml/ern/43'
        xsi = 'http://w3.org/2001/XMLSchema-instance'
        xsd = 'http://ddex.net/xml/ern/43 http://ddex.net/xml/ern/43/release-notification.xsd'
        root_tag = "NewReleaseMessage"

        mapping = {
            'ern': ern,
            'xsi': xsi,
        }
        # I removed xsi:schemaLocation as it did not hamper the validation test
        tag = et.Element(et.QName(ern, 'NewReleaseMessage'), nsmap=mapping, **attrs)
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
        
        # Need to create a list of parties to pass it into party_list

        party_list = PartyList(self.parties)

        resource_list = ResourceBuilder(
            audio_technical_detail_type=self.audio_technical_detail_type,
            image_technical_details_type=self.image_technical_detail_type,
            audio_filename=self.uri,
            image_filename=self.image_file,
            resource_id=self.song_id,
            pline_text=self.pline_text,
            sound_recording_reference=f"A{self.song_id}",
            artist_name=self.artist_name,
            title_text=self.song_name,
            artist_role=self.artist_role,
            parental_warning=self.parental_warning,
            image_reference=f"A{self.image_id}",
            image_type=self.image_type,
            party_id=self.sender_dpid,
            id_type=self.song_id_type,
            pline_year=self.pline_year,
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
            relationship_type="Unknown",
            release_id=self.song_id,
            release_type=self.release_type,
            sequence_number='1',
            resource_reference=f'A{self.song_id}',
            linked_resource_reference=f'A{self.song_id}' # LinkedResourceReference must have A as a prefix
        )

        deal_list = DealList(
                reference=f'R{self.song_id}',
                start_date=self.release_date,
                )

        root = self.build_root()
        root.append(message_header.write())
        root.append(party_list.write())
        root.append(resource_list.build())
        root.append(release_list.build())
        root.append(deal_list.write())
        return root


if __name__ == "__main__":
    import os
    from config import ROOT_DIR
    test_file_name = os.path.join(ROOT_DIR, 'docs/assets/resources/test_file.wav')
    image_file_name = os.path.join(ROOT_DIR, 'docs/assets/resources/INF232200812IMG.jpg')
    p1 = Party(
            name='Tanmay Jyoti Pathak',
            role="Singer"
            )
    p2 = Party(
            name='Banjit Pathak',
            role='Lyricist'
            )
    p3 = Party(
            name="Amit Soukadhara",
            role="Composer"
            )
    p4 = Party(
            name="Chafikhur Rahman",
            role="Director"
            )

    c1 = Contributor(
            id_="PBanjitPathak",
            role="Lyricist"
            )
    c2 = Contributor(
            id_="PAmitSoukadhara",
            role="Composer"
            )
    c3 = Contributor(
            id_="PChafikhurRahman",
            role="Director"
            )

    builder = DdexBuilder(
        song_name="Akash Nila Nila Sopun",
        song_id='8905778280390',
        release_date="2022-10-20",
        territory='Worldwide',
        artist_name='Tanmay Jyoti Pathak',
        artist_role='MainArtist',
        pline_text='Amit Soukadhara',
        cline_text='HRIDOI',
        genre='Regional',
        record_label_name='HRIDOI',
        uri=test_file_name,
        parental_warning='NotExplicit',
        image_id='INF232200812IMG',
        image_type='FrontCoverImage',
        image_file=image_file_name,
        sender_name='Forevision Digital',
        sender_dpid='PADPIDA2015010310U',
        receiver_name='Jaxsta',
        receiver_dpid='PADPIDA2016091404E',
        parties=[p1, p2, p3, p4],
        contributors=[c1, c2, c3],
    )

    root = builder.build()
    filename = "testing_image_file.xml"
    save(root, filename)
    print(f'Saved {filename}!')
