from django.contrib import admin

# Register your models here.
from .models import Persona, ObraSocial

admin.site.register(Persona)
admin.site.register(ObraSocial)