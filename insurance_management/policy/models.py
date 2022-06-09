from django.db import models
from insurance_company.models import Company


class Policy(models.Model):
    POLICY_CHOICES = (("1", "health"),
                      ("2", "bike"),
                      ("3", "car"))
    policy_number = models.IntegerField()
    name = models.CharField(max_length=50)
    policy_type = models.CharField(choices=POLICY_CHOICES, max_length=1)
    min_policy_amount = models.IntegerField()
    max_policy_amount = models.IntegerField()
    description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
