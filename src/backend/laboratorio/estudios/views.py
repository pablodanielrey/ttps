from django.shortcuts import render


import logging

from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets


from personas.views import SerializadorDePersona

class SerializadorTiposDeEstudio(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TiposDeEstudio
        fields = ['id','nombre']


class VistaTiposDeEstudio(viewsets.ModelViewSet):
    queryset = models.TiposDeEstudio.objects.all()
    serializer_class = SerializadorTiposDeEstudio

class SerializadorDiagnostico(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Diagnostico
        fields = ['id', 'nombre']


class VistaDiagnostico(viewsets.ModelViewSet):
    queryset = models.Diagnostico.objects.all()
    serializer_class = SerializadorDiagnostico


class SerializadorEstudios(serializers.HyperlinkedModelSerializer):

    #persona = SerializadorDePersona()
    #medico_derivante = SerializadorDePersona()
    #tipo = SerializadorTiposDeEstudio()
    #diagnostico = SerializadorDiagnostico()

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'presupuesto', 'diagnostico', 'paciente', 'medico_derivante', 'tipo']

class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = SerializadorEstudios