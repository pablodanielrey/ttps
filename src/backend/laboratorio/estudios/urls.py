from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('tiposEstudio', views.VistaTipoEstudio)
router.register('diagnosticos', views.VistaDiagnostico)


urlpatterns = router.urls