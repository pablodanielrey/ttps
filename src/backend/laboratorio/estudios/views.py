from django.shortcuts import render


import logging

from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets


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