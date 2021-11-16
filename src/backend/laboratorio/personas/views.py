
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

class VistaObraSocial(viewsets.ModelViewSet):
    queryset = models.ObraSocial.objects.all()
    serializer_class = SerializadorDeObraSocial


