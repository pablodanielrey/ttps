import uuid

from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.fields import related

from personas import models as personas_models

class UsuarioPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.OneToOneField(personas_models.Persona, on_delete=models.CASCADE, related_name='usuario')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class LoginModel:

    def obtener_persona_del_usuario(self, usuario):
        pass

    def _generar_usuario_django(self, usuario, grupo, clave=None, email=None):
        password = clave if clave else str(uuid.uuid4())
        email = email if email else ''
        u = User.objects.create_user(username=usuario, password=password, email=email)
        u.save()

        g = Group.objects.get(name=grupo)
        u.groups.add(g)
        u.save()

        return u

    def crear_usuario(self, persona_id:str, usuario:str, grupo:str, clave=None, email=None):
        persona = personas_models.Persona.objects.get(id=persona_id)

        usuarios = UsuarioPersona.objects.filter(persona=persona)
        usernames = [u.usuario.get_username() for u in usuarios]
        if usuario not in usernames:
            dusuario = self._generar_usuario_django(usuario, grupo, clave, email)
            up = UsuarioPersona(persona=persona, usuario=dusuario)
            up.save()

        
    def obtener_usuario(self, persona):
        return persona.usuario
