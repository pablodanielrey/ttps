import logging
from rest_framework import serializers

from estudios import serializers as estudio_serializers
from . import models
from estudios import models as estudio_models
class SerializadorDeEstudioDeLote(serializers.ModelSerializer):
    estudio = estudio_serializers.SerializadorEstudiosMinimo()
    class Meta:
        model = models.EstudioDeLote
        fields = ['id', 'estudio']

class SerializadorDeLote(serializers.ModelSerializer):
    estudios = SerializadorDeEstudioDeLote(many=True)
    class Meta:
        model = models.Lote
        fields = ['id', 'fecha', 'resultado','estudios']

    def update(self, instance, validated_data):
        logging.debug(validated_data)
        estudios_ok = [e['estudio']['id'] for e in validated_data.get('estudios',[])]
        logging.debug(f'estudios correctos {estudios_ok}')
        estudios_de_lote = instance.estudios.all()
        for estudioLote in estudios_de_lote:
            estudio = estudioLote.estudio
            if estudio.id in estudios_ok:
                logging.debug(f'cambiando estudio {estudio.id} a resuelto')
                estado = estudio.ultimo_estado
                estado.fecha_resultado = instance.fecha
                estado.resultado_url = instance.resultado
                estado.save()
                estudio_models.EsperandoInterpretacionDeResultados.objects.create(estudio=estudio)
            else:
                logging.debug(f'cambiando estudio {estudio.id} a fallado')
                estudio_models.EsperandoSeleccionDeTurnoParaExtraccion.objects.create(estudio=estudio)


        instance.resultado = validated_data.get('resultado', instance.resultado)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.save()

        return instance

