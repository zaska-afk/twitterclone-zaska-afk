from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TwitterUser(AbstractUser):
    username= models.CharField(max_length=30, unique=True)
    display_name = models.CharField(max_length=30, unique=True, null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username