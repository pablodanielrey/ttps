import logging
logging.getLogger().setLevel(logging.DEBUG)

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Person, Identification

# Create your views here.

def index(request):
    context = {
        'persons': Person.objects.all()
    }
    #template = loader.get_template('persons/index.tmpl')
    #return HttpResponse(template.render(context, request))
    return render(request, 'persons/index.tmpl', context)


def detail(request, person_id):
    logging.debug(f'buscando persona con id : {person_id}')
    person = Person.objects.filter(id=person_id).first()
    if not person:
        raise Http404('Persona no encontrada')
    context = {
        'person': person
    }
    logging.debug(context)
    return render(request, 'persons/detail.tmpl', context)




def add(request):
    try:
        dni = request.POST['dni']
        name = request.POST['name']
        lastname = request.POST['lastname']
        person = Person.objects.create_person(dni, name, lastname)
        return HttpResponseRedirect(reverse('persons:detail', args=(person.id,)))
    except KeyError:
        return render(request, 'persons/add.tmpl')
