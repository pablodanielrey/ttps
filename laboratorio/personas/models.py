from django.db import models

import uuid

# Create your models here.

class ObraSocial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    telefono = models.CharField(max_length=50)


class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)
    apellido = models.CharField(max_length=1024)
    dni = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    email = models.CharField(max_length=1024)
    telefono = models.CharField(max_length=50)
    historia_clinica = models.CharField(max_length=9216)

class ObraSocialPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obra_social')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    numero_afiliado = models.CharField(max_length=1024)

