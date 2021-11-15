from django.contrib import admin

# Register your models here
# .

from . import models

admin.site.register(models.ParametroDeTurnos)
admin.site.register(models.RangoDeTurnos)
admin.site.register(models.FechasSinTurno)
admin.site.register(models.TurnoConfirmado)
