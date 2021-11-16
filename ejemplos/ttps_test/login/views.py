from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return HttpResponse('ok')
    #if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse('login:login'))

    return HttpResponse('ok')

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse('ok')

    if request.method == 'GET':
        return render(request, 'login/login.tmpl')

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('usuario logueado ok')
    
    return HttpResponse('error')
    