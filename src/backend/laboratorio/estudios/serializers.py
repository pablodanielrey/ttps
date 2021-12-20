import logging
from dateutil import parser

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from turnos import views as turnos_views

from . import models
from turnos import models as turnos_models
from personas import models as personas_models
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


from admin_laboratorio import models as admin_models
class SerializadorEsperandoComprobanteDePago(serializers.ModelSerializer):
    fecha_procesado = serializers.DateTimeField(required=False, read_only=False)
    comprobante = SerializadorArchivos(required=False, read_only=False)
    class Meta:
        model = models.EsperandoComprobanteDePago
        fields = ['id','fecha','comprobante','fecha_procesado']



    def update(self, instance, validated_data):
        config = admin_models.Configuracion.objects.order_by('fecha').last()
        config.verificar_modo_de_operacion(self)

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

    def update(self, instance, validated_data):
        return instance

class SerializadorEnviarConsentimientoInformado(serializers.ModelSerializer):
    comprobante_invalido: serializers.BooleanField(required=False, read_only=False)
    class Meta:
        model = models.EnviarConsentimientoInformado
        fields = ['id','fecha','fecha_enviado']

    def update(self, instance, validated_data):

        usuario_logueado = self.context.get('request').user
        logging.debug(f'verificando si {usuario_logueado.username} es Empleado')
        if not personas_models.Empleado.usuario_es_tipo(usuario_logueado):
            raise login_models.PermisosAPIException("No tiene permisos para realizar esta acción")


        comporbante_invalido = validated_data.get('comprobante_invalido',False)
        if comporbante_invalido:
            """
                Todo pasar el estsado a esperando comprobante.
            """
            pass

        super().update(instance, validated_data)

        estudio = instance.estudio
        estado = models.EsperandoConsentimientoInformado(estudio=estudio)
        estado.save()
        return estado

class SerializadorEsperandoConsentimientoInformado(serializers.ModelSerializer):
    consentimiento = SerializadorArchivos(required=False, read_only=False)
    class Meta:
        model = models.EsperandoConsentimientoInformado
        fields = ['id','fecha','consentimiento']

    def update(self, instance, validated_data):
        config = admin_models.Configuracion.objects.order_by('fecha').last()
        config.verificar_modo_de_operacion(self)

        estudio = instance.estudio

        logging.debug('actualizando el documento de consentimiento')
        comprobante = validated_data.get('consentimiento')
        archivo = models.Archivo.from_datauri(comprobante['contenido'])
        archivo.save()
        instance.consentimiento = archivo
        instance.save()

        logging.debug('pasando al siguiente estado')
        estado = models.EsperandoSeleccionDeTurnoParaExtraccion(estudio=estudio)
        estado.save()
        return estado

class SerializadorEsperandoSeleccionDeTurnoParaExtraccion(serializers.ModelSerializer):
    turno = turnos_views.SerializadorTurnosConfirmados()
    class Meta:
        model = models.EsperandoSeleccionDeTurnoParaExtraccion
        fields = ['id','fecha','turno']

    def update(self, instance, validated_data):
        config = admin_models.Configuracion.objects.order_by('fecha').last()
        config.verificar_modo_de_operacion(self)

        estudio = instance.estudio

        turno = validated_data.get('turno')
        logging.debug(f'generando turno {turno}')
        paciente = personas_models.Persona.objects.get(id=estudio.paciente.id)
        # inicio = parser.parse(turno['inicio'])
        # fin = parser.parse(turno['fin'])
        inicio = turno['inicio']
        fin = turno['fin']
        turno = turnos_models.TurnoConfirmado(persona=paciente,inicio=inicio, fin=fin)
        turno.save()
        instance.turno = turno
        instance.save()

        estado = models.EsperandoTomaDeMuestra(estudio=estudio)
        estado.save()
        return estado

class SerializadorEsperandoTomaDeMuestra(serializers.ModelSerializer):

    turno = turnos_views.SerializadorTurnosConfirmados(required=False, read_only=True)
    expirado = serializers.BooleanField(required=False, read_only=False)

    class Meta:
        model = models.EsperandoTomaDeMuestra
        fields = ['id','fecha','fecha_muestra','mililitros','freezer','expirado','turno']

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

        estudio = instance.estudio
        expirado = validated_data.get('expirado',False)
        if expirado:
            """ vuelve a seleccionar un turno para extracción """
            estado = models.EsperandoSeleccionDeTurnoParaExtraccion(estudio=estudio)
        else:
            estado = models.EsperandoRetiroDeExtaccion(estudio=estudio)
        estado.save()
        return estado
        

class SerializadorEsperandoRetiroDeExtaccion(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoRetiroDeExtaccion
        fields = ['id','fecha','extracionista','fecha_retiro']

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        estudio = instance.estudio
        estado = models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio)
        estado.save()
        return estado

class SerializadorEsperandoLoteDeMuestraParaProcesamientoBiotecnologico(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico
        fields = ['id','fecha','numero_lote']

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        estudio = instance.estudio
        estado = models.EsperandoProcesamientoDeLoteBiotecnologico(estudio=estudio)
        estado.save()
        return estado

class SerializadorEsperandoProcesamientoDeLoteBiotecnologico(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoProcesamientoDeLoteBiotecnologico
        fields = ['id','fecha','resultado_url','fecha_resultado']

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        estudio = instance.estudio
        estado = models.EsperandoInterpretacionDeResultados(estudio=estudio)
        estado.save()
        return estado

from login import models as login_models
class SerializadorEsperandoInterpretacionDeResultados(serializers.ModelSerializer):
    medico_informante = medicos_serializers.SerializadorDeMedicoInformante(required=False, read_only=True)
    resultado_url = serializers.CharField(required=False, read_only=True)
    class Meta:
        model = models.EsperandoInterpretacionDeResultados
        fields = ['id','fecha','fecha_informe','medico_informante','informe','resultado','resultado_url']

    def update(self, instance, validated_data):

        usuario_django = self.context.get('request').user
        if not personas_models.MedicoInformante.usuario_es_tipo(usuario_django):
            raise ValidationError({'medico_informante':'la persona logueada no es un médico informante'})

        persona_logueada = login_models.LoginModel().obtener_persona_del_usuario(usuario_django)
            
        """ reemplazo el medico_informante """
        validated_data.pop('medico_informante',None)
        validated_data['medico_informante'] = persona_logueada

        super().update(instance, validated_data)
        estudio = instance.estudio
        estado = models.EsperandoEntregaAMedicoDerivante(estudio=estudio)
        estado.save()
        return estado
        

class SerializadorEsperandoEntregaAMedicoDerivante(serializers.ModelSerializer):
    class Meta:
        model = models.EsperandoEntregaAMedicoDerivante
        fields = ['id','fecha','fecha_entrega']

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        estudio = instance.estudio
        estado = models.ResultadoDeEstudioEntregado(estudio=estudio)
        estado.save()
        return estado


class SerializadorResultadoDeEstudioEntregado(serializers.ModelSerializer):
    class Meta:
        model = models.ResultadoDeEstudioEntregado
        fields = ['id','fecha']

    def update(self, instance, validated_data):
        return instance

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


class SerializadorEstudiosMinimo(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=False)
    paciente = SerializadorDePersonaResumido(required=False)
    medico_derivante = SerializadorDePersonaResumido(required=False)
    tipo = SerializadorTiposDeEstudio(required=False)
    diagnostico = SerializadorDiagnostico(required=False)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo']

