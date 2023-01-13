from django import forms


class SingleReleaseForm(forms.Form):
    SONG_ID_TYPE = [
        ('ISRC', 'ISRC'),
        ('GRid', 'GRid'),
        ('ProprietaryId', 'ProprietaryId')
    ]
    TERRITORY_TYPE = [
        ('Worldwide', 'Worldwide'),
    ]
    ARTIST_ROLE = [
        ('MainArtist', 'MainArtist'),
        ('Vocalist', 'Vocalist'),
        ('Artist', 'Artist'),
    ]
    CODEC_TYPE = [
        ('MP3', 'MP3'),
        ('WAV', 'WAV'),
    ]
    HASH_ALGORITHM = [
        ('md5', 'md5'),
        ('sha1', 'sha1'),
        ('sha256', 'sha256')
    ]
    PARENTAL_WARNING_TYPE = [
        ('Unknown', 'Unknown'),
        ('Explicit', 'Explicit'),
        ('NoExplicit', 'NoExplicit')
    ]
    IMAGE_TYPE = [
        ('FrontCoverImage', 'FrontCoverImage'),
        ('CoverArt', 'CoverArt')
    ]
    song_name = forms.CharField(max_length=250)
    song_id_type = forms.ChoiceField(choices=SONG_ID_TYPE)
    song_id = forms.CharField(max_length=20, required=True)  # need to write validator for the form
    territory = forms.ChoiceField(choices=TERRITORY_TYPE)
    artist_name = forms.CharField(max_length=250)
    artist_role = forms.ChoiceField(choices=ARTIST_ROLE)
    pline_year =  forms.CharField(max_length=4)  # Requires year validator and a more efficient way to handle year
    pline_text = forms.CharField(max_length=250)
    cline_year = forms.CharField(max_length=4)
    cline_text = forms.CharField(max_length=250)
    genre = forms.CharField(max_length=30)
    record_label_name = forms.CharField(max_length=250)
    codec = forms.ChoiceField(choices=CODEC_TYPE)
    bitrate = forms.CharField(max_length=10)
    channels = forms.IntegerField()
    sampling = forms.FloatField()
    duration = forms.FloatField()
    uri = forms.URLField()
    hash_algorithm = forms.ChoiceField(choices=HASH_ALGORITHM)
    hash_value = forms.CharField(max_length=120)
    parental_warning = forms.ChoiceField(choices=PARENTAL_WARNING_TYPE)
    image_id = forms.CharField(max_length=250)
    image_id_type = forms.ChoiceField(choices=SONG_ID_TYPE)
    image_type = forms.ChoiceField(choices=IMAGE_TYPE)


