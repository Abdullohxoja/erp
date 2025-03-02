from rest_framework import serializers
from .models import Homework
from accounts.models import User
from groups.models import Group
from courses.models import Lesson

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'submitted_by', 'group', 'lesson', 'file']
