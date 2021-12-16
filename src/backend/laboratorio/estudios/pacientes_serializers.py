from rest_framework import serializers as rest_serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from django.db import models as django_models

from . import models
from . import serializers


class EstadoVirtualL2e14EsperandoResultado:
    
    class Meta:
        object_name: str
        def __init__(self, name):
            self.object_name = name

    _meta = Meta('EstadoVirtualEsperandoResultado')

    def __init__(self, data):
        self.estados = data



class SerializadorL2e14EsperandoResultado(rest_serializers.Serializer):
    estados = serializers.SerializadorEstadoEstudioPolimorfico(many=True)



class SerializadorListaDeEstadosPaciente(rest_serializers.ListSerializer):

    class AgruparEstadosPacienteIterador:
        """
            L2e14 - sirve para realizar la agrupación de los estados reales del estudio a los estados que ve el paciente.
        """

        clases_a_agrupar = [
            models.EsperandoRetiroDeExtaccion,
            models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
            models.EsperandoProcesamientoDeLoteBiotecnologico,
            models.EsperandoInterpretacionDeResultados,
            models.EsperandoEntregaAMedicoDerivante
        ]

        finalizado = False

        def __init__(self, iterador):
            self.iterador = iterador.__iter__()

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.finalizado:
                raise StopIteration()
            e = self.iterador.__next__()
            if e.__class__ in self.clases_a_agrupar:
                grupo = [e]
                while e.__class__ in self.clases_a_agrupar:
                    grupo.append(e)
                    try:
                        e = self.iterador.__next__()
                    except StopIteration as e:
                        self.finalizado = True
                        return EstadoVirtualL2e14EsperandoResultado(grupo)
                return EstadoVirtualL2e14EsperandoResultado(grupo)
            else:
                return e

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, django_models.Manager) else data
        elementos = self.AgruparEstadosPacienteIterador(iterable)
        datos = [
            self.child.to_representation(item) for item in elementos
        ]
        return datos

    

class SerializadorEstadoEstudioPolimorfico(PolymorphicSerializer):
    model_serializer_mapping = {
        models.EstadoEstudio: serializers.SerializadorEstadoEstudio,
        models.EsperandoComprobanteDePago: serializers.SerializadorEsperandoComprobanteDePago,
        models.AnuladorPorFaltaDePago: serializers.SerializadorAnuladorPorFaltaDePago,
        models.EnviarConsentimientoInformado: serializers.SerializadorEnviarConsentimientoInformado,
        models.EsperandoConsentimientoInformado: serializers.SerializadorEsperandoConsentimientoInformado,
        models.EsperandoSeleccionDeTurnoParaExtraccion: serializers.SerializadorEsperandoSeleccionDeTurnoParaExtraccion,
        models.EsperandoTomaDeMuestra: serializers.SerializadorEsperandoTomaDeMuestra,
        EstadoVirtualL2e14EsperandoResultado: SerializadorL2e14EsperandoResultado,
        models.ResultadoDeEstudioEntregado: serializers.SerializadorResultadoDeEstudioEntregado
    }

    class Meta:
        list_serializer_class = SerializadorListaDeEstadosPaciente

    def _to_model(self, model_or_instance):
        if isinstance(model_or_instance, django_models.Model) or isinstance(model_or_instance, EstadoVirtualL2e14EsperandoResultado):
            return model_or_instance.__class__
        return model_or_instance


class SerializadorEstudios(rest_serializers.HyperlinkedModelSerializer):
    paciente = serializers.SerializadorDePersona()
    medico_derivante = serializers.SerializadorDePersona()
    tipo = serializers.SerializadorTiposDeEstudio()
    diagnostico = serializers.SerializadorDiagnostico()
    ultimo_estado = SerializadorEstadoEstudioPolimorfico()
    presupuesto = rest_serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo', 'ultimo_estado', 'presupuesto']
       

class SerializadorEstudiosDetalle(rest_serializers.ModelSerializer):
    paciente = serializers.SerializadorDePersona()
    medico_derivante = serializers.SerializadorDePersona()
    tipo = serializers.SerializadorTiposDeEstudio()
    diagnostico = serializers.SerializadorDiagnostico()
    estados = SerializadorEstadoEstudioPolimorfico(many=True)
    ultimo_estado = SerializadorEstadoEstudioPolimorfico()
    presupuesto = rest_serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = models.Estudio
        fields = ['id', 'fecha_alta', 'diagnostico', 'paciente', 'medico_derivante', 'tipo', 'estados', 'ultimo_estado', 'presupuesto']

