import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from . import persona_serializers

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
        

import datetime
from zoneinfo import ZoneInfo

class SerializadorDeTutor(serializers.ModelSerializer):
    tutor = persona_serializers.SerializadorDePersona()
    class Meta:
        model = models.TutorDePaciente
        fields = ['tutor']

class SerializadorDePaciente(serializers.ModelSerializer):
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica', read_only=False, required=False)
    obra_social = SerializadorDeObraSocialPersona(required=False, many=False, read_only=False)
    # obra_social = serializers.RelatedField(source='obra_social.obra_social', read_only=False, required=False)
    # numero_afiliado = serializers.CharField(source='obra_social.numero_afiliado', read_only=False, required=False)
    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion', 'historia_clinica', 'obra_social']


    def __edad(self, nacimiento):
        logging.debug(f'verificando nacimiento : {nacimiento}')
        ahora = datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))
        anos = ahora.year - nacimiento.year
        if datetime.date(year=nacimiento.year, month=ahora.month, day=ahora.day) < nacimiento:
            anos = anos - 1
        return anos

    def create(self, validated_data):
        fecha_nacimiento = validated_data.get('fecha_nacimiento')
        if 18 < self.__edad(fecha_nacimiento):
            for v in ['telefono', 'direccion', 'email']:
                if v not in validated_data:
                    raise ValidationError({v:'requerido'})

            hc = validated_data.pop('historia_clinica',None)
            obra_social = validated_data.pop('obra_social',None)

            paciente = models.Paciente.objects.create(**validated_data)
            if hc:
                models.HistoriaClinica.objects.create(persona=paciente, historia_clinica=hc['historia_clinica'])
            if obra_social:
                id_obra_social = obra_social['obra_social']['id']
                numero_afiliado = obra_social['numero_afiliado']
                obp = paciente.crear_obra_social(id_obra_social, numero_afiliado)
                obp.save()
            return paciente
        else:

            raise NotImplemented()
        

    def update(self, instance, validated_data):
        logging.debug(f'actualizando {instance}')
        historia_clinica = validated_data.pop('historia_clinica', None)
        if not historia_clinica:
            if models.HistoriaClinica.objects.filter(persona=instance).count() > 0:
                instance.historia_clinica.delete()
        else:
            if models.HistoriaClinica.objects.filter(persona=instance).count() <= 0:
                hc = models.HistoriaClinica(persona=instance, historia_clinica=historia_clinica['historia_clinica'])
                hc.save()
            else:
                hc = instance.historia_clinica
                hc.historia_clinica = historia_clinica['historia_clinica']
                hc.save()
       
        if models.ObraSocialPersona.objects.filter(persona=instance).count() > 0:
            instance.obra_social.delete()
        obra_social = validated_data.pop('obra_social',None)
        if obra_social:
            id_obra_social = obra_social['obra_social']['id']
            numero_afiliado = obra_social['numero_afiliado']
            obp = instance.crear_obra_social(id_obra_social, numero_afiliado)
            obp.save()

        instance.refresh_from_db()
        return super().update(instance, validated_data)

