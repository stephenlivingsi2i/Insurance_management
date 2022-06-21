from django.db import models


# Create your models here.
from employee.models import Employee
from organization.models import Organization
from policy.models import Policy
from property.models import Property


class Insurance(models.Model):
    INSURANCE_CHOICES = (("1", "self"),
                         ("2", "term"),
                         ("3", "individual"))
    insurance_number = models.CharField(unique=True, max_length=20)
    holder_name = models.CharField(max_length=50)
    insurance_type = models.CharField(choices=INSURANCE_CHOICES, max_length=1)
    insurance_amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    start_date = models.DateField(auto_now=True)
    renewal_date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    property = models.OneToOneField(Property, on_delete=models.CASCADE, null=True)

