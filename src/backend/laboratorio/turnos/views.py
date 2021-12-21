from django.shortcuts import render

import logging
import datetime

from rest_framework import serializers, views, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


from estudios import models as estudio_models


from . import permissions
from . import models
from . import serializers


class VistaParametroTurnos(viewsets.ModelViewSet):
    queryset = models.ParametroDeTurnos.objects.all()
    serializer_class = serializers.SerializadorParametroTurnos
    permission_classes = [ permissions.ParametroTurnosPermisos ]

class VistaFechasSinTurno(viewsets.ModelViewSet):
    queryset = models.FechasSinTurno.objects.all()
    serializer_class = serializers.SerializadorFechasSinTurno



from dateutil import parser



class VistaTurnosDisponibles(viewsets.ModelViewSet):

    queryset = models.ParametroDeTurnos.objects.none()
    permission_classes = [ permissions.TurnosDisponiblesPermisos ]

    def list(self, request, *args, **kwargs):
        """
        datos_rango = request
        inicio = request.query_params.get('inicio')

        inicio = datetime.datetime.now().replace(tzinfo=ZoneInfo("America/Argentina/Buenos_Aires"))
        inicio = inicio.replace(hour=0)
        fin = inicio + datetime.timedelta(days=4)
        """
        if not request.query_params.get('inicio',None):
            raise ValidationError({'inicio':'requerido'})

        if not request.query_params.get('fin',None):
           raise ValidationError({'fin':'requerido'})

        inicio = parser.parse(request.query_params.get('inicio'))
        fin = parser.parse(request.query_params.get('fin')) + datetime.timedelta(seconds=1)

        logging.debug(f'buscando turnos entre {inicio} y {fin}')

        turnos = models.ModeloTurnos().obtener_turnos(inicio,fin)

        return Response(turnos)






class VistaTurnosConfirmados(viewsets.ModelViewSet):

    queryset = models.TurnoConfirmado.objects.all()
    serializer_class = serializers.SerializadorTurnosConfirmados
    permission_classes = [ permissions.TurnosConfirmadosPermisos ]

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

        serializador = serializers.SerializadorTurnosConfirmados(turno, context={'request': request})
        return Response(serializador.data)


    def destroy(self, request, pk=None):
        instance = self.get_object()
        logging.debug(instance)

        models.ModeloTurnos().cancelar_turno(instance)
        estudio_models.EsperandoTomaDeMuestra.turno_cancelado(instance)

        serializer = self.serializer_class(instance=instance, context={'request':request})
        return Response(serializer.data)