from rest_framework import serializers
from .models import Lesson
from groups.models import Group

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'group', 'created_by', 'file', 'created_at']
        read_only_fields = ['created_by', 'created_at']

    def validate_group(self, value):
        """Ensure the group belongs to the current user (teacher)"""
        if self.context['request'].user not in value.teachers.all():
            raise serializers.ValidationError("You don't have permission to add lessons to this group")
        return value