from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.db import IntegrityError


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({'error': ugettext('Please provide both email and password')},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': ugettext('Invalid Credentials')},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def sign_up(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({'error': ugettext('Please provide both email and password')},    # pragma: no cover
                        status=HTTP_400_BAD_REQUEST)
    try:
        user = get_user_model().objects.create_user(email=email, password=password) # noqa
    except IntegrityError:
        return Response({'error': 'Email already exists'},
                        status=HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)
