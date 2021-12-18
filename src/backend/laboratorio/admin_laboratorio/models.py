import logging
import datetime
from zoneinfo import ZoneInfo
import uuid

from django.db import models

from personas import models as personas_models
from login import models as login_models


        
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