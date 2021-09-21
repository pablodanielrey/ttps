from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    r = {
        'status': 200
    }
    return JsonResponse(r)