from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import logging

from estudios import models


class InitSite(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):


        """
            aca genero todos los datos del modelo necesarios para que el sistema esté inicializado
        """
        logging.debug('inicializando sistema')

        return Response({'status':'sistema inicializado'})