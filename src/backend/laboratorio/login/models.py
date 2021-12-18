import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.fields import related

from personas import models as personas_models

class LoginModel:

    def obtener_persona_del_usuario(self, usuario):
        return personas_models.Persona.objects.get(usuario=usuario)

    def crear_usuario(self, usuario, grupo, clave=None, email=None):
        password = clave if clave else str(uuid.uuid4())
        email = email if email else ''
        u = User.objects.create_user(username=usuario, password=password, email=email)
        u.save()

        g = Group.objects.get(name=grupo)
        u.groups.add(g)
        u.save()

        return u

    def obtener_usuario(self, persona):
        return persona.usuario
