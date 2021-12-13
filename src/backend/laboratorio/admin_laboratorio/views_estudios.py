

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
from turnos import models as turnos_models

def generar_fecha_now():
    return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))


def pdf_minimo():
    return "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="

def generar_estudio(medico, paciente):
    archivo = estudio_models.Archivo(contenido=pdf_minimo(), content_type='application/pdf', encoding='base64')
    archivo.save()

    tipo_estudio = estudio_models.TiposDeEstudio.objects.first()
    diagnostico = estudio_models.Diagnostico.objects.first()
    estudio = estudio_models.Estudio(paciente=paciente, medico_derivante=medico, diagnostico=diagnostico, tipo=tipo_estudio, presupuesto=archivo)
    estudio.save()
    return estudio

def generar_estudio_anulado_por_falta_de_pago(empleado, medico, paciente):
    estudio = generar_estudio(medico, paciente)
    estado = estudio_models.EsperandoComprobanteDePago(estudio=estudio, persona=empleado)
    estado.save()
    estado = estudio_models.AnuladorPorFaltaDePago(estudio=estudio, persona=empleado, fecha_procesado=generar_fecha_now())
    estado.save()
    

def generar_estudios_estado1(empleado, medico, paciente):
    estudio = generar_estudio(medico, paciente)
    estado = estudio_models.EsperandoComprobanteDePago(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado2(empleado, medico, paciente):
    archivo = estudio_models.Archivo(contenido=pdf_minimo(), content_type='application/pdf', encoding='base64')
    archivo.save()
    estudio = generar_estudios_estado1(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.comprobante = archivo
    estado.save()
    estado = estudio_models.EnviarConsentimientoInformado(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado3(empleado, medico, paciente):
    estudio = generar_estudios_estado2(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_enviado = generar_fecha_now()
    estado.save()
    estado = estudio_models.EsperandoConsentimientoInformado(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado4(empleado, medico, paciente):
    archivo = estudio_models.Archivo(contenido=pdf_minimo(), content_type='application/pdf', encoding='base64')
    archivo.save()
    estudio = generar_estudios_estado3(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.consentimiento = archivo
    estado.save()
    estado = estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado5(empleado, medico, paciente):
    archivo = estudio_models.Archivo(contenido=pdf_minimo(), content_type='application/pdf', encoding='base64')
    archivo.save()
    turno = turnos_models.TurnoConfirmado(persona=paciente, inicio=generar_fecha_now(), fin=generar_fecha_now() + datetime.timedelta(hours=1))
    turno.save()
    estudio = generar_estudios_estado4(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.turno = turno
    estado.save()
    estado = estudio_models.EsperandoTomaDeMuestra(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudio_turno_expirado(empleado, medico, paciente):
    estudio = generar_estudios_estado5(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.expirado = True
    estado.save()
    estado = estudio_models.EsperandoSeleccionDeTurnoParaExtraccion(estudio=estudio, persona=empleado)
    estado.save()    

def generar_estudios_estado6(empleado, medico, paciente):
    estudio = generar_estudios_estado5(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_muestra = generar_fecha_now()
    estado.milimetros = 3.4
    estado.freezer = '10e'
    estado.save()
    estado = estudio_models.EsperandoRetiroDeExtaccion(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado7(empleado, medico, paciente):
    estudio = generar_estudios_estado6(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_retiro = generar_fecha_now()
    estado.extracionista = 'pepe se lo lleva'
    estado.save()
    estado = estudio_models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado8(empleado, medico, paciente):
    estudio = generar_estudios_estado7(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.numero_lote = 'loteeeeee'
    estado.save()
    estado = estudio_models.EsperandoProcesamientoDeLoteBiotecnologico(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado9(empleado, medico, paciente):
    estudio = generar_estudios_estado8(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_resultado = generar_fecha_now()
    estado.resutlado_url = 'http://www.google.com/'
    estado.save()
    estado = estudio_models.EsperandoInterpretacionDeResultados(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado10(empleado, medico, paciente):
    medico_informante = persona_models.MedicoInformante.objects.first()
    estudio = generar_estudios_estado9(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_informe = generar_fecha_now()
    estado.medico_informante = medico_informante
    estado.informe = pdf_minimo()
    estado.resultado = 'un resultado'
    estado.save()
    estado = estudio_models.EsperandoEntregaAMedicoDerivante(estudio=estudio, persona=empleado)
    estado.save()
    return estudio

def generar_estudios_estado11(empleado, medico, paciente):
    estudio = generar_estudios_estado10(empleado, medico, paciente)
    estado = estudio.ultimo_estado
    estado.fecha_entrega = generar_fecha_now()
    estado.save()
    estado = estudio_models.ResultadoDeEstudioEntregado(estudio=estudio, persona=empleado)
    estado.save()
    return estudio


def eliminar_estudios():
    for estados in estudio_models.EstadoEstudio.objects.all():
        estados.delete()
        
    for e in estudio_models.Estudio.objects.all():
        e.delete()


class Ejemplos(APIView):
    
    permission_classes= [permissions.IsAdminUser]

    def get(self, request, format=None):

        empleado = persona_models.Empleado.objects.first()
        medico_derivante = persona_models.MedicoDerivante.objects.first()
        paciente = persona_models.Paciente.objects.first()

        generar_estudio_anulado_por_falta_de_pago(empleado, medico_derivante, paciente)
        generar_estudios_estado1(empleado, medico_derivante, paciente)
        generar_estudios_estado2(empleado, medico_derivante, paciente)
        generar_estudios_estado3(empleado, medico_derivante, paciente)
        generar_estudios_estado4(empleado, medico_derivante, paciente)
        generar_estudios_estado5(empleado, medico_derivante, paciente)
        generar_estudios_estado6(empleado, medico_derivante, paciente)
        generar_estudios_estado7(empleado, medico_derivante, paciente)
        generar_estudios_estado8(empleado, medico_derivante, paciente)
        generar_estudios_estado9(empleado, medico_derivante, paciente)
        generar_estudios_estado10(empleado, medico_derivante, paciente)
        generar_estudios_estado11(empleado, medico_derivante, paciente)

        return Response({'status':'ejemplos de estudios generados'})

    def delete(self, request, format=None):
        eliminar_estudios()
        return Response({'status':'ejemplos eliminados'})

