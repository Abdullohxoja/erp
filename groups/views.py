from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from base.permissions import IsAdmin  # From your custom permissions
from groups.models import Group
from groups.serializers import GroupSerializer
from accounts.models import User  # Your custom user model

# class GroupViewSet(viewsets.ModelViewSet):
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated, IsAdmin]
#
#     def get_queryset(self):
#         """
#         Filter groups based on user role:
#         - Superusers see all groups
#         - Admins only see groups they created
#         """
#         if self.request.user.is_superuser:
#             return Group.objects.all()
#         return Group.objects.filter(created_by=self.request.user)
#
#     def perform_create(self, serializer):
#         """
#         Automatically set the creator of the group
#         and validate teacher/student assignments
#         """
#         # Get students/teachers from request data
#         students = self.request.data.get('students', [])
#         teachers = self.request.data.get('teachers', [])
#
#         # Validate users exist and have correct roles
#         student_users = User.objects.filter(
#             id__in=students,
#             role='student'
#         )
#         teacher_users = User.objects.filter(
#             id__in=teachers,
#             role='teacher'
#         )
#
#         # Save group with validated relationships
#         group = serializer.save(
#             created_by=self.request.user,
#             students=student_users,
#             teachers=teacher_users
#         )
#
#     def destroy(self, request, *args, **kwargs):
#         """
#         Custom delete handling to maintain data integrity
#         """
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(
#             {"detail": "Group deleted successfully"},
#             status=status.HTTP_204_NO_CONTENT
#         )


from .models import Group

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()  # Add this line
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get_queryset(self):
        """Override queryset to filter based on user role"""
        if self.request.user.is_superuser:
            return Group.objects.all()
        return Group.objects.filter(created_by=self.request.user)