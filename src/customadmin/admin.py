from django.contrib import admin
from models.ddex_models import Party, Album, Song, Clip, Image
from models.admin_models import Order

admin.site.register(Order)
admin.site.register(Party)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Clip)
admin.site.register(Image)
