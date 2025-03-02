from django.db import models
from accounts.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='student_groups')
    teachers = models.ManyToManyField(User, related_name='teacher_groups')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)