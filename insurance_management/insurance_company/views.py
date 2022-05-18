from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from insurance_company.models import InsuranceCompany
from insurance_company.serializer import InsuranceCompanySerializer


@api_view(['POST'])
def create_company(request):
    """Create new company"""

    new_company = InsuranceCompanySerializer(data=request.data)
    new_company.is_valid(raise_exception=True)
    new_company.save()
    return Response(new_company.data)


@api_view(['GET'])
def view_companies(request):
    """View all company details"""

    all_companies = InsuranceCompany.objects.all()
    all_companies = InsuranceCompanySerializer(instance=all_companies,
                                               many=True)
    return Response(all_companies.data)


@api_view(['put'])
def update_company(request, company_id):
    """Update existing company details"""

    old_company = InsuranceCompany.objects.get(pk=company_id)
    updated_company = InsuranceCompanySerializer(old_company,
                                            data=request.data, partial=True)
    if updated_company.is_valid(raise_exception=True):
        updated_company.save()
    return Response(updated_company.data)
