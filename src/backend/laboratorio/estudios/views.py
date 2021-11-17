from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseBadRequest



import logging
import datetime
from zoneinfo import ZoneInfo
from dateutil import parser

from . import models
from personas import models as personas_models
from estudios import models as estudio_models
from turnos import models as turnos_models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from personas.views_personas import SerializadorDePersona

from turnos import views as turnos_views

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

from rest_polymorphic.serializers import PolymorphicSerializer


class SerializadorEstadoEstudio(serializers.ModelSerializer):
    class Meta:
        model = models.EstadoEstudio
        fields = ['id','fecha']

# class SerializadorEsperandoPresupuesto(serializers.ModelSerializer):
#     class Meta:
#         model = models.EsperandoPresupuesto
#         fields = ['id','fecha','presupuesto']


class SerializadorEsperandoComprobanteDePago(serializers.ModelSerializer):
    class Meta:
        logging.debug("comprobante")
        model = models.EsperandoComprobanteDePago
        fields = ['id','fecha','comprobante']

class SerializadorAnuladorPorFaltaDePago(serializers.ModelSerializer):
    class Meta:
        model = models.AnuladorPorFaltaDePago
        fields = ['id','fecha','fecha_procesado']


class SerializadorEnviarConsentimientoInformado(serializers.ModelSerializer):
    class Meta:
        model = models.EnviarConsentimientoInformado
        fields = ['id','fecha','fecha_enviado']

class SerializadorEsperandoConsentimientoInformado(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoConsentimientoInformado
        fields = ['id','fecha','consentimiento']

class SerializadorEsperandoSeleccionDeTurnoParaExtraccion(serializers.ModelSerializer):
    turno = turnos_views.SerializadorTurnosConfirmados()
    class Meta:
        model = models.EsperandoSeleccionDeTurnoParaExtraccion
        fields = ['id','fecha','turno']

class SerializadorEsperandoTomaDeMuestra(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoTomaDeMuestra
        fields = ['id','fecha','fecha_muestra','mililitros','freezer','expirado']

class SerializadorEsperandoRetiroDeExtaccion(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoRetiroDeExtaccion
        fields = ['id','fecha','extracionista','fecha_retiro']

class SerializadorEsperandoLoteDeMuestraParaProcesamientoBiotecnologico(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico
        fields = ['id','fecha','numero_lote']

class SerializadorEsperandoProcesamientoDeLoteBiotecnologico(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoProcesamientoDeLoteBiotecnologico
        fields = ['id','fecha','resultado_url','fecha_resultado']


class SerializadorEsperandoInterpretacionDeResultados(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoInterpretacionDeResultados
        fields = ['id','fecha','fecha_informe','medico_informante','informe','resultado']

class SerializadorEsperandoEntregaAMedicoDerivante(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoEntregaAMedicoDerivante
        fields = ['id','fecha','fecha_entrega']


class SerializadorResultadoDeEstudioEntregado(serializers.ModelSerializer):
    class Meta:
        model = models.ResultadoDeEstudioEntregado
        fields = ['id','fecha']

class SerializadorEstadoEstudioPolimorfico(PolymorphicSerializer):
    model_serializer_mapping = {
        models.EstadoEstudio: SerializadorEstadoEstudio,
        # models.EsperandoPresupuesto: SerializadorEsperandoPresupuesto,
        models.EsperandoComprobanteDePago: SerializadorEsperandoComprobanteDePago,
        models.AnuladorPorFaltaDePago: SerializadorAnuladorPorFaltaDePago,
        models.EnviarConsentimientoInformado: SerializadorEnviarConsentimientoInformado,
        models.EsperandoConsentimientoInformado: SerializadorEsperandoConsentimientoInformado,
        models.EsperandoSeleccionDeTurnoParaExtraccion: SerializadorEsperandoSeleccionDeTurnoParaExtraccion,
        models.EsperandoTomaDeMuestra: SerializadorEsperandoTomaDeMuestra,
        models.EsperandoRetiroDeExtaccion: SerializadorEsperandoRetiroDeExtaccion,
        models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico: SerializadorEsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
        models.EsperandoProcesamientoDeLoteBiotecnologico: SerializadorEsperandoProcesamientoDeLoteBiotecnologico,
        models.EsperandoInterpretacionDeResultados: SerializadorEsperandoInterpretacionDeResultados,
        models.EsperandoEntregaAMedicoDerivante: SerializadorEsperandoEntregaAMedicoDerivante,
        models.ResultadoDeEstudioEntregado: SerializadorResultadoDeEstudioEntregado
    }


class VistaEstadoEstudio(viewsets.ModelViewSet):
    queryset = models.EstadoEstudio.objects.all()
    serializer_class = SerializadorEstadoEstudioPolimorfico

    workflow = [
        models.EsperandoComprobanteDePago,
        models.EnviarConsentimientoInformado,
        models.EsperandoConsentimientoInformado,
        models.EsperandoSeleccionDeTurnoParaExtraccion,
        models.EsperandoTomaDeMuestra,
        models.EsperandoRetiroDeExtaccion,
        models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
        models.EsperandoInterpretacionDeResultados,
        models.EsperandoEntregaAMedicoDerivante,
        models.ResultadoDeEstudioEntregado
    ]


    def create(self, request, *args, **kwargs):
        """
            En nuestro caso los creates no se realizan extrictamente cumpliendo REST.
            Los create para las interfaces son modify de los estados actuales y se ejecuta el workflow.
        """

        estudio_id = request.data.pop('estudio_id')
        estudio = estudio_models.Estudio.objects.get(id=estudio_id)

        """
            TODO: debemos estar seguros de que no actualizamos ningún id!!!!
        """
        for campo_solo_lectura in ['id','fecha']:
            try:
                request.data.pop(campo_solo_lectura)
            except KeyError as e:
                pass

        ultimo_estado = estudio.ultimo_estado
        
        logging.debug(ultimo_estado)
        clase_ultimo_estado = ultimo_estado.__class__

        """ aca manejo comportamientos especiales de los estados """
        if clase_ultimo_estado == models.EsperandoSeleccionDeTurnoParaExtraccion:
            """ genero un turno """
            paciente = personas_models.Persona.objects.get(id=estudio.paciente.id)
            inicio = parser.parse(request.data['inicio'])
            fin = parser.parse(request.data['fin'])
            turno = turnos_models.TurnoConfirmado(persona=paciente,inicio=inicio, fin=fin)
            turno.save()
            logging.debug(f'turno generado {turno.id}')

            """ actualizo el estado """
            ultimo_estado.turno = turno
            ultimo_estado.save()

        else:
            """ los casos normales de cambios de estado - se encarga el serializer """
            serializador = SerializadorEstadoEstudioPolimorfico.model_serializer_mapping[clase_ultimo_estado](instance=ultimo_estado, data=request.data)
            if not serializador.is_valid():
                return HttpResponseBadRequest(serializador.errors)
            if len(serializador.validated_data) <= 0:
                """ no existen datos enviados para actualizar el nuevo estado """
                return HttpResponseBadRequest()

            serializador.save()

        """
            Ahora paso al nuevo estado de acuerdo al workflow.
        """
        try:
            indice = self.workflow.index(clase_ultimo_estado)
            if indice+1 < len(self.workflow):
                clase_siguiente_estado = self.workflow[indice+1]
                siguiente_estado = clase_siguiente_estado(estudio=estudio)
                siguiente_estado.save()

        except ValueError as e:
            pass


        serializador = SerializadorEstadoEstudioPolimorfico(ultimo_estado, context={'request': request})
        return Response(serializador.data)

"""
    ///////////////////////////////////////////////
"""

class SerializadorEstudios(serializers.HyperlinkedModelSerializer):
    paciente = SerializadorDePersona()
    medico_derivante = SerializadorDePersona()
    tipo = SerializadorTiposDeEstudio()
    diagnostico = SerializadorDiagnostico()
    estados = SerializadorEstadoEstudioPolimorfico(many=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo', 'presupuesto', 'estados']

class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = SerializadorEstudios

    def create(self, request, *args, **kwargs):
        """
            Creamos el estudio e insertamos los estados iniciales por los que ya pasa en el momento de la generación.
        """

        datos = request.data
        #logging.debug(datos)
        presupuesto = datos['presupuesto']
        paciente = personas_models.Paciente.objects.get(id=datos['paciente']['id'])
        diagnostico = estudio_models.Diagnostico.objects.get(id=datos['diagnostico']['id'])
        tipo = estudio_models.TiposDeEstudio.objects.get(id=datos['tipo_estudio'])
        estudio = estudio_models.Estudio(
            paciente=paciente,
            medico_derivante=paciente,
            diagnostico=diagnostico,
            tipo=tipo,
            fecha_alta=datos['fecha_alta'],
            presupuesto=presupuesto
        )
        estudio.save()

        esperando_comprobante = estudio_models.EsperandoComprobanteDePago(estudio=estudio)
        esperando_comprobante.save()

        serializer = SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)

    def modify(self, request, *args, **kwargs):

        estudio_id = request.data['estudio_id']
        estudio = models.Estudio.objects.get(estudio_id)

        """
        ultimo_estado = estudio.estados.all('fecha').last()
        switch ultimo_estado.nombre:
            'EspernadoComprobante':
                comprobante_b64 = request.data['comprobante']
                ultimo_estado.comprobante = comprobante_b64
                ultimo_estado.save()
            
            'EsperandoPresupeusto':
                comprobante_b64 = request.data['presupuesto']
                ultimo_estado.presupuesto = comprobante_b64
                ultimo_estado.fecha = request.data['fecha']
                ultimo_estado.save()

        """
        serializer = SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)
        
    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        e = request.query_params.get('e',None)
        logging.debug(f'buscando a : {q}  en estado : {e}')

        estudios = models.Estudio.buscar(q, e)
        serializer = SerializadorEstudios(estudios, many=True, context={'request': request})
        return Response(serializer.data)
