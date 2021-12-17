
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
    matricula = serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','matricula']

    def update(self, instance, validated_data):
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        return super().update(instance, validated_data)

class VistaMedicoDerivante(viewsets.ModelViewSet):
    queryset = models.MedicoDerivante.all()
    serializer_class = SerializadorDeMedicoDerivante

    def create(self, request):
        # medico = self.model.crearMedicoDerivante(**request.data)
        # serializador = SerializadorDeMedicoDerivante(data=request.data, context={'request':request})
        serializador = SerializadorDeMedicoDerivante(data=request.data)
        serializador.is_valid()
        serializador.save()
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico derivante : {q}')
        personas = models.MedicoDerivante.buscar(q)
        serializer = SerializadorDeMedicoDerivante(personas, many=True, context={'request': request})
        return Response(serializer.data)




class SerializadorDeMedicoInformante(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.usuario.username', read_only=True)
    clave = serializers.CharField(source='usuario.usuario.password', read_only=False)
    matricula = serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.MedicoInformante
        fields = ['id','nombre','apellido','email','matricula', 'usuario', 'clave']

    def update(self, instance, validated_data):
        logging.info(validated_data)
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        
        credenciales = validated_data.pop('usuario')
        from django.contrib.auth.hashers import make_password
        usuario_django = instance.usuario
        usuario_django.password = make_password(credenciales['password'])
        usuario_django.save()

        return super().update(instance, validated_data)

class VistaMedicoInformante(viewsets.ModelViewSet):
    queryset = models.MedicoInformante.all()
    serializer_class = SerializadorDeMedicoInformante

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
        serializer = SerializadorDeMedicoInformante(personas, many=True, context={'request': request})
        return Response(serializer.data)