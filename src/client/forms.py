from django import forms

class SingleReleaseForm(forms.Form):
    song_name = forms.CharField(max_length=250)
    artist_name = forms.CharField(max_length=250)