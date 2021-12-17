from django.urls import path, include

from rest_framework import routers

from . import views
from . import views_personas
from . import views_pacientes
from . import views_medicos
from . import views_usuarios
from . import views_configuradores
from . import views_empleados

router = routers.DefaultRouter()
router.register('usuarios', views_usuarios.VistaUsuario)
router.register('configuradores', views_configuradores.VistaConfigurador)
router.register('empleados', views_empleados.VistaEmpleado)
router.register('personas', views_personas.VistaPersona)
router.register('pacientes', views_pacientes.VistaPaciente)

router.register('pacientes_v2', views_pacientes.VistaPaciente2)

router.register('obras_sociales', views.VistaObraSocial)
router.register('medicos_derivantes', views_medicos.VistaMedicoDerivante)
router.register('medicos_informantes', views_medicos.VistaMedicoInformante)

urlpatterns = router.urls
