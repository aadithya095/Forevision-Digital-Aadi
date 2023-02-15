from django import forms
from models.user_models import Profile, Order
from models.ddex_models import (
    Party, Song, Album, Clip, Image
)


# """
# TODO: need to refactor to ModelChoiceForm
# Potentially I can use ModelChoiceForm to send options from the model choices in
# case of foreignkeys.

# For example:
#     A user can have many orders and each orders can have albums and songs.
#     Each of those songs and albums has many artists and contributors.

#     In summary a user can have many artists and contributors.

#     If we are to use ModelForm for each case, then for the artists formed in
#     Order 1 will also be displayed in Order 2 since those artists belong to the
#     same user.

#     For such cases, we can make a form field using ModelChoiceForm from where
#     we can pass a queryset. The queryset will be the list of artists specific
#     to a particular order.

#     For example,
#     Order 1 has artists A, B, C and Order 2 has D, E and F. If ModelForm is
#     used the choices for artists in song can have all A to F. But if we use
#     ModelChoiceForm then only A, B and C will be shown as an option in Order 1
#     and D, E and F will be shown as an option in Order 2
# """

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'account_type', 'company_name',
                  'profile_image', 'description', 'address']


# class OrderForm(forms.ModelForm):
#     model = Order
#     fields = ['order_type', ]


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['type', 'role', 'name', 'description']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['id_type', 'id_value', 'name', 'order']


# class SongForm(forms.ModelForm):
#     class Meta:
#         model = Song
#         fields = [
#             'id_type',
#             'id_value',
#             'name',
#             'audio_file',
#             'has_crbt',
#             'crbt_start_time',
#             'crbt_code',
#             'has_clip',
#             'album',
#             'order',
#             'party',
#         ]


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = [
#             'id_type',
#             'id_value',
#             'name',
#             'image_file',
#             'song',
#         ]


# class ClipForm(forms.ModelForm):
#     class Meta:
#         model = Clip
#         fields = [
#             'name',
#             'audio_file',
#             'song',
#         ]


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = [
#             'plan_choice',
#             'release_type',
#         ]
