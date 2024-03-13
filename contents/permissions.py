from rest_framework import permissions


class SuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class ContentOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.method in permissions.SAFE_METHODS and request.user in obj.course.students.all()
