

from rest_framework import serializers

from estudios import models
from estudios import serializers as estudio_serializers

class SerializadorEstudios(serializers.HyperlinkedModelSerializer):
    paciente = estudio_serializers.SerializadorDePersonaResumido()
    tipo = estudio_serializers.SerializadorTiposDeEstudio()
    diagnostico = estudio_serializers.SerializadorDiagnostico()
    ultimo_estado = estudio_serializers.SerializadorEstadoEstudioPolimorfico()

    class Meta:
        model = models.Estudio
        fields = [ 'id', 'fecha_alta', 'diagnostico', 'paciente', 'tipo','ultimo_estado' ]