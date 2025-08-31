from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    location = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.BigIntegerField(unique=True, default=0,)
    parent_name = models.CharField(max_length=50, null=True)
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)

