from django.db import models

ID_TYPE = [
    ('ISRC', 'ISRC'),
    ('ICPN', 'ICPN'),
    ('GRid', 'GRid'),
    ('ProprietaryID', 'ProprietaryID')
]


class Image(models.Model):
    id_type = models.CharField(choices=ID_TYPE, max_length=15)
    warning = models.CharField(max_length=20)
    identifier = models.CharField(max_length=20, unique=True)
    file = models.ImageField(upload_to='resources/')

    def get_reference_id(self):
        return f"A{self.identifier}"

    def __str__(self):
        return self.get_reference_id()


class Artist(models.Model):
    ARTIST_ROLE = [
        ('Artist', 'Artist'),
        ('MainArtist', 'MainArtist'),
        ('other', 'Other')
    ]
    name = models.CharField(max_length=100)
    role = models.CharField(choices=ARTIST_ROLE, max_length=50)
    other_role = models.CharField(max_length=50, blank=True, null=True)

    def get_reference_id(self):
        return f"P{self.name}"

    def __str__(self):
        if self.role == 'other':
            return f"<{self.other_role}: {self.name}>"
        else:
            return f"{self.name}-{self.role}"


class Album(models.Model):
    name = models.CharField(max_length=100)
    id_type = models.CharField(choices=ID_TYPE, max_length=15)
    identifier = models.CharField(max_length=20, unique=True)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist)
    pline_year = models.PositiveBigIntegerField()
    pline_text = models.CharField(max_length=100)
    cline_year = models.PositiveBigIntegerField()
    cline_text = models.CharField(max_length=100)
    duration = models.DurationField()

    def get_reference_id(self):
        return f"A{self.identifier}"

    def __str__(self):
        return f"{self.name}_{self.id_type}_{self.identifier}"


class Song(models.Model):
    id_type = models.CharField(choices=ID_TYPE, max_length=15)
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=20, unique=True)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    pline_year = models.PositiveBigIntegerField()
    pline_text = models.CharField(max_length=100)
    cline_year = models.PositiveBigIntegerField()
    cline_text = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100, blank=True, null=True)
    duration = models.DurationField()

    def get_identifier(self):
        return self.identifier

    def get_reference_id(self):
        return f"A{self.identifier}"

    def __str__(self):
        return f"{self.name}_{self.identifier}"


class Clip(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    start_time = models.TimeField()
    duration = models.DurationField()
    type = models.CharField(max_length=30)

    def get_reference_id(self, song):
        return f"T{song.get_identifier()}"

    def __str__(self):
        return f"{self.song.name}_clip"
