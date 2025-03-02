from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Lesson
from .serializers import LessonSerializer
# from core.permissions import IsTeacher  # Your custom permission

class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated] #IsTeacher

    def get_queryset(self):
        """Show only lessons for groups the teacher is assigned to"""
        user = self.request.user
        return Lesson.objects.filter(
            group__teachers=user
        ).select_related('group', 'created_by')

    def perform_create(self, serializer):
        """Automatically set the lesson creator"""
        serializer.save(created_by=self.request.user)