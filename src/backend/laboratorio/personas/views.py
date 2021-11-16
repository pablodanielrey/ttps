
from django.http.request import HttpRequest
from django.shortcuts import render

from django.contrib.auth import models as auth_models



import logging

from . import models



"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action


class SerializadorDeObraSocial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ObraSocial
        fields = ['id','nombre','telefono','email']

class SerializadorDeUsuario(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ['first_name', 'last_name', 'username', 'email']

class SerializadorDeObraSocialPersona(serializers.HyperlinkedModelSerializer):
    # obra_social = SerializadorDeObraSocial()
    class Meta:
        model = models.ObraSocialPersona
        fields = ['obra_social','numero_afiliado']
        
class SerializadorDeHistoriaClinica(serializers.ModelSerializer):
    class Meta:
        model = models.HistoriaClinica
        fields = ['historia_clinica']

class SerializadorDePersona(serializers.HyperlinkedModelSerializer):
    obra_social = SerializadorDeObraSocialPersona(required=False, many=True)
    historia_clinica = SerializadorDeHistoriaClinica(required=False)
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','dni','fecha_nacimiento','telefono','historia_clinica','obra_social']


class VistaUsuario(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = SerializadorDeUsuario


class VistaPersona(viewsets.ModelViewSet):
    """
        esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Persona.objects.all()
    serializer_class = SerializadorDePersona

    def create(self, request, *args, **kwargs):
        datos_persona = request.data

        logging.debug(datos_persona)

        persona = models.Persona(           
            nombre=datos_persona['nombre'],
            apellido=datos_persona['apellido'],
            dni=datos_persona['dni'],
            email=datos_persona['email'],
            fecha_nacimiento=datos_persona['fecha_nacimiento'],
            telefono=datos_persona['telefono'],
            historia_clinica=datos_persona['historia_clinica']
        )
        persona.save()

        if 'obra_social' in datos_persona:
            ob = datos_persona['obra_social']
            obraSocial = models.ObraSocial.objects.get(id=ob)

            pacienteObraSocial = models.ObraSocialPersona(
                persona=persona,
                obra_social=obraSocial,
                numero_afiliado=datos_persona['numero_afiliado']
            )
            pacienteObraSocial.save()

        serializer = SerializadorDePersona(persona, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Persona.buscar(q)
        serializer = SerializadorDePersona(personas, many=True, context={'request': request})
        return Response(serializer.data)
        
class VistaObraSocialPersona(viewsets.ModelViewSet):
    queryset = models.ObraSocialPersona.objects.all()
    serializer_class = SerializadorDeObraSocialPersona

class VistaObraSocial(viewsets.ModelViewSet):
    queryset = models.ObraSocial.objects.all()
    serializer_class = SerializadorDeObraSocial



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


class VistaMedicoDerivante(views.APIView):

    model = models.PersonasModel()

    def post(self, request):
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        email = request.data['email']
        medico = self.model.crearMedicoDerivante(nombre=nombre, apellido=apellido, email=email)

        serializador = SerializadorDeMedicoDerivante(instance=medico, context={'request':request})
        return Response(serializador.data)


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
