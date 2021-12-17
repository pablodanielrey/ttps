
from django.urls import path, include
from . import views

urlpatterns = [
    path('estudios_por_tipo/', views.Lve23ReporteCantidadDeEstudiosPorTipo.as_view()),
    path('estudios_por_mes/', views.Lve25ReporteCantidadDeEstudiosPorMesAno.as_view()),
    path('demora_promedio_procesamiento/', views.Lve27ReporteDemoraDeEstudios.as_view())
]