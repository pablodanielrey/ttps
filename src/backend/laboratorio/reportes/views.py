from django.shortcuts import render

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import views

class Lve23ReporteCantidadDeEstudiosPorTipo(views.APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        return Response({'status':'ok'})


class Lve25ReporteCantidadDeEstudiosPorMesAno(views.APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        return Response({'status':'ok'})


class Lve27ReporteDemoraDeEstudios(views.APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [ IsAuthenticated ]

    def get(self, request, format=None):
        return Response({'status':'ok'})
