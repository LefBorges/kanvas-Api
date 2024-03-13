from rest_framework.permissions import BasePermission, SAFE_METHODS


class SuperUserPermissions(BasePermission):
    def has_permissions(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class CourseInstructorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.instructor


class CourseStudentsPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and request.user in obj.course.students.all()
