from rest_framework import serializers

from employee.models import Employee
from utils.dynamic_serializer import DynamicFieldsModelSerializer


class EmployeeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "employee_id", "name", "gender_type",
                  "dob", "mobile_number",  "email", "aadhar_number",
                  "current_project", "joining_date", "status",
                  "created_date", "updated_date", "organization")
