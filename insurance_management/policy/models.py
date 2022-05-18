from django.db import models
from insurance_company.models import InsuranceCompany


class Policy(models.Model):
    policy_number = models.IntegerField()
    name = models.CharField(max_length=50)
    min_policy_amount = models.IntegerField()
    max_policy_amount = models.IntegerField()
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    updated_date = models.DateField(auto_now=True)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
