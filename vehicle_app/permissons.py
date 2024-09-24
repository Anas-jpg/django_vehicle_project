from rest_framework.permissions import BasePermission


class CanEditVehicle(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH']:
            return obj.vehiclepermission.can_edit
        if request.method == 'DELETE':
            return obj.vehiclepermission.can_delete
        return True
