from rest_framework import serializers
from insurance_company.models import InsuranceCompany


class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'
