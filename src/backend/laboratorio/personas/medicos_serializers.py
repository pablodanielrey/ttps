import logging
import uuid

from rest_framework import serializers as rest_serializers
from rest_framework.exceptions import ValidationError

from django.db.utils import IntegrityError

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
        model = models.MedicoDerivante
        fields = ['id','nombre','apellido','email','matricula']

    def create(self, validated_data):
        matricula = validated_data.pop('matricula')
        usuario = login_models.LoginModel().crear_usuario(usuario=str(uuid.uuid4()), grupo=models.MedicoDerivante.NOMBRE_GRUPO, clave=str(uuid.uuid4()))
        validated_data['usuario'] = usuario
        medico = models.MedicoDerivante.objects.create(**validated_data)
        models.Matricula.objects.create(persona=medico, numero=matricula['numero'])
        medico.refresh_from_db()
        return medico

    def update(self, instance, validated_data):
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        return super().update(instance, validated_data)



class SerializadorDeMedicoInformante(rest_serializers.ModelSerializer):
    usuario = login_serializers.UsuarioSerializer(read_only=False, many=False, required=True)
    matricula = rest_serializers.CharField(source='matricula.numero', read_only=False)
    class Meta:
        model = models.MedicoInformante
        fields = ['id','nombre','apellido','email','matricula', 'usuario']

    def create(self, validated_data):
        usuario = validated_data.pop('usuario')
        for v in ['username', 'password']:
            if v not in usuario:
                raise ValidationError({v:'requerido'})
        try:                
            usuario = login_models.LoginModel().crear_usuario(usuario['username'], models.MedicoInformante.NOMBRE_GRUPO, clave=usuario['password'], email=validated_data.get('email',None))
        except IntegrityError:
            raise ValidationError({'usuario':'ya existente'})

        numero_matricula = validated_data.pop('matricula')['numero']

        medico = models.MedicoInformante.objects.create(usuario=usuario, **validated_data)
        models.Matricula.objects.create(persona=medico, numero=numero_matricula)

        medico.refresh_from_db()
        return medico

    def update(self, instance, validated_data):
        matricula = validated_data.pop('matricula')
        instance.matricula.numero = matricula['numero']
        instance.matricula.save()
        
        credenciales = validated_data.pop('usuario')
        from django.contrib.auth.hashers import make_password
        usuario_django = instance.usuario
        usuario_django.password = make_password(credenciales['password'])
        usuario_django.save()

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance