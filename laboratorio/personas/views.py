from django.forms.forms import Form
from django.http.request import HttpRequest
from django.shortcuts import render
from django.forms import ModelForm

from django.contrib import messages

from . import models

import logging
# Create your views here.

class FormularioPersona(ModelForm):
    class Meta:
        model = models.Persona
        fields = ['usuario', 'dni', 'telefono', 'fecha_nacimiento', 'historia_clinica']

def agregar_persona(request:HttpRequest):
    if request.method == 'POST':
        datos = FormularioPersona(request.POST)
        logging.debug(datos)
        messages.success(request, 'Paciente agregado correctamente')

    return render(request, 'personas/agregar.html', {
        'form': FormularioPersona()
    })