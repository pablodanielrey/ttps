
from rest_framework import permissions



class PermisoBase(permissions.BasePermission):

    def get_app(self):
        return ""

    def get_model(self):
        return ""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm(f'{self.get_app()}.view_{self.get_model()}')
        return request.user.has_perm(f'{self.get_app()}.change_{self.get_model()}') or request.user.has_perm(f'{self.get_app()}.delete_{self.get_model()}')

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm(f'{self.get_app()}.view_{self.get_model()}')
        return request.user.has_perm(f'{self.get_app()}.add_{self.get_model()}')
