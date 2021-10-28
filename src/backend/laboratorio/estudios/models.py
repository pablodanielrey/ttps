from django.db import models

import uuid
import datetime

from django.db.models.fields import related

from personas.models import Persona, ObraSocial

class Diagnostico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)

class TiposDeEstudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)
    consentimiento = models.CharField(max_length=9216, null=True)

class Estudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.ForeignKey(TiposDeEstudio, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='estudios')
    medico_derivante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='estudios_derivados')
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='estudios')
    fecha_alta = models.DateField(default=datetime.date.today)




from polymorphic.models import PolymorphicModel

class EstadoEstudio(PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name='estados')
    fecha = models.DateTimeField(auto_now=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)

class EsperandoPresupuesto(EstadoEstudio):
    presupuesto = models.FloatField()


class EsperandoFactura(EstadoEstudio):
    fecha_factura = models.DateField(auto_now=True)
    numero = models.CharField(max_length=255)
    monto = models.FloatField()
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE, null=True)

class EsperandoComprobanteDePago(EstadoEstudio):
    comprobante = models.TextField(null=True)

class AnuladorPorFaltaDePago(EstadoEstudio):
    fecha_procesado = models.DateTimeField(auto_now=True)

class EsperandoConsentimientoInformado(EstadoEstudio):
    consentimiento = models.TextField(null=True)

class EsperandoSeleccionDeTurnoParaExtraccion(EstadoEstudio):
    turno = models.DateTimeField(null=True)

class EsperandoTomaDeMuestra(EstadoEstudio):
    fecha_muestra = models.DateTimeField(null=True)
    mililitros = models.IntegerField(null=True)
    freezer = models.CharField(max_length=500,null=True)
    expirado = models.BooleanField(default=False)

class EsperandoRetiroDeExtaccion(EstadoEstudio):
    extracionista = models.CharField(max_length=1024, null=True)
    fecha_retiro = models.DateTimeField(null=True)

class EsperandoLotaDeMuestraParaProcesamientoBiotecnologico(EstadoEstudio):
    numero_lote = models.CharField(max_length=500, null=True)

class EsperandoInterpretacionDeResultados(EstadoEstudio):
    resultado_url = models.URLField()
    fecha_informe = models.DateField()
    medico_informante = models.ForeignKey(Persona, on_delete=models.CASCADE)
    informe = models.TextField()
   

class EsperandoEntregaAMedicoDerivante(EstadoEstudio):
    fecha_entrega = models.DateTimeField(null=True)



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

"""
    SELECCION DE TURNOS
"""


class ParametroDeTurnos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_valido = models.DateTimeField(auto_now=True)
    frecuencia = models.IntegerField(default=15)

class RangoDeTurnos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parametros = models.ForeignKey(ParametroDeTurnos, on_delete=models.CASCADE, related_name='rangos')
    hora_inicio = models.IntegerField(default=9)
    hora_fin = models.IntegerField(default=13)

class ModeloTurnos:

    def obtener_turnos(desde:datetime.datetime, hasta:datetime.datetime):
        """ 
            genera los turnos entre las fechas determinadas, a partir de los parámetros definidos dentro de la base.
        """
        