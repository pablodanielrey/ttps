from django.db import models

from estudios import models
class Reportes:

    """
        LV-E23
    """
    def cantidad_de_estudios_por_tipo(self):
        estudios = models.Estudio.objects.all()
        reporte = {}
        for e in estudios:
            tipo = e.tipo.nombre
            if tipo not in reporte:
                reporte[tipo] = 0
            reporte[tipo] += 1
        return reporte


    """
        LV-E25
    """
    def cantidad_de_estudios_por_mes(self):
        estudios = models.Estudio.objects.all()
        reporte = {}
        for e in estudios:
            mes = e.fecha_alta.month
            if mes not in reporte:
                reporte[mes] = 0
            reporte[mes] += 1
        return reporte


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
                    'procesados': 0,
                    'tardanza': 0
                }
            reporte[mes]['tardanza'] += tardanza
            reporte[mes]['procesados'] += 1

        return reporte