import logging
from django.shortcuts import render
from oauth2_provider.decorators import protected_resource
from prompt_toolkit.validation import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response

from family.models import Family
from family.serializer import FamilySerializer


logger = logging.getLogger('root')


@api_view(['POST'])
@protected_resource(scopes=['user'])
def add_relation(request):
    """Add new relation to the employee and store it to database"""
    try:
        new_relation = FamilySerializer(data=request.data)
        new_relation.is_valid(raise_exception=True)
        new_relation.save()
        logger.debug(f"Added family member to employee id {new_relation.data['employee']}")
        return Response(new_relation.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
@protected_resource(scopes=['admin user'])
def view_family(request, employee_id):
    """Get all family details of an employee from database"""

    fields = ("id", "name", "gender_type", "dob", "relation_type", "employee")
    family = Family.objects.filter(employee=employee_id)
    if family.exists():
        family = FamilySerializer(instance=family, many=True, fields=fields)
        logger.debug(f"Fetched family members of employee id {employee_id}")
        response = family.data
    else:
        logger.debug("family not exist")
        response = "family not exist"
    return Response(response)


@api_view(['PUT'])
@protected_resource(scopes=['user'])
def update_relation(request, family_id):
    """Validates the data and updates a relation."""

    try:
        old_relation_data = Family.objects.get(pk=family_id)
        updated_relation_data = FamilySerializer(old_relation_data,
                                                 data=request.data, partial=True)
        updated_relation_data.is_valid(raise_exception=True)
        updated_relation_data.save()
        logger.debug(f"updated user detail of id {family_id}")
        return Response(f"successfully updated user detail of id {family_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)

