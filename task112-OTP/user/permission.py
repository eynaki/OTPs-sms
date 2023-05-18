from rest_framework.permissions import BasePermission


class IsOwnerOrReadeOnly(BasePermission):
    message = 'permission denied, you are not the owner '

    # def has_permission(self, request, view):
    #     return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.owner == request.user
