

from django.db.utils import IntegrityError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import logging
import datetime
from zoneinfo import ZoneInfo
import random

from personas import models as persona_models

def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

def generar_usuarios_ejemplo():
    m = persona_models.PersonasModel()

    try:
        m.crearPaciente(nombre='Paciente',apellido='Cero',dni='11111111', historia_clinica='nada que contar')
    except IntegrityError:
        pass

    inicio = random.randrange(0,100)
    pacientes = []
    for i in range(inicio,inicio+10):
        ano = f'{i+1}'.zfill(2)
        pacientes.append(
            {
                'nombre': f'nombre{i}',
                'apellido': f'apellido{i}',
                'dni':f'{i}',
                'email': f'email{i}@gmail.com',
                'telefono': f'221 2222{i}',
                'direccion': f'calle {i} la plata',
                'fecha_nacimiento': f'2021-04-22',
                'historia_clinica': f'algo de historia {ano}'
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

    try:
        m.crearMedicoInformante(nombre='Medico', apellido="informante", email='medico1@simed.com', matricula='123er', usuario='medico2', clave='informante2')
    except IntegrityError as e:
        pass

def generar_usuarios_de_sistema():
    m = persona_models.PersonasModel()
    try:
        m.crearAdministrador("Super","Admin", "administrador", "ttp")
        m.crearConfigurador("Configurador","sistema", "configurador", "ttp")
        m.crearEmpleado("Empleado1", "Apellido1", "empleado", "ttp")
        m.crearEmpleado("Empleado2", "Apellido2", "empleado2", "ttp")
        m.crearMedicoInformante("Medico","Informante","medico@simed.com", "matricula_de_informante1", "medicoinf", "ttp")
    except IntegrityError as e:
        pass

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

        p1 = persona_models.Persona(nombre='Pablo', apellido='Marmol', dni='10561134', email='pablo@roca.com', telefono='2211234567', fecha_nacimiento='1980-12-01').save()
        persona_models.Persona(nombre='Leonardo', apellido='Da vinci', dni='6345345', email='leo@diflorencia.com', telefono='2211112233', fecha_nacimiento='1981-02-03').save()
        persona_models.Persona(nombre='Nicolas', apellido='Otamendi', dni='35123456', email='nico@afa.com.ar', telefono='2211112233', fecha_nacimiento='2004-05-04').save()

        mm = persona_models.Persona(nombre='Nick', apellido='Riviera', dni='22123123', email='barat@operation.com', telefono='2211112233', fecha_nacimiento='1995-06-02').save()

        generar_usuarios_ejemplo()
        generar_usuarios_de_sistema()

        return Response({'status':'ejemplos generados'})

    def delete(self, request, format=None):

        return Response({'status':'ejemplos eliminados'})

