from django.urls import path, include

from rest_framework import routers, viewsets

from . import views


router = routers.DefaultRouter()
router.register('tiposEstudio', views.VistaTiposDeEstudio)
router.register('diagnosticos', views.VistaDiagnostico)
router.register('estudios', views.VistaEstudios)
router.register('estadoEstudio', views.VistaEstadoEstudio)

#router.register('presupuestoEstudio', views.VistaPresupuestoEstudio)

router.register('parametroTurnos', views.VistaPrametroTurnos)

urlpatterns = router.urls