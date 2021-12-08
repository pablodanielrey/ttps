
import logging


from rest_framework import serializers, viewsets, views
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework.response import Response

from rest_framework.decorators import action

from . import models

from . import views_personas


class SerializadorDePaciente(serializers.ModelSerializer):
    #obra_social = views_personas.SerializadorDeObraSocialPersona(required=False, many=True, read_only=False)
    obra_social = serializers.CharField(source='obra_social.obra_social.id', required=False, read_only=False)
    numero_afiliado = serializers.CharField(source='obra_social.numero_afiliado', required=False, read_only=False)
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica', read_only=False)

    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion','historia_clinica','obra_social','numero_afiliado']
    
    def update(self, instance, validated_data):
        logging.info(validated_data)
        historia_clinica = validated_data.pop('historia_clinica')
        instance.historia_clinica.historia_clinica = historia_clinica['historia_clinica']
        instance.historia_clinica.save()
       
        #TODO: corregir este codigo porque no me está trayendo los datos el serializer
        if 'obra_social' in validated_data:
            obra_social = validated_data.pop('obra_social')
            logging.info(obra_social)

            id_obra_social = obra_social['obra_social']['id']
            numero_afiliado = obra_social['numero_afiliado']
            for obp in instance.obra_social.all():
                obp.delete()

            obp = instance.crear_obra_social(id_obra_social, numero_afiliado)
            obp.persona = instance
            obp.save()
            instance.obra_social.add(obp)
            instance.save()
            #obp.persona = instance
            #obp.save()

        return super().update(instance, validated_data)


"""
class SerializadorDePaciente(serializers.ModelSerializer):
    obra_social = views_personas.SerializadorDeObraSocialPersona(required=False, many=True, read_only=True)
    #obra_social = views_personas.SerializadorDeObraSocialPersona(source='obra_social.obraSocial', many=True, read_only=False)
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica', allow_null=True,read_only=True)

    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion','historia_clinica','obra_social']

    def update(self, instance, validated_data):
        logging.info(validated_data)
        historia_clinica = validated_data.pop('historia_clinica')
        instance.historia_clinica.historia_clinica = historia_clinica
        instance.historia_clinica.save()
       
        return super().update(instance, validated_data)    
"""

class VistaPaciente(viewsets.ModelViewSet):
    """
        TODO: esto es necesario cambiarlo para algo parecido a :
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    queryset = models.Paciente.all()
    serializer_class = SerializadorDePaciente
    #permission_classes = [ DjangoModelPermissions ]
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