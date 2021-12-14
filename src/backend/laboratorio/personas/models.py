from django.db import models
from django.contrib.auth.models import User, Group

from django.db.models.deletion import CASCADE, SET_NULL

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
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id} {self.nombre} {self.apellido}"

    NOMBRE_GRUPO = 'Pacientes'

    @classmethod
    def all(cls):
        return cls.objects.filter(usuario__groups__name=cls.NOMBRE_GRUPO)

    @classmethod
    def buscar(cls, termino:str):
        return cls.all().filter(models.Q(nombre__icontains=termino) | models.Q(apellido__icontains=termino) | models.Q(dni__icontains=termino))
        

class ObraSocialPersona(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE, related_name='obra_social') 
    # models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='obra_social')
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    numero_afiliado = models.CharField(max_length=1024)

class HistoriaClinica(models.Model):
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

    @classmethod
    def crear_obra_social(cls, id_obra_social, numero_afiliado):
        os = ObraSocial.objects.get(id=id_obra_social)
        osp = ObraSocialPersona(obra_social=os, numero_afiliado=numero_afiliado)
        return osp

class MedicoInformante(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Médicos_Informantes'

        
class MedicoDerivante(Persona):
    class Meta:
        proxy = True

    NOMBRE_GRUPO = 'Médicos_Derivantes'
 


class PersonasModel:

    def _generar_usuario_django(self, usuario, grupo, clave=None, email=None):
        password = clave if clave else str(uuid.uuid4())
        email = email if email else ''
        u = User.objects.create_user(username=usuario, password=password, email=email)
        u.save()

        g = Group.objects.get(name=grupo)
        u.groups.add(g)
        u.save()

        return u

    def _crear_usuario_del_sistema(self, nombre, apellido, usuario, clave, clase):
        persona = clase(nombre=nombre, apellido=apellido)
        persona.save()

        u = self._generar_usuario_django(usuario, clase.NOMBRE_GRUPO, clave)
        persona.usuario = u
        persona.save()

        return persona


    def crearAdministrador(self, nombre, apellido, usuario, clave):
        self._crear_usuario_del_sistema(nombre, apellido, usuario, clave, Administrador)

    def crearConfigurador(self, nombre, apellido, usuario, clave):
        self._crear_usuario_del_sistema(nombre, apellido, usuario, clave, Configurador)

    def crearEmpleado(self, nombre, apellido, usuario, clave):
        self._crear_usuario_del_sistema(nombre, apellido, usuario, clave, Empleado)


    def crearMedicoInformante(self, nombre, apellido, email, matricula, usuario, clave):
        medico = MedicoInformante(nombre=nombre, apellido=apellido, email=email)
        medico.save()
        matricula = Matricula(persona=medico, numero=matricula)
        matricula.save()

        u = self._generar_usuario_django(usuario, MedicoInformante.NOMBRE_GRUPO, clave, email)
        medico.usuario = u
        medico.save()

        return medico

    def crearMedicoDerivante(self, nombre, apellido, email, matricula):
        medico = MedicoDerivante(nombre=nombre, apellido=apellido, email=email)
        medico.save()
        matricula = Matricula(persona=medico, numero=matricula)
        matricula.save()

        u = self._generar_usuario_django(str(medico.id), MedicoDerivante.NOMBRE_GRUPO)    
        medico.usuario = u
        medico.save()

        return medico


    def crearPaciente(self, **kwargs):

        historia_clinica = kwargs.pop('historia_clinica')

        paciente = Paciente(**kwargs)
        paciente.save()

        hc = HistoriaClinica(persona=paciente, historia_clinica=historia_clinica)
        hc.save()

        u = self._generar_usuario_django(str(paciente.id), Paciente.NOMBRE_GRUPO)    
        paciente.usuario = u
        paciente.save()

        return paciente


