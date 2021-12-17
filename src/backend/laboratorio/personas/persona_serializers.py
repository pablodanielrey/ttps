
from rest_framework import serializers

from . import models

class SerializadorDePersona(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','dni','fecha_nacimiento','telefono','direccion']
