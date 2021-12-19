

from rest_framework import serializers

from . import models

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Configuracion
        fields = ['id','fecha','modo_operacion']
