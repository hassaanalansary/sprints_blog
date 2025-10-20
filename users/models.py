from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to="profile_images/", default="profile_images/default.png")
