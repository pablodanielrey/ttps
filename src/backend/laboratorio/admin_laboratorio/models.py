import logging
import datetime
from zoneinfo import ZoneInfo
import uuid

from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from personas import models as personas_models
from login import models as login_models


from rest_framework import exceptions
from rest_framework import status

class ModoOperacionAPIException(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code



class Configuracion(models.Model):

    class ModoOperacion(models.TextChoices):
        PACIENTE_OBLIGADO = 'PO', _('Paciente_Obligado')
        PACIENTE_NO_OBLIGADO = 'PNO', _('Paciente_No_Obligado')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modo_operacion = models.CharField(max_length=10, choices=ModoOperacion.choices, default=ModoOperacion.PACIENTE_NO_OBLIGADO)
    fecha = models.DateTimeField(default=now)

    def obtener_modo_de_operacion(self):
        return self.ModoOperacion(self.modo_operacion)

    def verificar_modo_de_operacion(self, serializador):            
        modo_de_operacion = self.obtener_modo_de_operacion()
        logging.debug(f'Modo de operación del sistema {modo_de_operacion}')
        if modo_de_operacion == self.ModoOperacion.PACIENTE_OBLIGADO:
            usuario_logueado = serializador.context.get('request').user
            logging.debug(f'verificando si {usuario_logueado.username} es Paciente')
            if not personas_models.Paciente.usuario_es_tipo(usuario_logueado):
                raise ModoOperacionAPIException(
                    {
                        "usuario":usuario_logueado.username,
                        "modo": modo_de_operacion
                    }
                )    




class PersonasModel:

    login_model = login_models.LoginModel()

    def __generar_fecha_now(self):
        return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

    def __edad(self, nacimiento, ahora):
        logging.debug(f'verificando nacimiento : {nacimiento} {ahora}')


        anos = ahora.year - nacimiento.year
        if datetime.date(year=nacimiento.year, month=ahora.month, day=ahora.day) < nacimiento:
            anos = anos - 1
        return anos

    def crearAdministrador(self, nombre, apellido, usuario, clave):
        u = self.login_model.crear_usuario(usuario, personas_models.Administrador.NOMBRE_GRUPO, clave=clave)
        admin = personas_models.Administrador(nombre=nombre, apellido=apellido, usuario=u)
        admin.save()


    def crearConfigurador(self, nombre, apellido, usuario, clave):
        u = self.login_model.crear_usuario(usuario, personas_models.Configurador.NOMBRE_GRUPO, clave=clave)
        config = personas_models.Configurador(nombre=nombre, apellido=apellido, usuario=u)
        config.save()
        

    def crearEmpleado(self, nombre, apellido, email, usuario, clave):
        u = self.login_model.crear_usuario(usuario, personas_models.Empleado.NOMBRE_GRUPO, clave=clave)
        empleado = personas_models.Empleado(nombre=nombre, apellido=apellido, email=email, usuario=u)
        empleado.save()
        

    def crearMedicoInformante(self, nombre, apellido, email, matricula, usuario, clave):
        u = self.login_model.crear_usuario(usuario, personas_models.MedicoInformante.NOMBRE_GRUPO, clave=clave)
        medico = personas_models.MedicoInformante(nombre=nombre, apellido=apellido, email=email, usuario=u)
        medico.save()
        matricula = personas_models.Matricula(persona=medico, numero=matricula)
        matricula.save()
        
        return medico

    def crearMedicoDerivante(self, nombre, apellido, email, matricula):
        usuario = str(uuid.uuid4())
        u = self.login_model.crear_usuario(usuario, personas_models.MedicoDerivante.NOMBRE_GRUPO, clave=str(uuid.uuid4()))
        medico = personas_models.MedicoDerivante(nombre=nombre, apellido=apellido, email=email, usuario=u)
        medico.save()
        matricula = personas_models.Matricula(persona=medico, numero=matricula)
        matricula.save()
        
        return medico

    def crearPaciente(self, tutor=None, **kwargs):
        historia_clinica = kwargs.pop('historia_clinica','')

        dni = kwargs.get('dni')
        usuario = self.login_model.crear_usuario(dni, personas_models.Paciente.NOMBRE_GRUPO, clave=dni)
        kwargs['usuario'] = usuario
        
        paciente = personas_models.Paciente(**kwargs)
        paciente.save()
        hc = personas_models.HistoriaClinica(persona=paciente, historia_clinica=historia_clinica)
        hc.save()

        ahora = self.__generar_fecha_now()
        if 18 > self.__edad(paciente.fecha_nacimiento, ahora):    
            personas_models.TutorDePaciente.objects.create(persona=paciente, tutor=tutor)

        return paciente
    
    def crearTutor(self, **kwargs):
        usuario = self.login_model.crear_usuario(str(uuid.uuid4()), personas_models.Tutor.NOMBRE_GRUPO, clave=str(uuid.uuid4()))
        kwargs['usuario'] = usuario
        tutor = personas_models.Tutor(**kwargs)
        tutor.save()
        return tutor