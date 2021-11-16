from django.shortcuts import render

# Create your views here.

import logging

from rest_framework import views
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class VistaToken(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        usuario = request.user
        logging.debug(f'usuario logueado : {usuario}')
        return Response(str(usuario))