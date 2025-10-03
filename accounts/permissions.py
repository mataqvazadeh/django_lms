from rest_framework.permissions import BasePermission

from accounts.models import UserRoles


class IsEducationEmployee(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.roles.filter(
                role=UserRoles.Roles.EducationEmployee
            ).exists()
        )

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.roles.filter(
                role=UserRoles.Roles.Teacher
            ).exists()
        )
    
