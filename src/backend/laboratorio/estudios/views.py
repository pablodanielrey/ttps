from django.db.models.query import QuerySet
from django.shortcuts import render



import logging
import datetime
from zoneinfo import ZoneInfo

from . import models
from personas import models as personas_models
from estudios import models as estudio_models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response


from personas.views import SerializadorDeObraSocial, SerializadorDePersona

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

class SerializadorEsperandoPresupuesto(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoPresupuesto
        fields = ['id','fecha','presupuesto']


class SerializadorEsperandoFactura(serializers.ModelSerializer):

    obra_social = SerializadorDeObraSocial()
    class Meta:
        model = models.EsperandoFactura
        fields = ['id','fecha','numero','fecha_factura','monto','obra_social']

class SerializadorEsperandoComprobanteDePago(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoComprobanteDePago
        fields = ['id','fecha','comprobante']

class SerializadorAnuladorPorFaltaDePago(serializers.ModelSerializer):
    class Meta:
        model = models.AnuladorPorFaltaDePago
        fields = ['id','fecha','fecha_procesado']


class SerializadorEsperandoConsentimientoInformado(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoConsentimientoInformado
        fields = ['id','fecha','consentimiento']

class SerializadorEsperandoSeleccionDeTurnoParaExtraccion(serializers.ModelSerializer):
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

class SerializadorEsperandoInterpretacionDeResultados(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoInterpretacionDeResultados
        fields = ['id','fecha','resultado_url','fecha_informe','medico_informante','informe']

class SerializadorEsperandoEntregaAMedicoDerivante(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoEntregaAMedicoDerivante
        fields = ['id','fecha','fecha_entrega']



class SerializadorEstadoEstudioPolimorfico(PolymorphicSerializer):
    model_serializer_mapping = {
        models.EstadoEstudio: SerializadorEstadoEstudio,
        models.EsperandoPresupuesto: SerializadorEsperandoPresupuesto,
        models.EsperandoFactura: SerializadorEsperandoFactura,
        models.EsperandoComprobanteDePago: SerializadorEsperandoComprobanteDePago,
        models.AnuladorPorFaltaDePago: SerializadorAnuladorPorFaltaDePago,
        models.EsperandoConsentimientoInformado: SerializadorEsperandoConsentimientoInformado,
        models.EsperandoSeleccionDeTurnoParaExtraccion: SerializadorEsperandoSeleccionDeTurnoParaExtraccion,
        models.EsperandoTomaDeMuestra: SerializadorEsperandoTomaDeMuestra,
        models.EsperandoRetiroDeExtaccion: SerializadorEsperandoRetiroDeExtaccion,
        models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico: SerializadorEsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
        models.EsperandoInterpretacionDeResultados: SerializadorEsperandoInterpretacionDeResultados,
        models.EsperandoEntregaAMedicoDerivante: SerializadorEsperandoEntregaAMedicoDerivante
    }

class VistaEstadoEstudio(viewsets.ModelViewSet):
    queryset = models.EstadoEstudio.objects.all()
    serializer_class = SerializadorEstadoEstudioPolimorfico


"""

class SerializadorPresupuestoEstudio(serializers.HyperlinkedModelSerializer):

    estado = SerializadorEstadoEstudio()
    class Meta:
        model = models.PresupuestoEstudio
        fields = ['id', 'estado', 'presupuesto']

class VistaPresupuestoEstudio(viewsets.ModelViewSet):
    queryset = models.PresupuestoEstudio.objects.all()
    serializer_class = SerializadorPresupuestoEstudio

"""

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
        paciente = personas_models.Persona.objects.get(id=datos['paciente']['id'])
        diagnostico = estudio_models.Diagnostico.objects.get(id=datos['diagnostico']['id'])
        tipo = estudio_models.TiposDeEstudio.objects.get(id=datos['tipo_estudio'])
        estudio = estudio_models.Estudio(
            paciente=paciente,
            medico_derivante=paciente,
            diagnostico=diagnostico,
            tipo=tipo,
            fecha_alta=datos['fecha_alta']

        )
        estudio.save()

        presupuesto = datos['presupuesto']
        ep = models.EsperandoPresupuesto(estudio=estudio, presupuesto=presupuesto)
        ep.save()

        serializer = SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)



"""
    Turnos
"""





class SerializadorRangoTurnos(serializers.ModelSerializer):
    class Meta:
        model = models.RangoDeTurnos
        fields = ['id', 'hora_inicio', 'hora_fin']

class SerializadorParametroTurnos(serializers.ModelSerializer):

    rangos = SerializadorRangoTurnos(many=True)
    class Meta:
        model = models.ParametroDeTurnos
        fields = ['id','fecha_valido','frecuencia','rangos']


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


class VistaListaTurnos(viewsets.ViewSet):

    queryset = models.ParametroDeTurnos.objects.none()

    def list(self, request, *args, **kwargs):

        inicio = datetime.datetime.utcnow().replace(tzinfo=ZoneInfo("America/Argentina/Buenos_Aires"))
        fin = inicio + datetime.timedelta(days=15)

        logging.debug(f'buscando turnos entre {inicio} y {fin}')

        turnos = models.ModeloTurnos().obtener_turnos(inicio,fin)

        return Response(turnos)
