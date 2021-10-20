
from django.http.request import HttpRequest
from django.shortcuts import render

from django.contrib.auth import models as auth_models

from rest_framework.response import Response

import logging

from . import models



"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets

class SerializadorDeObraSocial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ObraSocial
        fields = ['nombre','telefono','email']

class SerializadorDeUsuario(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ['first_name', 'last_name', 'username', 'email']

class SerializadorDeObraSocialPersona(serializers.HyperlinkedModelSerializer):
    # obra_social = SerializadorDeObraSocial()
    class Meta:
        model = models.ObraSocialPersona
        fields = ['obra_social','numero_afiliado']
class SerializadorDePersona(serializers.HyperlinkedModelSerializer):
    obra_social = SerializadorDeObraSocialPersona(required=False, many=True)
    class Meta:
        model = models.Persona
        fields = ['nombre','apellido','email','dni','fecha_nacimiento','telefono','historia_clinica','obra_social']


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
            obraSocial = models.ObraSocial.objects.get(nombre=ob)

            pacienteObraSocial = models.ObraSocialPersona(
                persona=persona,
                obra_social=obraSocial,
                numero_afiliado=datos_persona['numero_afiliado']
            )
            pacienteObraSocial.save()

        serializer = SerializadorDePersona(persona, context={'request': request})
        return Response(serializer.data)
        
class VistaObraSocialPersona(viewsets.ModelViewSet):
    queryset = models.ObraSocialPersona.objects.all()
    serializer_class = SerializadorDeObraSocialPersona

class VistaObraSocial(viewsets.ModelViewSet):
    queryset = models.ObraSocial.objects.all()
    serializer_class = SerializadorDeObraSocial