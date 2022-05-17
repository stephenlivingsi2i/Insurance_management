from django.db import models


class Employee(models.Model):
    employee_id = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    mobile_number = models.BigIntegerField()
    email = models.EmailField()
    current_project = models.CharField(max_length=50, null=True)
    joining_date = models.DateField(null=True)
    status = models.BooleanField(default=True)
    created_date = models.DateField()
    updated_date = models.DateField()
