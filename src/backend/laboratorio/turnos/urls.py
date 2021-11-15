from django.urls import path, include

from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter()

router.register('fechasSinTurnos', views.VistaFechasSinTurno)
router.register('parametroTurnos', views.VistaParametroTurnos)
router.register('turnos_disponibles', views.VistaTurnosDisponibles)
router.register('turnos_confirmados', views.VistaTurnosConfirmados)

urlpatterns = router.urls
for u in router.urls:
    print(u)