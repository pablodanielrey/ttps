from django.urls import path, include

from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter()
router.register('tiposEstudio', views.VistaTiposDeEstudio)
router.register('diagnosticos', views.VistaDiagnostico)
router.register('templateConsentimiento', views.VistaTemplateConsentimiento)
router.register('estudios', views.VistaEstudios)
router.register('estados', views.VistaEstadoEstudio)
router.register('archivos', views.VistaArchivos)
# router.register('estadisticas', views.VistaEstadisticas)


urlpatterns = router.urls
