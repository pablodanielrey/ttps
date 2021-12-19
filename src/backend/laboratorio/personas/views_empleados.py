
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import empleados_serializers



# class SerializadorDeEmpleado(serializers.ModelSerializer):
#     usuario = serializers.CharField(source='usuario.username', read_only=True)
#     clave = serializers.CharField(source='usuario.password', read_only=True)
#     class Meta:
#         model = models.Empleado
#         fields = ['id','nombre','apellido','usuario','clave']

class VistaEmpleado(viewsets.ModelViewSet):
    queryset = models.Empleado.all()
    serializer_class = empleados_serializers.SerializadorDeEmpleado

    # def create(self, request):
    #     serializador = self.serializer_class(data=request.data)
    #     serializador.is_valid()
    #     serializador.save()
    #     # configurador = self.model.crearEmpleado(**request.data)
    #     # serializador = self.serializer_class(instance=configurador, context={'request':request})
    #     return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando empleado : {q}')

        personas = models.Empleado.buscar(q)
        serializer = empleados_serializers.SerializadorDeEmpleado(personas, many=True, context={'request': request})
        return Response(serializer.data)