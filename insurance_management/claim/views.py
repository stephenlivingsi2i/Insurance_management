import logging
from django.core.exceptions import ValidationError
from django.shortcuts import render

# Create your views here.
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
from rest_framework.response import Response

from claim.models import Claim
from claim.serializer import ClaimSerializer
from employee.models import Employee
from insurance.models import Insurance
from insurance.serializer import InsuranceSerializer


logger = logging.getLogger('root')


@api_view(['POST'])
@protected_resource(scopes=['user'])
def create_claim(request):
    """ Create new claim from insurance """
    try:
        user = request.user
        employee = Employee.objects.get(user_id=user.id)
        insurance_id = request.data.get("insurance")
        request.data['employee'] = employee.id
        claimed_amount = request.data.get("claimed_amount")
        remaining_amount = claim_insurance(insurance_id, claimed_amount)
        request.data['remaining_insurance_amount'] = remaining_amount
        insurance = Insurance.objects.get(pk=insurance_id)
        request.data['claimed_by'] = insurance.holder_name
        new_claim = ClaimSerializer(data=request.data)
        new_claim.is_valid(raise_exception=True)
        new_claim.save()
        logger.debug(f"added claim for {insurance_id}")
        return Response(new_claim.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


# @api_view(['GET'])
# def view_claims(request):
#     """View all claim details from database"""
#
#     all_claims = Claim.objects.all()
#     if all_claims.exists():
#         all_claims = ClaimSerializer(instance=all_claims, many=True)
#         logger.debug()
#         return Response(all_claims.data)
#     else:
#         return Response("claim not exists")


def claim_insurance(insurance_id, claimed_amount):
    insurance_details = Insurance.objects.get(pk=insurance_id)
    insurance_details.remaining_amount = \
        insurance_details.remaining_amount - claimed_amount
    insurance_details.save()
    return insurance_details.remaining_amount
