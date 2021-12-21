
from login import permissions

class ReportePermisos(permissions.PermisoBase):

    def get_app(self):
        return "reportes"

    def get_model(self):
        return 'reporte'
