from django.db import models

# Create your models here.
from employee.models import Employee


class Property(models.Model):
    manufacturing_company = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    price = models.IntegerField()
    manufacturing_year = models.DateField()
    chase_number = models.CharField(max_length=20, unique=True)
    created_by = models.DateField(auto_now=True)
    updated_by = models.DateField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
