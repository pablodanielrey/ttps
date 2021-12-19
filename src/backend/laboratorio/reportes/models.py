import datetime
from zoneinfo import ZoneInfo

from django.db import models
from rest_framework.response import Response
from estudios import models
from django.db.models.functions import ExtractMonth
from django.db.models import Count
class Reportes:

    def __generar_fecha_now(self):
        return datetime.datetime.now(tz=ZoneInfo('America/Argentina/Buenos_Aires'))

    def __generar_cabecera_reporte(self):
        return {
            'fecha_de_reporte': self.__generar_fecha_now()
        }

    """
        LV-E23
    """
    def cantidad_de_estudios_por_tipo(self):
        tipos={}
        index=0
        tipoEstudio = models.TiposDeEstudio.objects.all()
        for tipo in tipoEstudio:  
            tipos[index]=({
                "tipo": tipo.nombre,
                "cantidad": models.Estudio.objects.filter(tipo= tipo).count()
            })
            index=index +1 
        
        return tipos



    """
        LV-E25d
        def cantidad_de_estudios_por_mes(self):
        estudios = models.Estudio.objects.all()
        reporte = {}
        for e in estudios:
            mes = e.fecha_alta.month
            if mes not in reporte:
                reporte[mes] = 0
            reporte[mes] += 1
            
        return {
            'reporte': self.__generar_cabecera_reporte(),
            'datos': reporte
        }

    """
    def cantidad_de_estudios_por_mes(self):
        cantidadPorMes = models.Estudio.objects.annotate(month=ExtractMonth('fecha_alta')).values('month').annotate(count=Count('id')).values('month', 'count')  
        return cantidadPorMes
    

    """
        LV-E27
    """
    def demora_de_procesamiento_de_estudios(self):
        estudios = models.Estudio.objects.all()
        reporte = {}
        for e in estudios:
            fecha_muestra = None
            fecha_entrega = None
            
            for estado in e.estados.order_by('fecha'):
                if isinstance(estado, models.EsperandoTomaDeMuestra):
                    fecha_muestra = estado.fecha_muestra
                elif isinstance(estado, models.EsperandoEntregaAMedicoDerivante):
                    fecha_entrega = estado.fecha_entrega
                if fecha_muestra and fecha_entrega:
                    break
            else:
                continue
            
            tardanza = (fecha_entrega - fecha_muestra).seconds
            mes = e.fecha_alta.month
            if mes not in reporte:
                reporte[mes] = {
                    "procesados": 0,
                    "tardanza_segundos": 0
                }
            reporte[mes]['tardanza_segundos'] += tardanza
            reporte[mes]['procesados'] += 1

        return {
            "reporte": self.__generar_cabecera_reporte(),
            "datos": reporte
        }
        
