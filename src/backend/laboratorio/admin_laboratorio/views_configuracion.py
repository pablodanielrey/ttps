from rest_framework import serializers, views, viewsets
from rest_framework.response import Response

from . import serializers
from . import models
from . import permissions

class VistaConfiguracion(viewsets.ModelViewSet):
    queryset = models.Configuracion.objects.all()
    serializer_class = serializers.ConfiguracionSerializer
    permission_classes = [ permissions.ConfiguracionPermisos ]

