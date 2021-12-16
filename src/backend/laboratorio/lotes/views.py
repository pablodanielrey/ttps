from django.shortcuts import render
from django.http.response import HttpResponseBadRequest

# Create your views here.
import logging
from dateutil import parser

from . import models


"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets, permissions
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
        fields = ['id', 'fecha', 'resultado','estudios']

class VistaLotes(viewsets.ModelViewSet):
    queryset = models.Lote.all_pending()
    serializer_class = SerializadorDeLote
    permission_classes = [ permissions.IsAuthenticated ]

    def create(self, request, *args, **kwargs):
        logging.debug("entra aca")
        logging.debug(request.data['estudios'])
        """ redefino el create debido a que va totalmente otra lógica """
        lote = models.ModeloLotes().generar_lote(request.data['estudios'])
        serializador = self.serializer_class(instance=lote, context={'request': request})
        return Response(serializador.data)


    def update(self, request, pk):
        lote = models.Lote.objects.get(id=pk)
        # serializador = self.serializer_class(instance=lote, context={'request': request})

        logging.debug(request.data)

        fecha = parser.parse(request.data['fecha'])
        resultado = request.data['resultado']

        "TODO: procesar estudios a cerrar"
        ids_de_estudios = request.data['estudios']
        "TODO: tengo que impementar el cerrar los estudios solos pasados por ahi y los demas volver a seleccionar el turno"
        models.ModeloLotes().cerrar_lote(lote, fecha, resultado)

        return Response({'status':200})

class VistaEstudios(views.APIView):

    queryset = models.Lote.objects.none()
    modelo = models.ModeloLotes()
    permission_classes = [ permissions.IsAuthenticated ]
    
    def get(self, request, format=None):
        estudios = self.modelo.obtener_estudios_para_lote()
        # serializador = estudio_views.SerializadorEstudios(estudios, many=True)
        # return Response(serializador.data)
        return Response([e.id for e in estudios])