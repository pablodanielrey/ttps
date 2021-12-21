

from login import permissions

class ConfiguradorPermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'configurador'

class AdministradorPermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'administrador'

class EmpleadoPermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'empleado'


class PacientePermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'paciente'

class MedicoInformantePermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'medicoinformante'


class MedicoDerivantePermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'medicoderivante'


class ObraSocialPermisos(permissions.PermisoBase):

    def get_app(self):
        return "personas"

    def get_model(self):
        return 'obrasocial'

