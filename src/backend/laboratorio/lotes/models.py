from django.db import models

import uuid

from estudios.models import Estudio

class Lote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    resultado = models.CharField(max_length=1024, null=True)


class EstudioDeLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, related_name="estudios")



class ModeloLotes:
    def __init__(self):
        pass

    def generar_lote(self):
        """ obtengo los estudios que se encuentran esperando un lote ordenados por fecha de extracción """
        Estudio.objects.filter()