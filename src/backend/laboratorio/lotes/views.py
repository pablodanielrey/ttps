from django.shortcuts import render

# Create your views here.


from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response

from estudios.views import SerializadorEstudios

class SerializadorDeEstudioDeLote(serializers.ModelSerializer):
    estudio = SerializadorEstudios()
    class Meta:
        model = models.EstudioDeLote
        fields = ['estudio']

class SerializadorDeLote(serializers.ModelSerializer):
    estudios = SerializadorDeEstudioDeLote(many=True)
    class Meta:
        model = models.Lote
        fields = ['id','fecha', 'resultado', 'estudios']


class VistaLotes(viewsets.ModelViewSet):
    queryset = models.Lote.objects.all()
    serializer_class = SerializadorDeLote