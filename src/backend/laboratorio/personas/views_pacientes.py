
import logging


from rest_framework import serializers, viewsets, views, mixins
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser, AllowAny
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import paciente_serializers

class VistaPaciente(viewsets.ModelViewSet):
    queryset = models.Paciente.all()
    serializer_class = paciente_serializers.SerializadorDePaciente

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Paciente.buscar(q)
        serializer = paciente_serializers.SerializadorDePaciente(personas, many=True, context={'request': request})
        return Response(serializer.data)        

class VistaRegistro(viewsets.ModelViewSet):
    queryset = models.Paciente.all()
    serializer_class = paciente_serializers.SerializadorDePaciente
    http_method_names = ['post']
    permission_classes = [ AllowAny ]