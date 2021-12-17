import uuid
from django.db import models
from django.contrib.auth.models import User, Group

from django.db.models.deletion import CASCADE, SET_NULL


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
    dni = models.CharField(max_length=50, null=True, unique=True)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=2096, null=True)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido}"

    NOMBRE_GRUPO = 'Personas'

    @classmethod
    def all(cls):
        return cls.objects.filter(usuario__usuario__groups__name=cls.NOMBRE_GRUPO)

    @classmethod
    def buscar(cls, termino:str):
        return cls.all().filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))
        

    @classmethod
    def usuario_es_tipo(cls, usuario_django):
        if not usuario_django:
            return False
        grupos = [g.name for g in usuario_django.groups.all()]
        return cls.NOMBRE_GRUPO in grupos


class ObraSocialPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='obra_social') 
    # models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obra_social')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    numero_afiliado = models.CharField(max_length=1024)

class HistoriaClinica(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='historia_clinica')
    historia_clinica = models.CharField(max_length=9216, null=True)

class Matricula(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='matricula')
    numero = models.CharField(max_length=500)



class Administrador(Persona):

    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Administradores'


class Empleado(Persona):

    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Empleados'

class Configurador(Persona):

    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Configuradores'

class Paciente(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Pacientes'

    def crear_obra_social(self, id_obra_social, numero_afiliado):
        os = ObraSocial.objects.get(id=id_obra_social)
        osp = ObraSocialPersona(persona=self, obra_social=os, numero_afiliado=numero_afiliado)
        return osp


class MedicoInformante(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Médicos_Informantes'

        
class MedicoDerivante(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Médicos_Derivantes'
 

class Tutor(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Tutores'



class TutorDePaciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='tutores')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)