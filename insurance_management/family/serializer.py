from rest_framework import serializers
from utils.dynamic_serializer import DynamicFieldsModelSerializer

from family.models import Family


class FamilySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "gender_type",
                  "dob", "relation_type", "aadhar_number",
                  "created_date", "updated_date", "employee")
