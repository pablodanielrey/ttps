from django.urls import path, include

from rest_framework import routers, viewsets

from . import views


router = routers.DefaultRouter()
router.register('tiposEstudio', views.VistaTiposDeEstudio)
router.register('diagnosticos', views.VistaDiagnostico)
router.register('estudios', views.VistaEstudios)
router.register('estadoEstudio', views.VistaEstadoEstudio)

#router.register('presupuestoEstudio', views.VistaPresupuestoEstudio)

router.register('fechasSinTurnos', views.VistaFechasSinTurno)
router.register('parametroTurnos', views.VistaParametroTurnos)
router.register('listaTurnos', views.VistaListaTurnos, basename='Turnos')
router.register('turnosConfirmados', views.VistaListaTurnosConfirmados, basename='TurnosConfirmados')


urlpatterns = router.urls