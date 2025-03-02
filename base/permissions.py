from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a teacher (based on your logic)
        return request.user.role == 'teacher'  # Adjust based on your User model

# Other permissions.

