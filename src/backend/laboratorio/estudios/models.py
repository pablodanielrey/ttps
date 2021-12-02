from django.db import models

import uuid
import datetime
import logging

from django.db.models.fields import related
from django.contrib.contenttypes.models import ContentType

from personas.models import Persona, ObraSocial
from turnos import models as turnos_models



class Archivo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contenido = models.TextField()
    content_type = models.CharField(max_length=500)
    encoding = models.CharField(max_length=500)

    @classmethod
    def from_datauri(cls, content):
        partes = content.split(";")
        content_type = partes[0].replace('data:','')
        encoding_partes = partes[1].split(',')
        encoding = encoding_partes[0]
        contenido = encoding_partes[1]
        return cls(contenido=contenido, encoding=encoding, content_type=content_type)


class TemplateConsentimientoInformado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    models.ForeignKey(Archivo, on_delete=models.CASCADE, null=False)

class Diagnostico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)

    def __str__(self):
        return self.nombre

class TiposDeEstudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)

class Estudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.ForeignKey(TiposDeEstudio, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='estudios')
    medico_derivante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='estudios_derivados')
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='estudios')
    fecha_alta = models.DateField(default=datetime.date.today)
    presupuesto = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=True)

    @property
    def ultimo_estado(self):
        return self.estados.order_by('fecha').last()

    @property
    def comprobante_de_pago(self):
        comprobantes = self.estados.instance_of(EsperandoComprobanteDePago)
        for ecomprobante in comprobantes:
            if ecomprobante.comprobante:
                return ecomprobante.comprobante.contenido
        return None

    @property
    def consentimiento_informado(self):
        consentiminetos = self.estados.instance_of(EsperandoConsentimientoInformado)
        for econsentimiento in consentiminetos:
            if econsentimiento.consentimiento:
                return econsentimiento.consentimiento.contenido
        return None


    @classmethod
    def buscar(cls, termino:str, estado=None):
        estudios = cls.objects
        if termino:
            estudios = estudios.filter(
                models.Q(tipo__nombre__icontains=termino) | 
                models.Q(diagnostico__nombre__icontains=termino) | 
                models.Q(paciente__dni__icontains=termino) |
                models.Q(paciente__nombre__icontains=termino) |
                models.Q(paciente__apellido__icontains=termino)
            )

        if estado:
            #estudios = cls.objects.filter(models.Q(estados__polymorphic_ctype=ContentType.objects.get_for_model(EsperandoComprobanteDePago)))
            poly = ContentType.objects.get(model=estado.lower())
            estudios = cls.objects.filter(models.Q(estados__polymorphic_ctype=poly))
            estudios_filtrados = [e for e in estudios if e.ultimo_estado.polymorphic_ctype.id == poly.id]
            return estudios_filtrados


        #polymorphic_ctype=ContentType.objects.get_for_model(SpecialGroup))
        return estudios


from polymorphic.models import PolymorphicModel

class EstadoEstudio(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='estados')
    fecha = models.DateTimeField(auto_now=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)

# class EsperandoPresupuesto(EstadoEstudio):
#     presupuesto = models.TextField(null=True)   

class EsperandoComprobanteDePago(EstadoEstudio):
    comprobante = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=True)

class AnuladorPorFaltaDePago(EstadoEstudio):
    fecha_procesado = models.DateTimeField(null=True)

class EnviarConsentimientoInformado(EstadoEstudio):
    fecha_enviado = models.DateTimeField(null=True)

class EsperandoConsentimientoInformado(EstadoEstudio):
    consentimiento = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=True)

class EsperandoSeleccionDeTurnoParaExtraccion(EstadoEstudio):
    turno = models.ForeignKey(turnos_models.TurnoConfirmado, on_delete=models.CASCADE, null=True)

class EsperandoTomaDeMuestra(EstadoEstudio):
    fecha_muestra = models.DateTimeField(null=True)
    mililitros = models.FloatField(null=True)
    freezer = models.CharField(max_length=500,null=True)
    expirado = models.BooleanField(default=False)

class EsperandoRetiroDeExtaccion(EstadoEstudio):
    extracionista = models.CharField(max_length=1024, null=True)
    fecha_retiro = models.DateTimeField(null=True)

class EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(EstadoEstudio):
    numero_lote = models.CharField(max_length=500,null=True)

class EsperandoProcesamientoDeLoteBiotecnologico(EstadoEstudio):
    fecha_resultado = models.DateField(null=True)
    resultado_url = models.URLField(null=True)

class EsperandoInterpretacionDeResultados(EstadoEstudio):
    fecha_informe = models.DateField(null=True)
    medico_informante = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    informe = models.TextField(null=True)
    resultado = models.CharField(max_length=500, null=True)
   
class EsperandoEntregaAMedicoDerivante(EstadoEstudio):
    fecha_entrega = models.DateTimeField(null=True)

class ResultadoDeEstudioEntregado(EstadoEstudio):
    pass

"""
class PresupuestoEstudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estado = models.ForeignKey(EstadoEstudio, on_delete=models.CASCADE)
    presupuesto = models.FloatField()

class EsperandoPresupuesto:

    def __init__(self, estudio, data):
        self.estudio = estudio
        self.presupuesto = data['presupuesto']

    def save(self):
        ee = EstadoEstudio(estudio=self.estudio, nombre=self.__class__.__name__)
        ee.save()
        pe = PresupuestoEstudio(estado=ee, presupuesto=self.presupuesto)
        pe.save()



import json
import datetime
class EstadosEstudio:

    def __init__(self):
        self.fecha = datetime.datetime.utcnow()
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class EstadoEsperandoFactura(EstadosEstudio):

    def __init__(self):
        super().__init__(self)
        self.monto = 103.4
        self.obra_social = 'id_de_obra'


"""


"""

class EstadosEstudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estudio = models.ForeignKey(Estudio, on_delete=models.SET_NULL, related_name='estados')
    estado = models.ForeignKey(EstadoEstudio, on_delete=models.SET_NULL)
    fecha = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.SET_NULL)
    

"""

