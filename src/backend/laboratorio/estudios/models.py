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
    presupuesto = models.TextField(null=True)

class EsperandoFactura(EstadoEstudio):
    factura = models.TextField(null=True)
    """
    fecha_factura = models.DateField(auto_now=True)
    numero = models.CharField(max_length=255)
    monto = models.FloatField()
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE, null=True)
    """

class EsperandoComprobanteDePago(EstadoEstudio):
    comprobante = models.TextField(null=True)

class AnuladorPorFaltaDePago(EstadoEstudio):
    fecha_procesado = models.DateTimeField(null=True)

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
    fecha_valido = models.DateTimeField()
    frecuencia = models.IntegerField(default=15)

class RangoDeTurnos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parametros = models.ForeignKey(ParametroDeTurnos, on_delete=models.CASCADE, related_name='rangos')
    hora_inicio = models.IntegerField(default=9)
    hora_fin = models.IntegerField(default=13)

class FechasSinTurno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()


class ModeloTurnos:

    def obtener_turnos_hoy(self):
        hoy = datetime.datetime.combine(datetime.date.today(), datetime.time(0))
        manana = datetime.timedelta(hours = 24) + hoy
        return self.obtener_turnos(hoy,manana)

    def obtener_turnos(self, desde:datetime.datetime, hasta:datetime.datetime):
        """ 
            genera los turnos entre las fechas determinadas, a partir de los parámetros definidos dentro de la base.
        """
        turnos = []

        """ selecciono la fecha/hora inicial de todo el rango de turnos """
        inicio = ParametroDeTurnos.objects.filter(fecha_valido__lte=desde).order_by('fecha_valido').last()
        if not inicio:
            inicio = ParametroDeTurnos.objects.order_by('fecha_valido').first()
        fecha_inicial = inicio.fecha_valido
        fecha_turnos_desde = fecha_inicial if fecha_inicial > desde else desde

        fechas_sin_turnos = [f.fecha for f in FechasSinTurno.objects.all()]

        turno_actual = hasta
        un_dia = datetime.timedelta(days=1)

        """ obtengo todos los parámetros definidos entre las fechas que me interesa obtener los turnos """
        parametros = ParametroDeTurnos.objects.filter(fecha_valido__gte=fecha_inicial, fecha_valido__lte=hasta).order_by('-fecha_valido').all()
        for parametro in parametros:
            frecuencia = datetime.timedelta(minutes=parametro.frecuencia)
            rangos:RangoDeTurnos = parametro.rangos.order_by('hora_inicio').all()
            a_partir_de = parametro.fecha_valido

            """ genero las fechas para el rango dado """
            while fecha_turnos_desde <= turno_actual and a_partir_de <= turno_actual:
                fecha_de_turno = turno_actual.date()
                if fecha_de_turno in fechas_sin_turnos:
                    turno_actual -= un_dia
                    continue
                if fecha_de_turno.weekday() >= 5:
                    """ 
                        asumo que los días laborables son de lunes-viernes
                        0 - lunes ..... 6 - domingo
                    """
                    turno_actual -= un_dia
                    continue
                turnos_del_dia = self._generar_turnos_para_dia(turno_actual, frecuencia, rangos)
                turnos.extend(turnos_del_dia)
                turno_actual -= un_dia

        return turnos

    def _generar_turnos_para_dia(self, fecha, frecuencia, rangos):
        turnos = []
        for rango in rangos:
            hora_de_turno = fecha.replace(hour=rango.hora_inicio, minute=0, second=0, microsecond=0)
            hora_de_fin = fecha.replace(hour=rango.hora_fin, minute=0, second=0, microsecond=0)
            nuevo_turno = hora_de_turno + frecuencia
            while nuevo_turno <= hora_de_fin:
                turnos.append(self._formatear_turno(hora_de_turno, nuevo_turno))
                hora_de_turno = nuevo_turno
                nuevo_turno += frecuencia
        return turnos

    def _formatear_turno(self, hora_turno, fin_turno):
        return {
            'inicio': hora_turno,
            'fin': fin_turno
        }



    def _completar_datos_turnos(self, turnos):
        return [{
            'hora':hora_de_turno,
            'fecha':hora_de_turno.date(),
            'día':self._dia_de_la_semana(hora_de_turno.date())
        } for hora_de_turno in turnos]

    def _dia_de_la_semana(self, fecha):
        dia = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return dia[fecha.weekday()]

    """
    zdesde = desde.replace(minute=0,second=0,microsecond=0)
    zhasta = hasta.replace(minute=0,second=0,microsecond=0)

    ddia = datetime.timedelta(days=1)
    fecha_turno = zhasta
    turnos = []
    for parametro in parametros:
        fecha_valido = parametro.fecha_valido
        while fecha_turno >= fecha_valido:
            freq = datetime.timedelta(minutes=parametro.frecuencia)
            rangos = parametro.rangos.order_by('hora_inicio').all()
            for rango in rangos:

                hora_turno = fecha_turno.replace(hour=rango.hora_inicio, minute=0, second=0, microsecond=0)
                hora_fin_rango = fecha_turno.replace(hour=rango.hora_fin, minute=0, second=0, microsecond=0)
                
                duracion_turno = hora_turno + freq
                while duracion_turno <= hora_fin_rango:
                    if duracion_turno <= zdesde:
                        return turnos
                    turnos.append(hora_turno)
                    hora_turno = duracion_turno
                    duracion_turno += freq
            fecha_turno = fecha_turno - ddia
                    
    return turnos
    """