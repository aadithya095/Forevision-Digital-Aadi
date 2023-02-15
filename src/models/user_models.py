from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    ACCOUNT_TYPE = (
        ('personal', 'Personal'),
        ('distributer', 'Distributer'),
        ('record label', 'Record Label'),

    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=False)

    username = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=1000, null=True, blank=True)
    account_type = models.CharField(max_length=100, choices=ACCOUNT_TYPE)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(
        upload_to='Profiles', null=True, blank=True, default='user-default.png')
    description = models.TextField(max_length=2000, null=True, blank=True)
    address = models.CharField(max_length=2000, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.username


class Order(models.Model):
    ORDER_TYPE = (
        ('single', 'Single'),
        ('album', 'Album'),
    )

    owner = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True,)
    order_type = models.CharField(max_length=100, choices=ORDER_TYPE)
    total_cost = models.FloatField(null=True, blank=True)
    total_song = models.SmallIntegerField(null=True, blank=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)


''' 
----------------------------------------------------------------
TODO:
    - class UserDocument(models.Model):
    - class AgreementForm(models.Model):
    - class OrderForm(models.Model):
----------------------------------------------------------------
'''
