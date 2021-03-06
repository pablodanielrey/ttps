
from django.contrib.auth.models import User
from rest_framework import permissions as rpermissions
from login import permissions

from personas import models as personas_models

class ReportePermisos(permissions.PermisoBase):

    def get_app(self):
        return "reportes"

    def get_model(self):
        return "reporte"

    def has_object_permission(self, request, view, obj):
        return personas_models.Empleado.usuario_es_tipo(request.user)
        if request.method in rpermissions.SAFE_METHODS:
            return request.user.has_perm(f'{self.get_app()}.view_{self.get_model()}')
        return request.user.has_perm(f'{self.get_app()}.change_{self.get_model()}') or request.user.has_perm(f'{self.get_app()}.delete_{self.get_model()}')

    def has_permission(self, request, view):
        return personas_models.Empleado.usuario_es_tipo(request.user)
        if request.method in rpermissions.SAFE_METHODS:
            return request.user.has_perm(f'{self.get_app()}.view_{self.get_model()}')
        return request.user.has_perm(f'{self.get_app()}.add_{self.get_model()}')

