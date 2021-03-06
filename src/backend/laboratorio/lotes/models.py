
from django.db import models


import uuid
import turnos
from turnos.models import ParametroDeTurnos

from estudios import models as estudio_models

class Lote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    resultado = models.CharField(max_length=1024, null=True)
    numero_lote = models.IntegerField(primary_key=False, default=0)

    @classmethod
    def all_pending(cls):
        return cls.objects.filter(resultado__isnull=True)

class EstudioDeLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE,  related_name="estudios")
    estudio = models.ForeignKey(estudio_models.Estudio, on_delete=models.CASCADE)


import logging

import datetime
from zoneinfo import ZoneInfo



def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))



class ModeloLotes:

    def obtener_estudios_para_lote(self):
        def _fecha_de_extraccion(estudio):
            estados_ordenados = sorted(estudio.estados.all(), key=lambda e: e.fecha)
            retiros = [e for e in estados_ordenados if isinstance(e, estudio_models.EsperandoRetiroDeExtaccion)]
            ultimo_retiro = retiros[-1]
            return ultimo_retiro.fecha_retiro

        """ obtengo los estudios que se encuentran esperando un lote ordenados por fecha de extracción """
        #estudio_models.Estudio.objects.filter()
        estados_esperando_lote = estudio_models.EstadoEstudio.objects.filter(instance_of=estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico, EsperandoLoteDeMuestraParaProcesamientoBiotecnologico___numero_lote__isnull=True)
        estudios_esperando_lote = [e.estudio for e in estados_esperando_lote]
        estudios_ordenados = sorted(estudios_esperando_lote, key=_fecha_de_extraccion)
        return estudios_ordenados[0:10]


    def generar_lote(self, estudios_ids):
        logging.debug(estudios_ids)
        if len(estudios_ids) != 10:
            raise Exception()

        cantidad = Lote.objects.all().count() + 1
        lote = Lote(fecha=generar_fecha_now().date(), numero_lote=cantidad)
        lote.save()

        for eid in estudios_ids:
            estudio = estudio_models.Estudio.objects.get(id=eid)
            
            """ actualizo el ultimo estado """
            ultimo_estado = estudio.ultimo_estado
            ultimo_estado.numero_lote = str(lote.numero_lote)
            ultimo_estado.save()

            """ cambio de estado el estudio """
            estudio_models.EsperandoProcesamientoDeLoteBiotecnologico(estudio=estudio).save()
            EstudioDeLote(lote=lote, estudio=estudio).save()

        return lote


    def cerrar_lote(self, lote, fecha, resultado):
        lote.resultado = resultado
        lote.fecha = fecha
        lote.save()
        self._actualizar_estudios_con_resultado(lote)

    def _actualizar_estudios_con_resultado(self, lote):
        for estudio_de_lote in lote.estudios.all():
            estudio = estudio_de_lote.estudio
            ultimo_estado = estudio.ultimo_estado
            ultimo_estado.fecha_resultado = lote.fecha
            ultimo_estado.resultado_url = lote.resultado
            ultimo_estado.save()
            estudio_models.EsperandoInterpretacionDeResultados(estudio=estudio).save()
