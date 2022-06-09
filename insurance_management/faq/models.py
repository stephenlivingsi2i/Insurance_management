from django.db import models


# Create your models here.
from insurance_company.models import Company


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
