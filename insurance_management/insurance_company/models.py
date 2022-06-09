from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_number = models.BigIntegerField()
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
