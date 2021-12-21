
from rest_framework import permissions



class PermisoBase(permissions.BasePermission):

    def get_model(self):
        return ""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm(f'turnos.view_{self.get_model()}')
        return request.user.has_perm(f'turnos.change_{self.get_model()}') or request.user.has_perm(f'turnos.delete_{self.get_model()}')

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm(f'turnos.view_{self.get_model()}')
        return request.user.has_perm(f'turnos.add_{self.get_model()}')
