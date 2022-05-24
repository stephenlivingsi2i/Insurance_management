from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer


@api_view(['POST'])
def create_insurance(request):
    """Create new insurance for employee and store it"""

    request.data["remaining_amount"] = request.data["insurance_amount"]
    new_insurance = InsuranceSerializer(data=request.data)
    new_insurance.is_valid(raise_exception=True)
    new_insurance.save()
    return Response(new_insurance.data)


@api_view(['GET'])
def view_insurances(request):
    """View all insurance details from database"""

    all_insurances = Insurance.objects.all()
    all_insurances = InsuranceSerializer(instance=all_insurances, many=True)
    return Response(all_insurances.data)


@api_view(['PUT'])
def update_insurance(request, insurance_id):
    """Update old insurance details"""
    old_insurance = Insurance.objects.get(pk=insurance_id)
    updated_insurance = InsuranceSerializer(old_insurance,
                                            data=request.data, partial=True)
    if updated_insurance.is_valid(raise_exception=True):
        updated_insurance.save()
    return Response(updated_insurance.data)



