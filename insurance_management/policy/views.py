import logging

from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from policy.models import Policy
from policy.serializer import PolicySerializer


logger = logging.getLogger('root')


@api_view(['POST'])
def create_policy(request):
    """Create new policy"""
    try:
        new_policy = PolicySerializer(data=request.data)
        new_policy.is_valid(raise_exception=True)
        new_policy.save()
        logger.debug(f"Created policy with id of {new_policy.data['id']}")
        return Response(new_policy.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
def view_policies(request):
    """View all policy details from database"""

    all_policies = Policy.objects.all()
    if all_policies.exists():
        all_policies = PolicySerializer(instance=all_policies, many=True)
        logger.debug("Fetched all policies")
        return Response(all_policies.data)
    else:
        logger.debug("policies not found")
        return Response("policies not found")


@api_view(['PUT'])
def update_policy(request, policy_id):
    """Update old policy details"""
    try:
        old_policy = Policy.objects.get(pk=policy_id)
        updated_policy = PolicySerializer(old_policy,
                                          data=request.data, partial=True)
        updated_policy.is_valid(raise_exception=True)
        updated_policy.save()
        logger.debug(f"updated policy detail of id {policy_id}")
        return Response(f"successfully updated user detail of id {policy_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)
