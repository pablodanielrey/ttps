from django.shortcuts import render

import logging
import datetime

# Create your views here.
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response


from estudios import models as estudio_models
from personas import views_personas

from . import models

class SerializadorRangoTurnos(serializers.ModelSerializer):
    class Meta:
        model = models.RangoDeTurnos
        fields = ['id', 'hora_inicio', 'hora_fin', 'frecuencia']

class SerializadorParametroTurnos(serializers.ModelSerializer):

    rangos = SerializadorRangoTurnos(many=True)
    class Meta:
        model = models.ParametroDeTurnos
        fields = ['id','fecha_valido','rangos']


class VistaParametroTurnos(viewsets.ModelViewSet):
    queryset = models.ParametroDeTurnos.objects.all()
    serializer_class = SerializadorParametroTurnos


class SerializadorFechasSinTurno(serializers.ModelSerializer):
    class Meta:
        model = models.FechasSinTurno
        fields = ['id','fecha']

class VistaFechasSinTurno(viewsets.ViewSet):
    queryset = models.FechasSinTurno.objects.all()
    serializer_class = SerializadorFechasSinTurno


from dateutil import parser


class VistaTurnosDisponibles(viewsets.ModelViewSet):

    queryset = models.ParametroDeTurnos.objects.none()

    def list(self, request, *args, **kwargs):
        """
        datos_rango = request
        inicio = request.query_params.get('inicio')

        inicio = datetime.datetime.now().replace(tzinfo=ZoneInfo("America/Argentina/Buenos_Aires"))
        inicio = inicio.replace(hour=0)
        fin = inicio + datetime.timedelta(days=4)
        """
        inicio = parser.parse(request.query_params.get('inicio'))
        fin = parser.parse(request.query_params.get('fin')) + datetime.timedelta(seconds=1)

        logging.debug(f'buscando turnos entre {inicio} y {fin}')

        turnos = models.ModeloTurnos().obtener_turnos(inicio,fin)

        return Response(turnos)




class SerializadorTurnosConfirmados(serializers.HyperlinkedModelSerializer):
    persona = views_personas.SerializadorDePersona()
    class Meta:
        model = models.TurnoConfirmado
        fields = ['id','persona','inicio','fin']

class VistaTurnosConfirmados(viewsets.ModelViewSet):

    queryset = models.TurnoConfirmado.objects.all()
    serializer_class = SerializadorTurnosConfirmados

    """
    def list(self, request, *args, **kwargs):
        super(VistaListaTurnosConfirmados).list()
        inicio = datetime.datetime.now().replace(tzinfo=ZoneInfo("America/Argentina/Buenos_Aires"))
        inicio = inicio - datetime.timedelta(days=3)
        fin = inicio + datetime.timedelta(days=15)

        logging.debug(f'buscando turnos entre {inicio} y {fin}')

        turnos = models.ModeloTurnos().obtener_turnos_confirmados(inicio,fin)

        return Response(turnos)
    """

    def create(self, request, *args, **kwargs):
        logging.debug(request.data)

        estudio_id = request.data['id_estudio']
        estudio = estudio_models.Estudio.objects.get(id=estudio_id)
        persona = estudio.paciente

        #id_persona = request.data['persona']
        #persona = [p for p in personas_models.Persona.objects.all() if p.id == id_persona][0]
        #persona = personas_models.Persona.objects.get(id_persona)
        
        
        inicio = parser.parse(request.data['inicio'])
        fin = parser.parse(request.data['fin'])

        turno = models.TurnoConfirmado(persona=persona, inicio=inicio, fin=fin)
        turno.save()

        serializador = SerializadorTurnosConfirmados(turno, context={'request': request})
        return Response(serializador.data)