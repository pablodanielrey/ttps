from typing import Sequence
from django.db import models

import uuid

from estudios import models as estudio_models

class Lote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    resultado = models.CharField(max_length=1024, null=True)


class EstudioDeLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    estudio = models.ForeignKey(estudio_models.Estudio, on_delete=models.CASCADE, related_name="estudios")







class ModeloLotes:
    def __init__(self):
        pass

    def generar_lote(self):
        def _fecha_de_extraccion(estudio):
            retiro = sorted(estudio.estados.all(), key=lambda e: e.fecha)[-2]
            return retiro.fecha_retiro

        """ obtengo los estudios que se encuentran esperando un lote ordenados por fecha de extracción """
        #estudio_models.Estudio.objects.filter()
        estados_esperando_lote = estudio_models.EstadoEstudio.objects.filter(instance_of=estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico, EsperandoLoteDeMuestraParaProcesamientoBiotecnologico___numero_lote__isnull=True)
        estudios_esperando_lote = [e.estudio for e in estados_esperando_lote]
        estudios_ordenados = sorted(estudios_esperando_lote, key=_fecha_de_extraccion)
        return estudios_ordenados[0:9]


    def _generar_datos_de_prueba(self):

        import datetime
        from zoneinfo import ZoneInfo
        
        def generar_fecha_now():
            return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))


        from personas import models as persona_models

        empleado = persona_models.Persona.objects.all().first()

        tipoe = estudio_models.TiposDeEstudio.objects.all().first()
        diagnostico = estudio_models.Diagnostico.objects.all().first()

        for _ in range(0,20):
            estudio = estudio_models.Estudio(paciente=empleado,  tipo=tipoe, medico_derivante=empleado, diagnostico=diagnostico)
            estudio.save()

            estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
            estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()
