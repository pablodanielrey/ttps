
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import medicos_serializers

class VistaMedicoDerivante(viewsets.ModelViewSet):
    queryset = models.MedicoDerivante.all()
    serializer_class = medicos_serializers.SerializadorDeMedicoDerivante

    def create(self, request):
        # medico = self.model.crearMedicoDerivante(**request.data)
        # serializador = SerializadorDeMedicoDerivante(data=request.data, context={'request':request})
        serializador = medicos_serializers.SerializadorDeMedicoDerivante(data=request.data)
        serializador.is_valid()
        serializador.save()
        return Response(serializador.data)

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

    def create(self, request):
        # serializador = self.serializer_class(instance=medico, context={'request':request})
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid()
        serializador.save()
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico informante : {q}')

        personas = models.MedicoInformante.buscar(q)
        serializer = medicos_serializers.SerializadorDeMedicoInformante(personas, many=True, context={'request': request})
        return Response(serializer.data)