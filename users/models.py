from djongo import models
from django import forms
from django.contrib.auth.models import User
import django.db.models as dmodels

# Create your models here.

class Profile(models.Model):
    id = dmodels.PositiveIntegerField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
    )
    profile_image = models.ImageField(upload_to='profile_images/')
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()
