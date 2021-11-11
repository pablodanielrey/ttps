from django.urls import path

from . import views

urlpatterns = [
    path('inicializar', views.InitSite.as_view()),
    path('ejemplos', views.Ejemplos.as_view())

]