from django.db import models


# Create your models here.
from employee.models import Employee


class Insurance(models.Model):
    insurance_number = models.CharField(max_length=15)
    uhid = models.BigIntegerField()
    insurance_name = models.CharField(max_length=50)
    insurance_type = models.CharField(max_length=50)
    insurance_amount = models.IntegerField()
    start_date = models.DateField()
    renewal_date = models.DateField()
    issued_by = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
