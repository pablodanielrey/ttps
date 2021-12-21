
import logging
from os import read

from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes

from django.contrib.auth import models as auth_models

from . import models
from . import persona_serializers


class VistaPersona(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Persona.objects.all()
    serializer_class = persona_serializers.SerializadorDePersona
    # permission_classes = [ DjangoModelPermissions ]


    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Persona.buscar(q)
        serializer = persona_serializers.SerializadorDePersona(personas, many=True, context={'request': request})
        return Response(serializer.data)
        

