from django.urls import path

from . import views
from . import views_usuarios, views_lotes, views_estudios

urlpatterns = [
    path('inicializar', views.InitSite.as_view()),
    path('usuarios', views_usuarios.Ejemplos.as_view()),
    path('lotes', views_lotes.Ejemplos.as_view()),
    path('estudios', views_estudios.Ejemplos.as_view())


]