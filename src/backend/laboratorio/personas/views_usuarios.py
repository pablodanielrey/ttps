
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth import models as auth_models

from . import models


class SerializadorDeUsuario(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = auth_models.User
        fields = ['first_name', 'last_name', 'username', 'email']


class VistaUsuario(viewsets.ModelViewSet):
    queryset = auth_models.User.objects.all()
    serializer_class = SerializadorDeUsuario
