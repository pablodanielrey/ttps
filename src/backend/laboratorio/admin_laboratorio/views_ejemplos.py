

from django.db.utils import IntegrityError
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import logging
import datetime
from zoneinfo import ZoneInfo

from estudios import models as estudio_models
from personas import models as persona_models

def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))


def generar_lote():
    from personas import models as persona_models

    empleado = persona_models.Persona.objects.all().first()

    tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    diagnostico = estudio_models.Diagnostico.objects.all().first()

    for _ in range(0,25):
        estudio = estudio_models.Estudio(paciente=empleado,  tipo=tipoe, medico_derivante=empleado, diagnostico=diagnostico)
        estudio.save()

        estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
        estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()


def aca_podes_editar_lean():

    # lean aca esta el codigo que va!!
    m = persona_models.PersonasModel()
    m.crearPaciente(nombre='Leandro', apellido='Bilbao', dni='32070891', email='leandrobilbao@gmail.com', telefono='2211234567', direccion='calle falsa 123', fecha_nacimiento='1995-06-02', historia_clinica='ufff por donde empiezo', )
    m2 = persona_models.PersonasModel()
    m2.crearPaciente(nombre='Leandro2', apellido='Bilbao2', dni='32070892', email='leandrobilbao2@gmail.com', telefono='2211234568', direccion='calle falsa 123bis', fecha_nacimiento='1995-06-03', historia_clinica='ufff por donde empiezo, mas atras', )



def generar_estudio_de_muestra():


    empleado = persona_models.Persona.objects.all().first()

    # p1 = persona_models.Paciente(nombre='Paciente', apellido='Cero', dni='000001', email='paciente@cero.com', telefono='221-1112233', fecha_nacimiento='1980-12-01')
    # p1.save()
    # mm = persona_models.Paciente(nombre='Medi', apellido='Cote', dni='2212211', email='m@hotmail.com', telefono='221-1112233', fecha_nacimiento='1995-06-02')
    # mm.save()

    # ob_social = persona_models.ObraSocial.objects.all().first()
    # obp = persona_models.ObraSocialPersona(persona=p1, obra_social=ob_social, numero_afiliado='afiliate12345')
    # obp.save()

    # tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    # diagnostico = estudio_models.Diagnostico.objects.all().first()
    # estudio = estudio_models.Estudio(paciente=p1,  tipo=tipoe, medico_derivante=mm, diagnostico=diagnostico)
    # estudio.save()


    # estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
    # estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()
    


    # #estudio_models.EsperandoPresupuesto(persona=empleado, estudio=estudio, presupuesto=10.3).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324324', monto=10.5).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324325', monto=11.5, obra_social=ob_social).save()
    # estudio_models.EsperandoComprobanteDePago(persona=empleado, estudio=estudio, comprobante='base64-del-comprobante').save()
    # estudio_models.AnuladorPorFaltaDePago(persona=empleado, estudio=estudio).save()


    # tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    # diagnostico = estudio_models.Diagnostico.objects.all().first()
    # estudio = estudio_models.Estudio(paciente=p1,  tipo=tipoe, medico_derivante=mm, diagnostico=diagnostico)
    # estudio.save()

    # #estudio_models.EsperandoPresupuesto(persona=empleado, estudio=estudio, presupuesto=10.3).save()
    # #estudio_models.EsperandoFactura(persona=empleado, estudio=estudio, numero='dsaasd324325', monto=11.5, obra_social=ob_social).save()
    # estudio_models.EsperandoComprobanteDePago(persona=empleado, estudio=estudio, comprobante='base64-del-comprobante').save()
    # estudio_models.EsperandoConsentimientoInformado(persona=empleado, estudio=estudio, consentimiento='base64-del-consntimiento').save()

    # #estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(persona=empleado, estudio=estudio, turno=generar_fecha_now()).save()
    # estudio_models.EsperandoTomaDeMuestra(persona=empleado, estudio=estudio, expirado=True).save()
    
    # #estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(persona=empleado, estudio=estudio, turno=generar_fecha_now()).save()
    # estudio_models.EsperandoTomaDeMuestra(persona=empleado, estudio=estudio, fecha_muestra=generar_fecha_now(), mililitros=145, freezer=10, expirado=False).save()
    # estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
    
    # estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(persona=empleado, estudio=estudio,numero_lote='2ef').save()
    # estudio_models.EsperandoProcesamientoDeLoteBiotecnologico(persona=empleado, estudio=estudio, resultado_url='https://www.google.com/informe.pdf', fecha_resultado=generar_fecha_now()).save()
    # estudio_models.EsperandoInterpretacionDeResultados(persona=empleado, estudio=estudio, fecha_informe=generar_fecha_now(), medico_informante=mm, informe='estas recontra bien. andate de vacaciones').save()
    # estudio_models.EsperandoEntregaAMedicoDerivante(persona=empleado, estudio=estudio, fecha_entrega=generar_fecha_now()).save()


def generar_usuarios_ejemplo():
    m = persona_models.PersonasModel()

    pacientes = []
    for i in range(0,10):
        ano = f'{i+1}'.zfill(2)
        pacientes.append(
            {
                'nombre': f'nombre{i}',
                'apellido': f'apellido{i}',
                'dni':f'{i}',
                'email': f'email{i}@gmail.com',
                'telefono': f'221 2222{i}',
                'direccion': f'calle {i} la plata',
                'fecha_nacimiento': f'2021-04-{ano}',
                'historia_clinica': ''
            }
        )
    for paciente in pacientes:
        try:
            m.crearPaciente(**paciente)
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
        m.crearAdministrador("Super","Admin", "administrador", "administrador")
        m.crearConfigurador("Configurador","sistema", "configurador", "configurador")
        m.crearEmpleado("Empleado1", "Apellido1", "empleado", "empleado")
        m.crearEmpleado("Empleado2", "Apellido2", "empleado2", "empleado2")
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

        p1 = persona_models.Persona(nombre='Pablo', apellido='Marmol', dni='10561134', email='pablo@roca.com', telefono='2211234567', fecha_nacimiento='1980-12-01')
        p1.save()
        persona_models.Persona(nombre='Leonardo', apellido='Da vinci', dni='6345345', email='leo@diflorencia.com', telefono='2211112233', fecha_nacimiento='1981-02-03').save()
        persona_models.Persona(nombre='Nicolas', apellido='Otamendi', dni='35123456', email='nico@afa.com.ar', telefono='2211112233', fecha_nacimiento='2004-05-04').save()

        mm = persona_models.Persona(nombre='Nick', apellido='Riviera', dni='22123123', email='barat@operation.com', telefono='2211112233', fecha_nacimiento='1995-06-02')
        mm.save()

        generar_estudio_de_muestra()
        generar_lote()

        generar_usuarios_ejemplo()
        generar_usuarios_de_sistema()
        aca_podes_editar_lean()

        return Response({'status':'ejemplos generados'})

    def delete(self, request, format=None):

        return Response({'status':'ejemplos eliminados'})

