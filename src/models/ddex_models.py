from django.db import models
from .admin_models import Order
from .tags import (
        IdTypeSet,
        PartyRoleSet,
        PartyTypeSet,
        )


"""
All DDEX related models are available here that includes
Party, Song, Image, Album and Clip

TODO:
    - Requires tests
"""


ID_TYPE_CHOICES = [(id_type.value, id_type.value) for id_type in IdTypeSet] # Creates choices for id type

PARTY_ROLE_CHOICES = [(role.value, role.value) for role in PartyRoleSet] # Creates choices for party roles



class Party(models.Model):
    """
    Stores data for PartyList tag in DDEX xml
    """
    class Meta:
        verbose_name_plural = "Parties"
    TYPE_CHOICES = [
            ('Artist', PartyTypeSet.artist.value),
            ('Contributor', PartyTypeSet.contributor.value)
            ]
    # default value is set to Artist from PartyTypeSet Enum
    party_type = models.CharField(choices=TYPE_CHOICES, max_length=250, default=PartyTypeSet.artist.value) # Determines the type of Party i.e. either Artist or Contributor
    role = models.CharField(choices=PARTY_ROLE_CHOICES, max_length=150, default=PartyRoleSet.main_artist.value) # Need to add choices
    name = models.CharField(max_length=250) # Full name of the party

    def get_reference(self, name, record_label):
        return f"P{self.name}_{name}_{record_label}"

    def __str__(self):
        return f"{self.party_type}: {self.name}"

class Album(models.Model):
    id_type = models.CharField(choices=ID_TYPE_CHOICES, max_length=100, default=IdTypeSet.icpn.value)
    # Same as song
    # Needs a seperate validator for different types of id types
    id_value = models.CharField(max_length=100, unique=True, default='A0')
    name = models.CharField(max_length=150) # Name of the album
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Album: {self.name}-{self.id_value}"



class Song(models.Model):
    id_type = models.CharField(choices=ID_TYPE_CHOICES, max_length=100)
    # Id value needs to have a proper validator
    # A seperate validator as per the id_type selected
    # max_length needs to be shorter
    id_value = models.CharField(max_length=150, unique=True, default=f"S0")
    name = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to='resources/')
    # If true then crbt fields will be required
    # If false then not
    has_crbt = models.BooleanField()
    crbt_start_time = models.CharField(max_length=10, blank=True)
    # needs a seperate validator for crbt code as well
    # but i am not sure how crbt code are handled
    crbt_code = models.CharField(max_length=50, blank=True)
    # if true the clip model will be required
    has_clip = models.BooleanField()
    
    # all fk and m2m fields
    # the party can be artist or contributor
    # so a context processor file must be created to
    # return either only artists or contributor type party object
    # to make the ddex xml file
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    party = models.ManyToManyField(Party)

    def __str__(self):
        return f"Song: {self.name}-{self.id_value}"



class Image(models.Model):
    # Image id type by default is set to proprietarty id
    id_type = models.CharField(choices=ID_TYPE_CHOICES, max_length=100, default=IdTypeSet.proprietary_id.value)
    id_value = models.CharField(max_length=100, unique=True, default="I0") # Needs a validator
    name = models.CharField(max_length=100) # Name of the image
    image_file = models.FileField(upload_to='resources/')
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image: {self.name}"


class Clip(models.Model):
    # maybe i should add a function to automatically generate
    # technical details from the audio file
    audio_file = models.FileField(upload_to='resources/')
    name = models.CharField(max_length=100) # Name of the clip of the song
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Clip: {self.name}"





