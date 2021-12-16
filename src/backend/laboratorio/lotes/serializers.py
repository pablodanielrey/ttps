
from rest_framework import serializers

from estudios import serializers as estudio_serializers
from . import models

class SerializadorDeEstudioDeLote(serializers.ModelSerializer):
    estudio = estudio_serializers.SerializadorEstudios()
    class Meta:
        model = models.EstudioDeLote
        fields = ['id', 'estudio']

class SerializadorDeLote(serializers.ModelSerializer):
    estudios = SerializadorDeEstudioDeLote(many=True)
    class Meta:
        model = models.Lote
        fields = ['id', 'fecha', 'resultado','estudios']
