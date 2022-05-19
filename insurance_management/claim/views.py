from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from claim.models import Claim
from claim.serializer import ClaimSerializer


@api_view(['POST'])
def create_claim(request):
    """Create new claim from insurance"""

    new_claim = ClaimSerializer(data=request.data)
    new_claim.is_valid(raise_exception=True)
    new_claim.save()
    return Response(new_claim.data)


@api_view(['GET'])
def view_claims(request):
    """View all claim details from database"""

    all_claims = Claim.objects.all()
    all_claims = ClaimSerializer(instance=all_claims, many=True)
    return Response(all_claims.data)


