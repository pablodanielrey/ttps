from django.db.models.query import QuerySet
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

from django.db.models import Count   
from django.db.models.functions import ExtractMonth


import base64
import logging
import datetime
from zoneinfo import ZoneInfo
from dateutil import parser

from . import models
from personas import models as personas_models
from estudios import models as estudio_models
from turnos import models as turnos_models

"""
    Las vistas de rest framework
"""
from rest_framework import serializers, views, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from . import serializers
from . import pacientes_serializers

class VistaArchivos(viewsets.ReadOnlyModelViewSet):
    queryset = models.Archivo.objects.all()
    serializer_class = serializers.SerializadorArchivos

class VistaEstadisticas(viewsets.ModelViewSet):
    queryset = models.TiposDeEstudio.objects.all()
    serializer_class = serializers.SerializadorTiposDeEstudio
    
class VistaTemplateConsentimiento(viewsets.ModelViewSet):
    queryset = models.TemplateConsentimiento.objects.all()
    serializer_class = serializers.SerializadorTemplateConsentimiento

    def create(self, request, *args, **kwargs):
        datos = request.data['consentimiento']
        if not datos:
            return HttpResponseBadRequest('debe enviar el template de consentimiento')
        archivo = models.Archivo.from_datauri(datos)
        archivo.save()
        template = models.TemplateConsentimiento(archivo=archivo)
        template.save()
        serializador = self.serializer_class(instance=template)
        return Response(serializador.data)

    @action(detail=False, methods=['GET'])
    def valido(self, request):
        templates = models.TemplateConsentimiento.objects.filter(historico=False).order_by('-fecha')
        for template in templates:
            datos = template.archivo
            if not datos:
                return HttpResponseBadRequest()
            return HttpResponse(base64.b64decode(datos.contenido), content_type='application/pdf')        
        return HttpResponseNotFound()


    @action(detail=True, methods=['GET'])
    def contenido(self, request, pk=None):
        template = self.get_object()
        datos = template.archivo
        if not datos:
            return HttpResponseBadRequest()
        return HttpResponse(base64.b64decode(datos.contenido), content_type='application/pdf')        
        


class VistaTiposDeEstudio(viewsets.ModelViewSet):
    queryset = models.TiposDeEstudio.objects.all()
    serializer_class = serializers.SerializadorTiposDeEstudio


class VistaDiagnostico(viewsets.ModelViewSet):
    queryset = models.Diagnostico.objects.all()
    serializer_class = serializers.SerializadorDiagnostico


"""
    //////////// ESTADO DE ESTUDIOS ///////////////////
"""

class VistaEstadoEstudio(viewsets.ModelViewSet):
    queryset = models.EstadoEstudio.objects.all()
    serializer_class = serializers.SerializadorEstadoEstudioPolimorfico

    workflow = [
        models.EsperandoComprobanteDePago,
        models.EnviarConsentimientoInformado,
        models.EsperandoConsentimientoInformado,
        models.EsperandoSeleccionDeTurnoParaExtraccion,
        models.EsperandoTomaDeMuestra,
        models.EsperandoRetiroDeExtaccion,
        models.EsperandoLoteDeMuestraParaProcesamientoBiotecnologico,
        models.EsperandoInterpretacionDeResultados,
        models.EsperandoEntregaAMedicoDerivante,
        models.ResultadoDeEstudioEntregado
    ]


    def create(self, request, *args, **kwargs):
        """
            En nuestro caso los creates no se realizan extrictamente cumpliendo REST.
            Los create para las interfaces son modify de los estados actuales y se ejecuta el workflow.
        """

        estudio_id = request.data.pop('estudio_id')
        estudio = estudio_models.Estudio.objects.get(id=estudio_id)

        """
            TODO: debemos estar seguros de que no actualizamos ningún dato sensible desde afuera.
        """
        for campo_solo_lectura in ['id','fecha']:
            try:
                request.data.pop(campo_solo_lectura)
            except KeyError as e:
                pass

        ultimo_estado = estudio.ultimo_estado
        
        logging.debug(ultimo_estado)
        clase_ultimo_estado = ultimo_estado.__class__

        """ aca verifico estados finales """
        if clase_ultimo_estado in [ models.AnuladorPorFaltaDePago, models.ResultadoDeEstudioEntregado ]:
            return HttpResponseBadRequest('no se puede cambiar un estado final')

        """ aca manejo comportamientos especiales de los estados """
        if clase_ultimo_estado == models.EsperandoComprobanteDePago:
            """ solo pueden darse 2 casos. 1 - comprobante de pago, 2 - anulado por falta de pago """
            if 'fecha_procesado' in request.data:
                estado = models.AnuladorPorFaltaDePago(estudio=estudio, fecha_procesado=request.data['fecha_procesado'])
                estado.save()
                estudio.estados.add(estado)
                serializador = serializers.SerializadorEstadoEstudioPolimorfico(estado, context={'request': request})
                return Response(serializador.data)

            elif 'comprobante' in request.data:
                archivo = models.Archivo.from_datauri(request.data['comprobante'])
                archivo.save()
                ultimo_estado.comprobante = archivo
                ultimo_estado.save()

            else:
                return HttpResponseBadRequest()

        elif clase_ultimo_estado == models.EsperandoConsentimientoInformado:
            archivo = models.Archivo.from_datauri(request.data['consentimiento'])
            archivo.save()
            ultimo_estado.consentimiento = archivo
            ultimo_estado.save()

        elif clase_ultimo_estado == models.EsperandoSeleccionDeTurnoParaExtraccion:
            """ genero un turno """
            paciente = personas_models.Persona.objects.get(id=estudio.paciente.id)
            inicio = parser.parse(request.data['inicio'])
            fin = parser.parse(request.data['fin'])
            turno = turnos_models.TurnoConfirmado(persona=paciente,inicio=inicio, fin=fin)
            turno.save()
            logging.debug(f'turno generado {turno.id}')

            """ actualizo el estado """
            ultimo_estado.turno = turno
            ultimo_estado.save()

        elif clase_ultimo_estado == models.EsperandoTomaDeMuestra:

            if 'expirado' in request.data:
                pass
            else:
                pass    

        else:
            """ los casos normales de cambios de estado - se encarga el serializer """
            serializador = serializers.SerializadorEstadoEstudioPolimorfico.model_serializer_mapping[clase_ultimo_estado](instance=ultimo_estado, data=request.data)
            if not serializador.is_valid():
                return HttpResponseBadRequest(serializador.errors)
            if len(serializador.validated_data) <= 0:
                """ no existen datos enviados para actualizar el nuevo estado """
                return HttpResponseBadRequest()

            serializador.save()

        """
            Ahora paso al nuevo estado de acuerdo al workflow.
        """
        try:
            indice = self.workflow.index(clase_ultimo_estado)
            if indice+1 < len(self.workflow):
                clase_siguiente_estado = self.workflow[indice+1]
                siguiente_estado = clase_siguiente_estado(estudio=estudio)
                siguiente_estado.save()

        except ValueError as e:
            pass


        serializador = serializers.SerializadorEstadoEstudioPolimorfico(ultimo_estado, context={'request': request})
        return Response(serializador.data)

"""
    ///////////////////////////////////////////////
"""


class VistaEstudios(viewsets.ModelViewSet):
    queryset = models.Estudio.objects.all()
    serializer_class = serializers.SerializadorEstudiosRestringido

    custom_serializer_class = {
        personas_models.Empleado.NOMBRE_GRUPO: {
            'retrieve': serializers.SerializadorEstudiosDetalle,
            'list':serializers.SerializadorEstudios
        },
        personas_models.Paciente.NOMBRE_GRUPO: {
            'retrieve': pacientes_serializers.SerializadorEstudiosDetalle,
            'list': pacientes_serializers.SerializadorEstudios
        }
    }

    def __obtener_grupos_usuario_logueado(self):
        usuario = self.request.user
        grupos = [g.name for g in usuario.groups.all()]
        return grupos

    def get_serializer_class(self):
        grupos = self.__obtener_grupos_usuario_logueado()
        try:
            for k,v in self.custom_serializer_class.items():
                if k in grupos:
                    return v[self.action]
        except (KeyError, AttributeError) as e:
            pass
        return super().get_serializer_class()


    def get_queryset(self):
        """
            L2V-P2 -
            Aca se implementa la restricción de que el paciente solo puede ver sus estudios.
            Los demás perfiles ven todos los estudios.
        """
        grupos = self.__obtener_grupos_usuario_logueado()
        usuario = self.request.user
        if personas_models.Paciente.usuario_es_tipo(usuario):
            paciente = personas_models.Paciente.obtener_persona_de_usuario(usuario)
            return models.Estudio.objects.filter(paciente=paciente)

        return super().get_queryset()




    def create(self, request, *args, **kwargs):
        """
            Creamos el estudio e insertamos los estados iniciales por los que ya pasa en el momento de la generación.
        """

        datos = request.data
        #logging.debug(datos)
        presupuesto = models.Archivo.from_datauri(datos['presupuesto'])
        presupuesto.save()

        paciente = personas_models.Paciente.objects.get(id=datos['paciente']['id'])
        medico_derivante = personas_models.MedicoDerivante.objects.get(id=datos['medico_derivante']['id'])
        diagnostico = estudio_models.Diagnostico.objects.get(id=datos['diagnostico']['id'])
        tipo = estudio_models.TiposDeEstudio.objects.get(id=datos['tipo_estudio'])
        estudio = estudio_models.Estudio(
            paciente=paciente,
            medico_derivante=medico_derivante,
            diagnostico=diagnostico,
            tipo=tipo,
            fecha_alta=datos['fecha_alta'],
            presupuesto=presupuesto
        )
        estudio.save()

        hc = personas_models.HistoriaClinica.objects.filter(persona=paciente).first()
        hc.historia_clinica = datos['diagnostico_presuntivo']
        hc.save()

        esperando_comprobante = estudio_models.EsperandoComprobanteDePago(estudio=estudio)
        esperando_comprobante.save()

        serializer = serializers.SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)

    def modify(self, request, *args, **kwargs):

        estudio_id = request.data['estudio_id']
        estudio = models.Estudio.objects.get(estudio_id)

        """
        ultimo_estado = estudio.estados.all('fecha').last()
        switch ultimo_estado.nombre:
            'EspernadoComprobante':
                comprobante_b64 = request.data['comprobante']
                ultimo_estado.comprobante = comprobante_b64
                ultimo_estado.save()
            
            'EsperandoPresupeusto':
                comprobante_b64 = request.data['presupuesto']
                ultimo_estado.presupuesto = comprobante_b64
                ultimo_estado.fecha = request.data['fecha']
                ultimo_estado.save()

        """
        serializer = serializers.SerializadorEstudios(estudio, context={'request': request})
        return Response(serializer.data)
        
    @action(detail=False, methods=['GET'])
    def buscar(self, request):
        q = request.query_params.get('q')
        e = request.query_params.get('e',None)
        logging.debug(f'buscando a : {q}  en estado : {e}')

        estudios = models.Estudio.buscar(q, e)
        serializer = serializers.SerializadorEstudios(estudios, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def presupuesto(self, request, pk=None):
        estudio = self.get_object()
        datos = estudio.presupuesto
        if not datos:
            return HttpResponseBadRequest('no existe presupuesto para el estudio')
        return HttpResponse(base64.b64decode(datos.contenido), content_type='application/pdf')


    @action(detail=True, methods=['GET'])
    def comprobante_de_pago(self, request, pk=None):
        estudio = self.get_object()
        datos = estudio.comprobante_de_pago
        if not datos:
            return HttpResponseBadRequest('no existe comprobante para el estudio')
        return HttpResponse(base64.b64decode(datos.contenido), content_type='application/pdf')
    
    @action(detail=True, methods=['GET'])
    def consentimiento_informado(self, request, pk=None):
        estudio = self.get_object()
        datos = estudio.consentimiento_informado
        if not datos:
            return HttpResponseBadRequest('no existe consentimiento para el estudio')
        return HttpResponse(base64.b64decode(datos.contenido), content_type='application/pdf')   
        


    """
        TODO: esto hace falta pasarlo a una api especifica de estadístinas y no en el estudio!
    """

    @action(detail=False, methods=['GET'])
    def estudios_estadisitcas_mes(self, request):        
        cantidadPorMes = models.Estudio.objects.annotate(month=ExtractMonth('fecha_alta')).values('month').annotate(count=Count('id')).values('month', 'count')  
        
        
        print(cantidadPorMes)
        return Response({'Estudios': cantidadPorMes})

    @action(detail=False, methods=['GET'])
    def tipos_estudio(self, request):        
        tipos={}
        index=0
        tipoEstudio = models.TiposDeEstudio.objects.all()
        for tipo in tipoEstudio:  
            tipos[index]=({
                "tipo": tipo.nombre,
                "cantidad": models.Estudio.objects.filter(tipo= tipo).count()
            })
            index=index +1 

        return Response({'Estudios': tipos})
    



