from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from claim.models import Claim
from claim.serializer import ClaimSerializer
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer


@api_view(['POST'])
def create_claim(request):
    """ Create new claim from insurance """
    insurance_id = request.data.get("insurance")
    claimed_amount = request.data.get("claimed_amount")
    claim_insurance(insurance_id, claimed_amount)
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


def claim_insurance(insurance_id, claimed_amount):
    insurance_details = Insurance.objects.get(pk=insurance_id)
    insurance_details.remaining_amount = \
        insurance_details.remaining_amount - claimed_amount
    insurance_details.save()
