
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action, permission_classes

from . import models
from . import empleados_serializers
from . import permissions


class VistaEmpleado(viewsets.ModelViewSet):
    queryset = models.Empleado.all()
    serializer_class = empleados_serializers.SerializadorDeEmpleado
    permission_classes = [ permissions.EmpleadoPermisos ]

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando empleado : {q}')

        personas = models.Empleado.buscar(q)
        serializer = empleados_serializers.SerializadorDeEmpleado(personas, many=True, context={'request': request})
        return Response(serializer.data)