import logging

import datetime
from zoneinfo import ZoneInfo

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from . import models
from . import persona_serializers
from login import models as login_models

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
        

class SerializadorDeTutor(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = ['id','nombre','apellido','email','telefono','direccion']

class SerializadorDeTutorPaciente(serializers.ModelSerializer):
    tutor = SerializadorDeTutor()
    class Meta:
        model = models.TutorDePaciente
        fields = ['id','tutor']

class SerializadorDePaciente(serializers.ModelSerializer):
    historia_clinica = serializers.CharField(source='historia_clinica.historia_clinica', read_only=False, required=False)
    obra_social = SerializadorDeObraSocialPersona(required=False, many=False, read_only=False)
    tutor = SerializadorDeTutorPaciente(required=False, many=False, read_only=False)
    class Meta:
        model = models.Paciente
        fields = ['id','nombre','apellido','dni','email','fecha_nacimiento','telefono','direccion', 'historia_clinica', 'obra_social', 'tutor']


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
        else:
            if 'tutor' not in validated_data:
                raise ValidationError({'tutor':'requerido'})

        dni = validated_data.get('dni')
        usuario = login_models.LoginModel().crear_usuario(dni, models.Paciente.NOMBRE_GRUPO, clave=dni, email=validated_data.get('email',None))

        hc = validated_data.pop('historia_clinica',None)
        obra_social = validated_data.pop('obra_social',None)
        tutor = validated_data.pop('tutor',None)

        paciente = models.Paciente.objects.create(usuario=usuario, **validated_data)
       
        if hc:
            models.HistoriaClinica.objects.create(persona=paciente, historia_clinica=hc['historia_clinica'])
        if obra_social:
            id_obra_social = obra_social['obra_social']['id']
            numero_afiliado = obra_social['numero_afiliado']
            obp = paciente.crear_obra_social(id_obra_social, numero_afiliado)
            obp.save()

        if tutor:
            persona_tutor = tutor['tutor']
            email = persona_tutor['email']
            """ 
                la unicidad al tutor la damos por email ya que es un sistema muy básico 
                tomo el primero que tenga ese correo.
            """
            if models.Tutor.objects.filter(email=email).count() <= 0:
                tutor = models.Tutor.objects.create(**persona_tutor)
                login_models.LoginModel().crear_usuario(tutor.id, tutor.id, models.Tutor.NOMBRE_GRUPO, clave=tutor.id, email=email)
            else:                       
                tutor = models.Tutor.objects.filter(email=email).first()
            models.TutorDePaciente.objects.create(persona=paciente, tutor=tutor)

        paciente.refresh_from_db()
        return paciente
        

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

