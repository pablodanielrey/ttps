from django.shortcuts import render
from django.http.response import HttpResponseBadRequest

# Create your views here.
import logging

from . import models


"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response

from estudios import views  as estudio_views

class SerializadorDeEstudioDeLote(serializers.ModelSerializer):
    estudio = estudio_views.SerializadorEstudios()
    class Meta:
        model = models.EstudioDeLote
        fields = ['id', 'estudio']

class SerializadorDeLote(serializers.ModelSerializer):
    estudios = SerializadorDeEstudioDeLote(many=True)
    class Meta:
        model = models.Lote
        fields = ['id', 'fecha', 'resultado', 'estudios']

class VistaLotes(viewsets.ModelViewSet):
    queryset = models.Lote.objects.all()
    serializer_class = SerializadorDeLote

    def create(self, request, *args, **kwargs):
        logging.debug('llego al create')
        """ redefino el create debido a que va totalmente otra lógica """
        lote = models.ModeloLotes().generar_lote(request.data['estudios'])
        serializador = self.serializer_class(instance=lote, context={'request': request})
        return Response(serializador.data)


class VistaEstudios(views.APIView):

    modelo = models.ModeloLotes()
    
    def get(self, request, format=None):
        estudios = self.modelo.obtener_estudios_para_lote()
        # serializador = estudio_views.SerializadorEstudios(estudios, many=True)
        # return Response(serializador.data)
        return Response([e.id for e in estudios])