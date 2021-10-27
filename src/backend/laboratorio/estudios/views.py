from django.db.models.query import QuerySet
from django.shortcuts import render


import logging

from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets
from rest_framework.response import Response


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


"""
    //////////// ESTADO DE ESTUDIOS ///////////////////
"""


class SerializadorEstadoEstudio(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EstadoEstudio
        fields = ['id','nombre','fecha','estudio']

class VistaEstadoEstudio(viewsets.ModelViewSet):
    queryset = models.EstadoEstudio.objects.all()
    serializer_class = SerializadorEstadoEstudio



class SerializadorPresupuestoEstudio(serializers.HyperlinkedModelSerializer):

    estado = SerializadorEstadoEstudio()
    class Meta:
        model = models.PresupuestoEstudio
        fields = ['id', 'estado', 'presupuesto']

class VistaPresupuestoEstudio(viewsets.ModelViewSet):
    queryset = models.PresupuestoEstudio.objects.all()
    serializer_class = SerializadorPresupuestoEstudio


"""
    ///////////////////////////////////////////////
"""

class SerializadorEstudios(serializers.HyperlinkedModelSerializer):

    #persona = SerializadorDePersona()
    #medico_derivante = SerializadorDePersona()
    #tipo = SerializadorTiposDeEstudio()
    #diagnostico = SerializadorDiagnostico()
    estados = SerializadorEstadoEstudio(many=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo', 'estados']

class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = SerializadorEstudios

    def create(self, request, *args, **kwargs):
        """
            Creamos el estudio e insertamos los estados iniciales por los que ya pasa en el momento de la generación.
        """

        datos = request.data
        logging.debug(datos)

        estudio = models.Estudio(
            paciente=datos['paciente'],
            medico_derivante=datos['medico_derivante'],
            diagnostico=datos['diagnostico']
        )
        estudio.save()

        ep = models.EsperandoPresupuesto(estudio, datos)
        ep.save()

        serializer = SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)