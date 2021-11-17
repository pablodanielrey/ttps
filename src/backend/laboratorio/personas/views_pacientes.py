
import logging

from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
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


class VistaPaciente(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Paciente.all()
    serializer_class = SerializadorDePaciente
    permission_classes = [ DjangoModelPermissions ]
    #permission_classes = [ IsAdminUser ]

    model = models.PersonasModel()

    def create(self, request, *args, **kwargs):
        datos_persona = request.data

        logging.debug(datos_persona)

        obra_social = None
        if 'obra_social' in datos_persona:
            obra_social = request.data.pop("obra_social")
            if obra_social:
                afiliado = request.data.pop("numero_afiliado")

        paciente = self.model.crearPaciente(**request.data)

        if obra_social:
            obraSocial = models.ObraSocial.objects.get(id=obra_social)

            pacienteObraSocial = models.ObraSocialPersona(
                persona=paciente,
                obra_social=obraSocial,
                numero_afiliado=afiliado
            )
            pacienteObraSocial.save()

        serializer = SerializadorDePaciente(paciente, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        logging.debug(f'buscando a : {q}')

        personas = models.Paciente.buscar(q)
        serializer = SerializadorDePaciente(personas, many=True, context={'request': request})
        return Response(serializer.data)        