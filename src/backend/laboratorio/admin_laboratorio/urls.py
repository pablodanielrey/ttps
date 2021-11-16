from django.urls import path

from . import views
from . import views_ejemplos

urlpatterns = [
    path('inicializar', views.InitSite.as_view()),
    path('ejemplos', views_ejemplos.Ejemplos.as_view())

]