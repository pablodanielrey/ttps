import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from turnos import views as turnos_views

from . import models
from personas import paciente_serializers
from personas import medicos_serializers

class SerializadorArchivos(serializers.ModelSerializer):
    content_type = serializers.CharField(required=False, read_only=True)
    encoding = serializers.CharField(required=False, read_only=True)
    contenido = serializers.CharField(required=True, read_only=False)
    class Meta:
        model = models.Archivo
        fields = ['id','content_type','encoding', 'contenido']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['contenido'] = ''
        return data

class SerializadorTiposDeEstudio(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TiposDeEstudio
        fields = ['id','nombre']

class SerializadorTemplateConsentimiento(serializers.ModelSerializer):
    archivo = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = models.TemplateConsentimiento
        fields  = ['id','fecha','archivo','historico']


class SerializadorTiposDeEstudio(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TiposDeEstudio
        fields = ['id','nombre']

class SerializadorDiagnostico(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Diagnostico
        fields = ['id', 'nombre']



"""
    ESTADOS ESTUDIO
"""

from rest_polymorphic.serializers import PolymorphicSerializer


class SerializadorEstadoEstudio(serializers.ModelSerializer):
    class Meta:
        model = models.EstadoEstudio
        fields = ['id','fecha']

class SerializadorEsperandoComprobanteDePago(serializers.ModelSerializer):
    fecha_procesado = serializers.DateTimeField(required=False, read_only=False)
    comprobante = SerializadorArchivos(required=False, read_only=False)
    class Meta:
        model = models.EsperandoComprobanteDePago
        fields = ['id','fecha','comprobante','fecha_procesado']

    def update(self, instance, validated_data):
        estudio = instance.estudio

        fecha_procesado = validated_data.pop('fecha_procesado',None)
        if fecha_procesado:
            """ se anula el comprobante por falta de pago, es necesario pasar el estudio a AnuladoPorFaltaDePago """
            logging.debug('anulando el estudio por falta de pago')    
            estado = models.AnuladorPorFaltaDePago(estudio=estudio, fecha_procesado=fecha_procesado)
            estado.save()
            return estado

        logging.debug('actualizando el estado con el comprobante')
        comprobante = validated_data.get('comprobante')
        archivo = models.Archivo.from_datauri(comprobante['contenido'])
        archivo.save()
        instance.comprobante = archivo
        instance.save()

        logging.debug('pasando al siguiente estado')
        estado = models.EnviarConsentimientoInformado(estudio=estudio)
        estado.save()
        return estado

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
        #fields = ['id','fecha']

class SerializadorEsperandoSeleccionDeTurnoParaExtraccion(serializers.ModelSerializer):
    turno = turnos_views.SerializadorTurnosConfirmados()
    class Meta:
        model = models.EsperandoSeleccionDeTurnoParaExtraccion
        fields = ['id','fecha','turno']



class SerializadorEsperandoTomaDeMuestra(serializers.ModelSerializer):

    turno = turnos_views.SerializadorTurnosConfirmados()

    class Meta:
        model = models.EsperandoTomaDeMuestra
        fields = ['id','fecha','fecha_muestra','mililitros','freezer','expirado','turno']

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
    medico_informante = medicos_serializers.SerializadorDeMedicoInformante()
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



"""
    /////////// ESTUDIO ////////////////77
"""


class SerializadorDePersonaResumido(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido']


class SerializadorEstudiosDetalle(serializers.HyperlinkedModelSerializer):
    paciente = paciente_serializers.SerializadorDePaciente()
    medico_derivante = medicos_serializers.SerializadorDeMedicoDerivante()
    tipo = SerializadorTiposDeEstudio()
    diagnostico = SerializadorDiagnostico()
    estados = SerializadorEstadoEstudioPolimorfico(many=True)
    ultimo_estado = SerializadorEstadoEstudioPolimorfico()
    presupuesto = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo', 'estados', 'ultimo_estado', 'presupuesto']


class SerializadorEstudios(serializers.HyperlinkedModelSerializer):
    paciente = SerializadorDePersonaResumido()
    medico_derivante = SerializadorDePersonaResumido()
    tipo = SerializadorTiposDeEstudio()
    diagnostico = SerializadorDiagnostico()
    # #estados = SerializadorEstadoEstudioPolimorfico(many=True)
    ultimo_estado = SerializadorEstadoEstudioPolimorfico()
    presupuesto = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo','ultimo_estado','presupuesto']

class SerializadorEstudiosRestringido(serializers.ModelSerializer):
    tipo = SerializadorTiposDeEstudio()
    diagnostico = SerializadorDiagnostico()

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo']

