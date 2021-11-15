from django.shortcuts import render

# Create your views here.


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




class VistaEstudios(views.APIView):

    modelo = models.ModeloLotes()
    
    def get(self, request, format=None):
        estudios = self.modelo.obtener_estudios_para_lote()
        serializador = estudio_views.SerializadorEstudios(estudios, many=True)
        return Response(serializador.data)