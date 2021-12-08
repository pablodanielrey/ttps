
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models

class SerializadorDeMatricula(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = ['numero']

class SerializadorDeMedicoDerivante(serializers.ModelSerializer):
    # matricula = SerializadorDeMatricula()
    matricula = serializers.CharField(source='matricula.numero', read_only=True)
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','matricula']

class VistaMedicoDerivante(viewsets.ModelViewSet):
    queryset = models.MedicoDerivante.all()
    serializer_class = SerializadorDeMedicoDerivante

    model = models.PersonasModel()

    def create(self, request):
        medico = self.model.crearMedicoDerivante(**request.data)
        serializador = SerializadorDeMedicoDerivante(instance=medico, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico derivante : {q}')
        personas = models.MedicoDerivante.buscar(q)
        serializer = SerializadorDeMedicoDerivante(personas, many=True, context={'request': request})
        return Response(serializer.data)




class SerializadorDeMedicoInformante(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username', read_only=True)
    clave = serializers.CharField(source='usuario.password', read_only=True)
    matricula = serializers.CharField(source='matricula.numero', read_only=True)
    class Meta:
        model = models.MedicoInformante
        fields = ['id','nombre','apellido','email','matricula','usuario','clave']

class VistaMedicoInformante(viewsets.ModelViewSet):
    queryset = models.MedicoInformante.all()
    serializer_class = SerializadorDeMedicoInformante

    model = models.PersonasModel()

    def create(self, request):
        medico = self.model.crearMedicoInformante(**request.data)
        serializador = self.serializer_class(instance=medico, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico informante : {q}')

        personas = models.MedicoInformante.buscar(q)
        serializer = SerializadorDeMedicoInformante(personas, many=True, context={'request': request})
        return Response(serializer.data)