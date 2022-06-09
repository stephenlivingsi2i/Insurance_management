from django.db import models
from django.core.validators import RegexValidator

from employee.models import Employee


class Family(models.Model):
    GENDER_CHOICE = (("1", "male"),
                     ("2", "female"),
                     ("3", "others"))
    RELATION_CHOICE = (("1", "mother"),
                       ("2", "father"),
                       ("3", "wife"),
                       ("4", "first_child"),
                       ("5", "second_child")
                       )
    name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^([A-Za-z]{3,})( [a-z]+)*( [a-z]+)*$',
            message='Please enter valid name',
            code='invalid_name'
        ),
    ])
    gender_type = models.CharField(choices=GENDER_CHOICE, max_length=1)
    dob = models.DateField()
    relation_type = models.CharField(choices=RELATION_CHOICE, max_length=1)
    aadhar_number = models.BigIntegerField(unique=True)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

