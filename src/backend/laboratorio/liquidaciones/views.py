from django.shortcuts import render

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views

from estudios import serializers

from . import models
from . import serializers



class Lve19LiquidacionesDeEstudios(views.APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    liquidaciones = models.Liquidaciones()

    def get(self, request, format=None):
        estudios = self.liquidaciones.obtener_estudios_a_liquidar()
        serializador = serializers.SerializadorEstudios(instance=estudios, many=True, context={'request':request})
        return Response(serializador.data)

    def post(self, request, format=None):
        estudio_ids = request.data.get('estudios')
        resumen = self.liquidaciones.liquidar_estudios(estudio_ids)
        return Response(resumen)

    @action(methods=['get'], detail=False)
    def liquidados(self, request):
        estudios = self.liquidaciones.obtener_estudios_liquidados()
        return estudios