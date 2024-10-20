from django.db import models
from django.contrib.auth.models import AbstractUser
#? this is the one that will let us custom our user model, without losing track of the predifined iser model giving by django
#? in short term this will extend the django predifined model for users

# Create your models here.
class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)    