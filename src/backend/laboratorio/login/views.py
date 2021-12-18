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

from personas import models as persona_models
from personas import persona_serializers

def obtener_roles(usuario):
    grupos = []
    for group in usuario.groups.all():
        grupos.append(group.name)
    return grupos

class VistaToken(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        usuario = request.user
        logging.debug(f'usuario logueado : {usuario}')

        try:
            persona = persona_models.Persona.objects.get(usuario=usuario)
            serializador = persona_serializers.SerializadorDePersona(instance=persona)
        except persona_models.Persona.DoesNotExist as e:
            serializador = None

        try:
            token = Token.objects.get(user_id__username=usuario.username)
        except Token.DoesNotExist as e:
            token = Token.objects.create(user=usuario)
            
        grupos = obtener_roles(usuario)
        return Response(
            {
                'token':token.key,
                'persona': serializador.data if serializador else '', 
                'roles': grupos
            }
        )


class VistaRoles(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        usuario = request.user
        grupos = obtener_roles(usuario)
        return Response(grupos)


