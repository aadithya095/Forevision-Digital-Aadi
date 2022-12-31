from django.forms import ModelForm
from django import forms
from models.models import Artist, Album, Song, Image, Clip

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'role', 'other_role']

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = [
                'id_type',
                'identifier',
                'name',
                'artists',
                'pline_year',
                'pline_text',
                'cline_year',
                'cline_text',
                'genre',
                'subgenre',
                'duration'
                ]

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = [
                'name',
                'id_type',
                'identifier',
                'pline_year',
                'pline_text',
                'cline_year',
                'cline_text',
                'duration'
                ]

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = (
                'id_type',
                'warning',
                'identifier'
                )

class ClipForm(ModelForm):
    class Meta:
        model = Clip
        fields = [
                'start_time',
                'duration',
                'type',
                'song'
                ]
