from rest_framework.permissions import BasePermission


class IsOwnerOrStuff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        elif request.method in ['DELETE', 'PATCH', 'PUT']:
            return request.user == obj.creator
