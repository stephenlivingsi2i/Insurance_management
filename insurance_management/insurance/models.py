from django.db import models


# Create your models here.
from employee.models import Employee
from organization.models import Organization
from policy.models import Policy


class Insurance(models.Model):
    insurance_number = models.CharField(max_length=15)
    uhid = models.BigIntegerField()
    insurance_type = models.CharField(max_length=50)
    insurance_amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    start_date = models.DateField()
    renewal_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)


