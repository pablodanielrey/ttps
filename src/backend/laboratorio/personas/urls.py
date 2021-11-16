from django.urls import path, include

from rest_framework import routers

from . import views
from . import views_personas
from . import views_medicos
from . import views_usuarios


router = routers.DefaultRouter()
router.register('usuarios', views_usuarios.VistaUsuario)
router.register('personas', views_personas.VistaPersona)
router.register('obras_sociales', views_personas.VistaObraSocial)
router.register('medicos_derivantes', views_medicos.VistaMedicoDerivante)
router.register('medicos_informantes', views_medicos.VistaMedicoInformante)

urlpatterns = router.urls

for u in urlpatterns:
    print(u)