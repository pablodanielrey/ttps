from rest_framework import serializers

from . import models
from personas import paciente_serializers

class SerializadorRangoTurnos(serializers.ModelSerializer):
    class Meta:
        model = models.RangoDeTurnos
        fields = ['id', 'hora_inicio', 'hora_fin', 'frecuencia']

class SerializadorParametroTurnos(serializers.ModelSerializer):

    rangos = SerializadorRangoTurnos(many=True, read_only=False)

    class Meta:
        model = models.ParametroDeTurnos
        fields = ['id','fecha_valido','rangos']

    def create(self, validated_data):
        fecha_valido = validated_data.get('fecha_valido')

        parametros = models.ParametroDeTurnos(fecha_valido=fecha_valido)
        parametros.save()

        rangos = validated_data.get('rangos')
        for r in rangos:
            models.RangoDeTurnos.objects.create(parametros=parametros, hora_inicio=r['hora_inicio'], hora_fin=r['hora_fin'], frecuencia=r['frecuencia'])

        parametros.refresh_from_db()
        return parametros


class SerializadorFechasSinTurno(serializers.ModelSerializer):
    class Meta:
        model = models.FechasSinTurno
        fields = ['id','fecha']


class SerializadorTurnosConfirmados(serializers.HyperlinkedModelSerializer):
    persona = paciente_serializers.SerializadorDePaciente(required=False, read_only=True)
    cancelado = serializers.DateTimeField(required=False,read_only=False)
    class Meta:
        model = models.TurnoConfirmado
        fields = ['id','persona','inicio','fin','cancelado']