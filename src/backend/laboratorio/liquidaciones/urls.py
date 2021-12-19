
from django.urls import path, include

from . import views

urlpatterns = [
    path('liquidaciones/', views.Lve19LiquidacionesDeEstudios.as_view()),
    path('liquidados/', views.Lve19EstudiosLiquidado.as_view())
]
