
from datetime import datetime
from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    profile_photo = models.ImageField(upload_to='image', default=datetime.now())
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True)
    address = models.TextField()
    pan = models.CharField(max_length=30, unique=True, null=True)
    description = models.TextField(default="")
    is_jobber = models.BooleanField(default=False)
    password = models.CharField(max_length=200)