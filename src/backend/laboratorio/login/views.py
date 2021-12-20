from django.shortcuts import render

# Create your views here.

import logging
import datetime
from zoneinfo import ZoneInfo

from rest_framework import views
from rest_framework import authentication
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes

from django.contrib.auth.models import User

from personas import models as persona_models
from personas import persona_serializers


def _generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

def obtener_roles(usuario):
    grupos = []
    for group in usuario.groups.all():
        grupos.append(group.name)
    return grupos

class VistaToken(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def __verificar_si_debe_cambiar_clave(self, usuario):
        if persona_models.Paciente.usuario_es_tipo(usuario):
            logging.debug(usuario.last_login)
            logging.debug(usuario.date_joined)
            if not usuario.last_login or usuario.last_login == usuario.date_joined:
                return True
        return False

    def get(self, request, format=None):
        usuario = request.user
        logging.debug(f'usuario logueado : {usuario}')

        cambiar_clave = self.__verificar_si_debe_cambiar_clave(usuario)

        usuario.last_login = _generar_fecha_now()
        usuario.save()

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
                'roles': grupos,
                'cambiar_clave': cambiar_clave
            }
        )


class VistaCambiarClave(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def post(self, request, format=None):
        usuario = request.user
        clave_anterior = request.data.get('clave_anterior')
        if not usuario.check_password(clave_anterior):
            return Response({'clave_anterior':'no es correcta'})
        nueva_clave = request.data.get('clave_nueva')

        usuario.set_password(nueva_clave)
        usuario.save()

        return Response({
            'status':'ok'
        })

class VistaRoles(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        usuario = request.user
        grupos = obtener_roles(usuario)
        return Response(grupos)


