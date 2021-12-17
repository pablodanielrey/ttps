
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.username', read_only=False)
    clave = serializers.CharField(source='usuario.password', read_only=False)
