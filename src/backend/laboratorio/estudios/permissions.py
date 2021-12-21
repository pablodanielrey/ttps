

from login import permissions

class EstudioPermisos(permissions.PermisoBase):

    def get_app(self):
        return "estudios"

    def get_model(self):
        return 'estudio'


class EstadoEstudioPermisos(permissions.PermisoBase):

    def get_app(self):
        return "estudios"

    def get_model(self):
        return 'estadoestudio'