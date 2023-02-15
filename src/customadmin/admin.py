from django.contrib import admin
from models.ddex_models import Party, Album, Song, Image, Clip
from models.user_models import Order, Profile

'''
----------------------------------------------------------------
TODO: make displaylist to all of models
----------------------------------------------------------------
'''


class ProfileList(admin.ModelAdmin):
    list_display = ['user', 'username', 'email', 'created']
    filter_display = ['username', 'email' 'created', 'account_type']
    search_fields = ['username', 'email', 'id']


admin.site.register(Profile, ProfileList)
admin.site.register(Order)
admin.site.register(Party)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Image)
admin.site.register(Clip)
