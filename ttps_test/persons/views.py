from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render


from .models import Person

# Create your views here.

def index(request):
    context = {
        'persons': Person.objects.all()
    }
    #template = loader.get_template('persons/index.tmpl')
    #return HttpResponse(template.render(context, request))
    return render(request, 'persons/index.tmpl', context)
