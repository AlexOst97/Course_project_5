from rest_framework import permissions


class IsOwners(permissions.BasePermission):
    """Проверка пользователя. Является ли владельцем"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
