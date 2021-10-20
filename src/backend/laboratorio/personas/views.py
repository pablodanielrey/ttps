
from django.http.request import HttpRequest
from django.shortcuts import render

from django.contrib.auth import models as auth_models
from . import models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets

class SerializadorDeUsuario(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ['first_name', 'last_name', 'username', 'email']
class SerializadorDePersona(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Persona
        fields = ['nombre','apellido','email','dni','fecha_nacimiento','telefono','historia_clinica']


class VistaUsuario(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = SerializadorDeUsuario

class VistaPersona(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = SerializadorDePersona
