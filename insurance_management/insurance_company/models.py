from django.db import models


class InsuranceCompany(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    contact_number = models.BigIntegerField()
    email = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    updated_date = models.DateField()
