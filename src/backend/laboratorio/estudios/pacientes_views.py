

from rest_framework import viewsets

from . import models
from . import pacientes_serializers

class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = pacientes_serializers.SerializadorEstudios

    custom_serializer_class = {
        'retrieve': pacientes_serializers.SerializadorEstudiosDetalle,
        'list': pacientes_serializers.SerializadorEstudios
    }

    def get_serializer_class(self):
        try:
            return self.custom_serializer_class[self.action]
        except (KeyError, AttributeError) as e:
            return super().get_serializer_class()

 
