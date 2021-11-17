
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes

from django.contrib.auth import models as auth_models

from . import models

class SerializadorDeObraSocialPersona(serializers.HyperlinkedModelSerializer):
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


class VistaPersona(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Persona.objects.all()
    serializer_class = SerializadorDePersona
    permission_classes = [ DjangoModelPermissions ]

    # def create(self, request, *args, **kwargs):
    #     datos_persona = request.data

    #     logging.debug(datos_persona)

    #     # persona = models.Persona(           
    #     #     nombre=datos_persona['nombre'],
    #     #     apellido=datos_persona['apellido'],
    #     #     dni=datos_persona['dni'],
    #     #     email=datos_persona['email'],
    #     #     fecha_nacimiento=datos_persona['fecha_nacimiento'],
    #     #     telefono=datos_persona['telefono'],
    #     #     historia_clinica=datos_persona['historia_clinica']
    #     # )
    #     # persona.save()

    #     # if 'obra_social' in datos_persona:
    #     #     ob = datos_persona['obra_social']
    #     #     obraSocial = models.ObraSocial.objects.get(id=ob)

    #     #     pacienteObraSocial = models.ObraSocialPersona(
    #     #         persona=persona,
    #     #         obra_social=obraSocial,
    #     #         numero_afiliado=datos_persona['numero_afiliado']
    #     #     )
    #     #     pacienteObraSocial.save()

    #     # serializer = SerializadorDePersona(persona, context={'request': request})
    #     # return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Persona.buscar(q)
        serializer = SerializadorDePersona(personas, many=True, context={'request': request})
        return Response(serializer.data)
        

