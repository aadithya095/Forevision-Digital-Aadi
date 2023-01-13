from release import Release, RelatedRelease, ResourceGroup, ReleaseIdType, ReleaseList


class ReleaseBuilder:
    def __init__(self,
                 reference,
                 display_title_text,
                 title_text,
                 territory,
                 artist_name,
                 artist_reference,
                 artist_role,
                 cline_year,
                 cline_company,
                 cline_text,
                 release_label_reference,
                 genre,
                 relationship_type,
                 release_id,
                 sequence_number,
                 resource_reference,
                 linked_resource_reference,
                 release_id_type=ReleaseIdType.proprietary_id.value,
                 sub_genre=None,
                 additional_title=None,
                 parental_warning="Unknown",
                 ):
        self.reference = reference
        self.display_title_text = display_title_text
        self.title_text = title_text
        self.territory = territory
        self.artist_name = artist_name
        self.artist_reference = artist_reference
        self.artist_role = artist_role
        self.cline_year = cline_year
        self.cline_company = cline_company
        self.cline_text = cline_text
        self.release_label_reference = release_label_reference
        self.genre = genre
        self.relationship_type = relationship_type
        self.release_id = release_id
        self.sequence_number = sequence_number
        self.resource_reference = resource_reference
        self.linked_resource_reference = linked_resource_reference
        self.release_id_type = release_id_type
        self.sub_genre = sub_genre
        self.additional_title = additional_title
        self.parental_warning = parental_warning

    def build(self):
        related_release = RelatedRelease(
            relationship_type=self.relationship_type,
            id_=self.release_id,
            id_type=self.release_id_type
        )

        resource_group = ResourceGroup(
            sequence_number=self.sequence_number,
            resource_reference=self.resource_reference,
            linked_resource_reference=self.linked_resource_reference
        )

        release = Release(
            reference=self.reference,
            id_=self.release_id,
            display_title_text=self.display_title_text,
            title_text=self.title_text,
            territory=self.territory,
            artist_name=self.artist_name,
            artist_reference=self.artist_reference,
            artist_role=self.artist_role,
            cline_year=self.cline_year,
            cline_company=self.cline_company,
            cline_text=self.cline_text,
            release_label_reference=self.release_label_reference,
            genre=self.genre,
            sub_genre=self.sub_genre,
            additional_title=self.additional_title,
            parental_warning=self.parental_warning,
            id_type=self.release_id_type,
            related_release=[related_release],
            resource_group=[resource_group]
        )
        release_list = ReleaseList(releases=[release])
        tag = release_list.write()
        return tag

if __name__ == "__main__":
    from utils import save

    builder = ReleaseBuilder(
        reference="R1",
        display_title_text="I love you",
        title_text="I love you",
        territory="Worldwide",
        artist_name="Ash King",
        artist_reference="P1",
        artist_role="MainArtist",
        cline_year="2012",
        cline_company="ForevisionDigital",
        cline_text="ForevisionDigital",
        release_label_reference="PForevesion",
        genre="pop",
        relationship_type="LinkedRelease",
        release_id="PAPI02903084",
        sequence_number="1",
        resource_reference="R1",
        linked_resource_reference="R1",
    )

    root = builder.build()
    save(root, "release.xml")
