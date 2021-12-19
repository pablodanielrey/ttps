
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import empleados_serializers

class VistaConfigurador(viewsets.ModelViewSet):
    queryset = models.Configurador.all()
    serializer_class = empleados_serializers.SerializadorDeConfigurador

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando configurador : {q}')

        personas = models.Configurador.buscar(q)
        serializer = empleados_serializers.SerializadorDeConfigurador(personas, many=True, context={'request': request})
        return Response(serializer.data)