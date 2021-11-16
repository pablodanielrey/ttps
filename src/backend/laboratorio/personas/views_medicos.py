
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models

class SerializadorDeMatricula(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = ['numero']

class SerializadorDeMedicoDerivante(serializers.ModelSerializer):
    # matricula = SerializadorDeMatricula()
    matricula = serializers.CharField(source='matricula.numero')
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','matricula']


# class VistaMedicoDerivante(views.APIView):

#     model = models.PersonasModel()

#     def post(self, request):
#         nombre = request.data['nombre']
#         apellido = request.data['apellido']
#         email = request.data['email']
#         medico = self.model.crearMedicoDerivante(nombre=nombre, apellido=apellido, email=email)

#         serializador = SerializadorDeMedicoDerivante(instance=medico, context={'request':request})
#         return Response(serializador.data)


class VistaMedicoDerivante(viewsets.ModelViewSet):
    queryset = models.MedicoDerivante.objects.all()
    serializer_class = SerializadorDeMedicoDerivante

    model = models.PersonasModel()

    def create(self, request):
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        email = request.data['email']
        matricula = request.data['matricula']
        medico = self.model.crearMedicoDerivante(nombre=nombre, apellido=apellido, email=email, matricula=matricula)

        serializador = SerializadorDeMedicoDerivante(instance=medico, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico derivante : {q}')

        personas = models.MedicoDerivante.buscar(q)
        serializer = SerializadorDeMedicoDerivante(personas, many=True, context={'request': request})
        return Response(serializer.data)




class SerializadorDeMedicoInformante(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email']

class VistaMedicoInformante(viewsets.ModelViewSet):
    queryset = models.MedicoInformante.objects.all()
    serializer_class = SerializadorDeMedicoInformante

    model = models.PersonasModel()

    def create(self, request):
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        email = request.data['email']
        medico = self.model.crearMedicoInformante(nombre=nombre, apellido=apellido, email=email)

        serializador = self.serializer_class(instance=medico, context={'request':request})
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando medico informante : {q}')

        personas = models.MedicoInformante.buscar(q)
        serializer = SerializadorDeMedicoInformante(personas, many=True, context={'request': request})
        return Response(serializer.data)