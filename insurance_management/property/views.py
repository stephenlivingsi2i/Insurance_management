import logging

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.shortcuts import render

# Create your views here.
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.models import Employee
from property.models import Property
from property.serializer import PropertySerializer


logger = logging.getLogger('root')


@api_view(['POST'])
@protected_resource(scopes=['user'])
def create_property(request):
    """Create new property and add it to employee"""
    try:
        user = request.user
        employee = Employee.objects.get(user_id=user.id)
        request.data['employee'] = employee.id
        new_property = PropertySerializer(data=request.data)
        new_property.is_valid(raise_exception=True)
        new_property.save()
        logger.debug(f"Created property for employee "
                     f"id{new_property.data['employee']}")
        return Response(new_property.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
@protected_resource(scopes=['user'])
def view_property_by_id(request):
    """Get all user properties of employee """
    user = request.user
    employee = Employee.objects.get(user_id=user.id)
    all_properties = Property.objects.filter(employee=employee.id)
    if all_properties.exists():
        all_properties = PropertySerializer(instance=all_properties, many=True)
        logger.debug(f"Fetched all properties of employee id {employee.id}")
        return Response(all_properties.data)
    else:
        logger.debug("Properties not found")
        return Response("Properties not found")


@api_view(['PUT'])
@protected_resource(scopes=['user'])
def update_property(request, property_id):
    """Validates the data and updates a property."""
    try:
        old_property_data = Property.objects.get(pk=property_id)
        updated_property_data = PropertySerializer(old_property_data,
                                                   data=request.data, partial=True)
        updated_property_data.is_valid(raise_exception=True)
        updated_property_data.save()
        logger.debug(f"updated property detail of id {property_id}")
        return Response(f"successfully updated user detail of id {property_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)

