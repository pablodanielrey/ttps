import logging

from rest_framework import serializers

from . import models


class SerializadorDeHistoriaClinica(serializers.ModelSerializer):
    class Meta:
        model = models.HistoriaClinica
        fields = ['historia_clinica']


class SerializadorDeObraSocial(serializers.ModelSerializer):
    """ 
        Se redefine el campo para cuando se hace el post/put del id lo pueda obtener en el validated_data
        sin esta redefinición los campos read_only son ignorados en validated_data
        https://github.com/encode/django-rest-framework/issues/2320
    """
    id = serializers.UUIDField(read_only=False)
    class Meta:
        model = models.ObraSocial
        fields = ['id','nombre']


class SerializadorDeObraSocialPersona(serializers.HyperlinkedModelSerializer):
    obra_social = SerializadorDeObraSocial()
    class Meta:
        model = models.ObraSocialPersona
        fields = ['obra_social','numero_afiliado']
        

class SerializadorDePaciente(serializers.ModelSerializer):
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica', read_only=False)
    obra_social = SerializadorDeObraSocialPersona(required=False, many=False)

    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion', 'historia_clinica', 'obra_social']
    
    def update(self, instance, validated_data):
        logging.info(validated_data)
        historia_clinica = validated_data.pop('historia_clinica')
        if models.HistoriaClinica.objects.filter(persona=instance).count() <= 0:
            hc = models.HistoriaClinica(persona=instance, historia_clinica=historia_clinica['historia_clinica'])
            hc.save()
        else:
            hc = instance.historia_clinica
            hc.historia_clinica = historia_clinica['historia_clinica']
            hc.save()
       
        if models.ObraSocialPersona.objects.filter(persona=instance).count() > 0:
            ob = instance.obra_social
            ob.delete()
            instance.obra_social = None
            instance.save()

        #TODO: corregir este codigo porque no me está trayendo los datos el serializer
        if 'obra_social' in validated_data:
            obra_social = validated_data.pop('obra_social')
            logging.info(obra_social)

            id_obra_social = obra_social['obra_social']['id']
            numero_afiliado = obra_social['numero_afiliado']

            # for obp in instance.obra_social.all():
            #     obp.delete()

            obp = instance.crear_obra_social(id_obra_social, numero_afiliado)
            # obp.persona = instance
            obp.save()
            instance.obra_social = obp
            instance.save()
            #obp.persona = instance
            #obp.save()

        return super().update(instance, validated_data)

