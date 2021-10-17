from django.http.request import HttpRequest
from django.shortcuts import render

from django.contrib import messages

import logging
# Create your views here.

def agregar_persona(request:HttpRequest):
    if request.method == 'POST':
        logging.debug(request.POST['nombre'])
        logging.debug(request.POST['apellido'])
        messages.success(request, 'Paciente agregado correctamente')

    return render(request, 'personas/agregar.html')