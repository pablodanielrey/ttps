import logging
import datetime
from zoneinfo import ZoneInfo

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
        admin = personas_models.Administrador(nombre=nombre, apellido=apellido)
        admin.save()
        self.login_model.crear_usuario(admin.id, usuario, personas_models.Administrador.NOMBRE_GRUPO, clave=clave)

    def crearConfigurador(self, nombre, apellido, usuario, clave):
        config = personas_models.Configurador(nombre=nombre, apellido=apellido)
        config.save()
        self.login_model.crear_usuario(config.id, usuario, personas_models.Configurador.NOMBRE_GRUPO, clave=clave)

    def crearEmpleado(self, nombre, apellido, email, usuario, clave):
        empleado = personas_models.Empleado(nombre=nombre, apellido=apellido, email=email)
        empleado.save()
        self.login_model.crear_usuario(empleado.id, usuario, personas_models.Empleado.NOMBRE_GRUPO, clave=clave)

    def crearMedicoInformante(self, nombre, apellido, email, matricula, usuario, clave):
        medico = personas_models.MedicoInformante(nombre=nombre, apellido=apellido, email=email)
        medico.save()
        matricula = personas_models.Matricula(persona=medico, numero=matricula)
        matricula.save()
        self.login_model.crear_usuario(medico.id, usuario, personas_models.MedicoInformante.NOMBRE_GRUPO, clave=clave)
        return medico

    def crearMedicoDerivante(self, nombre, apellido, email, matricula):
        logging.debug('creando médico derivante')
        medico = personas_models.MedicoDerivante(nombre=nombre, apellido=apellido, email=email)
        medico.save()
        matricula = personas_models.Matricula(persona=medico, numero=matricula)
        matricula.save()
        self.login_model.crear_usuario(medico.id, str(medico.id), personas_models.MedicoDerivante.NOMBRE_GRUPO, clave=str(medico.id))
        return medico

    def crearPaciente(self, tutor=None, **kwargs):
        historia_clinica = kwargs.pop('historia_clinica','')
        paciente = personas_models.Paciente(**kwargs)
        paciente.save()
        hc = personas_models.HistoriaClinica(persona=paciente, historia_clinica=historia_clinica)
        hc.save()

        dni = paciente.dni.lower().strip()
        self.login_model.crear_usuario(paciente.id, dni, personas_models.Paciente.NOMBRE_GRUPO, clave=dni)

        ahora = self.__generar_fecha_now()
        if 18 > self.__edad(paciente.fecha_nacimiento, ahora):    
            personas_models.TutorDePaciente.objects.create(persona=paciente, tutor=tutor)


        return paciente
    
    def crearTutor(self, **kwargs):
        tutor = personas_models.Tutor(**kwargs)
        tutor.save()
        self.login_model.crear_usuario(tutor.id, str(tutor.id), personas_models.Tutor.NOMBRE_GRUPO, clave=str(tutor.id))
        return tutor