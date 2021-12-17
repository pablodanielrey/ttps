
import logging


from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models
from . import views_personas
from . import paciente_serializers


class VistaPaciente(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Paciente.all()
    serializer_class = paciente_serializers.SerializadorDePaciente
    #permission_classes = [ DjangoModelPermissions ]
    #permission_classes = [ IsAdminUser ]

    def create(self, request, *args, **kwargs):
        datos_persona = request.data

        logging.debug(datos_persona)

        obra_social = None
        if 'obra_social' in datos_persona:
            obra_social = request.data.pop("obra_social")
            if obra_social:
                afiliado = request.data.pop("numero_afiliado")

        # paciente = self.model.crearPaciente(**request.data)
        paciente = None

        if obra_social:
            obraSocial = models.ObraSocial.objects.get(id=obra_social)

            pacienteObraSocial = models.ObraSocialPersona(
                persona=paciente,
                obra_social=obraSocial,
                numero_afiliado=afiliado
            )
            pacienteObraSocial.save()

        serializer = paciente_serializers.SerializadorDePaciente(paciente, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Paciente.buscar(q)
        serializer = paciente_serializers.SerializadorDePaciente(personas, many=True, context={'request': request})
        return Response(serializer.data)        

class VistaPaciente2(viewsets.ModelViewSet):
    queryset = models.Paciente.all()
    serializer_class = paciente_serializers.SerializadorDePaciente

