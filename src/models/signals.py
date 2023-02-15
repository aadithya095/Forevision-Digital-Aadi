from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .user_models import Profile
from django.contrib.auth.models import User


'''
----------------------------------------------------------------
- Automatically create Profiles when User is created
- Automatially Delete Profile when User is deleted Because of CASCADE
        Only(username, name, email)

----------------------------------------------------------------
'''

# Creating Profile With User


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            email=user.email,
            username=user.username,
            name=user.first_name + ' ' + user.last_name
        )
