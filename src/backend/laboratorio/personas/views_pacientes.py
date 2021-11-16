
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models

from . import views_personas


class SerializadorDePaciente(serializers.ModelSerializer):
    obra_social = views_personas.SerializadorDeObraSocialPersona(required=False, many=True)
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica')
    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion','historia_clinica','obra_social']


class VistaPacientes(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Paciente.all()
    serializer_class = SerializadorDePaciente

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
            obraSocial = models.ObraSocial.objects.get(id=ob)

            pacienteObraSocial = models.ObraSocialPersona(
                persona=persona,
                obra_social=obraSocial,
                numero_afiliado=datos_persona['numero_afiliado']
            )
            pacienteObraSocial.save()

        serializer = SerializadorDePersona(persona, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Persona.buscar(q)
        serializer = SerializadorDePersona(personas, many=True, context={'request': request})
        return Response(serializer.data)        