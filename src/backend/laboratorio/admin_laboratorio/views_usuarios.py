

from django.db.utils import IntegrityError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import logging
import datetime
from zoneinfo import ZoneInfo
import random

from . import models
from personas import models as persona_models

def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

def fecha_de_nac_menor():
    ano = random.randrange(2004,2020,1)
    mes = random.randrange(1,12,1)
    dia = random.randrange(1,27,1)
    return datetime.date(year=ano, month=mes, day=dia)

def fecha_de_nac_mayor():
    ano = random.randrange(1940,2000,1)
    mes = random.randrange(1,12,1)
    dia = random.randrange(1,27,1)
    return datetime.date(year=ano, month=mes, day=dia)


def generar_pacientes_mayores():
    m = models.PersonasModel()

    pacientes = []
    for i in range(1,5):
        pacientes.append(
            {
                'nombre': f'Paciente {i}',
                'apellido': f'Cero {i}',
                'dni':f'{i}',
                'email': f'email{i}@gmail.com',
                'telefono': f'221 2222{i}',
                'direccion': f'calle {i} la plata',
                'fecha_nacimiento': fecha_de_nac_mayor(),
                'historia_clinica': f'algo de historia'
            }
        )
    contador = 0
    for paciente in pacientes:
        try:
            contador += 1
            paux = m.crearPaciente(**paciente)
            if contador % 2 == 0:
                ob = persona_models.ObraSocial.objects.first()
                obp = persona_models.ObraSocialPersona(persona=paux, obra_social=ob, numero_afiliado=f'numero-{paux.id}')
                obp.save()
        except IntegrityError as e:
            pass

def generar_pacientes_menores():
    m = models.PersonasModel()

    tutor1 = m.crearTutor(nombre='Un super tutor', apellido='ape', telefono='1112222tutor', email="tutor@gmail.com", direccion="calle tutorias numero tute")
    tutor2 = m.crearTutor(nombre='Un super tutor2', apellido='ape', telefono='1', email="tutor2@gmail.com", direccion="calle tutorias numero tute")
    tutor3 = m.crearTutor(nombre='Un super tutor3', apellido='ape', telefono='1112222tutor', email="tutor3@gmail.com", direccion="calle tutorias numero tute")

    pacientes = []
    for i in range(5,12):
        pacientes.append(
            {
                'nombre': f'Paciente {i}',
                'apellido': f'Cero {i}',
                'dni':f'{i}',
                'email': f'email{i}@gmail.com',
                'telefono': f'221 2222{i}',
                'direccion': f'calle {i} la plata',
                'fecha_nacimiento': fecha_de_nac_menor(),
                'historia_clinica': f'algo de historia'
            }
        )
    contador = 0
    for paciente in pacientes:
        try:
            contador += 1
            paux = m.crearPaciente(tutor=tutor1, **paciente)
            if contador % 2 == 0:
                ob = persona_models.ObraSocial.objects.first()
                obp = persona_models.ObraSocialPersona(persona=paux, obra_social=ob, numero_afiliado=f'numero-{paux.id}')
                obp.save()
        except IntegrityError as e:
            pass


def crear_medicos_derivantes():
    m = models.PersonasModel()
    try:
        m.crearMedicoDerivante(nombre='Medico1', apellido="derivante", email='medico2@simed.com', matricula='122223er')
    except IntegrityError as e:
        pass

    try:
        m.crearMedicoDerivante(nombre='Medico2', apellido="derivante2", email='medico3@simed.com', matricula='123er')
    except IntegrityError as e:
        pass

    try:
        m.crearMedicoDerivante(nombre='Medico3', apellido="derivante3", email='medico4@simed.com', matricula='1223er')
    except IntegrityError as e:
        pass


def generar_usuarios_de_sistema():
    m = models.PersonasModel()
    try:
        m.crearAdministrador("Super","Admin", "administrador", "ttp")
    except IntegrityError as e:
        pass

    try:
        m.crearConfigurador("Configurador","sistema", "configurador", "ttp")
    except IntegrityError as e:
        pass

    try:
        m.crearEmpleado("Empleado1", "Apellido1", "empleo1@gmail.com", "empleado", "ttp")
    except IntegrityError as e:
        pass

    try:
        m.crearEmpleado("Empleado2", "Apellido2", "empleo2@gmail.com", "empleado2", "ttp")
    except IntegrityError as e:
        pass

    try:
        m.crearMedicoInformante("Medico","Informante","medico@simed.com", "matricula_de_informante1", "medicoinf", "ttp")
    except IntegrityError as e:
        pass

    try:
        m.crearMedicoInformante("Medico2","Informante2","medico2@simed.com", "matricula_de_informante2", "medicoinf2", "ttp")
    except IntegrityError as e:
        pass
    

from django.contrib.auth import models as django_auth_models

def definir_permisos():
    
    def asociar_permiso_a_grupo(grupo, entidad, permisos=['add','change','delete','view']):
        grupo = django_auth_models.Group.objects.get(name=grupo)
        for permiso in permisos:
            permission = django_auth_models.Permission.objects.get(codename=f'{permiso}_{entidad}')
            grupo.permissions.add(permission)
    
    for p in django_auth_models.Permission.objects.all():
        logging.debug(p.codename)

    asociar_permiso_a_grupo(persona_models.Configurador.NOMBRE_GRUPO, 'parametrodeturnos')

    asociar_permiso_a_grupo(persona_models.Empleado.NOMBRE_GRUPO, 'turnoconfirmado')
    asociar_permiso_a_grupo(persona_models.Empleado.NOMBRE_GRUPO, 'estadoestudio')
    asociar_permiso_a_grupo(persona_models.Empleado.NOMBRE_GRUPO, 'estudio')
    asociar_permiso_a_grupo(persona_models.Empleado.NOMBRE_GRUPO, 'liquidacion')
    asociar_permiso_a_grupo(persona_models.Empleado.NOMBRE_GRUPO, 'lote')

    asociar_permiso_a_grupo(persona_models.Paciente.NOMBRE_GRUPO, 'estadoestudio')
    asociar_permiso_a_grupo(persona_models.Paciente.NOMBRE_GRUPO, 'estudio', permisos=['view'])


class Ejemplos(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
            Inicializo datos de ejemplo de una persona y un estudio
        """
        persona_models.ObraSocial(nombre='Osde', telefono='221-4237467', email='consutlas@osde.com.ar').save()
        persona_models.ObraSocial(nombre='Swiss Medical', telefono='221-4237468', email='consutlas@swiss.com.ar').save()
        persona_models.ObraSocial(nombre='IOMA', telefono='221-4237467', email='consultas@ioma.gob.ar').save()
        persona_models.ObraSocial(nombre='OSFATUN', telefono='221-4237469', email='consultas@osfatun.com.ar').save()

        definir_permisos()
        crear_medicos_derivantes()
        generar_usuarios_de_sistema()
        generar_pacientes_mayores()
        generar_pacientes_menores()
        

        return Response({'status':'ejemplos generados'})

    def delete(self, request, format=None):

        return Response({'status':'ejemplos eliminados'})

