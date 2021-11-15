from django.urls import path, include

from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter()
router.register('tiposEstudio', views.VistaTiposDeEstudio)
router.register('diagnosticos', views.VistaDiagnostico)
router.register('estudios', views.VistaEstudios)
router.register('estados', views.VistaEstadoEstudio)

urlpatterns = router.urls
for u in router.urls:
    print(u)