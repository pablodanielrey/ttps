from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Persona)
admin.site.register(models.ObraSocialPersona)
admin.site.register(models.ObraSocial)