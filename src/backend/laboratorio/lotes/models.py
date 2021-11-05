from django.db import models

import uuid

from estudios.models import Estudio

class Lote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    resultado = models.CharField(max_length=1024)


class EstudioDeLote(models.Model):
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)
