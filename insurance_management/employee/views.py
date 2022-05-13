from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employee.models import Employee
from employee.serializer import EmployeeSerializer


@api_view(['POST'])
def create_user(request):
    new_user = EmployeeSerializer(data=request.data)
    new_user.is_valid(raise_exception=True)
    new_user.save()
    return Response(new_user.data)


@api_view(['GET'])
def view_user(request):
    all_user = Employee.objects.all()
    all_users = EmployeeSerializer(instance=all_user, many=True)
    return Response(all_users.data)


@api_view(['PUT'])
def update_user(request, user_id):
    """Validates the data and updates a user."""

    old_user_data = Employee.objects.get(pk=user_id)
    if not old_user_data.is_active:
        raise ObjectDoesNotExist()
    updated_user_data = EmployeeSerializer(old_user_data,
                                           data=request.data, partial=True)
    if updated_user_data.is_valid(raise_exception=True):
        updated_user_data.save()
    return Response(updated_user_data.data)


@api_view(['DELETE'])
def delete_user(request, user_id):
    """Makes a user inActive."""

    try:
        user = Employee.objects.get(pk=user_id)
        user.is_active = False
        user.save()
        return Response(status=204)
    except ObjectDoesNotExist:
        return Response({'message': 'No such user'}, status=404)

