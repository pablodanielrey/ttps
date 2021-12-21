from django.urls import path, include

from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter()


router.register('parametro_turnos', views.VistaParametroTurnos)
router.register('turnos_disponibles', views.VistaTurnosDisponibles)
router.register('turnos_confirmados', views.VistaTurnosConfirmados)
router.register('fechas_sin_turnos', views.VistaFechasSinTurno)

urlpatterns = router.urls
