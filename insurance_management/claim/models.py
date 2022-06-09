from django.db import models

# Create your models here.
from insurance.models import Insurance


class Claim(models.Model):
    applied_amount = models.IntegerField()
    claimed_amount = models.IntegerField()
    remaining_insurance_amount = models.IntegerField()
    claimed_date = models.DateField(auto_now=True)
    claimed_by = models.CharField(max_length=50)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
