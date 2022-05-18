from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from policy.models import Policy
from policy.serializer import PolicySerializer


@api_view(['POST'])
def create_policy(request):
    """Create new policy"""

    new_policy = PolicySerializer(data=request.data)
    new_policy.is_valid(raise_exception=True)
    new_policy.save()
    return Response(new_policy.data)


@api_view(['GET'])
def view_policies(request):
    """View all policy details from database"""

    all_policies = Policy.objects.all()
    all_policies = PolicySerializer(instance=all_policies, many=True)
    return Response(all_policies.data)


@api_view(['PUT'])
def update_policy(request, policy_id):
    """Update old policy details"""

    old_policy = Policy.objects.get(pk=policy_id)
    updated_policy = PolicySerializer(old_policy,
                                      data=request.data, partial=True)
    if updated_policy.is_valid(raise_exception=True):
        updated_policy.save()
    return Response(updated_policy.data)
