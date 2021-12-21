

from login import permissions

class LotesPermisos(permissions.PermisoBase):

    def get_app(self):
        return "lotes"

    def get_model(self):
        return 'lote'