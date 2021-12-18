from django.contrib.auth.models import User
from rest_framework import serializers

from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def to_representation(self, instance):
        instance.password = ''
        return super().to_representation(instance)