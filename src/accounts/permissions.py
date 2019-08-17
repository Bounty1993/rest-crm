from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsServiceStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        departament = request.user.departament
        if request.method in SAFE_METHODS:
            return True
        if departament.name == 'Wsparcie techniczne':
            return True
        return False


class HasDepartament(BasePermission):
    def has_permission(self, request, view):
        return request.user.departament


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj
