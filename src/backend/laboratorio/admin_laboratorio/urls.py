from django.urls import path

from . import views

urlpatterns = [
    path('inicializar', views.InitSite.as_view())
]