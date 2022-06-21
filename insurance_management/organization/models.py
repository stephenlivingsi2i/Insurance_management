from django.db import models

from user.models import User


class Organization(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

