from django.db import models
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE

import uuid


class ObraSocial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    telefono = models.CharField(max_length=50)

class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # lo siguiente es para cuando se implemente el paciente como usuario.
    # por ahora es un objeto de nuestro sistema. no un sujeto.
    #     
    # usuario = models.ForeignKey(User, on_delete=CASCADE, null=True)

    # @property
    # def nombre(self):
    #     return self.usuario.first_name
    
    # @nombre.setter
    # def __set_nombre(self, var):
    #     self.usuario.first_name = var

    # @property
    # def apellido(self):
    #     return self.usuario.last_name

    # @apellido.setter
    # def __set_apellido(self, var):
    #     self.usuario.last_name = var

    # @property
    # def email(self):
    #     return self.usuario.email

    # @email.setter
    # def __set_email(self, var):
    #     self.usuario.email = var

    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    email = models.EmailField()
    dni = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=50)
    historia_clinica = models.CharField(max_length=9216, null=True)

    def __str__(self):
        # return f"{self.usuario.__str__()} {self.nombre} {self.apellido} {self.dni}"
        return f"{self.nombre} {self.apellido} {self.dni}"


class ObraSocialPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obra_social')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    numero_afiliado = models.CharField(max_length=1024)
