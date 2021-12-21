
import logging


from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response

from rest_framework.decorators import action, permission_classes

from . import models
from . import paciente_serializers
from . import permissions

class VistaTutores(viewsets.ModelViewSet):
    queryset = models.Tutor.all()
    serializer_class = paciente_serializers.SerializadorDeTutor
    permission_classes = [ permissions.PacientePermisos ]

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Tutor.buscar(q)
        serializer = paciente_serializers.SerializadorDeTutor(personas, many=True, context={'request': request})
        return Response(serializer.data)
