import logging

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import organization
from claim.models import Claim
from claim.serializer import ClaimSerializer
from employee.models import Employee
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer
from organization.models import Organization
from organization.serializer import OrganizationSerializer
from policy.models import Policy


logger = logging.getLogger('root')


@api_view(['POST'])
def create_organization(request):
    """Create new organization"""
    try:
        new_organization = OrganizationSerializer(data=request.data)
        new_organization.is_valid(raise_exception=True)
        new_organization.save()
        logger.debug(f"Created organization id of {new_organization.data['id']}")
        return Response(new_organization.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
def view_organizations(request):
    """View all organization details from database"""
    all_organization = Organization.objects.all()
    if all_organization.exists():
        all_organization = OrganizationSerializer(instance=all_organization,
                                                  many=True)
        logger.debug("Fetched all organizations")
        return Response(all_organization.data)
    else:
        logger.debug("organization not found")
        return Response("organization not found")


@api_view(['PUT'])
def update_organization(request, organization_id):
    """Update organization details"""
    try:
        old_organization = Organization.objects.get(pk=organization_id)
        if old_organization.exists():
            updated_organization = OrganizationSerializer(old_organization,
                                                          data=request.data, partial=True)
            updated_organization.is_valid(raise_exception=True)
            updated_organization.save()
            logger.debug(f"Updated organization detail"
                         f" of id {organization_id}")
            return Response(f"successfully updated organization detail"
                            f" of id {organization_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
def get_organization_insurances(request, organization_id):
    try:
        insurances = Insurance.objects.filter(organization=organization_id)
        if len(insurances) != 0:
            insurances = InsuranceSerializer(instance=insurances, many=True)
            logger.debug("Fetched all organization provided insurances")
            response = insurances.data
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "insurance not found"
    return Response(response)


@api_view(['GET'])
def get_particular_organization_insurance(request, organization_id, employee_id):
    try:
        organization_details = Organization.objects.get(pk=organization_id)
        employee = Employee.objects.get(pk=employee_id)
        insurances = Insurance.objects.filter(
            organization=organization_id, employee=employee_id)
        if len(insurances) != 0:
            insurances = InsuranceSerializer(instance=insurances,
                                             many=True)
            logger.debug(f"Fetched insurance of employee if {employee_id}")
            response = insurances.data
        else:
            logger.debug("insurance not found")
            response = "insurance not found"
    except Organization.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "organization not found"
    except Employee.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "employee not found"
    return Response(response)


@api_view(['GET'])
def get_insurances_by_policy(request, organization_id, policy_id):
    try:
        organization_details = Organization.objects.get(pk=organization_id)
        policy = Policy.objects.get(pk=policy_id)
        insurances = Insurance.objects.filter(organization_id=organization_id,
                                              policy_id=policy_id)
        if len(insurances) > 0:
            insurance_list = InsuranceSerializer(instance=insurances, many=True)
            logger.debug(f"Fetched insurances of policy id {policy_id}")
            response = insurance_list.data
        else:
            logger.debug("no insurance exist")
            response = "no insurance exist"

    except Organization.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "organization not found"
    except Policy.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "Policy not found"
    return Response(response)


@api_view(['GET'])
def get_particular_organization_insurance_claim(request,
                                                organization_id, employee_id):
    try:
        organization_details = Organization.objects.get(pk=organization_id)
        employee = Employee.objects.get(pk=employee_id)
        claim_list = []
        insurances = Insurance.objects.filter(
            organization=organization_id, employee=employee_id)
        if len(insurances) != 0:
            for insurance in insurances:
                claim = Claim.objects.filter(insurance=insurance.id)
                claim_list.extend(claim)
            claim_list = ClaimSerializer(instance=claim_list, many=True)
            logger.debug(f"Fetched claims of employee id {employee_id}")
            response = claim_list.data
        else:
            logger.debug("claim not found")
            response = "claim not found"
    except Organization.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "organization not found"
    except Employee.DoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        response = "employee not found"
    return Response(response)



