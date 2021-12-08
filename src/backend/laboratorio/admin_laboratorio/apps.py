import logging

from django.apps import AppConfig
from django.contrib.auth import get_user_model


class AdminLaboratorioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_laboratorio'

    """
    @classmethod
    def ready(cls):
        user_model = get_user_model()
        log = logging.getLogger(cls.label)

        try:
            if not user_model.objects.filter(username="admin").first():
                log.info("Creando superusuario por defecto: adminy clave: nimda")
                user_model.objects.create_superuser('admin', 'admin@admin.admin', 'nimda')
        except Exception:
            log.warn("No se pudo crear el usuario admin")
    """
