from django.shortcuts import render


import logging

from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets


from personas.views import SerializadorDePersona

class SerializadorTipoEstudio(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TipoEstudio
        fields = ['id','nombre']


class VistaTipoEstudio(viewsets.ModelViewSet):
    queryset = models.TipoEstudio.objects.all()
    serializer_class = SerializadorTipoEstudio


class SerializadorDiagnostico(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Diagnostico
        fields = ['id', 'nombre']


class VistaDiagnostico(viewsets.ModelViewSet):
    queryset = models.Diagnostico.objects.all()
    serializer_class = SerializadorDiagnostico


class SerializadorEstudios(serializers.HyperlinkedModelSerializer):

    persona = SerializadorDePersona()
    medico_derivante = SerializadorDePersona()
    diagnostico = SerializadorDiagnostico()
    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'presupuesto', 'diagnostico', 'persona', 'medico_derivante']

class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = SerializadorEstudios