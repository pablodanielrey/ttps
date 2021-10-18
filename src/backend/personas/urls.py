from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('usuarios', views.VistaUsuario)
router.register('personas', views.VistaPersona)


urlpatterns = router.urls