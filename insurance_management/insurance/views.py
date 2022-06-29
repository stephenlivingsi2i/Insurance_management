import smtplib
import logging
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render

# Create your views here.
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.models import Employee
from family.models import Family
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer
from datetime import datetime
from datetime import timedelta, date
import uuid

from organization.models import Organization

logger = logging.getLogger('root')


@api_view(['POST'])
@protected_resource(scopes=['user'])
def self_insurance(request):
    """Create new insurance for employee and store it"""
    try:
        user = request.user
        employee = Employee.objects.get(user_id=user.id)
        request.data['employee'] = employee.id
        request.data["remaining_amount"] = request.data["insurance_amount"]
        request.data["renewal_date"] = date.today(). \
            replace(year=date.today().year + 5)
        request.data["insurance_number"] = \
            "P000" + str(date.today()).replace("-", "") \
            + (str(request.data["employee"]))
        employee = Employee.objects.get(pk=request.data["employee"])
        request.data['holder_name'] = employee.name
        new_insurance = InsuranceSerializer(data=request.data)
        new_insurance.is_valid(raise_exception=True)
        new_insurance.save()
        logger.debug(f"self insurance created for employee {new_insurance.data['employee']}")
        return Response("Insurance created successfully")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['POST'])
@protected_resource(scopes=['admin'])
def term_insurance(request):
    try:
        user = request.user
        organization = Organization.objects.get(user_id=user.id)
        request.data['organization'] = organization.id
        request.data["remaining_amount"] = request.data["insurance_amount"]
        request.data["insurance_number"] = request.data["insurance_number"] = \
            "H0000" + str(date.today()).replace("-", "") \
            + (str(request.data["employee"]))
        request.data["renewal_date"] = date.today(). \
            replace(year=date.today().year + 5)
        employee = Employee.objects.get(pk=request.data["employee"])
        request.data['holder_name'] = employee.name
        new_insurance = InsuranceSerializer(data=request.data)
        new_insurance.is_valid(raise_exception=True)
        new_insurance.save()
        logger.debug(f"term insurance created for employee {new_insurance.data['employee']}")
        return Response("Insurance created successfully")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['POST'])
@protected_resource(scopes=['admin'])
def family_individual_insurance(request):
    try:
        user = request.user
        organization = Organization.objects.get(user_id=user.id)
        request.data["remaining_amount"] = request.data["insurance_amount"]
        request.data["insurance_number"] = \
            "H0000" + str(date.today()).replace("-", "") \
            + (str(request.data["employee"]))
        request.data["renewal_date"] = date.today(). \
            replace(year=date.today().year + 5)
        request.data['organization'] = organization.id
        employee = Employee.objects.get(pk=request.data["employee"])
        request.data['holder_name'] = employee.name
        new_insurance = InsuranceSerializer(data=request.data)
        new_insurance.is_valid(raise_exception=True)
        new_insurance.save()
        members = Family.objects.filter(employee=request.data['employee'])
        for member in members:
            request.data["remaining_amount"] = request.data["insurance_amount"]
            request.data['holder_name'] = member.name
            request.data["renewal_date"] = date.today(). \
                replace(year=date.today().year + 5)
            request.data["insurance_number"] = \
                "H00" + str(date.today()).replace("-", "") \
                + (str(request.data["employee"]) + (str(member.id)))
            request.data['organization'] = organization.id
            new_insurance = InsuranceSerializer(data=request.data)
            new_insurance.is_valid(raise_exception=True)
            new_insurance.save()
            logger.debug(f"family insurance created for employee"
                         f" {new_insurance.data['employee']}")
        return Response("Insurance created successfully")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)

#
# @api_view(['GET'])
# def view_insurances(request):
#     """View all insurance details from database"""
#     all_insurances = Insurance.objects.all()
#     if all_insurances.exists():
#         all_insurances = InsuranceSerializer(instance=all_insurances, many=True)
#         logger.debug("Fetched all insurances")
#         return Response(all_insurances.data)
#     else:
#         logger.debug("insurances not found")
#         return Response("insurances not found")
#
#
# @api_view(['PUT'])
# def update_insurance(request, insurance_id):
#     """Update old insurance details"""
#     try:
#         old_insurance = Insurance.objects.get(pk=insurance_id)
#         updated_insurance = InsuranceSerializer(old_insurance,
#                                                 data=request.data, partial=True)
#         updated_insurance.is_valid(raise_exception=True)
#         logger.debug(f"Updated insurance detail of id {insurance_id}")
#         return Response(f"successfully updated insurance detail of id {insurance_id}")
#     except ValidationError as error:
#         logger.debug(f'Validation error:{error.message}')
#         return Response({'message': error.message}, status=400)
#


