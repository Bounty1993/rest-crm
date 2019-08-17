from rest_framework.permissions import BasePermission


class IsServiceStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        departament = request.user.departament
        if request.method in ['POST', 'PUT', 'DELETE']:
            print(departament.name)
            if departament.name != 'Wsparcie techniczne':
                return False
        return True


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.id == obj.id:
            return True
        return False