import logging

from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from faq.models import Faq
# Create your views here.
from faq.serializer import FaqSerializer

logger = logging.getLogger('root')


@api_view(['POST'])
def create_faq(request):
    try:
        new_qa = FaqSerializer(data=request.data)
        new_qa.is_valid(raise_exception=True)
        new_qa.save()
        logger.debug(f"Employee created successfully with id of{new_qa.data['id']}")
        return Response(new_qa.data)
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


@api_view(['GET'])
def view_answers(request, company_id):
    answers = Faq.objects.filter(company=company_id)
    if answers.exists():
        answers = FaqSerializer(instance=answers, many=True)
        logger.debug(f"Fetched answers of company id {company_id}")
        response = answers.data
    else:
        logger.debug("company not exist")
        response = "company not exist"
    return Response(response)


@api_view(['PUT'])
def update_answer(request, faq_id):
    try:
        details = Faq.objects.get(pk=faq_id)
        updated_details = FaqSerializer(details, data=request.data, partial=True)
        updated_details.is_valid(raise_exception=True)
        updated_details.save()
        logger.debug(f"Faq {faq_id} is updated")
        return Response(f"successfully updated Faq detail of id {faq_id}")
    except ValidationError as error:
        logger.debug(f'Validation error:{error.message}')
        return Response({'message': error.message}, status=400)


