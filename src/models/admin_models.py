from django.db import models
from .ddex_models import Party, Song, Album
from .tags import PlanSet
from ddex.config import ReleaseTypeSet

PLAN_CHOICES = [(plan.value, plan.value) for plan in PlanSet]
RELEASE_TYPE_CHOICE = [(release_option, release_option) for release_option in ReleaseTypeSet]

class Order(models.Model):
    """
    Order table consists of all the data that is specific to 
    a particular order.

    The artists that are created and stored are specific to one order
    and must be maintained that way.

    Not only artists but the song details must also limit itself to one 
    specific order.
    """
    plan_choice = models.CharField(choices=PLAN_CHOICES, max_length=8)
    release_type = models.CharField(choices=RELEASE_TYPE_CHOICE, max_length=40)
    # if plan choice is album then only album will be shown in the admin panel
    # if plan choice is song then only song will be shown in the admin panel
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        if self.plan_choice == PlanSet.album.value:
            return f"Order{self.id}: {self.album.name}"
        if self.plan_choice == PlanSet.single.value:
            return f"Order{self.id}: {self.song.name}"
    
