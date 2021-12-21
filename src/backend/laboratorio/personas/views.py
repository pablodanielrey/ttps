
from django.http.request import HttpRequest
from django.shortcuts import render

from django.contrib.auth import models as auth_models



import logging

from rest_framework.permissions import DjangoModelPermissions

from . import models



"""
    Las vistas de rest framework
"""
from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action, permission_classes

from . import permissions

class SerializadorDeObraSocial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ObraSocial
        fields = ['id','nombre','telefono','email']

class VistaObraSocial(viewsets.ModelViewSet):
    queryset = models.ObraSocial.objects.all()
    serializer_class = SerializadorDeObraSocial
    permission_classes = [ permissions.ObraSocialPermisos ]
    # permission_classes = [ DjangoModelPermissions ]

    @action(detail=False, methods=['GET'])
    def p(self, request):
        usuario = request.user
        r = usuario.has_perm('personas.view_obrasocial')
        return Response(r)


