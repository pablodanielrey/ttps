from login import permissions

class LiquidacionesPermisos(permissions.PermisoBase):

    def get_app(self):
        return "liquidaciones"

    def get_model(self):
        return 'liquidacion'
