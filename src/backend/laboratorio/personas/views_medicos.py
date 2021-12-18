
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import medicos_serializers

class VistaMedicoDerivante(viewsets.ModelViewSet):
    queryset = models.MedicoDerivante.all()
    serializer_class = medicos_serializers.SerializadorDeMedicoDerivante

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico derivante : {q}')
        personas = models.MedicoDerivante.buscar(q)
        serializer = medicos_serializers.SerializadorDeMedicoDerivante(personas, many=True, context={'request': request})
        return Response(serializer.data)





class VistaMedicoInformante(viewsets.ModelViewSet):
    queryset = models.MedicoInformante.all()
    serializer_class = medicos_serializers.SerializadorDeMedicoInformante

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico informante : {q}')

        personas = models.MedicoInformante.buscar(q)
        serializer = medicos_serializers.SerializadorDeMedicoInformante(personas, many=True, context={'request': request})
        return Response(serializer.data)