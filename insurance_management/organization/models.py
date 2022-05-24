from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_date = models.DateField()
    updated_date = models.DateField(auto_now=True)
