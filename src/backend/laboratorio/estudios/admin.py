from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Estudio)
admin.site.register(models.EstadoEstudio)
admin.site.register(models.Diagnostico)
admin.site.register(models.ParametroDeTurnos)
admin.site.register(models.RangoDeTurnos)
admin.site.register(models.FechasSinTurno)
admin.site.register(models.TurnoConfirmado)
