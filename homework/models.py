from django.db import models
from accounts.models import User
from groups.models import Group
from courses.models import Lesson

class Homework(models.Model):
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='homework/')