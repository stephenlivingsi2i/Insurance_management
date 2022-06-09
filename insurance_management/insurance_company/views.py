import logging
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from insurance_company.models import Company
from insurance_company.serializer import CompanySerializer


logger = logging.getLogger('root')


@api_view(['POST'])
def create_company(request):
    """Create new company"""
    try:
        new_company = CompanySerializer(data=request.data)
        new_company.is_valid(raise_exception=True)
        new_company.save()
        logger.debug(f"Insurance company created with id of {new_company.data['id']}")
        return Response(new_company.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
def view_companies(request):
    """View all company details"""

    all_companies = Company.objects.all()
    if all_companies.exists():
        all_companies = CompanySerializer(instance=all_companies,
                                          many=True)
        logger.debug("Fetched all insurance companies")
        return Response(all_companies.data)
    else:
        logger.debug("Insurance companies not found")
        return Response("companies not found")


@api_view(['put'])
def update_company(request, company_id):
    """Update existing company details"""
    try:
        old_company = Company.objects.get(pk=company_id)
        updated_company = CompanySerializer(old_company,
                                            data=request.data, partial=True)
        updated_company.is_valid(raise_exception=True)
        updated_company.save()
        logger.debug(f"Updated company details of id {company_id}")
        return Response(f"successfully updated company detail of id {company_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)
