
from django.urls import path, include

from . import views

urlpatterns = [
    path('liquidaciones/', views.Lve19LiquidacionesDeEstudios.as_view())
]
