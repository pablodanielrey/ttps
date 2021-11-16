from django.shortcuts import render

# Create your views here.

import logging

from rest_framework import views
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action


from django.contrib.auth.models import User

class VistaToken(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        usuario = request.user

        logging.debug(f'usuario logueado : {usuario}')

        try:
            token = Token.objects.get(user_id__username=usuario.username)
        except User.DoesNotExist as e:
            token = Token.objects.create(user=usuario)
            
        return Response({'token':token.key})