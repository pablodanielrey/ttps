import logging

from rest_framework import serializers as rest_serializers

from . import models
from . import serializers


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
    usuario = serializers.UsuarioSerializer(read_only=False, many=False, required=True)
    matricula = rest_serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.MedicoInformante
        fields = ['id','nombre','apellido','email','matricula', 'usuario']

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