from django.db import models
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE

import uuid


class ObraSocial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.email} {self.telefono}"

class Persona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    email = models.EmailField()
    dni = models.CharField(max_length=50, null=True)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=2096, null=True)
    
    @classmethod
    def buscar(cls, termino:str):
        return cls.objects.filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))


class HistoriaClinica(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='historia_clinica')
    historia_clinica = models.CharField(max_length=9216, null=True)

class Matricula(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='matricula')
    numero = models.CharField(max_length=500)


class MedicoInformante(Persona):
    class Meta:
        proxy = True

    @classmethod
    def buscar(cls, termino:str):
        return cls.objects.filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))


class MedicoDerivante(Persona):
    class Meta:
        proxy = True

    @classmethod
    def buscar(cls, termino:str):
        return cls.objects.filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))


class Paciente(Persona):
    class Meta:
        proxy = True

    @classmethod
    def buscar(cls, termino:str):
        return cls.objects.filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))


class ObraSocialPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obra_social')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    numero_afiliado = models.CharField(max_length=1024)


class PersonasModel:

    def crearPersona(self, nombre, apellido, dni, email, direccion):
        paciente = Paciente(nombre=nombre, apellido=apellido, dni=dni, email=email, direccion=direccion)
        paciente.save()
        return paciente

    def crearMedicoDerivante(self, nombre, apellido, email, matricula):
        medico = MedicoDerivante(nombre=nombre, apellido=apellido, email=email)
        medico.save()
        matricula = Matricula(persona=medico, numero=matricula)
        matricula.save()
        return medico

    def crearMedicoInformante(self, nombre, apellido, email):
        medico = MedicoDerivante(nombre=nombre, apellido=apellido)
        medico.save()
