from django.db import models

from estudios import models

class Liquidaciones:

    def __init__(self):
        self.estados_invalidos = [
            models.EsperandoComprobanteDePago,
            models.AnuladorPorFaltaDePago,
            models.EnviarConsentimientoInformado,
            models.EsperandoConsentimientoInformado,
            models.EsperandoSeleccionDeTurnoParaExtraccion
        ]

    def obtener_estudios_a_liquidar(self):
        estudios = models.Estudio.objects.all()
        estudios_filtrados = (e for e in estudios if e.ultimo_estado.__class__ not in self.estados_invalidos)
        return estudios_filtrados

    def liquidar_estudios(self, estudios):
        pass