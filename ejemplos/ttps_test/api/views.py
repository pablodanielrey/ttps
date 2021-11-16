import logging
logging.getLogger().setLevel(logging.DEBUG)

import json

from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    r = {
        'status': 200
    }
    return JsonResponse(r)

@csrf_exempt
def process(request:HttpRequest):
    if request.method != 'POST':
        raise Http404()
    if request.content_type.lower() != 'application/json':
        raise Http404()

    logging.debug(request.body)
    logging.debug(json.loads(request.body))
    r = {
        'status':200
    }
    return JsonResponse(r)