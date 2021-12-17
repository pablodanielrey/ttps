
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models



class SerializadorDeConfigurador(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username', read_only=True)
    clave = serializers.CharField(source='usuario.password', read_only=True)
    class Meta:
        model = models.Configurador
        fields = ['id','nombre','apellido','usuario','clave']

class VistaConfigurador(viewsets.ModelViewSet):
    queryset = models.Configurador.all()
    serializer_class = SerializadorDeConfigurador

    def create(self, request):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid()
        serializador.save()        
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando configurador : {q}')

        personas = models.Configurador.buscar(q)
        serializer = SerializadorDeConfigurador(personas, many=True, context={'request': request})
        return Response(serializer.data)