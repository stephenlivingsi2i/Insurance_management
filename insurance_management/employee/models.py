from django.db import models


class Employee(models.Model):
    # GENDER_CHOICE = (
    #     ('1', 'male'),
    #     ('2', 'female'),
    # )
    name = models.CharField(max_length=50)
    # gender = models.CharField(choices=GENDER_CHOICE, max_length=1)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    mobile_number = models.BigIntegerField()
    email = models.EmailField()
    created_date = models.DateField()
    updated_date = models.DateField()
    is_active = models.BigIntegerField(default=True)
