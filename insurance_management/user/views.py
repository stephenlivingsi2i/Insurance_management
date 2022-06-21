import json

import requests
from django.contrib.auth import authenticate
from oauth2_provider.models import Application, AccessToken
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.constants import SCOPE_OF_SUPERUSER, SCOPE_OF_ORGANIZATION, SCOPE_OF_EMPLOYEE


def give_scopes_based_on_user_role(user):
    scope = None
    if user.is_active and user.user_role == "super_user":
        scope = SCOPE_OF_SUPERUSER
    elif user.is_active and user.user_role == "organization":
        scope = SCOPE_OF_ORGANIZATION
    elif user.is_active and user.user_role == "employee":
        scope = SCOPE_OF_EMPLOYEE
    return scope


@api_view(['POST'])
@permission_classes((AllowAny,))
def login_user(request):
    user = authenticate(username=request.data['username'], password=request.data['password'])
    print(user.user_role)

    if user:
        token_obj = AccessToken.objects.filter(user=user)
        # print(token_obj)
        app_obj = Application.objects.filter(user=user)

        print(app_obj[0].client_id)
        url = 'http://' + request.get_host() + '/o/token/'
        data_dict = {
            "grant_type": "password",
            "username": request.data['username'],
            "password": request.data['password'],
            "client_id": app_obj[0].client_id,
            "scope": give_scopes_based_on_user_role(user)
        }
        # if user.is_active or not user.is_admin or not user.is_staff or not user.is_superuser:
        #     print("welcome")
        #     data_dict["scope"] = 'read'
        token_obj = requests.post(url=url, data=data_dict)
        token_obj = json.loads(token_obj.text)
        # print(">>>>>>>>>>>", token_obj.keys())
        #return Response("ok")
    else:
        return Response("not ok")

    return Response(token_obj)
