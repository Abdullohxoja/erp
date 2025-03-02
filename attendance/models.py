
from django.db import models
from accounts.models import User
from groups.models import Group

class Attendance(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class AttendanceRecord(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)