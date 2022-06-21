import logging
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import transaction
from django.shortcuts import render
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
from rest_framework.response import Response

from claim.models import Claim
from claim.serializer import ClaimSerializer
from employee.models import Employee
from employee.serializer import EmployeeSerializer
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer
from organization.models import Organization
from user.models import User
from user.serializer import UserSerializer

logger = logging.getLogger('root')


@api_view(['POST'])
@transaction.atomic()
@protected_resource(scopes=['admin'])
def create_employee(request):
    """Create new employee and store it to database"""
    try:
        user = request.user
        organization = Organization.objects.get(user_id=user.id)
        request.data['user_role'] = 'employee'
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user = user.save()

        employee = Employee.objects.create(
            employee_id=request.data['employee_id'],
            name=request.data['name'],
            gender_type=request.data['gender_type'],
            role_type=request.data['role_type'],
            dob=request.data['dob'],
            mobile_number=request.data['mobile_number'],
            email=request.data['email'],
            aadhar_number=request.data['aadhar_number'],
            current_project=request.data['current_project'],
            organization=organization,
            user=user
        )

        employee.save()
        logger.debug(f"Employee created successfully with id of{employee.id}")
        return Response(EmployeeSerializer(instance=employee).data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
@protected_resource(scopes=['admin'])
def view_employees(request):
    """Get all user details from database"""

    fields = ("id", "employee_id", "name", "dob",
              "gender_type", "mobile_number", "email", "current_project")

    employees = Employee.objects.all().filter(status=True)
    if employees.exists():
        all_employees = EmployeeSerializer(instance=employees, many=True, fields=fields)
        logger.debug("Fetched all employees")
        return Response(all_employees.data)
    else:
        logger.debug("Employees not found")
        return Response("Employees not found")


@api_view(['PUT'])
@protected_resource(scopes=['user'])
def update_employee(request, user_id):
    """Validates the data and updates a user."""

    try:
        old_employee_data = Employee.objects.get(pk=user_id)
        updated_user_data = EmployeeSerializer(old_employee_data,
                                               data=request.data, partial=True)
        updated_user_data.is_valid(raise_exception=True)
        updated_user_data.save()
        logger.debug(f"Employee id {user_id} updated")
        return Response(f"successfully updated user detail of id {user_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['DELETE'])
@protected_resource(scopes=['admin'])
def delete_employee(request, user_id):
    """Makes a user status as inActive."""

    try:
        employee_details = Employee.objects.get(pk=user_id)
        if employee_details.status:
            employee_details.is_active = False
            employee_details.save()
            logger.debug(f"Employee id {user_id} deleted")
            return Response(f"user id {user_id} is deleted_successfully")
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist as error:
        logger.debug(f'Validation error:{error.message}')
        return Response(f"No employee found for this id")


@api_view(['GET'])
@protected_resource(scopes=['user'])
def get_employee_insurances(request, employee_id):

    try:
        employee = Employee.objects.get(pk=employee_id)
        if employee.status:
            insurances = Insurance.objects.filter(employee=employee_id)
            if len(insurances) == 0:
                logger.debug("no insurance found")
                response = "no insurance found"
            else:
                insurances = InsuranceSerializer(instance=insurances, many=True)
                logger.debug(f"Fetched all insurance of "
                             f"employee id {employee_id}")
                response = insurances.data
        else:
            raise ObjectDoesNotExist

    except ObjectDoesNotExist as error:
        logger.debug("employee not found")
        response = "employee not found"
    return Response(response)


@api_view(['GET'])
@protected_resource(scopes=['user'])
def get_particular_employee_insurance(request, employee_id, insurance_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        if employee.status:
            insurances = Insurance.objects.filter(employee=employee_id, id=insurance_id)
            if len(insurances) == 0:
                logger.debug("no insurance found")
                response = "no insurance found"
            else:
                insurance = InsuranceSerializer(instance=insurances[0])
                logger.debug("Fetched particular insurance of employee")
                response = insurance.data
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist as error:
        logger.debug("employee not found")
        response = "employee not found"

    return Response(response)


@api_view(['GET'])
@protected_resource(scopes=['user'])
def get_claim_details(request, employee_id):

    try:
        employee = Employee.objects.get(pk=employee_id)
        if employee.status:
            insurances = Insurance.objects.filter(employee=employee_id)
            claim_list = []
            for insurance in insurances:
                claim = Claim.objects.filter(insurance=insurance.id)
                claim_list.extend(claim)
            claim_list = ClaimSerializer(instance=claim_list, many=True)
            logger.debug(f"Fetched all claim details of employee {employee_id}")
            response = claim_list.data
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist as error:
        logger.debug("employee not found")
        response = "employee not found"
    return Response(response)


@api_view(['GET'])
@protected_resource(scopes=['user'])
def get_particular_claim_details(request, employee_id, insurance_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        if employee.status:
            insurances = Insurance.objects.filter(employee=employee_id,
                                                  id=insurance_id)
            if len(insurances) == 0:
                logger.debug("no insurance found")
                response = "no insurance found"
            else:
                claim = Claim.objects.filter(insurance=insurances[0].id)
                if len(claim) == 0:
                    logger.debug("no claim found")
                    response = "no claim found"
                else:
                    claim = Claim.objects.filter(insurance=insurances[0].id)
                    claim = ClaimSerializer(instance=claim, many=True)
                    logger.debug(f"Fetched claim details of insurance id {insurance_id}")
                    response = claim.data
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist as error:
        logger.debug("employee not found")
        response = "employee not found"
    return Response(response)
