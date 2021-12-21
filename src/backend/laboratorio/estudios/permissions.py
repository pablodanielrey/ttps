

from login import permissions

class EstudioPermisos(permissions.PermisoBase):

    def get_app(self):
        return "estudios"

    def get_model(self):
        return 'estudio'


class EstadoEstudioPermisos(permissions.PermisoBase):

    def get_app(self):
        return "estudios"

    def get_models(self):
        return ['estadoestudio', 'esperandointerpretacionderesultados']

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            for model in self.get_models():
                if request.user.has_perm(f'{self.get_app()}.view_{model}'):
                    return True
            return False

        for model in self.get_models():
            if request.user.has_perm(f'{self.get_app()}.change_{model}') or request.user.has_perm(f'{model}.delete_{model}'):
                return True
        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            for model in self.get_model():
                if request.user.has_perm(f'{self.get_app()}.view_{model}'):
                    return True
            return False
        for model in self.get_models():
            if request.user.has_perm(f'{self.get_app()}.add_{model}'):
                return True
        return False


class TemplateConsentimientoPermisos(permissions.PermisoBase):

    def get_app(self):
        return "estudios"

    def get_model(self):
        return 'templateconsentimiento'