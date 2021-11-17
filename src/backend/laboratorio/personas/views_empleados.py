
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models



class SerializadorDeEmpleado(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username')
    clave = serializers.CharField(source='usuario.password')
    class Meta:
        model = models.Empleado
        fields = ['id','nombre','apellido','usuario','clave']

class VistaEmpleado(viewsets.ModelViewSet):
    queryset = models.Configurador.all()
    serializer_class = SerializadorDeEmpleado

    model = models.PersonasModel()

    def create(self, request):
        configurador = self.model.crearEmpleado(**request.data)
        serializador = self.serializer_class(instance=configurador, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando empleado : {q}')

        personas = models.Empleado.buscar(q)
        serializer = SerializadorDeEmpleado(personas, many=True, context={'request': request})
        return Response(serializer.data)