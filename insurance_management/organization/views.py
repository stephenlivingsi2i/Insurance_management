from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

import organization
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer
from organization.models import Organization
from organization.serializer import OrganizationSerializer
from policy.models import Policy


@api_view(['POST'])
def create_organization(request):
    """Create new organization"""

    new_organization = OrganizationSerializer(data=request.data)
    new_organization.is_valid(raise_exception=True)
    new_organization.save()
    return Response(new_organization.data)


@api_view(['GET'])
def view_organizations(request):
    """View all organization details from database"""

    all_organization = Organization.objects.all()
    all_organization = OrganizationSerializer(instance=all_organization, many=True)
    return Response(all_organization.data)


@api_view(['PUT'])
def update_organization(request, organization_id):
    """Update organization details"""
    old_organization = Organization.objects.get(pk=organization_id)
    updated_organization = OrganizationSerializer(old_organization,
                                                  data=request.data, partial=True)
    if updated_organization.is_valid(raise_exception=True):
        updated_organization.save()
    return Response(updated_organization.data)


@api_view(['GET'])
def get_organization_insurances(request, organization_id):
    insurances = Insurance.objects.filter(organization=organization_id)
    insurances = InsuranceSerializer(instance=insurances, many=True)
    return Response(insurances.data)


@api_view(['GET'])
def get_particular_organization_insurance(request, organization_id, employee_id):
    insurances = Insurance.objects.filter(
        organization=organization_id, employee=employee_id)
    insurances = InsuranceSerializer(instance=insurances, many=True)
    return Response(insurances.data)


@api_view(['GET'])
def get_insurances_by_policy(request, organization_id, policy_id):
    insurances = Insurance.objects.filter(organization_id=organization_id,
                                          policy_id=policy_id)
    insurance_list = InsuranceSerializer(instance=insurances, many=True)
    return Response(insurance_list.data)



