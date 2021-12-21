
from login import permissions


class ParametroTurnosPermisos(permissions.PermisoBase):

    def get_model(self):
        return 'parametrodeturnos'
