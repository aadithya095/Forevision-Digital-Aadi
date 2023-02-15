from django import forms
import datetime
from .form_functions import MethodForm


class SingleReleaseForm(forms.Form):

    '''
        TODO: Make Multiple Image Upload

    '''
    id_type = forms.ChoiceField(
        choices=MethodForm.formIdTypehoice(), initial='Select',
        validators=[MethodForm.checkIdType],
        label="ID Type*",
        widget=forms.Select(
            attrs={'class': 'choice-field', 'style': 'min-width:200px; padding: 3px 10px; '}),
    )

    id_value = forms.CharField(max_length=100, label='ID value : Not mandatory if something',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'ID value...'}),
                               )
    song_title = forms.CharField(max_length=400, required=True,
                                 label='Song Title*',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Song title...'}),
                                 )

    released_date = forms.DateField(required=False,
                                    widget=forms.DateInput(
                                        attrs={'type': 'date', 'min': '1900-12-01', 'max': datetime.date.today, }),
                                    validators=[MethodForm.validateDateRange],
                                    label='Released Date'
                                    )

    released_year = forms.IntegerField(required=True, max_value=2023, min_value=1900,
                                       label='Released Year*'
                                       )

    song_file = forms.FileField(required=True, validators=[MethodForm.clean_file],
                                label='Song File* : Must be in .MP3 .Wav ... format!'
                                )

    record_label = forms.CharField(max_length=400, required=False,
                                   widget=forms.TextInput(attrs={
                                       'placeholder': 'Record Label...',
                                   }),
                                   label='Name of Record Label',
                                   )
    language = forms.CharField(max_length=200, required=False,
                               label='Song Language...'
                               )

    genre = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Genre...',
                            }),)

    coverart = forms.FileField(required=False,
                               label='Cover Art for song if available '
                               )
    coverart_name = forms.CharField(max_length=100, required=False,
                                    widget=forms.TextInput(attrs={
                                        'placeholder': 'Cover Art Title...'
                                    }),

                                    label='Name if Cover Art is Available',
                                    )

    lyrics = forms.CharField(max_length=20000, required=False,
                             widget=forms.Textarea(attrs={
                                 'placeholder': 'Lyrics...',
                                 'style': 'resize: none;',
                             }),
                             label='Lyrics if you want to provide',
                             )
