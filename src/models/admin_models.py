from django.db import models
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

    def __str__(self):
        if self.plan_choice == PlanSet.album.value:
            return f"Order{self.id}"
        if self.plan_choice == PlanSet.single.value:
            return f"Order{self.id}"
    
