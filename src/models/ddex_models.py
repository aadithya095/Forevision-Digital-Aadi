from django.db import models
from .user_models import Order
from .tags import Tags
import uuid

"""
----------------------------------------------------------------
All DDEX related models are available here that includes Party, Song, Image, Album and Clip
----------------------------------------------------------------
TODO:
"""


class Album(models.Model):
    '''
     TODO: make signal if album id_type is specified then all song have same id_type
    '''

    id_type = models.CharField(
        max_length=100, null=True, blank=True, choices=Tags.ID_TYPE_CHOICE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=300, null=True, blank=True)
    band_or_artist_name = models.CharField(max_length=300)
    released_date = models.DateField(null=True, blank=True)
    released_year = models.IntegerField(null=True, blank=True)

    record_label = models.CharField(max_length=500, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.owner


class Song(models.Model):
    '''
    ----------------------------------------------------------------
    - album and order is passed in signal so only one can be filled
    - if album = true then order = false, and vice versa

    TODO: create Signal for album and order
         -Create Signal for duration of song
    ----------------------------------------------------------------
    '''

    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True)

    track_number = models.IntegerField(blank=True, null=True)
    record_label = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=500)
    lyrics = models.TextField(null=True, blank=True)
    song_file = models.FileField(
        upload_to='songs', null=True, blank=True)
    # auto generated when file is uploaded
    duration = models.TimeField(blank=True, null=True)
    language = models.CharField(max_length=400, null=True, blank=True)
    genre = models.CharField(max_length=300, blank=True, null=True)
    released_date = models.DateField(null=True, blank=True)
    released_year = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=500, null=True, blank=True)

    id_type = models.CharField(
        max_length=100, choices=Tags.ID_TYPE_CHOICE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Party(models.Model):
    """
    Stores data for PartyList tag in DDEX xml

    """
    PARTY_TYPE = (
        ('artist', 'Artist'),
        ('contributor', 'Contributor'),
    )

    type = models.CharField(max_length=100, choices=PARTY_TYPE)
    role = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.song)

    class Meta:
        verbose_name_plural = "parties"


class Image(models.Model):
    '''
    ----------------------------------------------------------------
    Image can be either of Song or Album
    TODO: to make signal for it Toggeling Album or Song
    ----------------------------------------------------------------
    '''
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(upload_to='Images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)


class Clip(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    cbrt = models.CharField(max_length=100, null=True, blank=True)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
