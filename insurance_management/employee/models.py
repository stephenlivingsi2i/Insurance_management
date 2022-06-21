from django.db import models
from django.core.validators import RegexValidator

from organization.models import Organization
from user.models import User


class Employee(models.Model):
    GENDER_CHOICE = (("1", "male"),
                     ("2", "female"),
                     ("3", "others"))
    ROLE_CHOICE = (("1", "hr"),
                   ("2", "others")
                   )
    employee_id = models.IntegerField()
    name = models.CharField(max_length=250, validators=[
        RegexValidator(
            regex='^([A-Za-z]{3,})( [a-z]+)*( [a-z]+)*$',
            message='Please enter valid name',
            code='invalid_name'
        ),
    ])
    gender_type = models.CharField(choices=GENDER_CHOICE, max_length=1)
    role_type = models.CharField(choices=ROLE_CHOICE, max_length=1)
    dob = models.DateField()
    mobile_number = models.BigIntegerField(validators=[
        RegexValidator(
            regex='^[6789]\d{9}$',
            message='Phone number must be 10 digits and starts with either(6,7,8,9)',
            code='invalid_number'
        ),
    ], unique=True)
    email = models.EmailField(unique=True)
    aadhar_number = models.BigIntegerField()
    current_project = models.CharField(max_length=50)
    joining_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
