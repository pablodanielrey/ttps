from rest_framework import serializers as rest_serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from django.db import models as django_models

from . import models
from . import serializers


class L2e14Restricciones:

    class AgruparEstadosPacienteIterador:
        """
            L2e14 - sirve para realizar la agrupación de los estados reales del estudio a los estados que ve el paciente.
        """
        finalizado = False

        def __init__(self, restricciones, iterador):
            self.restricciones = restricciones
            self.iterador = iterador.__iter__()

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.finalizado:
                raise StopIteration()
            e = self.iterador.__next__()
            if self.restricciones.es_elemento_a_agrupar(e):
                grupo = [e]
                while self.restricciones.es_elemento_a_agrupar(e):
                    grupo.append(e)
                    try:
                        e = self.iterador.__next__()
                    except StopIteration as e:
                        self.finalizado = True
                        return self.restricciones.agrupar_elementos(grupo)
                return self.restricciones.agrupar_elementos(grupo)
            else:
                return e


    clases_a_agrupar = [
        models.EsperandoRetiroDeExtaccion,
        models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
        models.EsperandoProcesamientoDeLoteBiotecnologico,
        models.EsperandoInterpretacionDeResultados,
        models.EsperandoEntregaAMedicoDerivante
    ]

    def es_elemento_a_agrupar(self, e):
        return e.__class__ in self.clases_a_agrupar

    def agrupar_elementos(self, elementos:list):
        return EstadoVirtualL2e14EsperandoResultado(elementos)

    def agrupador(self, iterable):
        return self.AgruparEstadosPacienteIterador(self, iterable)

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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        estados = rep.pop('estados')
        for e in estados:
            rep.update(e)
        rep.pop('id')
        return rep

class SerializadorListaDeEstadosPaciente(rest_serializers.ListSerializer):

    restricciones = L2e14Restricciones()

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, django_models.Manager) else data
        elementos = self.restricciones.agrupador(iterable)
        datos = [
            self.child.to_representation(item) for item in elementos
        ]
        return datos

    
import logging
class SerializadorEstadoEstudioPolimorfico(PolymorphicSerializer):

    restricciones = L2e14Restricciones()

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

    def __eliminar_campos_restringidos(self, datos):
        datos.pop('resultado_url',None)
        datos.pop('extraccionista',None)
        datos.pop('freezer',None)

    def to_representation(self, instance):
        if self.restricciones.es_elemento_a_agrupar(instance):
            instance = self.restricciones.agrupar_elementos([instance])
        rep = super().to_representation(instance)
        self.__eliminar_campos_restringidos(rep)
        return rep

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

