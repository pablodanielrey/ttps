import uuid
from django.db import models
from django.utils.timezone import now

from estudios import models as estudio_models


class Liquidacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    estudio = models.OneToOneField(estudio_models.Estudio, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=now)

class Liquidaciones:

    def __init__(self):
        self.estados_invalidos = [
            estudio_models.EsperandoComprobanteDePago,
            estudio_models.AnuladorPorFaltaDePago,
            estudio_models.EnviarConsentimientoInformado,
            estudio_models.EsperandoConsentimientoInformado,
            estudio_models.EsperandoSeleccionDeTurnoParaExtraccion
        ]

    def obtener_estudios_a_liquidar(self):
        liquidados = Liquidacion.objects.only('estudio').all()
        estudios = estudio_models.Estudio.objects.exclude(id__in=liquidados).all()
        estudios_filtrados = (e for e in estudios if e.ultimo_estado.__class__ not in self.estados_invalidos)
        return estudios_filtrados

    def obtener_estudios_liquidados(self):
        liquidaciones = Liquidacion.objects.value('estudio').all()
        return liquidaciones

    def liquidar_estudios(self, estudios):
        resumen = {
            'liquidados': 0
        }
        return resumen