import logging

from rest_framework import serializers as rest_serializers

from . import models
from login import serializers as login_serializers
from login import models as login_models


class SerializadorDeMatricula(rest_serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = ['numero']

class SerializadorDeMedicoDerivante(rest_serializers.ModelSerializer):
    matricula = rest_serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.Persona
        fields = ['id','nombre','apellido','email','matricula']

    def update(self, instance, validated_data):
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        return super().update(instance, validated_data)



class SerializadorDeMedicoInformante(rest_serializers.ModelSerializer):
    # usuario = serializers.CharField(source='usuario.usuario.username', read_only=True)
    # clave = serializers.CharField(source='usuario.usuario.password', read_only=False)
    usuario = login_serializers.UsuarioSerializer(read_only=False, many=False, required=True)
    matricula = rest_serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.MedicoInformante
        fields = ['id','nombre','apellido','email','matricula', 'usuario']

    def create(self, validated_data):
        logging.debug(validated_data)

        usuario = validated_data.pop('usuario')
        logging.debug(usuario)

        numero_matricula = validated_data.pop('matricula')
        medico = models.MedicoInformante.objects.create(**validated_data)
        models.Matricula.objects.create(persona=medico, numero=numero_matricula)

        django_usuario = usuario['usuario']
        login_models.LoginModel().crear_usuario(medico.id, django_usuario['username'], models.MedicoInformante.NOMBRE_GRUPO, clave=django_usuario['password'], email=validated_data.get('email',None))

        medico.refresh_from_db()
        return medico


    def update(self, instance, validated_data):
        logging.info(validated_data)
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        
        credenciales = validated_data.pop('usuario')
        from django.contrib.auth.hashers import make_password
        usuario_django = instance.usuario
        usuario_django.password = make_password(credenciales['password'])
        usuario_django.save()

        return super().update(instance, validated_data)