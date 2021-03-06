from django.db import models

import uuid
import datetime
import logging


from django.utils.timezone import now
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


class TemplateConsentimiento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now=True)
    archivo = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=False)
    historico = models.BooleanField(default=False)

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
    presupuesto = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=False)

    @property
    def ultimo_estado(self):
        return self.estados.order_by('fecha').last()

    @property
    def comprobante_de_pago(self):
        comprobantes = self.estados.instance_of(EsperandoComprobanteDePago)
        for ecomprobante in comprobantes:
            if ecomprobante.comprobante:
                return ecomprobante.comprobante
        return None

    @property
    def consentimiento_informado(self):
        consentiminetos = self.estados.instance_of(EsperandoConsentimientoInformado)
        for econsentimiento in consentiminetos:
            if econsentimiento.consentimiento:
                return econsentimiento.consentimiento
        return None

    @property
    def informe_resultado(self):
        resultados = self.estados.instance_of(EsperandoInterpretacionDeResultados)
        for resultado in resultados:
            if resultado.informe:
                return resultado.informe
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
    # fecha = models.DateTimeField(auto_now=True)
    fecha = models.DateTimeField(default=now)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)

# class EsperandoPresupuesto(EstadoEstudio):
#     presupuesto = models.TextField(null=True)   

class EsperandoComprobanteDePago(EstadoEstudio):
    comprobante = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=True)

class AnuladorPorFaltaDePago(EstadoEstudio):
    fecha_procesado = models.DateTimeField(null=True)

class EnviarConsentimientoInformado(EstadoEstudio):
    fecha_enviado = models.DateTimeField(null=True)
    comprobante_invalido = models.BooleanField(null=True)

class EsperandoConsentimientoInformado(EstadoEstudio):
    consentimiento = models.ForeignKey(Archivo, on_delete=models.CASCADE, null=True)

class EsperandoSeleccionDeTurnoParaExtraccion(EstadoEstudio):
    turno = models.ForeignKey(turnos_models.TurnoConfirmado, on_delete=models.CASCADE, null=True)



class EsperandoTomaDeMuestra(EstadoEstudio):
    fecha_muestra = models.DateTimeField(null=True)
    mililitros = models.FloatField(null=True)
    freezer = models.CharField(max_length=500,null=True)
    expirado = models.BooleanField(default=False)

    @property
    def turno(self):
        for estado in self.estudio.estados.order_by('-fecha'):
            if isinstance(estado, EsperandoSeleccionDeTurnoParaExtraccion):
                return estado.turno
        return None

    def cancelar_turno(self):
        estudio = self.estudio
        if self == estudio.ultimo_estado:
            nuevo_turno = EsperandoSeleccionDeTurnoParaExtraccion.objects.create(estudio=estudio)
            nuevo_turno.save()
            return nuevo_turno
        return None

    @classmethod
    def turno_cancelado(cls, turno):
        turnos = EsperandoSeleccionDeTurnoParaExtraccion.objects.filter(turno=turno).all()
        for estado in turnos:
            ultimo_estado = estado.estudio.ultimo_estado
            if isinstance(ultimo_estado, cls):
                nuevo_estado = ultimo_estado.cancelar_turno()
                if nuevo_estado:
                    return nuevo_estado
        return None

    

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
   
    @property
    def resultado_url(self):
        for estado in self.estudio.estados.order_by('-fecha'):
            if isinstance(estado, EsperandoProcesamientoDeLoteBiotecnologico):
                return estado.resultado_url
        return None

class EsperandoEntregaAMedicoDerivante(EstadoEstudio):
    fecha_entrega = models.DateTimeField(null=True)

class ResultadoDeEstudioEntregado(EstadoEstudio):
    pass
