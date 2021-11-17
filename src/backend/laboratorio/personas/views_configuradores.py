
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models



class SerializadorDeConfigurador(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username')
    clave = serializers.CharField(source='usuario.password')
    class Meta:
        model = models.Configurador
        fields = ['id','nombre','apellido','usuario','clave']

class VistaConfigurador(viewsets.ModelViewSet):
    queryset = models.Configurador.all()
    serializer_class = SerializadorDeConfigurador

    model = models.PersonasModel()

    def create(self, request):
        configurador = self.model.crearConfigurador(**request.data)
        serializador = self.serializer_class(instance=configurador, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando configurador : {q}')

        personas = models.Configurador.buscar(q)
        serializer = SerializadorDeConfigurador(personas, many=True, context={'request': request})
        return Response(serializer.data)