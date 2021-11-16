

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


def generar_estudio_de_muestra():

    empleado = persona_models.Persona.objects.all().first()

    p1 = persona_models.Persona(nombre='Paciente', apellido='Cero', dni='000001', email='paciente@cero.com', telefono='221-1112233', fecha_nacimiento='1980-12-01')
    p1.save()
    mm = persona_models.Persona(nombre='Medi', apellido='Cote', dni='2212211', email='m@hotmail.com', telefono='221-1112233', fecha_nacimiento='1995-06-02')
    mm.save()

    ob_social = persona_models.ObraSocial.objects.all().first()
    obp = persona_models.ObraSocialPersona(persona=p1, obra_social=ob_social, numero_afiliado='afiliate12345')
    obp.save()

    tipoe = estudio_models.TiposDeEstudio.objects.all().first()
    diagnostico = estudio_models.Diagnostico.objects.all().first()
    estudio = estudio_models.Estudio(paciente=p1,  tipo=tipoe, medico_derivante=mm, diagnostico=diagnostico)
    estudio.save()


    estudio_models.EsperandoRetiroDeExtaccion(persona=empleado, estudio=estudio, extracionista='pepe se la lleva a la muestra', fecha_retiro=generar_fecha_now()).save()
    estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado).save()
    


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



class Ejemplos(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
            Inicializo datos de ejemplo de una persona y un estudio
        """
        persona_models.ObraSocial(nombre='Osde', telefono='221-4237467', email='consutlas@osde.com.ar').save()
        persona_models.ObraSocial(nombre='IOMA', telefono='221-4237467', email='consutlas@ioma.gov.ar').save()

        p1 = persona_models.Persona(nombre='Pablo', apellido='R', dni='1', email='pablo@supermail.com', telefono='221-1112233', fecha_nacimiento='1980-12-01')
        p1.save()
        persona_models.Persona(nombre='Leonardo', apellido='B', dni='2211', email='leo@supermail.com', telefono='221-1112233', fecha_nacimiento='1981-02-03').save()
        persona_models.Persona(nombre='Nico', apellido='G', dni='2222211', email='nico@supermail.com', telefono='221-1112233', fecha_nacimiento='2004-05-04').save()

        mm = persona_models.Persona(nombre='Medi', apellido='Cote', dni='2212211', email='m@hotmail.com', telefono='221-1112233', fecha_nacimiento='1995-06-02')
        mm.save()

        generar_estudio_de_muestra()
        generar_lote()

        return Response({'status':'ejemplos generados'})

    def delete(self, request, format=None):

        return Response({'status':'ejemplos eliminados'})

