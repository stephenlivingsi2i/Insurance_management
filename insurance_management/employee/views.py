from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from claim.models import Claim
from claim.serializer import ClaimSerializer
from employee.models import Employee
from employee.serializer import EmployeeSerializer
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer


@api_view(['POST'])
def create_employee(request):
    """Create new employee and store it to database"""

    new_employee = EmployeeSerializer(data=request.data)
    new_employee.is_valid(raise_exception=True)
    new_employee.save()
    return Response(new_employee.data)


@api_view(['GET'])
def view_employees(request):
    """Get all user details from database"""

    all_employees = Employee.objects.all()
    all_employees = EmployeeSerializer(instance=all_employees, many=True)
    return Response(all_employees.data)


@api_view(['PUT'])
def update_employee(request, user_id):
    """Validates the data and updates a user."""

    old_employee_data = Employee.objects.get(pk=user_id)
    if not old_employee_data.status:
        raise ObjectDoesNotExist()
    updated_user_data = EmployeeSerializer(old_employee_data,
                                           data=request.data, partial=True)
    if updated_user_data.is_valid(raise_exception=True):
        updated_user_data.save()
    return Response(updated_user_data.data)


@api_view(['DELETE'])
def delete_employee(request, user_id):
    """Makes a user status as inActive."""

    try:
        employee = Employee.objects.get(pk=user_id)
        employee.status = False
        employee.save()
        return Response(status=204)
    except ObjectDoesNotExist:
        return Response({'message': 'No such user'}, status=404)


@api_view(['GET'])
def get_employee_insurances(request, employee_id):
    insurances = Insurance.objects.filter(employee=employee_id)
    insurances = InsuranceSerializer(instance=insurances, many=True)
    return Response(insurances.data)


@api_view(['GET'])
def get_particular_employee_insurance(request, employee_id, insurance_id):
    insurances = Insurance.objects.filter(employee=employee_id, id=insurance_id)
    insurance = InsuranceSerializer(instance=insurances[0])
    return Response(insurance.data)


@api_view(['GET'])
def get_claim_details(request, employee_id):
    insurances = Insurance.objects.filter(employee=employee_id)
    claim_list = []
    for insurance in insurances:
        claim = Claim.objects.filter(insurance=insurance.id)
        claim_list.extend(claim)
    claim_list = ClaimSerializer(instance=claim_list, many=True)
    return Response(claim_list.data)


@api_view(['GET'])
def get_particular_claim_details(request, employee_id, insurance_id):
    insurances = Insurance.objects.filter(employee=employee_id, id=insurance_id)
    claim = Claim.objects.filter(insurance=insurances[0].id)
    claim = ClaimSerializer(instance=claim, many=True)
    return Response(claim.data)





