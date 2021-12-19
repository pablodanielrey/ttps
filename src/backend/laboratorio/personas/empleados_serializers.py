from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from login import serializers as login_serializers
from login import models as login_models
from . import models

class SerializadorDeEmpleado(serializers.ModelSerializer):
    usuario = login_serializers.UsuarioSerializer()

    class Meta:
        model = models.Empleado
        fields = ['id','nombre','apellido','email', 'usuario']

    _login_model = login_models.LoginModel()

    def create(self, validated_data):
        usuario = validated_data.pop('usuario')
        username = usuario['username']
        clave = usuario['password']
        try:
            usuario_django = self._login_model.crear_usuario(username, models.Empleado.NOMBRE_GRUPO, clave, validated_data.get('email',None))
        except IntegrityError:
            raise ValidationError({'usuario':'ya existe'})
        empleado = models.Empleado.objects.create(usuario=usuario_django, **validated_data)
        return empleado