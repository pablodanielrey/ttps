from login import permissions

class ConfiguracionPermisos(permissions.PermisoBase):

    def get_app(self):
        return "admin_laboratorio"

    def get_model(self):
        return 'configuracion'
