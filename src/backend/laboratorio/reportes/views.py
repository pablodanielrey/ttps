from django.shortcuts import render

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views

from . import models
from . import permissions
class Lve23ReporteCantidadDeEstudiosPorTipo(views.APIView):

    # authentication_classes = [BasicAuthentication]
    permission_classes = [ permissions.ReportePermisos ]

    reportes = models.Reportes()

    def get(self, request, format=None):
        reporte = self.reportes.cantidad_de_estudios_por_tipo()
        return Response(reporte)


class Lve25ReporteCantidadDeEstudiosPorMesAno(views.APIView):

    # authentication_classes = [BasicAuthentication]
    permission_classes = [ permissions.ReportePermisos ]

    reportes = models.Reportes()

    def get(self, request, format=None):
        reporte = self.reportes.cantidad_de_estudios_por_mes()
        return Response(reporte)


class Lve27ReporteDemoraDeEstudios(views.APIView):

    # authentication_classes = [BasicAuthentication]
    permission_classes = [ permissions.ReportePermisos ]

    reportes = models.Reportes()

    def get(self, request, format=None):
        reporte = self.reportes.demora_de_procesamiento_de_estudios()
        return Response(reporte)
