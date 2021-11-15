from django.db import models

# Create your models here.
import uuid
import logging
import datetime

from personas.models import Persona, ObraSocial

class ParametroDeTurnos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_valido = models.DateTimeField()

    def __str__(self):
        rangos = " | ".join([r.__str__() for r in self.rangos.all() ])
        return f"desde : {self.fecha_valido} rangos: [ {rangos} ]" 

class RangoDeTurnos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parametros = models.ForeignKey(ParametroDeTurnos, on_delete=models.CASCADE, related_name='rangos')
    hora_inicio = models.IntegerField()
    hora_fin = models.IntegerField()
    frecuencia = models.IntegerField(default=15)

    def __str__(self):
        return f"inicio:{self.hora_inicio} - fin:{self.hora_fin} - freq:{self.frecuencia}"

class FechasSinTurno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()

    def __str__(self):
        return self.fecha


class TurnoConfirmado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

# from dataclasses import dataclass
# @dataclass
# class Turno:
#     inicio: datetime.datetime
#     fin: datetime.datetime

class ModeloTurnos:

    def obtener_turnos_hoy(self):
        hoy = datetime.datetime.combine(datetime.date.today(), datetime.time(0))
        manana = datetime.timedelta(hours = 24) + hoy
        al_infinito_y_mas_alla = hoy + datetime.timedelta(days=30)
        return self.obtener_turnos(hoy,al_infinito_y_mas_alla)

    def obtener_turnos_confirmados(self, desde:datetime.datetime, hasta:datetime.datetime):
        confirmados = TurnoConfirmado.objects.filter(inicio__range=[desde, hasta])
        return confirmados

    def _eliminar_turnos_confirmados(self, turnos_confirmados, turnos):
        """ 
            TODO: totalmente ineficiente!!! se debe reemplazar por las clases correctas
            dataclasess, estructuras estilo set, binary search ,etc
            lo dejo para llegar con el tiempo y despues analizar
        """ 
        def _chequear_que_no_solapa(turno, turno_confirmado):
            return turno['inicio'] > turno_confirmado.fin or turno['fin'] < turno_confirmado.inicio  
    
        def _eliminar_turnos_solapados(turno_confirmado, turnos):
            return [t for t in turnos if _chequear_que_no_solapa(t, turno_confirmado) ]                    
        
        turnos_filtrados = []
        turnos_filtrados.extend(turnos)
        for turno_confirmado in turnos_confirmados:
            turnos_filtrados = _eliminar_turnos_solapados(turno_confirmado, turnos_filtrados)
        return turnos_filtrados

    def obtener_turnos(self, desde:datetime.datetime, hasta:datetime.datetime):
        """ 
            genera los turnos entre las fechas determinadas, a partir de los parámetros definidos dentro de la base.
        """
        turnos_confirmados = self.obtener_turnos_confirmados(desde, hasta)

        turnos = []

        """ selecciono la fecha/hora inicial de todo el rango de turnos """
        inicio = ParametroDeTurnos.objects.filter(fecha_valido__lte=desde).order_by('fecha_valido').last()
        if not inicio:
            inicio = ParametroDeTurnos.objects.order_by('fecha_valido').first()
        fecha_inicial = inicio.fecha_valido
        fecha_turnos_desde = fecha_inicial if fecha_inicial > desde else desde

        fechas_sin_turnos = [f.fecha for f in FechasSinTurno.objects.all()]

        turno_actual = hasta
        un_dia = datetime.timedelta(days=1)

        """ obtengo todos los parámetros definidos entre las fechas que me interesa obtener los turnos """
        parametros = ParametroDeTurnos.objects.filter(fecha_valido__gte=fecha_inicial, fecha_valido__lte=hasta).order_by('-fecha_valido').all()
        for parametro in parametros:
            rangos:RangoDeTurnos = parametro.rangos.order_by('hora_inicio').all()
            a_partir_de = parametro.fecha_valido

            """ genero las fechas para el rango dado """
            while fecha_turnos_desde <= turno_actual and a_partir_de <= turno_actual:
                fecha_de_turno = turno_actual.date()
                if fecha_de_turno in fechas_sin_turnos:
                    turno_actual -= un_dia
                    continue
                if fecha_de_turno.weekday() >= 5:
                    """ 
                        asumo que los días laborables son de lunes-viernes
                        0 - lunes ..... 6 - domingo
                    """
                    turno_actual -= un_dia
                    continue
                turnos_del_dia = self._generar_turnos_para_dia(turno_actual, rangos)

                """ TODO: ver si no es mejor resolverlo de otra forma """
                #turnos_del_dia_filtrados = turnos_del_dia
                turnos_del_dia_filtrados = self._eliminar_turnos_confirmados(turnos_confirmados, turnos_del_dia)

                turnos.extend(turnos_del_dia_filtrados)
                turno_actual -= un_dia

        return sorted(turnos, key=lambda x: x['inicio'])

    def _generar_turnos_para_dia(self, fecha, rangos):
        """
            TODO: verificar que fecha siempre esta en la hora 00 del timezone que queremos manejar.
        """
        un_segundo = datetime.timedelta(seconds=1)
        turnos = []
        for rango in rangos:
            frecuencia = datetime.timedelta(minutes=rango.frecuencia)
            # hora_de_turno = fecha.replace(hour=rango.hora_inicio, minute=0, second=0, microsecond=0)
            # hora_de_fin = fecha.replace(hour=rango.hora_fin, minute=0, second=0, microsecond=0)
            hora_de_turno = fecha + datetime.timedelta(hours=rango.hora_inicio)
            hora_de_fin = fecha + datetime.timedelta(hours=rango.hora_fin)
            nuevo_turno = hora_de_turno + frecuencia
            while nuevo_turno <= hora_de_fin:
                turnos.append(self._formatear_turno(hora_de_turno, nuevo_turno - un_segundo))
                hora_de_turno = nuevo_turno
                nuevo_turno += frecuencia
        return turnos

    def _formatear_turno(self, hora_turno, fin_turno):
        return {
            'inicio': hora_turno,
            'fin': fin_turno
        }
        #return Turno(inicio=hora_turno, fin=hora_turno)


    def _completar_datos_turnos(self, turnos):
        return [{
            'hora':hora_de_turno,
            'fecha':hora_de_turno.date(),
            'día':self._dia_de_la_semana(hora_de_turno.date())
        } for hora_de_turno in turnos]

    def _dia_de_la_semana(self, fecha):
        dia = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        return dia[fecha.weekday()]
        