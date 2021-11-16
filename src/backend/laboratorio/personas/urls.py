from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('usuarios', views.VistaUsuario)
router.register('personas', views.VistaPersona)
router.register('obrasSociales', views.VistaObraSocial)
router.register('obraSocialPersonas', views.VistaObraSocialPersona)


urlpatterns = router.urls

for u in urlpatterns:
    print(u)