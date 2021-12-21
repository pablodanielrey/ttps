
from login import permissions


class ParametroTurnosPermisos(permissions.PermisoBase):

    def get_model(self):
        return 'parametrodeturnos'

class TurnosDisponiblesPermisos(permissions.PermisoBase):

    def get_model(self):
        return 'turnoconfirmado'

class TurnosConfirmadosPermisos(permissions.PermisoBase):

    def get_model(self):
        return 'turnoconfirmado'
